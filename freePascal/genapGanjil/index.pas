Program genapGanjil;
Uses crt; 
Var lanjut: boolean;

Function start(): integer;
    Var angka: integer;
    var bilangan: string;
    Var lanjutGak: char;
    Begin clrscr;
        write('Silahkan masukan angka : '); readln(angka);
        if (angka mod 2 = 0) then bilangan := 'genap' else bilangan := 'ganjil';
        writeln('Angka yang kamu masukkan adalah bilangan ', bilangan);
        write('Apakah kamu masih mau lanjut? (Y/N) : '); readln(lanjutGak);
        While Not ((LowerCase(lanjutGak) = 'y') Or (LowerCase(lanjutGak) = 'n')) Do Begin
                Write('Apakah kamu masih mau lanjut? (Y/N) : ');
                readln(lanjutGak);
            End;
        If LowerCase(lanjutGak) = 'y' Then lanjut := true
        Else lanjut := false;
        exit(0);
    End;

Begin
    lanjut := true;
    While lanjut Do start();
End.
