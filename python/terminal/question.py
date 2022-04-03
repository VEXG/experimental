get_nama = input('Masukan nama : ')

try:
    get_umur = int(input('Masukan umur : '))
except Exception as e:
    print('Harus pakek angka ya')
else:
    print(f'Halo {get_nama.capitalize()}!')
    print(f'Umur kamu {str(get_umur)}')
