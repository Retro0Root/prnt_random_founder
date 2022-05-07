import random
import string
import constants
import urllib3
from bs4 import BeautifulSoup
import os

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_random_number():
    return random.randint(1000, 9999)


def get_content_url(url):
    # Get source code
    http = urllib3.PoolManager()
    response = http.request('GET', url)

    # Get images
    soup_mysite = BeautifulSoup(response.data, 'html.parser')
    images = soup_mysite.find_all("img", {"class": "screenshot-image"})
    urlImage = images[0]['src']
    finalPath = constants.FINAL_PATH + get_random_string(5) + '.png'
    os.system("wget -O {0} {1}".format(finalPath, urlImage))

def main():
    for i in range(constants.ITERATIONS):
        urlToCheck = constants.URL_PRNT + get_random_string(2) + str(get_random_number())
        get_content_url(urlToCheck)
        print(urlToCheck)

main()