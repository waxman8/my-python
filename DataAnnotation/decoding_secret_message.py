import requests as req
from bs4 import BeautifulSoup

def get_doc_text(doc_url):
    fetch_response = req.get(doc_url)
    if fetch_response.status_code == 200:
        return fetch_response.text
    else:
        print(f"Failed to fetch document: {fetch_response.status_code} : {fetch_response.reason}")
        return "INVALID"

def get_x_and_y_limits(table_rows):
    mx = 0
    my = 0
    for row in table_rows:
        if mx < int(row[0]):
            mx = int(row[0])
        if my < int(row[2]):
            my = int(row[2])    
    return mx, my

def parse_google_doc(doc_text):
    raw_rows = []
    soup = BeautifulSoup(doc_text, 'html.parser')
    table = soup.find('table')
    i=0
    for row in table.find_all('tr'):
        if i==0:
            i+=1
            continue
        cells = row.find_all('td')
        row_data = [cell.get_text(strip=True) for cell in cells]
        raw_rows.append(row_data)
        
    x,y = get_x_and_y_limits(raw_rows)
    rows = [[' ' for _ in range(x+1)] for _ in range(y+1)]
    for raw_row in raw_rows:
        rows[int(raw_row[2])][int(raw_row[0])] = str(raw_row[1])
    return rows

def print_the_message(doc_rows):
    for row in reversed(doc_rows):
        print("".join(row))

#this function is the starting point with the URL as input parameter
def decode_and_print_message(the_url):
    doc_text = get_doc_text(the_url)
    if doc_text == "INVALID":
        print("An Error occurred getting the document content")
        exit(1)
    doc_rows = parse_google_doc(doc_text)
    print_the_message(doc_rows)

if __name__ == "__main__":
    decode_and_print_message("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")

# https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub