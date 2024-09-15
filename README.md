Requisitos

Asegúrate de tener Python 3.x instalado. Puedes verificarlo ejecutando:
python --version o python3 --version

Bibliotecas Requeridas:

El proyecto requiere las siguientes bibliotecas de Python:

random (incorporada)

heapq (incorporada)

numpy (para operaciones numéricas)

matplotlib (para visualización, si es necesario para futuras expansiones)

Puedes instalar numpy y matplotlib ejecutando: pip install numpy matplotlib o para usuarios de Python 3: pip3 install numpy matplotlib

Instrucciones para ejecutar el proyecto:

Descargar el Proyecto: Si descargas el archivo ZIP, descomprímelo en un directorio en tu computadora.

Ejecutar el Script de Python: Ejecuta el script para realizar la simulación con ambas estrategias: Movimiento Aleatorio y Búsqueda A*.


Proyecto de Simulación de Aspiradora

Este proyecto implementa dos estrategias para que una aspiradora limpie un entorno basado en una cuadrícula:

Estrategia de Movimiento Aleatorio: La aspiradora se mueve aleatoriamente, seleccionando una de las celdas adyacentes (arriba, abajo, izquierda o derecha) y evita obstáculos.

Estrategia de Búsqueda A: La aspiradora utiliza el algoritmo de búsqueda A para encontrar el camino más corto para limpiar todas las celdas sucias, evitando obstáculos y optimizando el movimiento. El proyecto simula el rendimiento de la aspiradora en entornos de cuadrícula pequeños y grandes, midiendo el número de pasos necesarios para limpiar todas las celdas sucias.

El proyecto incluye escenarios de evaluación para entornos de cuadrícula pequeños y grandes:

Mundo Pequeño:

Cuadrícula de 5x5: 3 obstáculos y 4 celdas sucias.
Cuadrícula de 10x10: 5 obstáculos y 8 celdas sucias.
Mundo Grande:

Cuadrícula de 50x50: 30 obstáculos y 40 celdas sucias.
Cuadrícula de 100x100: 40 obstáculos y 50 celdas sucias.
Puedes modificar el tamaño de la cuadrícula, el número de obstáculos y el número de celdas sucias cambiando los parámetros en las siguientes funciones:

evaluate_random_movement(X, Y, num_obstacles, num_dirty_cells)
evaluate_a_star(X, Y, num_obstacles, num_dirty_cells)
Por ejemplo, para ejecutar una simulación en una cuadrícula de 20x20 con 10 obstáculos y 15 celdas sucias, puedes modificar la llamada a la función de la siguiente manera:

evaluate_random_movement(20, 20, num_obstacles=10, num_dirty_cells=15)
evaluate_a_star(20, 20, num_obstacles=10, num_dirty_cells=15)
Este proyecto se puede expandir con:

Visualización: Usando matplotlib para crear representaciones visuales de los movimientos de la aspiradora en la cuadrícula.

Variaciones en la Densidad de Obstáculos: Aumentando la complejidad añadiendo más obstáculos o diferentes formas de obstáculos.

Estrategias Más Sofisticadas: Implementando algoritmos adicionales de búsqueda o aprendizaje (por ejemplo, el algoritmo de Dijkstra, Q-learning).
