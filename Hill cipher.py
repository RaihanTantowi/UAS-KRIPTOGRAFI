import numpy as np


def prepare_input(text, key_size):
    matrix = []
    for char in text:
        if char.isalpha():
            matrix.append(
                ord(char) - ord("A") if char.isupper() else ord(char) - ord("a")
            )

    while len(matrix) % key_size != 0:
        matrix.append(0)

    return np.array(matrix)


def hill_encrypt(plain_text, key_matrix):
    key_size = len(key_matrix)
    plain_matrix = prepare_input(plain_text, key_size)

    # Menambahkan padding jika panjang pesan tidak habis dibagi oleh key_size
    while len(plain_matrix) % key_size != 0:
        plain_matrix = np.append(plain_matrix, [0])

    plain_matrix = plain_matrix.reshape(-1, key_size)

    # Mengubah matriks teks menjadi matriks terenkripsi menggunakan kunci
    encrypted_matrix = np.dot(plain_matrix, key_matrix) % 26

    # Mengembalikan teks terenkripsi
    return "".join([chr(x + ord("A")) for row in encrypted_matrix for x in row])


def main():
    # Memasukkan teks dan kunci enkripsi dari pengguna
    plain_text = input("Masukkan teks yang akan dienkripsi: ")
    key_text = input(
        "Masukkan kunci enkripsi (sebagai matriks 3x3, contoh: '2 4 5 9 2 1 3 17 7') gunakan spasi: "
    )

    # Mengonversi kunci enkripsi menjadi matriks
    key_matrix = np.array([int(x) for x in key_text.split()]).reshape(3, 3)

    # Memanggil fungsi enkripsi
    encrypted_text = hill_encrypt(plain_text, key_matrix)

    # Menampilkan teks terenkripsi
    print("Teks terenkripsi:", encrypted_text)


if __name__ == "__main__":
    main()
