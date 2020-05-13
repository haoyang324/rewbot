#!/usr/bin/env python
#-*-coding:utf-8-*-

from bs4 import BeautifulSoup
import time
import re

import downloader
import htmlparser
import database


def main(entrance_url):
    current_page = downloader.get_html(entrance_url)
    urls = htmlparser.get_urls(current_page)
    for url in urls:
        if not database.check_url_in_db(url):
            time.sleep(3)
            print("Working on " + url)
            html = downloader.get_html(url)
            property_dict = htmlparser.parse_content(html)
            if property_dict:
                property_dict['url'] = url
                database.write_data(property_dict)
            else: 
                print("Nothing here " + url)
#         else: 
#             print("Already have it " + url)
    print("Done with " + entrance_url)
    
    next_page_url = htmlparser.get_next_page_urls(current_page)
    if next_page_url:
        main(next_page_url)


if __name__ == '__main__':
    with open('bc_sub_area_list.txt', 'r+') as fd:
        for line in fd:   
            main("https://www.rew.ca/properties/areas/" + line.strip())
        # fd.truncate(0)
    # main('https://www.rew.ca/properties/areas/vancouver-bc')

