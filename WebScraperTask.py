from bs4 import BeautifulSoup  # Import BeautifulSoup for parsing HTML
import re  # Import the re module for regular expressions
import html  # Import the html module for unescaping HTML characters


class WebScraper:  # Define a class for web scraping

    def __init__(self, html_file_path):  # Constructor for the WebScraper class
        with open(html_file_path, "r") as HTMLFile:  # Open the HTML file
            reader = HTMLFile.read()  # Read the content of the HTML file
            self.soup = BeautifulSoup(reader, 'html.parser')  # Parse the HTML content
            self.products = []  # Initialize an empty list to store the products

    def scrape(self):  # Method to scrape the HTML content
        items = self.soup.find_all('div', class_='item')  # Find all div elements with the class 'item'

        for item in items:  # Iterate through each item
            product = {}  # Create a dictionary to store product information
            product_name = html.unescape(item.find('h4').text.strip())  # Extract and unescape the product name
            product['productName'] = product_name  # Store the product name in the dictionary

            price_string = item.find('span', class_='price-display').text  # Extract the price string
            price = re.sub(r'[^\d.]', '', price_string)  # Remove non-numeric characters from the price

            parts = price.split('.')  # Split the price into integer and decimal parts

            integer_part = parts[0]  # Extract the integer part of the price
            decimal_part = parts[1][:2]  # Extract the first two digits of the decimal part
            two_decimal_price = f"{integer_part}.{decimal_part}"  # Construct the price with two decimal places

            product['price'] = two_decimal_price  # Store the formatted price in the dictionary

            rating = float(item['rating'])  # Extract the rating as a float
            rating = (rating / 10) * 5 if rating > 5 else rating  # Normalize the rating if it's on a different scale
            if rating.is_integer():  # Check if the rating is an integer
                product['rating'] = int(rating)  # Store the integer rating in the dictionary
            else:
                product['rating'] = round(rating, 1)  # Store the rounded rating with one decimal place in the dictionary

            self.products.append(product)  # Append the product dictionary to the list of products

        return self.products  # Return the list of products


html_file_path = "html_doc.html"  # Replace with the actual file path
scraper = WebScraper(html_file_path)  # Create an instance of the WebScraper class
results = scraper.scrape()  # Call the scrape method to extract product information
print(results)  # Print the extracted product information