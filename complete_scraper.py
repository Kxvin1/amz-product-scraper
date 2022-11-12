# ---------------------------------------------------------------------------------------------- #
# [SLOW] Grabs asin, price, total review rating, number of reviews and then export to csv using pandas
# ---------------------------------------------------------------------------------------------- #

# requests-html docs: https://pypi.org/project/requests-html/

# Import necessary libraries
from requests_html import HTMLSession
import pandas as pd

# user searches are typically separated by spaces, not +
user_search_term = "nvme 1tb"  # change the string here to what you want
# in amazon query, spaces are replaced with a +
amz_search_term = user_search_term.replace(" ", "+")
# target url (search results page)
url = f"https://www.amazon.com/s?k={amz_search_term}"
# Define the url to scrape
url = "https://www.amazon.com/s?k=ssd&i=computers&rh=n%3A541966&dc&qid=1580774382&rnid=2941120011&ref=sr_nr_n_1"

# Create an HTML Session object
s = HTMLSession()
# Use the object above to connect to needed webpage
r = s.get(url)
# Run JavaScript code on webpage
r.html.render(sleep=1)
# Parse HTML code
items = r.html.find("div[data-asin]")

# Create empty list to store needed data
asins = []
# Loop through the results and store each ASIN number
for item in items:
    if item.attrs["data-asin"] != "":
        asins.append(item.attrs["data-asin"])

# Create empty list to store more detailed data
products = []

# Loop through each ASIN and grab the title, price, rating, and number of reviews
for asin in asins:
    print("Gathering data for", asin)
    url = f"https://www.amazon.com/dp/{asin}"
    s = HTMLSession()
    r = s.get(url)
    r.html.render(sleep=1)

    title = r.html.find("#productTitle", first=True).full_text.strip()
    price = r.html.find(".a-offscreen", first=True).full_text
    rating = r.html.find("span.a-icon-alt", first=True).full_text
    reviews = r.html.find("#acrCustomerReviewText", first=True).full_text

    product = {
        "asin": asin,
        "title": title,
        "price": price,
        "rating": rating,
        "reviews": reviews,
    }

    products.append(product)
    print(f"Finished Grabbing Data For ASIN {asin}\nProduct Object: {product}")

    # for testing purposes so products isn't scraping a bunch of data if only testing
    if len(products) == 1:
        break

# Convert list of dictionaries into pandas DataFrame
df = pd.DataFrame(products)
# Export DataFrame into a CSV file
df.to_csv("complete_scrape.csv", index=False)
