#!/usr/bin/env python
# -*-coding:utf-8-*-

import requests
# import cfscrape
import cloudscraper
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

# scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance
scraper = cloudscraper.create_scraper()

headers = {
    'User-Agent	': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
}


def get_html(url, Referer_url=None):
    '''get_html(url),download and return html'''
    proxies = {"http": config['DEFAULT']['HTTP_PROXY']}
    if Referer_url:
        headers['Referer'] = Referer_url
    req = scraper.get(url, headers=headers, proxies=proxies)
    return req.content
