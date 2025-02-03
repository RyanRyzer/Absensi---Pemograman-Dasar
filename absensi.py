import qrcode
import random
import string
import os

def generate_random_code(length=8):
    """Generate a random alphanumeric code."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_qr_code(data, filename):
    """Generate a QR Code and save it as an image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def main():
    print("=== Sistem Absensi QR Code ===")
    if not os.path.exists("qrcodes"):
        os.makedirs("qrcodes")  # Create a folder to save QR codes

    while True:
        nama = input("Masukkan Nama Siswa: ").strip()
        if not nama:
            print("Nama tidak boleh kosong!")
            continue

        id_siswa = input("Masukkan ID Unik Siswa: ").strip()
        if not id_siswa:
            print("ID Unik tidak boleh kosong!")
            continue

        # Generate random code
        random_code = generate_random_code()
        
        # Combine data into a single string
        data = f"Nama: {nama}\nID: {id_siswa}\nKode: {random_code}"
        print(f"Data untuk QR Code:\n{data}")

        # Create and save QR Code
        filename = f"qrcodes/{nama.replace(' ', '_')}_{id_siswa}.png"
        create_qr_code(data, filename)
        print(f"QR Code berhasil dibuat dan disimpan sebagai {filename}\n")

        # Prompt to continue or exit
        lanjut = input("Ingin menambahkan siswa lain? (y/n): ").strip().lower()
        if lanjut != 'y':
            print("Program selesai. Semua QR Code tersimpan di folder 'qrcodes'.")
            break

if __name__ == "__main__":
    main()