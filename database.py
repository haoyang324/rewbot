#!/usr/bin/env python
# -*-coding:utf-8-*-

import pymysql.cursors
import re
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

connection = pymysql.connect(host=config['DEFAULT']['MYSQL_HOST'],
                            port=int(config['DEFAULT']['MYSQL_PORT']),
                             user=config['DEFAULT']['MYSQL_USER'],
                             password=config['DEFAULT']['MYSQL_PASSWORD'],
                             db=config['DEFAULT']['MYSQL_DATABASE'],
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def write_data(property):
    with connection.cursor() as cursor:
        try:
            sql = "INSERT INTO `property` (`address`, `price`, `city`, `province`, `postal_code`, `bed`, `bath`, `sqft`, `type`, `built_in`, `area`, `sub_area`, `style`, `depth`, `frontage`, `url`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(sql, (property['address'], property['price'], property['city'], property['province'], property['postal_code'], property['bed'], property['bath'], property['sqft'], property['type'],
                                 int(property['built_in']), property['area'], property['sub_area'], property['style'], property['depth'], property['frontage'], property['url']))
        except Exception as e:
            print(e)
            print("Failed property: %s" % property['address'])
            with open('fail.txt', 'a') as fd:
                fd.write('%s\n' % e)
                fd.write('%s\n\n\n' % property['address'])
    connection.commit()


def check_url_in_db(url):
    with connection.cursor() as cursor:
        sql = "SELECT `url` FROM `property` WHERE `url`= %s"
        cursor.execute(sql, url)
        result = cursor.fetchone()
    if result:
        return True
    return False
