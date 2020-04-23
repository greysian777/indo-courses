from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from tqdm import tqdm
from typing import List
from dataclasses import dataclass
from pathlib import Path
import time
from selenium.webdriver.chrome.options import Options


@dataclass
class Scraper():
    url: str = None
    titles: List = None
    chrome_options = Options()
    prefs = {}
    chrome_options.experimental_options['prefs'] = prefs
    # prefs["profile.default_content_settings"] = {"images": 2}
    # prefs["profile.managed_default_content_settings"] = {"images": 2}
    chrome_options.add_argument("--disable-popup-blocking")
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path=r'../../chromedriver', options=chrome_options)

    def set_url(self, url):
        self.url = url
        self.driver.get(self.url)

    def get_title(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        titles = soup.find_all('h5', {'data-testid': 'category-course-title'})
        self.titles = [t.text for t in titles]

    def save_to_txt(self, name, list_save=None, output_path=None):
        sumber = self.url.split('/')[-2]
        if output_path is None:
            output_path = './'
        if list_save:
            self.titles = list_save
        if self.titles is not None:
            with open(f'{output_path}{name}-{sumber}.txt', 'w') as f:
                for a in self.titles:
                    f.writelines(f'{a}\n')
            print('saved')
        else:
            print('skipped cause no gems')
        return True

    def get_all_a(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        a = soup.find_all('a')
        hasil = []
        for link in a:
            try:
                hasil.append(link['href'])
            except:
                pass
        self.titles = list(set(hasil))

    def get_course_content_mba(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        titles = soup.find_all('a', class_='post-title')
        self.titles = set([t.text.strip() for t in titles])

    # pjm
    def get_cards(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        time.sleep(30)
        cards = soup.find_all('p')
        for c in cards:
            print(c.text)
            input('enter to continue')

    def get_title_idx(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        titles= soup.find_all('h4', class_='course-card__title')
        self.titles = [t.text for t in titles]



    def quit(self):
        self.driver.quit()


def skillacademy():
    skillacademy = Scraper()
    courses = {
        'teknologi': 'https://skillacademy.com/courses/CAT-I25XOX83',
        'bisnis': 'https://skillacademy.com/courses/CAT-HT1X5Q6E',
        'selfhelp': 'https://skillacademy.com/courses/CAT-DZYYVTRF',
        'persiapan_tes': 'https://skillacademy.com/courses/CAT-IWEODQGX',
        'webinar': 'https://skillacademy.com/courses/CAT-MFJ12D81'
    }
    for course_name, course_link in courses.items():

        skillacademy.set_url(course_link)
        skillacademy.get_title()
        skillacademy.save_to_txt(course_name)
    time.sleep(10)
    skillacademy.quit()


def maubelajarapa():
    belajar = Scraper()
    # belajar.set_url('https://maubelajarapa.com/')
    # belajar.save_to_txt('belajar_link',belajar.get_all_a())
    belajar_links = open('./belajar_link-.txt').read().splitlines()
    for i, link in enumerate(belajar_links):
        belajar.set_url(link)
        belajar.get_course_content_mba()
        belajar.save_to_txt(f'{i}_mba', output_path='mba/')
        # input('enter')

    belajar.quit()


def pijarmahir():
    pj = Scraper()
    pj.set_url('https://pijarmahir.id/filter-materi/Semua')
    pj.get_cards()
    # pj.save_to_txt('pjm_link', pj.get_all_a())

def indonesiax():
    idn = Scraper()
    idn.set_url('https://www.indonesiax.co.id/courses')
    idn.get_title_idx()
    idn.save_to_txt('indonesiax')

def kelaskita():
    kk = Scraper()
    kk.set_url('https://kelaskita.com/index/kategori/')
    kk.get_all_a()
    kk.save_to_txt('kelaskita-links')
    kk.quit()


if __name__ == "__main__":
    # maubelajarapa()
    # pijarmahir()
    # indonesiax()
    kelaskita()
