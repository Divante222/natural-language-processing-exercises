from bs4 import BeautifulSoup

# Read HTML from a file
with open('example.html', 'r') as file:
    html_content = file.read()

# Create BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <p> tags
paragraphs = soup.find_all('p')

# Write the results to a file
with open('output.txt', 'w') as file:
    for paragraph in paragraphs:
        file.write(paragraph.text + '\n')