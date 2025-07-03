import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import csv

url = input("Enter website URL (e.g., https://example.com): ")

try:
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    links = set()

    for tag in soup.find_all('a', href=True):
        href = tag['href']
        if href.startswith('/'):
            href = url.rstrip('/') + href
        elif href.startswith('#') or href.startswith('mailto:') or href.startswith('javascript:'):
            continue
        links.add(href)

    print("\n🔗 All URLs with Parameters:\n")

    # Prepare CSV file
    with open('url_parameters.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Full URL', 'Parameter', 'Value'])

        for link in links:
            parsed = urlparse(link)
            params = parse_qs(parsed.query)
            if params:
                print(link)
                for key, values in params.items():
                    for val in values:
                        writer.writerow([link, key, val])

    print("\n✅ Parameters saved in 'url_parameters.csv'")

except Exception as e:
    print("❌ Error:", e)