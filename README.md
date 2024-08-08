# Amazon Products Scraper

The Amazon Product Scraper is a tool designed to extract key details from Amazon product listings using BeautifulSoup, a Python library for parsing HTML and XML documents. This scraper efficiently gathers information such as product titles, URLs, ratings, and prices, allowing users to quickly compile data from multiple products in a structured format like a spreadsheet.

Features:
Title and URL Extraction: Scrapes product titles and corresponding URLs.
Rating and Price Retrieval: Collects product ratings and prices for easy comparison.
Structured Data Output: Outputs the scraped data in a CSV or Excel format for analysis and record-keeping.
Scraping Limits:
Due to Amazon's strict policies and anti-scraping measures, the scraper has built-in limitations to ensure compliance and avoid triggering Amazon’s defenses:

Rate Limiting: Implements delays between requests to prevent IP blocking.
Captcha Handling: The scraper pauses if a CAPTCHA is encountered, alerting the user to manually resolve it.
Request Throttling: Restricts the number of requests per hour to avoid detection and maintain access.
This scraper is ideal for developers and data enthusiasts who need to gather product information from Amazon while adhering to the platform's restrictions.

Sample Output:
Here’s a glimpse of the scraper’s output:

Title: "Reebok Unisex Club C 85 Sneaker"
URL: "https://www.amazon.com/dp/B07DPL9H6H"
Rating: "4.6 out of 5 stars"
Price: "$50.00"
This tool is an efficient solution for those looking to aggregate product data from Amazon while respecting the platform's terms of service.
