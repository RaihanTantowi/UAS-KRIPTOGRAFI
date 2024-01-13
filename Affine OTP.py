def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0

    for char in plaintext:
        # Enkripsi menggunakan operasi XOR antara ASCII plaintext dan kunci
        encrypted_char = chr(ord(char) ^ ord(key[key_index]))
        ciphertext += encrypted_char

        # Perbarui indeks kunci atau kembali ke awal jika sudah mencapai akhir
        key_index = (key_index + 1) % len(key)

    return ciphertext

def decrypt(ciphertext, key):
    # Fungsi enkripsi dan dekripsi sama dalam operasi XOR
    return encrypt(ciphertext, key)

# Input
plaintext = input("Masukkan plaintext: ")
kunci = input("Masukkan kunci: ")

# Enkripsi
hasil_enkripsi = encrypt(plaintext, kunci)
print("Hasil Enkripsi:", hasil_enkripsi)

# Dekripsi
hasil_deskripsi = decrypt(hasil_enkripsi, kunci)
print("Hasil Deskripsi:", hasil_deskripsi)
