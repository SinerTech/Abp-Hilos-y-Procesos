import multiprocessing
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

    procesos = []

    proceso_principal = psutil.Process()

    inicio = time.time()

    psutil.cpu_percent(interval=None)

    # Crea y lanza los procesos
    for url in urls:

        p = multiprocessing.Process(
            target=descargar_pagina,
            args=(url,)
        )

        procesos.append(p)

        p.start()

    # Espera a que todos terminen
    for p in procesos:
        p.join()

    fin = time.time()

    cpu = psutil.cpu_percent(interval=None)

    memory = proceso_principal.memory_info().rss / 1024 / 1024

    print("\n === PROCESOS I/O-BOUND === ")
    print(f"Tiempo total: {fin - inicio:.2f} segundos")
    print(f"Uso de CPU: {cpu}%")
    print(f"Uso de memoria: {memory:.2f} MB")

if __name__ == "__main__":
    main()
