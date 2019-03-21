import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('ul', class_='pagn').find('li', class_='pagn-last').find('a').get('href')
    total_pages = pages.split('=')[1]
    return int(total_pages)

def write_csv(data):
    with open('lalafo_phones.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['title'],
                          data['price'],
                          data['photos_link']) )

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='list-view').find_all('div', class_='category-item')
    for ad in ads:
        try:
            title = ad.find('div', class_='details').find('a', class_='name').text
        except:
            title = ''
        try:
            price = ad.find('div', class_='price').text.strip()
        except:
            price = ''
        try:
            photos_link = ad.find('div', class_='image').find('a', class_='image-holder').get('href')
        except:
            photos_link = ''

        data = {'title': title,
                'price': price,
                'photos_link': photos_link}

        write_csv(data)

def main():
    url = 'https://lalafo.kg/kyrgyzstan/mobilnye-telefony-i-aksessuary'
    page_part = '?page='
    total_pages = get_total_pages(get_html(url))
    for i in range(1, total_pages):
        url_gen = url + page_part + str(i)
        #print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)

if __name__ == '__main__':
    main()
