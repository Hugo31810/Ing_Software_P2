from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from lectura_voltaje import lecturaVoltaje


# --- CLASE INTERNA DEL SERVIDOR ---
# Definimos la clase aquí para asegurar que tiene los métodos exactos que el servidor necesita
class CerebroServidor:
    def __init__(self):
        self.modelo = RandomForestClassifier(n_estimators=50, random_state=42)
        self.entrenado = False

    def entrenar_sistema_interno(self):
        """ Realiza la lectura del CSV y el entrenamiento del modelo """
        print("--> [Servidor] Iniciando carga de datos...")
        lector = lecturaVoltaje()
        # Asegúrate de que el CSV esté en la misma carpeta o ajusta la ruta
        df = lector.leerCSV("./Dataset-CV.csv")

        if df is None:
            print("❌ ERROR: No se pudo cargar el Dataset-CV.csv")
            return False

        print("--> [Servidor] Generando etiquetas de entrenamiento...")
        # Generar etiquetas artificiales (Training Labeling)
        df['target'] = np.select(
            [(df['voltageReceiver1'] < 50), (df['voltageReceiver1'] > 2000)],
            ['AusenciaDatos', 'SaltoVoltaje'],
            default='Normal'
        )

        X = df[['voltageReceiver1', 'voltageReceiver2', 'status']]
        y = df['target']

        # Split 80/20
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

        print("--> [Servidor] Entrenando Random Forest...")
        self.modelo.fit(X_train, y_train)
        self.entrenado = True
        print("--> [Servidor] IA Entrenada y Lista. ✅")
        return True

    def detectarSaltoFrecuencia(self, datos_json):
        """ Predice en base a un solo dato recibido del cliente """
        if not self.entrenado:
            return "Servidor No Entrenado"

        # Convertimos el JSON recibido a un formato que entienda el modelo (DataFrame de 1 fila)
        # El orden de las columnas debe ser IGUAL al del entrenamiento
        input_data = pd.DataFrame([{
            'voltageReceiver1': datos_json['voltageReceiver1'],
            'voltageReceiver2': datos_json['voltageReceiver2'],
            'status': datos_json['status']
        }])

        prediccion = self.modelo.predict(input_data)[0]
        return prediccion


# --- FLASK (Infraestructura HTTP) ---
app = Flask(__name__)

# Instanciamos nuestra clase corregida
cerebro = CerebroServidor()

# Entrenamos al iniciar el script
cerebro.entrenar_sistema_interno()


@app.route('/analizar', methods=['POST'])
def endpoint_analizar():
    datos = request.json
    # Ahora sí existe este método en la clase
    resultado = cerebro.detectarSaltoFrecuencia(datos)
    return jsonify({"diagnostico": resultado})


if __name__ == '__main__':
    app.run(port=5000, debug=True)