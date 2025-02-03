import qrcode
import random
import string
import os

def generate_random_code(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_qr_code(data, filename):
    if os.path.exists(filename):  # Cek apakah file sudah ada
        print(f"❌ QR Code untuk {filename} sudah ada, tidak perlu dibuat ulang.")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR Code berhasil dibuat: {filename}")

def main():
    print("=== Sistem Absensi QR Code ===")

    # Buat folder "qrcodes" jika belum ada
    if not os.path.exists("qrcodes"):
        os.makedirs("qrcodes")

    # Buat set untuk menyimpan data yang sudah dibuat
    existing_data = set()

    while True:
        nama = input("Masukkan Nama Siswa: ").strip()
        if not nama:
            print("❌ Nama tidak boleh kosong!")
            continue

        id_siswa = input("Masukkan ID Unik Siswa: ").strip()
        if not id_siswa:
            print("❌ ID Unik tidak boleh kosong!")
            continue

        # Buat key unik dari nama dan ID untuk mengecek duplikasi
        unique_key = f"{nama.lower()}_{id_siswa}"
        if unique_key in existing_data:
            print("⚠️ Data ini sudah pernah dibuat, tidak boleh duplikat!")
            continue

        # Tambahkan ke set agar tidak dibuat ulang
        existing_data.add(unique_key)

        # Generate random code
        random_code = generate_random_code()

        # Gabungkan data menjadi string
        data = f"Nama: {nama}\nID: {id_siswa}\nKode: {random_code}"
        print(f"📌 Data untuk QR Code:\n{data}")

        # Buat nama file QR Code
        filename = f"qrcodes/{nama.replace(' ', '_')}_{id_siswa}.png"

        # Buat QR Code (hanya jika belum ada)
        create_qr_code(data, filename)

        # Pilihan untuk melanjutkan atau keluar
        lanjut = input("Ingin menambahkan siswa lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("✅ Program selesai. Semua QR Code tersimpan di folder 'qrcodes'.")
            break

if __name__ == "__main__":
    main()
