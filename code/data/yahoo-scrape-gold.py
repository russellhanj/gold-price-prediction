# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# # Step 1: Define the URL for Yahoo Finance historical data
# url = "https://finance.yahoo.com/quote/GC%3DF/history/?period1=1388534400&period2=1735603200"

# # Step 2: Set up headers to mimic a browser request
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
# }

# # Step 3: Send an HTTP GET request to fetch the webpage
# response = requests.get(url, headers=headers)

# # Check for successful response
# if response.status_code == 200:
#     print("Successfully fetched the webpage.")
# else:
#     print(f"Failed to fetch webpage. Status code: {response.status_code}")
#     exit()

# # Step 4: Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Step 5: Locate the historical data table
# table = soup.find('table', {'class': 'W(100%) M(0)'})  # Class may need to be updated

# # Check if the table was found
# if not table:
#     print("Failed to find the data table on the webpage.")
#     exit()

# # Step 6: Extract rows from the table
# rows = table.find_all('tr')

# # Step 7: Parse the data rows into a list
# data = []
# for row in rows[1:]:  # Skip the header row
#     cols = row.find_all('td')
#     cols = [col.text.strip() for col in cols]
#     if len(cols) > 0:  # Skip empty rows
#         data.append(cols)

# # Step 8: Define column names for the DataFrame
# columns = ["Date", "Open", "High", "Low", "Close*", "Adj Close**", "Volume"]

# # Step 9: Create a Pandas DataFrame
# df = pd.DataFrame(data, columns=columns)

# # Step 10: Display the first few rows
# print("\nPreview of the data:")
# print(df.head())  # Displays the first 5 rows of the DataFrame

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
# import time

# # Step 1: Set up Selenium WebDriver
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")

# # Set up the path to the ChromeDriver
# driver_path = "/Users/russellhanjosef/Downloads/chromedriver-mac-arm64/chromedriver"  # Replace with your actual path to ChromeDriver
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Step 2: Define the URL
# url = "https://finance.yahoo.com/quote/GC%3DF/history/?period1=1388534400&period2=1735603200"

# # Step 3: Load the webpage
# print("Loading the webpage...")
# driver.get(url)
# time.sleep(5)  # Allow time for JavaScript to load the table

# # Step 4: Locate the table and extract data
# print("Extracting the table data...")
# rows = driver.find_elements(By.XPATH, '//table[contains(@class, "W(100%) M(0)")]/tbody/tr')

# # Parse the rows
# data = []
# for row in rows:
#     cols = row.find_elements(By.TAG_NAME, "td")
#     if len(cols) > 0:  # Skip empty rows
#         data.append([col.text.strip() for col in cols])

# # Step 5: Define column names and create DataFrame
# columns = ["Date", "Open", "High", "Low", "Close*", "Adj Close**", "Volume"]
# df = pd.DataFrame(data, columns=columns)

# # Step 6: Display the first few rows
# print("\nPreview of the data:")
# print(df.head())  # Display the first 5 rows

# Updated

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# Step 1: Set up Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set up the path to the ChromeDriver
driver_path = "/Users/russellhanjosef/Downloads/chromedriver-mac-arm64/chromedriver"  # Replace with your actual path to ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 2: Define the URL
url = "https://finance.yahoo.com/quote/GC%3DF/history/?period1=1388534400&period2=1735603200"

# Step 3: Load the webpage
print("Loading the webpage...")
driver.get(url)
time.sleep(5)  # Allow time for JavaScript to load the table

# Step 4: Locate the table and extract data
print("Extracting the table data...")
try:
    # Locate the table using the class name or XPath
    rows = driver.find_elements(By.XPATH, '//table[contains(@class, "table yf-1jecxey noDl")]/tbody/tr')

    # Parse the rows
    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) > 0:  # Skip empty rows
            data.append([col.text.strip() for col in cols])

    # Step 5: Define column names and create DataFrame
    columns = ["Date", "Open", "High", "Low", "Close*", "Adj Close**", "Volume"]
    df = pd.DataFrame(data, columns=columns)

    # Step 6: Display the first few rows
    print("\nPreview of the data:")
    print(df.head())  # Display the first 5 rows

    # Step 7: Save the data to a CSV file
    output_file = "gold_historical_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\nData has been saved to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")

# Step 8: Close the browser
driver.quit()
