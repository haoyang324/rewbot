from bs4 import BeautifulSoup
import re

def get_urls(html):
    """get_urls(html), parser every property's url on one page"""

    soup = BeautifulSoup(html,"html.parser")
    
    for property_html in soup.select('.displaypanel-photo_container > a'):
        yield "https://www.rew.ca" + property_html.get('href').split('?')[0]


def get_next_page_urls(html):

    soup = BeautifulSoup(html, "html.parser")
    if soup.select_one('.paginator-next_page a'):
        return "https://www.rew.ca" + soup.select_one('.paginator-next_page a').get('href').split('?')[0]


def parse_content(html):
    soup = BeautifulSoup(html,"html.parser")

    if not soup.select_one(".propertyheader-address > span"):
        return None

    property_dict = {}
    
    property_dict['address'] = soup.select_one(".propertyheader-address > span").string.strip()
    property_dict['price'] = re.sub(r'[^\d.]', '', soup.select_one(".propertyheader-price").string.strip())
    property_dict['city'] = soup.select(".propertyheader-secondary span")[0].string.strip()
    property_dict['province'] = soup.select(".propertyheader-secondary span")[1].string.strip()
    property_dict['postal_code'] = soup.select(".propertyheader-secondary span")[2].string.strip() if len(soup.select(".propertyheader-secondary span")) == 3 else None
    property_dict['bed'] = soup.select(".clearfix strong")[0].string.strip()
    property_dict['bath'] = soup.select(".clearfix strong")[1].string.strip()
    property_dict['sqft'] = soup.select(".clearfix strong")[2].string.strip() if soup.select(".clearfix strong")[2].string.strip() != 'N/A' else 0
    property_dict['type'] = soup.select(".clearfix strong")[3].string.strip()

    property_age_tag = soup.find('th', text="Property Age")
    property_dict['built_in'] = re.search(r'\d{4}', property_age_tag.parent.select_one("td").string.strip()).group(0) if property_age_tag else 0
    
    area_tag = soup.find('th', text="Area")
    property_dict['area'] = area_tag.parent.select_one("td").string.strip() if area_tag else ''
    
    sub_area_tag = soup.find('th', text="Sub-Area/Community")
    property_dict['sub_area'] = sub_area_tag.parent.select_one("td").string.strip() if sub_area_tag else ''

    style_tag = soup.find('th', text="Style")
    property_dict['style'] = style_tag.parent.select_one("td").string.strip() if style_tag else ''

    depth_tag = soup.find('th', text="Depth")
    property_dict['depth'] = depth_tag.parent.select_one("td").string.strip() if depth_tag else None

    frontage_tag = soup.find('th', text="Frontage")
    # property_dict['frontage'] = re.search(r'\d+.\d{2}', frontage_tag.parent.select_one("td").string.strip()).group(0) if frontage_tag else None # Reserved for getting decimal values 
    property_dict['frontage'] = frontage_tag.parent.select_one("td").string.strip() if frontage_tag else None
    return property_dict