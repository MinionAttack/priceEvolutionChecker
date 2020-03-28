#!/usr/bin/python3
#  -*- coding: utf-8 -*-

###############################################
##  Author: MinionAttack                     ##
##  GitHub: https://github.com/MinionAttack  ##
###############################################

import csv
from decimal import Decimal
from pathlib import Path
from time import strftime, localtime

import requests
from lxml.html import fromstring
from progress.bar import FillingCirclesBar

from mm_components import MBs

__COMPONENTS_LIST = [MBs]

__header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Charset': 'UTF-8',
    'DNT': str(1),
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
    'Upgrade-Insecure-Requests': str(1)
}


def get_path_and_create_if_not_exists(family_name):
    user_home = Path.home()
    data_folder = user_home / 'priceCheckerHistory'
    Path(data_folder).mkdir(mode=0o777, parents=True, exist_ok=True)
    family_folder = data_folder / family_name
    Path(family_folder).mkdir(mode=0o777, parents=True, exist_ok=True)

    return family_folder


def write_data_to_csv(family_type, brand_name, items):
    family_path = get_path_and_create_if_not_exists(family_type)
    brand_file = family_path / (brand_name + '.csv')
    columns_headers = ['Product name', 'Normal price', 'Reduced price', 'Discount', 'Date']
    with open(brand_file, mode='a', buffering=1, encoding='utf-8', errors='strict', newline='', closefd=True) as file:
        writer = csv.DictWriter(file, fieldnames=columns_headers, dialect='excel')
        writer.writeheader()
        for item in items:
            product_name = item.get('name')
            normal_price = item.get('price')
            reduced_price = item.get('reduced_price')
            discount = item.get('discount')
            if reduced_price is None and discount is None:
                reduced_price = ''
                discount = ''
            actual_date = strftime("%A, %d %B %Y %H:%M:%S UTC %z", localtime())
            writer.writerow({'Product name': product_name, 'Normal price': normal_price, 'Reduced price': reduced_price,
                             'Discount': discount, 'Date': actual_date})


def process_items(items):
    processed_items = []
    index = 1
    number_of_items = len(items)
    progress_bar = FillingCirclesBar('Processing pages', max=number_of_items)

    for item in items:
        product_name = item.xpath('.//a[@class="productName product1Name"]/span')[0].text_content().strip()
        actual_price = item.xpath('.//div[@class="mm-price media__price"]')[0].text_content().strip()
        processed_item = {'name': product_name, 'price': Decimal(actual_price), 'reduced_price': None, 'discount': None}
        processed_items.append(processed_item)
        index = index + 1
        progress_bar.next()
    progress_bar.finish()

    return processed_items


def process_data(url, brand_id, items_per_page):
    url_parameters = 'm/{}/ajax?perPage={}'.format(brand_id, items_per_page)
    url_with_parameters = url + url_parameters
    processed_data = []
    try:
        html_response = requests.get(url_with_parameters, headers=__header, timeout=5)
        if html_response.status_code == requests.codes.ok:
            content = html_response.content
            fixed_content = fromstring(content)  # parse the HTML and correct malformed HTML
            items = fixed_content.xpath('//ul/li')
            processed_items = process_items(items)
            processed_data.extend(processed_items)
        else:
            print("Warning, status code: {}".format(html_response.status_code))
        html_response.cookies.clear()
    except requests.exceptions.HTTPError as http_error:
        print("Http Error: {} \nURL: {}".format(http_error, url_with_parameters))
    except requests.exceptions.ConnectionError as connection_error:
        print("Error Connecting: {} \nURL: {}".format(connection_error, url_with_parameters))
    except requests.exceptions.Timeout as timeout_error:
        print("Timeout Error: {} \nURL: {}".format(timeout_error, url_with_parameters))
    except requests.exceptions.TooManyRedirects as too_many_redirects_error:
        print("Too Many Redirects Error: {} \nURL: {}".format(too_many_redirects_error, url_with_parameters))
    except requests.exceptions.RequestException as request_exception:
        print("Request Exception: {} \nURL: {}".format(request_exception, url_with_parameters))

    return processed_data


def request_data(url, brand_id):
    add_brand = 'm/{}'.format(brand_id)
    url_with_parameters = url + add_brand
    data_content = []
    try:
        html_response = requests.get(url_with_parameters, headers=__header, timeout=5)
        if html_response.status_code == requests.codes.ok:
            html_response.encoding = 'utf-8'
            content = html_response.content
            fixed_content = fromstring(content)  # parse the HTML and correct malformed HTML
            items_per_page_node = fixed_content.xpath('/html/body/div[2]/div/div[2]/div[2]/div[2]/div/form['
                                                      '1]/div/div[2]/div[2]/select')
            items_per_page_node_options = items_per_page_node[0].value_options
            last_option = len(items_per_page_node_options) - 1
            items_per_page = items_per_page_node_options[last_option]
            processed_data = process_data(url, brand_id, items_per_page)
            data_content.extend(processed_data)
        else:
            print("Warning, status code: {}".format(html_response.status_code))
        html_response.cookies.clear()
    except requests.exceptions.HTTPError as http_error:
        print("Http Error: {} \nURL: {}".format(http_error, url_with_parameters))
    except requests.exceptions.ConnectionError as connection_error:
        print("Error Connecting: {} \nURL: {}".format(connection_error, url_with_parameters))
    except requests.exceptions.Timeout as timeout_error:
        print("Timeout Error: {} \nURL: {}".format(timeout_error, url_with_parameters))
    except requests.exceptions.TooManyRedirects as too_many_redirects_error:
        print("Too Many Redirects Error: {} \nURL: {}".format(too_many_redirects_error, url_with_parameters))
    except requests.exceptions.RequestException as request_exception:
        print("Request Exception: {} \nURL: {}".format(request_exception, url_with_parameters))

    return data_content


def collect_components():
    for component in __COMPONENTS_LIST:
        family_type = component['TYPE']
        url = component['URL']
        brands = component['BRANDS']
        for brand in brands.items():
            brand_id = brand[1]
            result = request_data(url, brand_id)
            if len(result) > 0:
                write_data_to_csv(family_type, brand_id.title(), result)


if __name__ == '__main__':
    collect_components()
