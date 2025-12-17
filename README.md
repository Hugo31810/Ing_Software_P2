# Práctica 2 – Desarrollo, testing y rediseño  
**Ingeniería del Software – Universidad Rey Juan Carlos**

Este repositorio contiene el desarrollo de la **Práctica 2 de la asignatura Ingeniería del Software**, correspondiente al curso académico **2025–2026**, centrada en el **desarrollo en Python**, el **testing del sistema** y el **rediseño parcial** del modelo cuando ha sido necesario, partiendo de los requisitos y el diseño definidos en la Práctica 1.

---

## 📌 Objetivo de la práctica

El objetivo de esta práctica es **implementar el sistema diseñado en la Práctica 1**, realizando:

- Desarrollo del sistema en **Python**
- Aplicación de **técnicas de testing**
- Uso de **Machine Learning** para la predicción de incidencias
- **Rediseño parcial** del diagrama de clases y paquetes en caso necesario

Todo ello siguiendo el enunciado oficial de la Práctica 2 proporcionado por la asignatura :contentReference[oaicite:0]{index=0}.

---

## 🧩 Contexto del sistema

El sistema implementado corresponde a una **aplicación para la detección y predicción de incidencias en vías ferroviarias**, basada en datos eléctricos almacenados en ficheros CSV.

Los datos incluyen:
- Estado de la vía (`status` / `medida`):
  - `1`: no hay tren
  - `0`: hay tren
- Valores de voltaje procedentes de dos receptores:
  - `voltageReceiver1` (canal a)
  - `voltageReceiver2` (canal b)
- Información temporal asociada a cada medición

---

## 👥 Equipo y roles

Los roles del equipo han sido reasignados conforme a lo establecido en la Práctica 2:

### 🧑‍💻 Desarrolladores
(Arquitectos de la P1 + un analista)
- **Pablo Sastre Noriega**
- **Héctor Santiago Martínez**


### 🧪 Tester
(Jefe de proyecto de la P1)
- **Hugo Salvador Aizpún**
- - **Iván De Rada López**

### 🏗️ Arquitecto Software
(Otro analista de la P1, con apoyo en testing)
- **Raúl Vicente Sánchez**

### 👤 Apoyo en análisis y validación
- **Tomás Cano Santa Catalina**

Cada miembro ha asumido las responsabilidades indicadas para garantizar la calidad del desarrollo, las pruebas y la correcta evolución del diseño.

---

## 🧠 Algoritmo de Machine Learning

Para la predicción de incidencias se ha seleccionado un **algoritmo de Machine Learning** adecuado al tipo de datos disponibles.

Características del proceso:
- División del dataset:
  - 80% para entrenamiento
  - 20% para predicción
- Predicción de:
  - Ausencia prolongada de datos
  - Saltos de voltaje ≥ 0.5 V
- Evaluación del rendimiento del modelo durante la fase de testing

---

## 🧪 Testing

El sistema ha sido sometido a un proceso de **testing sistemático**, que incluye:

- Tests unitarios de los principales módulos
- Verificación de la correcta lectura del dataset
- Validación de los resultados del modelo de predicción
- Detección de errores y fallos lógicos

Los fallos detectados y las soluciones aplicadas se documentan tanto en el código como en la presentación final.

---

## 🔄 Rediseño

Durante el desarrollo se ha evaluado la necesidad de realizar un **rediseño parcial del diagrama de clases y paquetes**.

El rediseño se ha llevado a cabo únicamente cuando ha sido imprescindible, documentando:
- Problema detectado
- Cambios realizados
- Justificación del rediseño

---

## 📄 Entregables

La práctica incluye los siguientes entregables:

- Código fuente completo en Python
- Tests automatizados
- Dataset adaptado
- Presentación en PowerPoint con:
  - Explicación del desarrollo
  - Resultados del testing
  - Rediseño realizado
  - Librerías utilizadas
  - Decisiones técnicas relevantes



---

## ✍️ Autores

Práctica realizada por el **Grupo G6**  
Asignatura: Ingeniería del Software  
Universidad Rey Juan Carlos  
Curso 2025–2026
