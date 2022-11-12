# ---------------------------------------------------------------------------------------------- #
# [SLOW] Grabs asin, price, total review rating, number of reviews and then export to csv using pandas
# ---------------------------------------------------------------------------------------------- #

# requests-html docs: https://pypi.org/project/requests-html/

# Import necessary libraries
from requests_html import HTMLSession
import pandas as pd
from pprint import pprint as pprint
import json

# loading icon library
from yaspin import yaspin


def complete_scraper(search_term, filename):
    # user searches are typically separated by spaces, not +
    user_search_term = search_term  # change the string here to what you want
    # in amazon query, spaces are replaced with a +
    amz_search_term = user_search_term.replace(" ", "+")
    # target url (search results page)
    url = f"https://www.amazon.com/s?k={amz_search_term}"

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

    with yaspin(text="Fetching ASIN data", color="cyan") as sp:
        # Loop through each ASIN and grab the title, price, rating, and number of reviews
        for asin in asins:
            sp.write(f"Current ASIN: {asin}")
            url = f"https://www.amazon.com/dp/{asin}"

            # start the session
            s = HTMLSession()
            # get the request url
            r = s.get(url)
            # required so amazon doesn't block you (it won't think you're a bot)
            # timeout 20 in case the request takes longer than 20 seconds
            r.html.render(sleep=1, timeout=20)

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
            sp.write(f"Finished Grabbing Data For ASIN {asin}")
            sp.write(json.dumps(product, indent=4))
            sp.write("-------------------------")

            # for testing purposes so products isn't scraping a bunch of data if only testing
            if len(products) == 2:
                sp.ok("✔")
                break

        # once loop is finished, change loading icon to a green check mark
        # sp.ok("✔")

    print(
        f"Finished writing data for search query: '{user_search_term}'\nExported to {filename}.csv"
    )

    # Convert list of dictionaries into pandas DataFrame
    df = pd.DataFrame(products)
    # Export DataFrame into a CSV file
    df.to_csv(f"{filename}.csv", index=False)


# CHANGE ARGS HERE: complete_scraper(your_search_term, your_desired_file_name)
complete_scraper("nvme 1tb", "test")
