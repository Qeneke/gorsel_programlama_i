kaynak = "şçöğüıŞÇÖĞÜİş"
hedef = "scoguiSCOGUIa"
# !ş s ve a önemli!

çeviri_tablosu = str.maketrans(kaynak, hedef)

# Tablomuzu ekrana bastırıyoruz (translate fonksiyonunu kullanmadan)
print(çeviri_tablosu)
# --ÇIKTI--
# {351: 115, 231: 99, 246: 111, 287: 103, 252: 117, 305: 105,
#   350: 83, 199: 67, 214: 79, 286: 71, 220: 85, 304: 73}
# --ÇIKTI--
# --PRETTY--
# {
#   351: 115,
#   231: 99,
#   246: 111,
#   287: 103,
#   252: 117,
#   305: 105,
#   350: 83,
#   199: 67,
#   214: 79,
#   286: 71,
#   220: 85,
#   304: 73
# }
# --PRETTY--

# Translate fonksiyonu buradaki kütüphaneyi kullanarak dönüşümleri yapıyor


# chr(351)
# chr(115)
# chr(97)
