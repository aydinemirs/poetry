def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():
    try:
        number = int(input("Bir sayı girin: "))
        if is_prime(number):
            print(f"{number} bir asal sayıdır.")
        else:
            print(f"{number} bir asal sayı değildir.")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    main()

