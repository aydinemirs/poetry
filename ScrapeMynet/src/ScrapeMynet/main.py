from data_fetcher import fetch_data
from data_processor import process_data
from user_interface import user_interface

def main():
    url = 'https://finans.mynet.com/borsa/hisseler/'

    page_content = fetch_data(url)
    if page_content:
        df = process_data(page_content)
        if df is not None:
            user_interface(df)

if __name__ == "__main__":
    main()
