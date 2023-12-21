import os

def getSize(ruta):
    total = 0
    try:
        for entrada in os.scandir(ruta):
            if entrada.is_file():
                total += entrada.stat().st_size
            elif entrada.is_dir():
                total += getSize(entrada.path)
    except PermissionError:
        print(f"No se tienen los permisos necesarios para acceder al directorio: {ruta}")
    except NotADirectoryError:
        print(f"No se pudo acceder: {ruta}")
    except FileNotFoundError:
        print(f"No se encontro: {ruta}")
    return total

def listBigElements(ruta, num_elementos):
    elementos = [(getSize(os.path.join(ruta, nombre)), nombre) for nombre in os.listdir(ruta)]
    elementos.sort(reverse=True)
    return elementos[:num_elementos]

biggerElements = listBigElements('C:\\', 10)
for tamano, nombre in biggerElements:
    print(f"({tamano / (1024 * 1024 * 1024):.2f} GB :Tamano ) {nombre} ")