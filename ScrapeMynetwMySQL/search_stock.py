from colorama import Fore, Style

def search_stock(df):
    while True:
        hisse_adi = input(f"{Fore.WHITE}Lütfen bir hisse adı girin (Çıkmak için 'exit' yazın): ").strip().upper()

        if hisse_adi == 'EXIT':
            break

        found = False
        for _, row in df.iterrows():
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
