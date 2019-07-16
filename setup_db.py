#!/usr/bin/env python
import os
import sys
import requests
import tarfile
import shutil


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


if __name__ == "__main__":
    print("Setting up DB...")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    EXTRACT_PATH = os.path.join(BASE_DIR, 'geoip-api/geoip/temp')
    DB_DIR_PATH = os.path.join(BASE_DIR, 'geoip-api/geoip/GeoLite2-City')

    if not os.path.exists(DB_DIR_PATH):
        os.makedirs(DB_DIR_PATH)
    if not os.path.exists(EXTRACT_PATH):
        os.makedirs(EXTRACT_PATH)

    DB_TEMP_PATH = os.path.join(EXTRACT_PATH, 'GeoLite2-City.tar.gz')
    # Gets DB from:  https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
    url = 'https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz'
    r = requests.get(url)
    print(DB_TEMP_PATH)
    with open(DB_TEMP_PATH, 'wb') as f:
        f.write(r.content)

    tar = tarfile.open(DB_TEMP_PATH, "r:gz")
    tar.extractall(path=EXTRACT_PATH)
    tar.close()

    db_file = find('GeoLite2-City.mmdb', EXTRACT_PATH)

    shutil.move(db_file, os.path.join(DB_DIR_PATH, 'GeoLite2-City.mmdb'))
