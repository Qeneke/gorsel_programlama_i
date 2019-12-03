kaynak = "şçöğüıŞÇÖĞÜİ"  # kaynak (var olan) stringimiz (char dizisi)
hedef = "scoguiSCOGUI"  # hedef (dönüştürülecek) stringimiz (char dizisi)

# kaynak char dizimizi hedef char dizimiz ile değiştiriyoruz
tablo = str.maketrans(kaynak, hedef)

# maketrans işlemini gerçekleştireceğimiz metnimiz
metin = "İnternette bazen Türkçe karakterleri kullanırken sıkıntılar çekiyoruz."

# metnimizi ekrana bastırıyoruz (string yapısında bulunan translate fonksiyonu sayesinde)
print(metin.translate(tablo))
# --ÇIKTI--
# "Internette bazen Turkce karakterleri kullanirken sikintilar cekiyoruz."
# --ÇIKTI--

# Gördüğünüz gibi türkçe karakterler (kaynak dizimizde bulunanlar)
# ingilizce karakterler(hedef dizimizde bulunanlar) ile değişti
