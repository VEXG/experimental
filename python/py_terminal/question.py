# experiment : just a random question
# using this instead freepascal, bahasa jelek :<
# creator : VEXG aka Helmi

# getting the name // mengambil atau menginput nama
get_nama = input('Halo nama kamu siapa? : ')

# getting the age // mengambil atau menginput umur
try:  # trying the code below, if got an err. then move to execption // mencoba code dibawah ini, jika terdapat err. pindah ke execption
    get_umur = int(input('umur kamu? : '))
except Exception as e:  # catch the error // menangkap errornya
    # the try is for detecting user/client from inputing string type / anything except interger type // trynya itu untuk mendeteksi jika user/client menginput type string / lainnya kecuali type interger
    print('Harus pakek angka kak')
else:  # if get_umur is interger type // jika get_umur itu typenya interger
    # output
    # note: f'' itu adalah versi simple dari format()
    # formet() docs : https://www.w3schools.com/python/python_strings_format.asp
    print(f'Halo {get_nama.capitalize()}!')
    print(f'Umur kamu {str(get_umur)}')
