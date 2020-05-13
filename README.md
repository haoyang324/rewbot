# rewbot

``` sql
CREATE TABLE IF NOT EXISTS `rew`.`property` ( 
    `address` VARCHAR(80) NOT NULL, 
    `price` DECIMAL(8) NOT NULL, 
    `city` VARCHAR(80) NOT NULL, 
    `province` VARCHAR(20) NOT NULL, 
    `postal_code` VARCHAR(20), 
    `bed` VARCHAR NOT NULL, 
    `bath` VARCHAR(4) NOT NULL, 
    `sqft` DECIMAL(8), 
    `type` VARCHAR(20) NOT NULL, 
    `built_in` SMALLINT, 
    `area` VARCHAR(20), 
    `sub_area` VARCHAR(80), 
    `style` VARCHAR(80), 
    `depth` VARCHAR(20), 
    `frontage` VARCHAR(20), 
    `url` VARCHAR(255), 
    PRIMARY KEY (`address`)) ENGINE = InnoDB;
```

For Ubuntu
``` bash
sudo apt upgrade
sudo apt update
sudo apt install python3.7 python3-pip nodejs  -y
pip3 install BeautifulSoup pymysql configparser
```