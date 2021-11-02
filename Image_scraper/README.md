# Image scraper

### This program web scrapes images from search engines

Use as:

```
from Image_scraper import ImageScrapper

image_scraper = ImageScrapper(save_path='\\saved_images', engine='Google')

image_scraper.search_and_download(search_term='Cats in hats', number_images=3)

```

Reconfigure search engine:

```
image_scraper.configure_engine('Duckduckgo')
```

Search operation such as exact match:

```
image_scraper.search_and_download(search_term='Cat in wig', number_images=7, exact_match=True)
```

Exclude words and phrases from search:

```
shroom = 'Inocybe geophylla  -lilacina'

image_scraper.search_and_download(search_term=shroom, number_images=number_images, exact_match=True)
```

### Todo:
    
* Add Bing, Pinterest
* time efficiency
* Add chromedriver installation notes
