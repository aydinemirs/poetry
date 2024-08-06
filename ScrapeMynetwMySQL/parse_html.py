from bs4 import BeautifulSoup

def parse_html(page_content):
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
            row_data = [cell.get_text(strip=True) for cell in cells]
            if row_data:
                data.append(row_data)
    return data
