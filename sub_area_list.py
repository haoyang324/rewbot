import downloader
from bs4 import BeautifulSoup

def get_sub_areas(city):
    url_prefix = "https://www.rew.ca/sitemap/real-estate/"
    city_url = url_prefix + city
    html = downloader.get_html(city_url)

    soup = BeautifulSoup(html, "html.parser")
    sub_areas = soup.select(".gridblock-link")
    if sub_areas:
        for sub_area in sub_areas:
            yield sub_area.get('href').split('/')[3]
    else:
        yield city

def get_list(province):
    url_prefix = "https://www.rew.ca/sitemap/real-estate/"
    province_url = url_prefix + province
    html = downloader.get_html(province_url)

    soup = BeautifulSoup(html, "html.parser")
    areas = soup.select(".gridblock-link")
    for area in areas: 
        for i in get_sub_areas(area.get('href').split('/')[3]):
            print(i)
            with open(province + '_sub_area_list.txt', 'a') as fd:
                fd.write('%s\n' % i)

