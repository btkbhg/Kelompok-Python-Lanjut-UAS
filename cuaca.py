from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Fungsi untuk mengambil data cuaca dari halaman BMKG
def get_weather_data(location_url):
    # Inisialisasi webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Akses halaman cuaca untuk lokasi yang dipilih
    driver.get(location_url)

    # Tunggu beberapa detik untuk memastikan halaman sepenuhnya dimuat
    time.sleep(5)

    try:
        # Mengambil kelembapan
        Kelembapan = driver.find_element(By.XPATH, "//span[contains(text(),'Kelembapan')]//following-sibling::span").text
        
        # Mengambil kecepatan angin
        wind_speed = driver.find_element(By.XPATH, "//span[contains(text(),'Wind Speed')]//following-sibling::span").text
        
        # Mengambil arah angin
        wind_direction = driver.find_element(By.XPATH, "//span[contains(text(),'Wind Direction')]//following-sibling::span").text
        
        # Menampilkan data cuaca yang diambil
        print(f"Kelembapan: {Kelembapan}")
        print(f"Kecepatan Angin: {wind_speed}")
        print(f"Arah Angin: {wind_direction}")

    except Exception as e:
        print("Error saat mengambil data:", e)
    
    # Menunggu 5 menit sebelum menutup browser
    print("Menunggu selama 5 menit sebelum menutup browser...")
    time.sleep(300)

    # Tutup browser setelah 5 menit
    driver.quit()
    print("Browser ditutup setelah 5 menit.")

# Menu pilihan lokasi
def show_location_menu():
    print("Pilih lokasi cuaca yang diinginkan:")
    print("1. Condong Catur")
    print("2. Sidomulyo, Godean")
    print("3. Maguwoharjo")
    print("4. Purbayan, Kotagede")
   

    # Input pilihan lokasi
    choice = input("Masukkan nomor lokasi (1-4): ")

    # Menentukan URL berdasarkan pilihan
    if choice == '1':
        location_url = "https://www.bmkg.go.id/cuaca/prakiraan-cuaca/34.04.07.2003"
    elif choice == '2':
        location_url = "https://www.bmkg.go.id/cuaca/prakiraan-cuaca/34.04.02.2003"
    elif choice == '3':
        location_url = "https://www.bmkg.go.id/cuaca/prakiraan-cuaca/34.04.07.2002"
    elif choice == '4':
        location_url = "https://www.bmkg.go.id/cuaca/prakiraan-cuaca/34.71.14.1003"
    else:
        print("Pilihan tidak valid. Program akan keluar.")
        return

    # Panggil fungsi untuk mengambil data cuaca dari halaman yang dipilih
    get_weather_data(location_url)

# Jalankan program
show_location_menu()