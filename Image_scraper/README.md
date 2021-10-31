# Image scraper

This program downloads images from Google and Duckduckgo

Usage as follows:

```
from Image_scraper import ImageScrapper

image_scraper = ImageScrapper(save_path='\\saved_images', engine='Google')

image_scraper.search_and_download(search_term='Cats in hats', number_images=3)

```

Which can be reconfigured for other engines and use search operation such as exact matches

```
image_scraper.configure_engine('Duckduckgo')

image_scraper.search_and_download(search_term='Cat in wig', number_images=7, exact_match=True)
```


### Todo:
    
* Add Bing, Pinterest
* time efficiency
* Fix load more button issue
* Add chromedriver installation notes
