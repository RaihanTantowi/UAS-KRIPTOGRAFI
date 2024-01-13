import cv2
import numpy as np
import matplotlib.pyplot as plt

def hitung_mse(data_input, data_output):
    mse = np.mean((data_input.astype(np.float32) - data_output.astype(np.float32))**2)
    return mse

def hitung_psnr(data_input, data_output, nilai_maks=255):
    mse = hitung_mse(data_input, data_output)

    # Mengatasi pembagian dengan nol
    if mse == 0:
        psnr = float('inf')
    else:
        psnr = 20 * np.log10(nilai_maks / np.sqrt(mse))

    return psnr

# Path gambar input dan output
path_gambar_input = "profil1.jpg"
path_gambar_output = "profil1.jpg"

# Baca gambar input dan output
gambar_input = cv2.imread(path_gambar_input)
gambar_output = cv2.imread(path_gambar_output)

# Konversi gambar BGR ke RGB (Matplotlib menggunakan format RGB)
gambar_input_rgb = cv2.cvtColor(gambar_input, cv2.COLOR_BGR2RGB)
gambar_output_rgb = cv2.cvtColor(gambar_output, cv2.COLOR_BGR2RGB)

# Kalkulasi PSNR dan MSE
mse = hitung_mse(gambar_input, gambar_output)
psnr = hitung_psnr(gambar_input, gambar_output)

# Tampilkan gambar dan hasil kalkulasi
plt.subplot(1, 2, 1)
plt.imshow(gambar_input_rgb)
plt.title("Gambar Input")

plt.subplot(1, 2, 2)
plt.imshow(gambar_output_rgb)
plt.title("Gambar Output")

plt.show()

print(f"MSE: {mse:.2f}")
print(f"PSNR: {psnr:.2f}")
