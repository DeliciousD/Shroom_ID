# Shroom_ID


A machine learning application in aid of identifying British mushroom species


This is particularly useful for an initial guess as to what the species may be and for cross referencing with a reliable source


description of the app....


#### ______________ Notes on Dataset & App _____________________

There are several alternate apps and databases available online, 
however they tend to be limited in the number of quality images and have a huge number of classes, 
many of which are not found in the UK.

I have curated this database using a combination of my own images acquired while foraging and an image scraping tool (https://github.com/DeliciousD/Shroom_ID/tree/master/Image_scraper) 
I have developed to retrieve around 400 hundred images from several search engines, of roughly 150 UK mushroom species

While grabbing whatever results a search engine spits out typically would not make for a good dataset, the fact that we can specify an exact match to a mushrooms Binomial name, greatly enhances the dataset quality. 

Further, we can remove similar species or varieties from the search such as:

```
shroom = 'Inocybe geophylla  -lilacina'

image_scraper.search_and_download(search_term=shroom, number_images=number_images, exact_match=True)
```

Which allows us to distinguish between the two varieties of Inocybe_geophylla and Inocybe_geophylla var.lilacina

I also have also glancingly reviewed much of the dataset by eye, checking for obvious misclassifications, poor quality images and the occasional random image.


________ further notes on dataset _____________

I hope future iterations of the database will weed out poor quality of incorrectly classified images

The dataset will be uploaded to kaggle

I intend to integrate more data sources for a larger collection

The app, likely to be streamlit based initially, will allow users to upload images to the database


#### _________________ Disclaimer _____________________

This is NOT purporting to be a one-stop solution for identifying mushrooms

Information given here MUST cross reference with AT LEAST two credible references (see below)

NEVER consume any wild mushroom unless you are certain of what it is


#### ________________ Why you should be in a forest right now _____________________

Why mushroom foraging is cool, references to books

### ________________ How to use Image_Scraper ____________________(to be its own repo)
