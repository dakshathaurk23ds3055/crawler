# Web Application Parameter Extractor

##  Project Overview:
This tool is designed to scan a given website URL and extract all hyperlinks containing query parameters (e.g., ?user=1&name=test). It helps identify which URLs may be vulnerable to cyber threats like SQL Injection or XSS by listing all parameters in a structured file.

##  Objective:
To create a simple desktop-based application that aids in web security assessment by crawling pages and identifying parameterized URLs.

##  Technologies Used:
- Python
- Tkinter (for the GUI)
- Requests (for fetching HTML content)
- BeautifulSoup (for HTML parsing)
- urllib (for breaking down URLs)
- CSV (to save the extracted parameters)

##  Features:
- Graphical User Interface (GUI)
- User enters the target website URL
- Crawls and extracts all <a> tags
- Parses links for parameters (e.g., ?id=123)
- Saves results in a CSV file named url_parameters.csv

##  Output:
A CSV file containing:
- Full URL
- Parameter Name
- Parameter Value

 ## GUI Preview:
![Screenshot 2025-07-03 213715](https://github.com/user-attachments/assets/c13ef80d-dcdc-4777-9e29-a82828356437)

## How to Run:
```bash
python crawler_gui.py
