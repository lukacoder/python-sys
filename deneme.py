import sys
def exit():
    print('Çikiliyor...')
    sys.exit()

if len(sys.argv) < 2:
    print('Gerekli parametreleri girmediniz!')
    exit()

elif len(sys.argv) > 2:
    print('Çok fazla parametre girdiniz!')
    exit()

elif sys.argv[1] in ['-ver', '-VER']:
    print('Program sürümü: 0.8')

else:
    mesaj = 'Girdiğiniz parametre ({}) anlaşilamadi!'
    print(mesaj.format(sys.argv[1]))
    exit()