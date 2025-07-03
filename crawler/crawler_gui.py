import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
import csv
import tkinter as tk
from tkinter import messagebox

def crawl_website():
    url = entry.get()

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

        with open('url_parameters.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Full URL', 'Parameter', 'Value'])

            for link in links:
                parsed = urlparse(link)
                params = parse_qs(parsed.query)
                if params:
                    for key, values in params.items():
                        for val in values:
                            writer.writerow([link, key, val])

        messagebox.showinfo("Done", "✅ Parameters saved in 'url_parameters.csv'")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Cybersecurity Web Crawler")
root.geometry("500x200")
root.configure(bg="#f0f0f0")

label = tk.Label(root, text="Enter website URL:", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Crawl Website", command=crawl_website, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"))
button.pack(pady=20)

root.mainloop()