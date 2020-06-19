
# Şifrelemeyi Yapan Fonksiyon
def kurucu():
    print('şifrelenecek metni gir')
    sifrelenecek = input()
    # inputu asciiye çevir
    sifrelenecekascii = [ord(c) for c in sifrelenecek]
    # çıkan ascii değeri 3 ile çarp
    sifrelenen = [i * 3 for i in sifrelenecekascii]
    sifrelenenmesaj = [chr(sifrelenen[i]) for i in range(0, len(sifrelenen))]
    print('sifreli mesaj:')
    print(''.join(sifrelenenmesaj))
    seçim()

# Şifrelemeyi Tersine Çeviren Fonksiyon
def bozan():
    # Decrypt Kısım
    print('şifreli mesajı girin')
    sifrelitext = input()
    # girilen sifreli texti ascii değerlere çevir
    asciisifre = [ord(c) for c in sifrelitext]
    cozumascii = [i // 3 for i in asciisifre]
    # çözülen asciiyi texte geri çevir
    cozuluasciimetin = [chr(cozumascii[i]) for i in range(0, len(cozumascii))]
    print('çözülen mesajınız:')
    print(''.join(cozuluasciimetin))
    seçim()

# Seçim Yapma Fonksiyonu
def seçim():
    x = int(input("şifrelemek için 1e çözmek için 2ye bas ve enterla"))
    if x == 1:
     kurucu()
    if x == 2:
     bozan()
    else: print('lütfen sadece 1 veya 2 ye basın')
    seçim()

seçim()
