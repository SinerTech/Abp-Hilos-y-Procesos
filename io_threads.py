import threading
import time
import psutil
import requests

def descargar_pagina(url):
    requests.get(url)
    return f"Descargada: {url}"

def main():
    urls = [
        "https://www.google.com",
        "https://www.wikipedia.org",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.google.com",
        "https://www.wikipedia.org"
        ] * 4
    
    threads = []
    proceso = psutil.Process()
    
    inicio = time.time()
    
    psutil.cpu_percent(interval=None)  # Inicializa el contador de CPU
    
    # Crear y lanzar hilos para descargar páginas
    for url in urls:
        t = threading.Thread(target=descargar_pagina, args=(url,))
        threads.append(t)
        t.start()

    # Esperar a que todos los hilos terminen
    for t in threads:
        t.join()

    fin = time.time()
    cpu = psutil.cpu_percent(interval=None)
    memory = proceso.memory_info().rss / 1024 / 1024  # MB

    print ("\n === THREADS I/O-BOUND === ")
    print(f"Tiempo total: {fin - inicio:.2f} segundos")
    print(f"Uso de CPU: {cpu}%")
    print(f"Uso de memoria: {memory:.2f} MB")
    
if __name__ == "__main__":
    main()