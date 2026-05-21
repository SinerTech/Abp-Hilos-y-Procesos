import time
import psutil
import os


def calcular():
    total = 0
    for i in range(10000000):
        total += i


inicio = time.time()

for _ in range(4):
    calcular()

fin = time.time()

proceso = psutil.Process(os.getpid())

cpu = psutil.cpu_percent(interval=1)
memoria = proceso.memory_info().rss / 1024 / 1024

print("=== SECUENCIAL ===")
print(f"Tiempo: {fin - inicio:.2f} segundos")
print(f"CPU usado: {cpu}%")
print(f"Memoria usada: {memoria:.2f} MB")
