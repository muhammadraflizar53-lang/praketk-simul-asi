# data target nilai untuk masing-masing mahasiswa 
target_mhs = {
    'Andi' : 70,
    'Budi' : 75,
    'Citra' : 80,
}

# input nama mahasiswa 
nama = input('Nama :'). strip ()

# Pengecekan apakah nama mahasiswa terdaftar 
if nama in target_mhs :
    target = target_mhs [nama]
    print (f'target nilai untuk { nama} adalah : {target}\n')
    
    percobaan = 1
    maksimal_percobaan = 3
    lulus = False
    
    # 2 & 3. perulangan (while) maksimal 3 kali untuk remedial/mengulang ujian 
    while percobaan <= maksimal_percobaan:
        nilai = float(input(f'nilai {percobaan} :'))
        
        # percabangan (if-else) untuk cek nilai terhadap target
        if nilai >= target:
            lulus = True
            break
        else:
            percobaan += 1
            
    # Tampilkan pesan sesuai hasil akhir
    if lulus:
        print(f'\nOutput: {nama} berhasil lulus setelah {percobaan} kali percobaan!')
    else:
        print(f'\nOutput: {nama} tidak lulus setelah {maksimal_percobaan} kali percobaan!')
    
else:
    print('Nama mahasiswa tidak ditemukan dsalam data (pilih Andi, Budi, atau Citra).')