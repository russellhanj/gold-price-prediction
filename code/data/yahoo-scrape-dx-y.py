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

# Step 2: Define the URL (Updated)
url = "https://finance.yahoo.com/quote/DX-Y.NYB/history/?period1=1388534400&period2=1735603200"

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
    output_file = "dx_y_historical_data.csv"
    df.to_csv(output_file, index=False)
    print(f"\nData has been saved to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")

# Step 8: Close the browser
driver.quit()
