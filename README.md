### Web Scraper for Amazon.com products

---

### Technology Used

![python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![amazon](https://img.shields.io/badge/Amazon-FF9900.svg?style=for-the-badge&logo=Amazon&logoColor=white)

---

### See it in action with a video example:
https://user-images.githubusercontent.com/91479661/201498309-da533957-c8ae-4737-8ddd-ec39c49049ca.mp4


---

### How to use:

###### [FAST] Option 1: Scrape product ASINs only and exports to csv under 1 column
```bash
Step 1: Open asin_only_scraper.py and edit the args at the very bottom (examples included)

Step 2: Run the asin_only_scraper.py script in the terminal (without quotes): 'python asin_only_scraper.py'

Step 3: After the script finishes you will see a newly created csv file that 
contains all ASINs for each product on the first page of your search term
```

###### [SLOW] Option 2: Scrape asin, price, total review rating, number of reviews and then export to csv under 5 columns (ASIN, Title, Price, Rating, Reviews)
```bash
Step 1: Open complete_scraper.py and edit the args at the very bottom (examples included)

Step 2: Run the complete_scraper.py script in the terminal (without quotes): 'python complete_scraper.py'

Step 3: After the script finishes you will see a newly created csv file that contains all details 
for each product (ASIN, title, price, rating, reviews) on the first page of your search term
```

---

### Todo:

###### 1. Add both functionalities to JARVIS (my discord bot)
###### 2. Speed up scraping (one of these?: multithreading, multiprocessing, asyncio)
###### 3. Pagination option if results are wanted for products past the first page
