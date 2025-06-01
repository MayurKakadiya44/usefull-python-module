# Install BeautifulSoup if not already installed: pip install beautifulsoup4 requests
from bs4 import BeautifulSoup
import requests

# Sample HTML content (for demonstration; we'll also fetch a real webpage)
sample_html = """
<html>
<head><title>Sample Page</title></head>
<body>
    <h1>Welcome to Web Scraping</h1>
    <div class="container" id="main">
        <p class="intro">This is a sample paragraph.</p>
        <p class="intro">Another paragraph with <a href="https://example.com">a link</a>.</p>
        <ul id="items">
            <li class="item" data-id="1">Item 1</li>
            <li class="item" data-id="2">Item 2</li>
        </ul>
    </div>
    <div class="footer">Footer content</div>
</body>
</html>
"""

# --- 1. Parsing HTML with BeautifulSoup ---
# Create a BeautifulSoup object to parse the sample HTML
# sample_html=requests.get('https://www.ambitionbox.com/list-of-companies?page=1').text
soup = BeautifulSoup(sample_html, 'html.parser')  # 'html.parser' is the default parser

# --- 2. Navigating the Parse Tree ---
print("--- Navigating the Parse Tree ---")
# Access tags directly
title = soup.title  # Get the <title> tag
print("Title:", title.text)  # Output: Title: Sample Page

# Access the first occurrence of a tag
h1 = soup.h1
print("H1:", h1.text)  # Output: H1: Welcome to Web Scraping

# Access tag attributes
div = soup.find('div', id='main')
print("Main div class:", div['class'])  # Output: Main div class: ['container']

# Navigate to parent, children, and siblings
container = soup.find('div', class_='container')
parent = container.parent  # Get parent (body)
print("Parent of container:", parent.name)  # Output: Parent of container: body

children = list(container.children)  # Get all children of container
print("Children of container:", [child.name for child in children if child.name])  # Output: ['h1', 'p', 'p', 'ul']

next_sibling = container.find_next_sibling()  # Get next sibling of container
print("Next sibling of container:", next_sibling['class'])  # Output: Next sibling of container: ['footer']

# --- 3. Searching the Parse Tree ---
print("\n--- Searching the Parse Tree ---")
# Find a single element
first_p = soup.find('p')  # First <p> tag
print("First paragraph:", first_p.text)  # Output: First paragraph: This is a sample paragraph.

# Find all elements
all_p = soup.find_all('p')  # All <p> tags
print("All paragraphs:", [p.text for p in all_p])  # Output: All paragraphs: ['This is a sample paragraph.', 'Another paragraph with a link.']

# Find by class
intros = soup.find_all('p', class_='intro')
print("Paragraphs with class 'intro':", len(intros))  # Output: Paragraphs with class 'intro': 2

# Find by attributes
item = soup.find('li', attrs={'data-id': '1'})
print("Item with data-id='1':", item.text)  # Output: Item with data-id='1': Item 1

# Using CSS selectors with select()
links = soup.select('div.container a')  # Select <a> tags inside div with class 'container'
print("Links in container:", [link['href'] for link in links])  # Output: Links in container: ['https://example.com']

# --- 4. Extracting Data ---
print("\n--- Extracting Data ---")
# Get text content
all_text = soup.get_text(strip=True)  # Get all text, stripped of extra whitespace
print("All text (stripped):", all_text[:50], "...")  # Output: All text (stripped): Sample PageWelcome to Web ScrapingThis is a sample ...

# Get attribute values
link = soup.find('a')
print("Link href:", link['href'])  # Output: Link href: https://example.com

# --- 5. Modifying the Parse Tree ---
print("\n--- Modifying the Parse Tree ---")
# Create a new tag
new_tag = soup.new_tag('p')
new_tag.string = "New paragraph added!"
soup.body.append(new_tag)  # Append to body
print("Added new paragraph:", soup.find_all('p')[-1].text)  # Output: Added new paragraph: New paragraph added!

# Modify existing tag
h1 = soup.h1
h1.string = "Updated Title"
print("Updated h1:", soup.h1.text)  # Output: Updated h1: Updated Title

# --- 6. Real-World Example: Fetching and Scraping a Webpage ---
print("\n--- Real-World Web Scraping ---")
# Fetch a webpage
url = "https://example.com"
response = requests.get(url)
web_soup = BeautifulSoup(response.text, 'html.parser')

# Extract title
web_title = web_soup.title.text
print("Webpage title:", web_title)  # Output: Webpage title: Example Domain

# Find all links
web_links = web_soup.find_all('a')
print("Links on webpage:", [link.get('href') for link in web_links if link.get('href')])  # Output: Links on webpage: ['https://www.iana.org/domains/example']

# --- 7. Handling Errors and Edge Cases ---
print("\n--- Handling Errors ---")
# Handle missing tags
missing = soup.find('nonexistent')
print("Missing tag:", missing)  # Output: Missing tag: None

# Handle missing attributes
try:
    print(div['nonexistent'])  # Raises KeyError
except KeyError:
    print("Attribute not found")  # Output: Attribute not found

# --- 8. Working with Different Parsers ---
# Using lxml parser (requires: pip install lxml)
soup_lxml = BeautifulSoup(sample_html, 'lxml')
print("\n--- Using lxml Parser ---")
print("Title with lxml:", soup_lxml.title.text)  # Output: Title with lxml: Sample Page

# --- 9. Pretty Printing ---
print("\n--- Pretty Printing ---")
print(soup.prettify()[:150], "...")  # Print formatted HTML (first 150 chars)

# --- 10. Advanced: Extracting Nested Content ---
print("\n--- Extracting Nested Content ---")
ul = soup.find('ul', id='items')
items = ul.find_all('li')
for item in items:
    print(f"Item {item['data-id']}: {item.text}")  # Output: Item 1: Item 1, Item 2: Item 2
