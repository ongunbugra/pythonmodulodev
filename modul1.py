def harf_oranlari(metin):
    harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
    harf_frekansi = {harf: 0 for harf in harfler}
    toplam_harf = 0

    for harf in metin.lower():
        if harf in harfler:
            harf_frekansi[harf] += 1
            toplam_harf += 1

    if toplam_harf == 0:
        print("Uyarı: Metinde hiç harf bulunmamaktadır!")
    else:
        for harf in harfler:
            yuzde = (harf_frekansi[harf] / toplam_harf) * 100
            print(f"{harf}: %{yuzde:.2f}, {harf_frekansi[harf]} kez kullanıldı")
            
def hakkimda():
    print("Buğra Öngün 211220047 Belki Hiç bir şey yolunda gitmedi ama hiç bir şeyde beni yolundan etmedi")
    
def degistirme(harf):
    if harf.isupper():
        return harf.lower()
    else:
        return harf

def kelime_sayisi(metin):
    kelimeler = metin.split()
    return len(kelimeler)

