#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
# import cfscrape
import cloudscraper

# scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
scraper = cloudscraper.create_scraper() 

headers = {
    'User-Agent	' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15', 
}

def get_html(url, Referer_url=None):
    '''get_html(url),download and return html'''
    if Referer_url:
        headers['Referer'] = Referer_url
    req = scraper.get(url, headers=headers)
    return req.content
