import requests
from bs4 import BeautifulSoup
import pandas as pd
from colorama import Fore, Style

def main():
    url = 'https://finans.mynet.com/borsa/hisseler/'

    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.content
    else:
        print(f"Error: {response.status_code}")
        return

    soup = BeautifulSoup(page_content, 'html.parser')

    tables = soup.find_all('table')
    if not tables:
        print("Tablo bulunamadı. HTML yapısını kontrol edin.")
        return

    data = []
    for i, table in enumerate(tables):
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
    
    print(f"{Fore.GREEN}Veriler başarıyla alındı.{Style.RESET_ALL}")

    while True:
        hisse_adi = input(f"{Fore.WHITE}Lütfen bir hisse adı girin (Çıkmak için 'exit' yazın): ").strip().upper()

        if hisse_adi == 'EXIT':
            break

        found = False
        for index, row in df.iterrows():
            if hisse_adi in str(row[0]).upper():
                if not found:
                    print(f"{Fore.BLACK}Bulunan Hisseler:{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Hisse Adı: {Style.BRIGHT}{Fore.WHITE}{row[0]}")
                print(f"{Fore.CYAN}Son Fiyat: {Style.BRIGHT}{Fore.WHITE}{row[2]}")
                print(f"{Fore.CYAN}Değişim Yüzde: {Style.BRIGHT}{Fore.WHITE}{row[3]}")
                print(f"{Fore.CYAN}Hacim(TL): {Style.BRIGHT}{Fore.WHITE}{row[4]}")
                print(f"{Fore.CYAN}Saat: {Style.BRIGHT}{Fore.WHITE}{row[5]}")
                print(f"{Fore.WHITE}----------------")
                found = True

        if not found:
            print(f"{Fore.RED}Hisse adı '{hisse_adi}' bulunamadı.")
            print(f"{Fore.WHITE}............")

if __name__ == "__main__":
    main()
