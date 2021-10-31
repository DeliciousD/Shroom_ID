# Shroom scraping

*   UK mushroom info from: https://www.wildfooduk.com/mushroom-guide/?mushroom_orderby=latin_name&mushroom_order=ASC
    Search engine image scrapping

Todo:
    
    Grab from FGVCx Fungi dataset https://github.com/visipedia/fgvcx_fungi_comp
    
    use does not include search operator "Inocybe geophylla"  -"var. lilacina"
    
    Remove microscope images


# Shroom classification

Possible avenues:
    
    Include season for classification
    
    Use googles labeled images of mushrooms to identify locations of mushroom in the scraped images, creating new images for each mushroom indentified in scaped image, discarding those not found.
    
    https://storage.googleapis.com/openimages/web/visualizer/index.html?set=train&type=segmentation&r=false&c=%2Fm%2F052sf
    https://storage.googleapis.com/openimages/web/download.html#download_using_fiftyone
    
    Use confusion matrix to compare for likely mistakes
    