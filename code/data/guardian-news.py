import requests
from dotenv import load_dotenv
import csv
import os

load_dotenv()  
GUARDIAN_API_KEY = os.getenv("GUARDIAN_API_KEY")

def fetch_guardian_headlines(
    query="gold price",
    from_date="2024-01-01",
    to_date="2024-12-31",
    page_size=200,
    max_pages=50,
    show_fields="headline",
    section="money"
):
    """
    Fetch headlines from The Guardian's API, given a query, date range, and optional section filter.
    
    - query: Keywords to search, e.g., "gold price"
    - from_date, to_date: YYYY-MM-DD for the start/end of the period
    - page_size: # of items per page (max ~200 for Guardian)
    - max_pages: limit on how many pages to fetch to avoid infinite loops
    - show_fields: e.g. 'headline', 'all'
    - section: Filter by Guardian section, e.g. 'money', 'business'; set to None for no filter
    
    Returns a list of (headline, publication_date, section_name) tuples.
    """
    base_url = "https://content.guardianapis.com/search"
    all_headlines = []

    # Pagination loop
    for page in range(1, max_pages + 1):
        params = {
            "api-key": GUARDIAN_API_KEY,
            "q": query,
            "from-date": from_date,
            "to-date": to_date,
            "page-size": page_size,
            "page": page,
            "show-fields": show_fields,
        }
        # If a section is specified, add it to params
        if section:
            params["section"] = section

        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print(f"Request failed with status code {response.status_code}")
            break

        data = response.json()
        if "response" not in data:
            print("Invalid response format.")
            break

        results = data["response"].get("results", [])
        if not results:
            # No more articles => stop
            break

        for article in results:
            fields = article.get("fields", {})
            headline = fields.get("headline", "No headline")
            pub_date = article.get("webPublicationDate", "No date")
            section_name = article.get("sectionName", "No section")
            all_headlines.append((headline, pub_date, section_name))

        # Print progress info
        current_page = data["response"].get("currentPage", page)
        total_pages = data["response"].get("pages", page)
        print(f"Fetched page {current_page} of {total_pages} - {len(results)} articles")

        # If we've reached the last page, stop
        if current_page >= total_pages:
            break

    return all_headlines


def save_headlines_to_csv(headlines, filename):
    """
    Save the list of headlines to a CSV file with columns: headline, publication_date, section_name.
    """
    # Ensure output directory exists (optional)
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["headline", "publication_date", "section_name"])
        writer.writerows(headlines)
    print(f"Saved {len(headlines)} records to {filename}")


if __name__ == "__main__":
    # Example usage: pulling headlines from 2014 to 2024, year by year
    start_year = 2014
    end_year = 2024

    for year in range(start_year, end_year + 1):
        from_date = f"{year}-01-01"
        to_date = f"{year}-12-31"

        print(f"\n=== Fetching headlines for {year} ===")
        headlines_data = fetch_guardian_headlines(
            query="gold price",
            from_date=from_date,
            to_date=to_date,
            page_size=200,
            max_pages=100,
            show_fields="headline",
            section="money"  # or None if you don't want a specific section filter
        )

        filename = f"dataset/raw/guardian_headlines_money_{year}.csv"
        save_headlines_to_csv(headlines_data, filename)
