from flask import Flask, request, jsonify
# Importamos la clase que ya tiene toda la lógica
from detector_incidencias import DetectorIncidencias

# 1. Configuración inicial
app = Flask(__name__)
cerebro = DetectorIncidencias()

# 2. Entrenamiento al arrancar (Sustituye a tus +20 líneas de entrenamiento manual)
print("--> [Servidor] Iniciando sistema...")
exito = cerebro.entrenar_sistema_interno()

if exito:
    print("--> [Servidor] IA Entrenada y Lista con requisitos del PDF.")
else:
    print("--> [Error] No se pudo entrenar el sistema.")

# 3. Endpoint de análisis
@app.route('/analizar', methods=['POST'])
def endpoint_analizar():
    datos = request.json
    if not datos:
        return jsonify({"error": "No data provided"}), 400
        
    # Aquí delegamos todo el trabajo a la clase externa
    # Esto detecta AusenciaDatos (>120s) y SaltoVoltaje (>=0.5V)
    resultado = cerebro.analizar_dato_tiempo_real(datos)
    
    return jsonify({"diagnostico": resultado})

# 4. Ejecución
if __name__ == '__main__':
    app.run(port=5000, debug=True)
