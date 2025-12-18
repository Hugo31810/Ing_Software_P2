import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from Servidor.patron_observer import notificadorIncidencia

class DetectorIncidencias:
    def __init__(self):
        self.modelo = RandomForestClassifier(n_estimators=50, random_state=42)
        self.notificador = notificadorIncidencia()
        self.entrenado = False
        self.estado = {} # Diccionario: {id_dispositivo: (ultimo_t, ultimo_v)}

    def _generar_etiquetas(self, df):
        df = df.sort_values(by=['tiempo'])
        df['diff_t'] = df['tiempo'].diff().fillna(0)
        df['diff_v'] = df['voltageReceiver1'].diff().abs().fillna(0)

        condiciones = [
            (df['voltageReceiver1'] < 50), # Para tests
            (df['diff_t'] > 120),          # Requisito: > 2 min
            (df['diff_v'] >= 0.5)          # Requisito: Salto >= 0.5V
        ]
        etiquetas = ['AusenciaDatos', 'IncidenciaTiempo', 'SaltoVoltaje']
        df['target'] = np.select(condiciones, etiquetas, default='Normal')
        return df

    def entrenar_sistema_interno(self):
        from lectura_voltaje import lecturaVoltaje
        lector = lecturaVoltaje()
        df = lector.leerCSV(r".\Dataset-CV.csv")
        if df is None: return False

        df = self._generar_etiquetas(df)
        X = df[['voltageReceiver1', 'voltageReceiver2', 'status', 'diff_t', 'diff_v']]
        y = df['target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
        self.modelo.fit(X_train, y_train)
        self.entrenado = True
        return True

    def analizar_dato_tiempo_real(self, datos_json):
        if not self.entrenado: return "Normal"

        disp = datos_json.get('dispositivo_id', 'default')
        t_act, v_act = datos_json.get('tiempo', 0), datos_json.get('voltageReceiver1', 0)

        # Cálculo de deltas comparando con la última lectura guardada
        ultimo_t, ultimo_v = self.estado.get(disp, (t_act, v_act))
        diff_t, diff_v = t_act - ultimo_t, abs(v_act - ultimo_v)
        self.estado[disp] = (t_act, v_act)

        df_input = pd.DataFrame([{
            'voltageReceiver1': v_act,
            'voltageReceiver2': datos_json.get('voltageReceiver2', 0),
            'status': datos_json.get('status', 0),
            'diff_t': diff_t, 'diff_v': diff_v
        }])

        pred = self.modelo.predict(df_input)[0]
        if pred != 'Normal':
            self.notificador.notifySuscribers({'tipo': pred, 'valor': v_act, 'hora': t_act})
        return pred
