# Comparación de Threads y Procesos en Python

## Objetivo

Comparar el rendimiento de distintas formas de concurrencia en Python utilizando:

- Threads (Hilos)
- Procesos (Multiprocessing)

sobre dos tipos de tareas:

- CPU-bound
- IO-bound

---

# ¿Qué es una tarea CPU-bound?

Una tarea CPU-bound es una tarea que exige mucho procesamiento del procesador.

El rendimiento depende principalmente del uso de CPU.

Ejemplos:

- cálculos matemáticos
- procesamiento de datos
- algoritmos complejos

En este proyecto se realiza una suma intensiva utilizando millones de iteraciones.

---

# ¿Qué es una tarea IO-bound?

Una tarea IO-bound es una tarea que pasa gran parte del tiempo esperando operaciones de entrada/salida.

Ejemplos:

- internet
- archivos
- bases de datos
- APIs

En este proyecto se realizan descargas de páginas web usando la librería `requests`.

---

# Archivos del proyecto

```text
cpu_threads.py
cpu_procesos.py
io_threads.py
io_procesos.py
1) CPU-BOUND con Threads

Archivo:

cpu_threads.py
¿Cómo funciona?

Se crean varios hilos que realizan cálculos matemáticos al mismo tiempo.

Todos los hilos comparten la misma memoria del proceso principal.

Características
Menor consumo de memoria
Fácil de implementar
No aprovecha completamente múltiples núcleos por el GIL de Python
Resultado esperado
=== THREADS ===
Tiempo: 5.20 segundos
CPU usado: 25.4%
Memoria usada: 32.10 MB
2) CPU-BOUND con Procesos

Archivo:

cpu_procesos.py
¿Cómo funciona?

Se crean múltiples procesos independientes para realizar cálculos intensivos.

Cada proceso utiliza su propia memoria y puede ejecutarse en diferentes núcleos del procesador.

Características
Mejor rendimiento en tareas CPU-bound
Mayor uso de memoria
Aprovecha múltiples núcleos del CPU
Resultado esperado
=== PROCESOS ===
Tiempo: 2.90 segundos
CPU usado: 78.6%
Memoria usada: 48.50 MB
3) IO-BOUND con Threads

Archivo:

io_threads.py
¿Cómo funciona?

Se crean varios hilos para descargar páginas web simultáneamente.

Mientras un hilo espera respuesta de internet, otro continúa ejecutándose.

Características
Muy eficiente para tareas IO-bound
Bajo consumo de memoria
Excelente aprovechamiento del tiempo de espera
Resultado esperado
=== THREADS I/O-BOUND ===
Tiempo total: 2.01 segundos
Uso de CPU: 19.1%
Uso de memoria: 38.27 MB
4) IO-BOUND con Procesos

Archivo:

io_procesos.py
¿Cómo funciona?

Cada descarga web se ejecuta en un proceso independiente.

Cada proceso tiene sus propios recursos y memoria.

Características
Buen rendimiento
Mayor consumo de memoria
Más pesado que threads para tareas IO-bound
Resultado esperado
=== PROCESOS I/O-BOUND ===
Tiempo total: 2.36 segundos
Uso de CPU: 31.5%
Uso de memoria: 45.80 MB
Librerías utilizadas
threading
multiprocessing
requests
psutil
time
os
Instalación del entorno virtual
1) Crear entorno virtual

Abrir la terminal en VSCode y ejecutar:

python -m venv venv
2) Activar entorno virtual
En Windows
venv\Scripts\activate
3) Instalar dependencias
pip install requests psutil

o utilizando:

pip install -r requirements.txt
Conclusión
CPU-bound

Las tareas CPU-bound funcionan mejor utilizando procesos.

Esto sucede porque Python tiene una limitación llamada GIL (Global Interpreter Lock), que impide que múltiples threads ejecuten código Python intensivo al mismo tiempo.

Por eso:

Threads consumen menos memoria, pero no mejoran demasiado el rendimiento.
Procesos aprovechan múltiples núcleos y aceleran los cálculos.
IO-bound

Las tareas IO-bound funcionan muy bien utilizando threads.

Mientras un hilo espera respuesta de internet, otros pueden seguir trabajando.

Por eso:

Threads ofrecen excelente rendimiento y bajo consumo de recursos.
Procesos también funcionan, pero consumen más memoria y CPU innecesariamente.