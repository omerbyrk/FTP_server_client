#!/bin/python3

from ftplib import FTP
from os import system
import sys
r = '\033[1;31m'
b = '\033[1;34m'
w = '\033[1;97m'
g = '\033[1;32m'
c = '\033[1;36m'
try:
    IP = sys.argv[1]
    USER = str(sys.argv[2])
    PASS = str(sys.argv[3])
except:
    print(f'{r}Örnek\n\tKullanım: \t python', sys.argv[0], '{ip_address} {username} {password}'); exit()
try:
    ftp = FTP()
    ftp.connect("localhost", 2121)
    ftp.login("omer", "123456")
    print(f'{c}[{g}ok{c}] - {c} başarıyla bağlanıldı')
    ftp.getwelcome()
except:
    print(f'{r}[error] - Bağlanırken hata oluştu! '); exit()
while True:
    cmd = str(input(f'{c}FTP> {b}'))
    if cmd.lower() == 'help':
        print(f'''{b}

        ls                    | dosyaları listeler.
        pwd                   | üzerinde çalışılan klasör yolunu gösterir.
        quit                  | çıkış yapar.
        put      [dosya_adı]  | dosya yükleme yapar.
        cd       [klasör_yolu]| üzerinde çalışılan klasörü değiştirir
        get      [dosya_adı]  | dosya indirir.
        mkdir    [klasör_adı] | klasör oluşturur.
        rmdir    [klasör_adı] | klasörü siler.
        rmfile   [dosya_adı]  | dosyayı siler.
        
        ''')
        
    elif cmd.lower() == 'ls':
        ftp.retrlines('LIST')
    elif 'rmdir' in cmd or 'RMDIR' in cmd and cmd.split() > 1:
        try:
            ftp.rmd(f'{cmd.split()[1]}')
        except:
            print(f'{r}[ error ] - yetkiniz yok.')
    elif cmd.lower() == 'quit':
        ftp.quit(); print(f'{c}221 Güle güle.'); exit()
    elif cmd.lower() == 'clear':
        system('clear')

    elif 'put' in cmd or 'PUT' in cmd and cmd.split() > 1:
        try:
            file = open(f'{cmd.split()[1]}','rb')
        except:
            print(f'{r}[ error ] - dosya bulunamadı ')
        try:
            ftp.storbinary(f'STOR {cmd.split()[1]}', file)
            print(f'{c}[{g}ok{c}] - dosya başarıyla yüklendi!'); file.close()
        except:
            print(f'{r}[ error ] - yetkiniz yok')
    elif 'rmfile' in cmd or 'RMFILE' in cmd and cmd.split() > 1:
        try:
            ftp.delete(f'{cmd.split()[1]}')
        except:
            print(f'{r}[ error ] - yetkiniz yok')
    elif cmd.lower() == 'pwd':
        print(ftp.pwd())
    elif 'mkdir' in cmd or 'MKDIR' in cmd and cmd.split() > 1: 
        try:
            ftp.mkd(f'{cmd.split()[1]}'); print(f'{c}[{g}ok{c}]{g} -{c} folder {b}{cmd.split()[1]}{c}created successfully!')
        except:
            print(f'{r}[ error ] - yetkiniz yok')
    elif 'cd' in cmd or 'CD' in cmd:
        ftp.cwd(cmd.split()[1])
    elif 'get' in cmd or 'GET' in cmd:
        file = open(f'{cmd.split()[1]}', 'wb')
        try:
            ftp.retrbinary(f'RETR {cmd.split()[1]}', file.write); file.close()
            print(f'{c}[{g}ok{c}] - dosya başarıyla indirildi', ftp.size(cmd.split()[1]))
        except:
            print(f'{r}[ error ] - dosya {b}{cmd.split()[1]}{r} bulunamadı..')
            system(f'rm -rf {cmd.split()[1]}')
    else:
        print(f'{r}[ error ] - Kod bulunamadı! lütfen kodları görüntülemek için [ {b}help{r} ] yazın.')
