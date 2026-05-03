def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr, n):
    for i in range(n - 1):
        pos = i
        for j in range(i + 1, n):
            if arr[j] < arr[pos]:
                pos = j
        if pos != i:
            tukar(arr, i, pos)

def klasifikasi_nilai(nilai):
    if nilai >= 76:
        return 'A'
    elif nilai >= 66:
        return 'B'
    elif nilai >= 56:
        return 'C'
    elif nilai >= 50:
        return 'D'
    else:
        return 'E'

def main():
    try:
        n = int(input("Masukkan jumlah nilai mahasiswa yang ingin diinput: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan nilai-nilai mahasiswa:")
    for i in range(n):
        while True:
            try:
                nilai = int(input())
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
    print(f"Rata-rata nilai mahasiswa = {sum(arr) / len(arr) }  ")
    print(f"Nilai sebelum diurutkan: {arr}")
    selection_sort(arr, n)
    print("Nilai setelah diurutkan (Selection Sort):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()
    print("Klasifikasi nilai (setelah diurutkan):")
    for i in range(n):
        grade = klasifikasi_nilai(arr[i])
        print(f"Nilai {arr[i]} = {grade}")

if __name__ == "__main__":
    main()