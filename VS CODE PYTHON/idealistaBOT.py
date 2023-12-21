import requests
from bs4 import BeautifulSoup

def obtener_propiedades(rango_precio, zona):
    try:
        url = f"https://www.idealista.com/venta-viviendas/{zona}/"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        propiedades = []
        for propiedad in soup.find_all('div', class_='item-info-container'):
            precio = propiedad.find('span', class_='item-price h2-simulated').text
            precio = int(precio.replace("€", "").replace(",", "").strip())
            metros = propiedad.find('span', class_='item-detail').text
            metros = int(metros.replace("m²", "").strip())

            if rango_precio[0] <= precio <= rango_precio[1]:
                propiedades.append((precio, metros, precio/metros))

        propiedades.sort(key=lambda x: x[2])
        return propiedades
    except Exception as e:
        print(f"Se produjo un error: {e}")

rango_precio = (int(input("Introduce el precio mínimo: ")), int(input("Introduce el precio máximo: ")))
zona = input("Introduce la zona: ")
mejores_propiedades = obtener_propiedades(rango_precio, zona)

if mejores_propiedades:
    with open('propiedades.txt', 'w') as f:
        for propiedad in mejores_propiedades:
            f.write(f"Precio: {propiedad[0]}€, Metros: {propiedad[1]}m², Precio por metro: {propiedad[2]}€/m²\n")
else:
    print("No se encontraron propiedades que cumplan con los criterios especificados.")
