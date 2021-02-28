'''
Kekurangan program :
1. Harus convert bentuk Hexa (yang ada hurufnya) dengan manual, contoh : ketika ada A, maka harus menuliskan 10
2. Tida bisa merubah KE Hexa berbentuk huruf (khusus untuk sisa berangka 10 - 16),
jadi yang tertampil adalah angka 10 - 16 bukan A - G

created by Muhammad Pascal Dewantara, Informatika'20 Telkom University
'''

def konversi_kali(x,basis_x):
    '''
    konversi x to desi
    '''
    if basis_x != 16 or x != 0:
        lis = [int(i) for i in str(x)]
        total = 0
        jmlh_digit = len(lis) - 1

        for i in lis:
            hasil = i * basis_x**jmlh_digit
            
            if jmlh_digit == len(lis) - 1:
                print(f"({i} x {basis_x}^{jmlh_digit})",end="")
            else:
                print(f" + ({i} x {basis_x}^{jmlh_digit})",end="")
            
            total += hasil
            jmlh_digit -= 1

    elif basis_x == 16 and x == 0:
        lis_hexa = []
        selesai = False
        digit = 1
        while not selesai:
            tanya = input(f"Digit ke-{digit} (dari kiri) = ")
            digit+=1
            if tanya == "selesai":
                selesai = True
                break

            lis_hexa.append(int(tanya))
        
        total = 0
        jmlh_digit = len(lis_hexa) - 1

        for i in lis_hexa:
            hasil = i * basis_x**jmlh_digit
            
            if jmlh_digit == len(lis_hexa) - 1:
                print(f"({i} x {basis_x}^{jmlh_digit})",end="")
            else:
                print(f" + ({i} x {basis_x}^{jmlh_digit})",end="")
            
            total += hasil
            jmlh_digit -= 1

    print(f" = {total}")

def konversi_sisa(desimal,basis_y):
    '''
    konversi desi to y
    '''
    lis = []

    def aksi(desimal,basis_y):
        hasil = desimal // basis_y
        sisa = desimal % basis_y
        print(f"{desimal} : {basis_y} = {hasil} sisa {sisa}")

        lis.append(sisa)

        if hasil != 0:
            aksi(hasil,basis_y)
    aksi(desimal,basis_y)
    print()

    for i in lis[::-1]:
        print(i,end="")
            
def tanya_input():
    mau = input('Mau kali atau sisa ? \n\nkalo dari x ke desimal, maka ketik "kali"\nkalo dari desimal ke y, maka ketik "sisa"\n\nMaunya ')
    if mau == "sisa":
        desi = int(input("Desimal = "))
        bas_y = int(input("Basis tujuan (tuliskan dlm bntk angka, tanpa spasi) = "))
        konversi_sisa(desi,bas_y)
    elif mau == "kali":
        basis_bil = int(input("Basis asal (tuliskan dlm bntk angka) = "))
        if basis_bil != 16:
            bil = int(input("Bilangan (tuliskan dlm bntk angka) = "))
            konversi_kali(bil,basis_bil)
        elif basis_bil == 16: #Parameter bilangan jadi ga wajib, karena kita input 1 per 1 untuk hexa
            ada_huruf = input("Ada huruf (iye atau ga) ? ")
            if ada_huruf == "iye":
                print('Ketik "selesai" apabila sudah tertulis semua\n')
                konversi_kali(0,basis_bil)
            if ada_huruf == "ga":
                bil = int(input("Bilangan (tuliskan dlm bntk angka, tanpa spasi) = "))
                konversi_kali(bil,basis_bil)          

tanya_input()