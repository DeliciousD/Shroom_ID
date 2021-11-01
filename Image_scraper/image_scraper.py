import time
import os
from PIL import Image
from tqdm.notebook import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
import hashlib
from bs4 import BeautifulSoup

class ImageScrapper():

    def __init__(self, save_path='', engine='Google'):
        self.save_path = os.getcwd() + save_path
        self.engine = engine
        self.configure_engine(self.engine)

    def configure_engine(self, engine):

        self.engine = engine

        if engine.lower() == 'bing':
            self.search_url = 'http://www.bing.com/images/search?q={q}&FORM=HDRSC2'
            self.thumbnail_selector = ''

        elif engine.lower() == 'duckduckgo':
            self.search_url = 'https://duckduckgo.com/?q={q}&t=h_&iax=images&ia=images'
            self.thumbnail_selector = 'img.js-lazyload'
            self.image_selector = 'img.js-detail-img-high'
            self.load_more_button = '' # has no load more button

        elif engine.lower() == 'pinterest':
            self.search_url = 'https://www.pinterest.co.uk/search/pins/?q={q}'

        else:
            self.search_url = 'https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img'
            self.thumbnail_selector = 'img.Q4LuWd'
            self.image_selector = 'img.n3VNCb'
            self.load_more_button = '.mye4qd'


    def scroll_to_bottom(self, wd:webdriver):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)


    def fetch_image_urls(self, max_links_to_fetch:int, wd:webdriver, exact_match=False):

        if exact_match:
            wd.get(self.search_url.format(q = '"' + self.search_term + '"'))
        else:
            wd.get(self.search_url.format(q = self.search_term))

        image_urls = set()
        image_count = 0
        results_start = 0

        # Scroll to the bottom several times to reveal more images
        [self.scroll_to_bottom(wd=wd) for _ in range(3)]

        while image_count < max_links_to_fetch:

            self.scroll_to_bottom(wd)

            # get all image thumbnail results
            thumbnail_results = wd.find_elements(By.CSS_SELECTOR, self.thumbnail_selector)

            number_results = len(thumbnail_results)

            for img in tqdm(thumbnail_results[results_start:number_results],
                            desc=f'Extracting {max_links_to_fetch} links from {number_results} {self.engine} results',
                            position=0,
                            leave=False):

                # click thumbnails to retrieve image
                try:
                    img.click()
                    time.sleep(0.25)
                except Exception as e:
                    print('Failed to click thumbnail')
                    continue

                # extract image urls
                actual_images = wd.find_elements(By.CSS_SELECTOR, self.image_selector)

                for actual_image in actual_images:

                    if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                        image_urls.add(actual_image.get_attribute('src'))

                image_count = len(image_urls)

                if len(image_urls) >= max_links_to_fetch:
                    break

            else:

                try:
                    print('Retrieving more results')
                    time.sleep(2)

                    return image_urls
                    load_more_button = wd.find_elements(By.CSS_SELECTOR, self.load_more_button)
                    if load_more_button:
                        wd.execute_script("document.querySelector('.mye4qd').click();")   # This .mye4qd is specific to google
                except Exception as e:
                    print(f'Failed to retrieve more images: {e}')

            # move the result startpoint further down
            results_start = len(thumbnail_results)

        return image_urls

    def persist_image(self, url:str):

        try:
            image_content = requests.get(url).content
        except Exception as e:
            print(f'Failed to access image URL - {e}')

        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            file_path = os.path.join(self.target_folder, hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')

            with open(file_path, 'wb') as f:
                image.save(f, 'JPEG', quality=85)
        except Exception as e:
            print(f'Could not save image URL - {e}')

    def search_and_download(self, search_term:str, number_images=1 , exact_match=False):

        self.search_term = search_term

        self.target_folder = os.path.join(self.save_path, '_'.join(self.search_term.lower().split(' ')).replace('"', ''))

        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)

        with webdriver.Chrome() as wd:
            res = self.fetch_image_urls(
                max_links_to_fetch=number_images,
                wd=wd,
                exact_match=exact_match)

        # saving images
        try:
            for elem in tqdm(res, desc=f'Saving Images: ', position=1, leave=False):
                self.persist_image(elem)
        except Exception as e:
            print(f'Failed to save images: {e}')


if __name__ == '__main__':

    searcher = ImageScrapper(engine='Duckduckgo', save_path='./images_test')

    searcher.search_and_download(search_term='Cats in red hats', number_images=10, exact_match=True)
    