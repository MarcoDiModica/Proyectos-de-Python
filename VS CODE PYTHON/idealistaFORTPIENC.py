import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import logging

class IdealistaScraper:
    BASE_URL = 'https://www.idealista.com'
    CSV_FILE = 'properties.csv'

    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    ]

    def validate_url(self, url):
        # Validar el formato básico de la URL
        if not url.startswith('https://www.idealista.com/'):
            raise ValueError("La URL no es válida para Idealista.")

    def validate_price_range(self, price_range):
        # Validar el formato del rango de precios
        if not isinstance(price_range, tuple) or len(price_range) != 2:
            raise ValueError("El rango de precios debe ser una tupla de dos elementos.")

    def __init__(self, url, price_range=(250000, 300000), min_size=75, min_floor=2, min_rooms=3):
        self.validate_url(url)
        self.validate_price_range(price_range)
        self.url = url
        self.price_range = price_range
        self.min_size = min_size
        self.min_floor = min_floor
        self.min_rooms = min_rooms
        logging.basicConfig(filename='scraper_log.txt', level=logging.ERROR)

    def get_page_content(self, url):
        try:
            headers = {'User-Agent': random.choice(self.USER_AGENTS)}
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.RequestException as e:
            logging.error(f"Error al obtener el contenido de la página: {e}")
            return None

    def extract_price(self, price_str):
        try:
            return int(price_str.replace('€', '').replace(',', ''))
        except ValueError as e:
            logging.error(f"Error al extraer el precio: {e}")
            return None

    def parse_page(self, soup):
        properties = soup.find_all('div', class_='item-info-container')
        data = []
        for property in properties:
            try:
                price = self.extract_price(property.find('span', class_='item-price h2-simulated').text)
                size = int(property.find('span', class_='item-detail').text.split('m')[0])
                floor = property.find_all('span', class_='item-detail')[1].text
                rooms = int(property.find_all('span', class_='item-detail')[2].text.split(' ')[0])

                if 'Bajo' not in floor and 'Entreplanta' not in floor:
                    floor = int(floor.split('ª')[0])
                    if (self.price_range[0] <= price <= self.price_range[1] and
                            size > self.min_size and floor >= self.min_floor and rooms >= self.min_rooms):
                        link = property.find('a', class_='item-link')['href']
                        data.append({
                            'link': self.BASE_URL + link,
                            'price': price,
                            'size': size,
                            'floor': floor,
                            'rooms': rooms
                        })
            except Exception as e:
                logging.error(f"Error al parsear la propiedad: {e}")
        return data

    def scrape(self):
        try:
            data = []
            next_page = self.url
            while next_page:
                soup = self.get_page_content(next_page)
                if soup:
                    data.extend(self.parse_page(soup))
                    next_page_link = soup.find('a', class_='icon-arrow-right-after')
                    next_page = self.BASE_URL + next_page_link['href'] if next_page_link else None

                    # Pausa entre 5 y 15 segundos para evitar sobrecargar los servidores
                    time.sleep(random.uniform(5, 15))
        except Exception as e:
            logging.error(f"Error durante el proceso de scraping: {e}")

        with open(self.CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['link', 'price', 'size', 'floor', 'rooms'])
            writer.writeheader()
            writer.writerows(data)

scraper = IdealistaScraper('https://www.idealista.com/venta-viviendas/barcelona/eixample/el-fort-pienc/')
scraper.scrape()