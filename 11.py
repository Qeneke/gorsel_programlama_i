metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir
programcı tarafından 90'lı yılların başında geliştirilmeye başlanmıştır.
Çoğu insan, isminin Python olmasına bakarak, bu programlama dilinin, adını
piton yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu
programlama dilinin adı piton yılanından gelmez. Guido Van Rossum bu
programlama dilini, The Monty Python adlı bir İngiliz komedi grubunun, Monty
Python's Flying Circus adlı gösterisinden esinlenerek adlandırmıştır. Ancak
her ne kadar gerçek böyle olsa da, Python programlama dilinin pek çok yerde
bir yılan figürü ile temsil edilmesi neredeyse bir gelenek halini almıştır
diyebiliriz."""  # Sesli harfleri silinecek metnimiz

sesl_harfler = "aeıioöuüAEIİOÖUÜ"  # Sesli harflerimiz

çeviri_tablosu = str.maketrans('bc', 'BÇ', sesl_harfler)
# ''.maketrans(x, y, z)
# x-> kaynak string
# y-> hedef string
# z-> silinecek string

print(çeviri_tablosu)
