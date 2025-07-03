import requests
from bs4 import BeautifulSoup

# Ask user to enter a website URL
url = input("Enter website URL (e.g., https://example.com): ")

try:
    # Get the page content
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status
    soup = BeautifulSoup(response.text, 'html.parser')

    print("\n🔗 List of URLs found on the page:\n")

    links = set()  # Use set to avoid duplicates

    for link in soup.find_all('a', href=True):
        full_url = link['href']
        if full_url.startswith('/'):
            full_url = url.rstrip('/') + full_url
        print(full_url)
        links.add(full_url)

    # Save to file
    with open("output_urls.txt", "w") as f:
        for link in links:
            f.write(link + "\n")

    print("\n✅ URLs saved to output_urls.txt")

except Exception as e:
    print("❌ Error:", e)