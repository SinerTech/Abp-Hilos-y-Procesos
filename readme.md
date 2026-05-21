# Comparación de ejecución IO-BOUND en Python

## Objetivo

Comparar el rendimiento de tres formas de ejecución en Python:

## TAREAS

- Secuencial
- Hilos (Threads) Nico y Franco
- Procesos (Multiprocessing) Ana y Tibi

utilizando tareas **IO-bound**, es decir, tareas que dependen de operaciones de entrada/salida como descargas web.

---

# ¿Qué es una tarea IO-bound?

Una tarea IO-bound es una tarea que pasa gran parte del tiempo esperando:

- internet
- archivos
- bases de datos
- APIs

En este proyecto se realizan descargas de páginas web usando la librería `requests`.

---

# Archivos utilizados

```text
io_secuencial.py
io_threads.py
io_procesos.py
```

---

# 1) Ejecución Secuencial

## ¿Cómo funciona?

Las páginas se descargan una por una.

El programa espera que termine una descarga para comenzar la siguiente.

## Características

- Más simple
- Menor consumo de recursos
- Más lento

## Resultado esperado

```python
=== SECUENCIAL IO-BOUND ===
Tiempo: 11.80 segundos
CPU usado: 8.5%
Memoria usada: 30.10 MB
```

---

# 2) Ejecución con Hilos (Threads)

## ¿Cómo funciona?

Se crean varios hilos que trabajan al mismo tiempo compartiendo memoria.

Mientras un hilo espera internet, otro puede continuar ejecutándose.

## Características

- Mucho más rápido para tareas IO-bound
- Bajo consumo de memoria
- Mejor aprovechamiento del tiempo de espera

## Resultado esperado

```python
=== HILOS IO-BOUND ===
Tiempo: 2.01 segundos
CPU usado: 19.1%
Memoria usada: 38.27 MB
```

---

# 3) Ejecución con Procesos

## ¿Cómo funciona?

Cada tarea se ejecuta en un proceso independiente.

Cada proceso tiene su propia memoria y recursos.

## Características

- Muy rápido
- Mayor consumo de memoria
- Mayor uso de CPU

## Resultado esperado

```python
=== PROCESOS IO-BOUND ===
Tiempo: 2.36 segundos
CPU usado: 31.5%
Memoria usada: 45.80 MB
```

---

# Librerías utilizadas

```python
requests
threading
multiprocessing
psutil
time
```

---

# Instalación en entorno virtual

## 1) Crear entorno virtual

Abrir la terminal en VSCode y ejecutar:

```bash
python -m venv venv
```

---

## 2) Activar entorno virtual

### En Windows

```bash
venv\Scripts\activate
```

---

## 3) Instalar librerías necesarias

```bash
pip install -r requirements.txt
```

---

# Conclusión

Las tareas IO-bound funcionan mucho mejor utilizando concurrencia.

- El modo secuencial tarda más porque trabaja de a una tarea.
- Los hilos mejoran mucho el tiempo aprovechando las esperas de internet.
- Los procesos también aceleran la ejecución, aunque consumen más recursos del sistema.