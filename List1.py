# Latihan 1
def tiga_angka_terbaik():
    data = input("Masukkan beberapa angka, pisahkan dengan spasi: ")
    angka_list = list(map(int, data.split()))
    urutan = sorted(angka_list, reverse=True)
    tiga_tertinggi = urutan[:3]
    print("3 bilangan terbaik:", tiga_tertinggi)

tiga_angka_terbaik()

# Latihan 2
def hitung_rata_rata():
    angka_list = []

    while True:
        data = input("Masukkan angka (atau ketik 'done' untuk selesai): ")
        if data.lower() == "done":
            break
        try:
            angka = float(data)
            angka_list.append(angka)
        except ValueError:
            print("Input tidak valid. Masukkan angka atau 'done'.")

    if angka_list:
        rata_rata = sum(angka_list) / len(angka_list)
        print("Rata-rata dari bilangan yang dimasukkan adalah:", rata_rata)
    else:
        print("Tidak ada angka yang dimasukkan.")

hitung_rata_rata()

# Latihan 3
def tampilkan_kata_unik(file):
    try:
        with open(file, 'r') as file:
            artikel = file.read().lower()
            
            kata_list = artikel.split()
            
            kata_unik = set(kata_list)
          
            print("Kata-kata unik yang ditemukan dalam artikel:")
            for kata in kata_unik:
                print(kata)
    
    except FileNotFoundError:
        print("File tidak ditemukan. Pastikan file path sudah benar.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

file = input("Masukkan path file teks: ")
tampilkan_kata_unik(file)
