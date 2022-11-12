# ---------------------------------------------------------------------------------------------- #
# [FAST] Grabs asins only and export to csv using pandas
# ---------------------------------------------------------------------------------------------- #

# requests-html docs: https://pypi.org/project/requests-html/

# Import necessary libraries
import pandas as pd
from requests_html import HTMLSession

# user searches are typically separated by spaces, not +
user_search_term = "nvme 1tb"  # change the string here to what you want
# in amazon query, spaces are replaced with a +
amz_search_term = user_search_term.replace(" ", "+")
# target url (search results page)
url = f"https://www.amazon.com/s?k={amz_search_term}"

# start the session
s = HTMLSession()
# get the request url
r = s.get(url)
# required so amazon doesn't block you (it won't think you're a bot)
r.html.render(sleep=1)

# 'products' is an array of objects, we look in the html and find the data-asin key and extract the value (the asin)
products = r.html.find("div[data-asin]")
# append to empty list, in the real program this will be exported to a csv
asins = []
for product in products:
    # if the asin isn't an empty string,
    if product.attrs["data-asin"] != "":
        # append it to our output list
        asins.append(product.attrs["data-asin"])

# example of exporting to csv using pandas
# # Convert list of dictionaries into pandas DataFrame
df = pd.DataFrame(asins)
# # Export DataFrame into a CSV file
df.to_csv("asins_only.csv", index=False)
