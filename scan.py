import cv2 #pip install opencv-python pyzbar
import numpy as np #pip install numpy
from pyzbar.pyzbar import decode

def scan_qr_code():
    """Fungsi untuk mendeteksi dan membaca QR Code menggunakan webcam."""
    cap = cv2.VideoCapture(0)  #Mengakses kamera (0 untuk kamera default)

    while True:
        ret, frame = cap.read()  #Membaca frame dari kamera
        if not ret:
            print("Gagal mengakses kamera!")
            break

        decoded_objects = decode(frame)  #Mendeteksi QR Code di dalam frame
        for obj in decoded_objects:
            qr_data = obj.data.decode("utf-8")  #Mendapatkan data QR Code
            print(f"Data QR Code: {qr_data}")

            # Menampilkan QR Code yang terdeteksi dengan kotak
            points = obj.polygon
            if len(points) == 4:  # Pastikan bentuknya persegi
                pts = [(point.x, point.y) for point in points]
                cv2.polylines(frame, [np.array(pts, np.int32)], isClosed=True, color=(0, 255, 0), thickness=3)

            # Ubah ke grayscale untuk pemindaian lebih akurat
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Ubah ke grayscale
            decoded_objects = decode(gray)  # Scan dalam grayscale agar lebih akurat


            # Menampilkan teks data QR di layar
            cv2.putText(frame, qr_data, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow("QR Code Scanner", frame)  #Menampilkan kamera dengan hasil pemindaian

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_code()
