import mysql.connector

def save_to_database(data):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='aydinemir',
            password='Ae20054545',
            database='hissescraping'
        )
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hisseler (
                id INT AUTO_INCREMENT PRIMARY KEY,
                hisse_adi VARCHAR(255),
                son_fiyat VARCHAR(255),
                degisim_yuzde VARCHAR(255),
                hacim_tl VARCHAR(255),
                saat VARCHAR(255)
            )
        """)

        for row in data:
            cursor.execute("""
                INSERT INTO hisseler (hisse_adi, son_fiyat, degisim_yuzde, hacim_tl, saat) 
                VALUES (%s, %s, %s, %s, %s)
            """, (row[0], row[2], row[3], row[4], row[5]))

        connection.commit()
        cursor.close()
        connection.close()
        print(f"{Fore.GREEN}Veriler başarıyla veritabanına eklendi.{Style.RESET_ALL}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
