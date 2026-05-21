import requests
import time
import psutil


def descargar_pagina(url):
    requests.get(url)


def main():

    urls = [
        "https://www.google.com",
        "https://www.wikipedia.org",
        "https://www.github.com",
        "https://www.python.org",
        "https://www.google.com",
        "https://www.wikipedia.org",
    ] * 4

    proceso = psutil.Process()

    inicio = time.time()

    psutil.cpu_percent(interval=None)

    for url in urls:
        descargar_pagina(url)

    fin = time.time()

    cpu = psutil.cpu_percent(interval=1)
    memoria = proceso.memory_info().rss / 1024 / 1024

    print("\n=== SECUENCIAL I/O-BOUND ===")
    print(f"Tiempo: {fin - inicio:.2f} segundos")
    print(f"CPU usado: {cpu}%")
    print(f"Memoria usada: {memoria:.2f} MB")


if __name__ == "__main__":
    main()
