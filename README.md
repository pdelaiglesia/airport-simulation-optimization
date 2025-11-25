# Airport Simulation and Optimization

Este proyecto implementa un modelo de simulación de un aeropuerto utilizando SimPy, orientado a evaluar el rendimiento del sistema bajo diferentes configuraciones de recursos.  
Además, incluye dos métodos de optimización para identificar la combinación óptima de recursos que minimiza el tiempo medio de espera de los aviones.

## Objetivo del proyecto

Modelar el flujo de aviones a través de:
- Pistas de aterrizaje
- Fingers de embarque
- Líneas de seguridad
- Puestos de check-in

Posteriormente:
- Evaluar tiempos de espera promedio.
- Obtener la mejor configuración mediante:
  - Producto cartesiano (búsqueda exhaustiva).
  - Particle Swarm Optimization (PSO).

## Tecnologías utilizadas

- Python 3
- SimPy
- NumPy
- Pandas
- PySwarm (PSO)
- itertools

## Estructura del proyecto

Archivos principales:
- `main.py` – ejecuta la simulación, el producto cartesiano y la optimización PSO.
- `airplane.py` – modelo del avión y su recorrido por el aeropuerto.
- `train.py` – modelo del tren interno.
- `security.py` – proceso de seguridad.
- `checkinstand.py` – proceso de check-in.

Recursos del sistema:
- Pistas
- Fingers
- Líneas de seguridad
- Puestos de check-in

## Funcionamiento general

### Simulación

La función `run_simulation`:
- Crea un entorno SimPy.
- Define recursos con capacidades configurables.
- Genera aviones periódicamente.
- Calcula el tiempo total de espera y lo devuelve como media.

### Búsqueda por producto cartesiano

La función `cartesian_product`:
- Define rangos predeterminados de recursos.
- Evalúa todas las combinaciones posibles.
- Guarda los resultados en `cartesian_results.csv`.

### Optimización mediante PSO

La función `run_pso_optimization`:
- Define límites de búsqueda.
- Llama a `pso()` para minimizar la función objetivo.
- Devuelve la mejor combinación encontrada.

## Ejecución

Para ejecutar el proyecto:


Durante la ejecución:
- Se genera el producto cartesiano y se muestra un DataFrame con resultados.
- Se ejecuta PSO para encontrar la mejor configuración.

## Resultados generados

- `cartesian_results.csv`: contiene todas las combinaciones evaluadas y sus tiempos medios de espera.
- Resultados de PSO mostrados en consola con la combinación óptima.

## Requisitos

Instalar dependencias:

