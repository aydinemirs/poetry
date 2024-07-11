def asal_mi(n):
    """Bir sayının asal olup olmadığını kontrol eder."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def asal_sayilari_bul(maks):
    """Belirtilen maksimum değere kadar olan asal sayıları döndürür."""
    asal_sayilar = []
    for sayi in range(2, maks + 1):
        if asal_mi(sayi):
            asal_sayilar.append(sayi)
    return asal_sayilar

# 1000'e kadar olan asal sayıları bul
maks_sayi = 1000
asal_sayilar = asal_sayilari_bul(maks_sayi)

# Asal sayıları ekrana yazdır
print(f"1 ile {maks_sayi} arasındaki asal sayılar: {asal_sayilar}")

