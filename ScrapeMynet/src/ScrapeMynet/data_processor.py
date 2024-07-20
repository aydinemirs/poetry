from bs4 import BeautifulSoup
import pandas as pd

def process_data(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')

    tables = soup.find_all('table')
    if not tables:
        print("Tablo bulunamadı. HTML yapısını kontrol edin.")
        return None

    data = []
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            row_data = []
            for cell in cells:
                text = cell.get_text(strip=True)
                row_data.append(text)
            if row_data:
                data.append(row_data)

    df = pd.DataFrame(data)
    return df
