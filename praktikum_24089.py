def cek_umur(umur):
    if umur <5:
        print("masi balita")
    elif umur < 13:
        print("masih anak anak")
    elif umur < 20:
        print("anda suda remaja")
    elif umur < 35:
        print("anda sudah dewasa")
umur_pengguna = int(input("masukan umur anda :"))
cek_umur(umur_pengguna)