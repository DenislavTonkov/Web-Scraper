# Web Scraper for HTML Documents

## Overview
The provided script defines a `WebScraper` class in Python for scraping and processing data from an HTML file called `html_doc.html`. The class uses BeautifulSoup for parsing HTML, regular expressions for text processing, and the `html` module for unescaping HTML entities.

## Class: WebScraper
- **Purpose**: To encapsulate the functionality required to scrape and process data from an HTML file.
- **Initialization (`__init__`)**: The constructor takes a path to an HTML file. It reads the file, and then uses BeautifulSoup to parse this HTML content, initializing a soup object. An empty list `products` is also initialized to store scraped data.
  
## Method: scrape
- **Functionality**: This method scrapes the HTML content to extract product information.
- **Process**:
  - **Finding Items**: It locates all `div` elements with the class `item`, representing individual products.
  - **Iterating Over Items**: For each item, it creates a dictionary `product` to store its details.
  - **Extracting Product Name**: The product name is extracted from an `h4` tag, unescaped, and stored in the dictionary.
  - **Extracting and Formatting Price**:
    - The price is extracted from a `span` with class `price-display`.
    - Non-numeric characters are removed using a regular expression.
    - The price is split into integer and decimal parts, and then formatted to two decimal places.
  - **Extracting and Normalizing Rating**:
    - The rating is extracted and converted to a float.
    - If the rating system is different (e.g., out of 10), it's normalized to a 5-point scale.
    - Ratings are then rounded appropriately and stored.
  - **Storing Product Information**: Each product dictionary is appended to the `products` list.
- **Output**: Returns the list of products with their details.

## Executing the Scraper
The script concludes with creating an instance of `WebScraper`, providing it with the path to `html_doc.html`, and then calling the `scrape` method. The results are printed to the console.


