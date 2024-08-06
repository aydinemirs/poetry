import pandas as pd

def main():
    url = 'https://finans.mynet.com/borsa/hisseler/'

    page_content = fetch_page_content(url)
    if not page_content:
        return

    data = parse_html(page_content)
    if data is None:
        return

    df = pd.DataFrame(data)
    save_to_database(data)
    search_stock(df)

if __name__ == "__main__":
    main()
