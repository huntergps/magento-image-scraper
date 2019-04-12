# Magento Image Scraper
## Overview
Python script for scraping product images from a Magento site and saving in local directories named after the products.

## Install & Requirements
Written in Python 3.7
This program utilises BeautifulSoup 4 and urllib to download all the images from the product pages that are listed in the sitemap page of the site. 
It creates local directories if not already present and names those after the product url. Images are them saved to the directory and named after the product name / url plus and incremented number.

## Why I Created This
I created this script in order to migrate the product images from a Magento site to a Woocommerce site and wanted the images in a better organised structure than magento cache structure that is not user friendly or intuitive for seeing which image should be assigned to which product.

## Notes
It has only been tested on Magento 1.9 and Local OS of Windows 10. It could of course be used to scrape site by simply adjusting the correct html tags, classes etc used for identifying the images links.
If using you should be careful in case your hosting blocks or throttles your IP if it think the scraper is malicious activity. You can enabled the 1 second pause if you want to help avoid this.
