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

çeviri_tablosu = str.maketrans('', '', sesl_harfler)
# ''.maketrans(x, y, z)
# x-> kaynak string
# y-> hedef string
# z-> silinecek string

print(metin.translate(çeviri_tablosu))
# --ÇIKTI--
# B prgrmlm dl Gd Vn Rssm dl Hllndl br
# prgrmc trfndn 90'l yllrn bşnd glştrlmy bşlnmştr.
# Çğ nsn, smnn Pythn lmsn bkrk, b prgrmlm dlnn, dn
# ptn ylnndn ldğn dşnr. nck znndldğnn ksn b
# prgrmlm dlnn d ptn ylnndn glmz. Gd Vn Rssm b
# prgrmlm dln, Th Mnty Pythn dl br nglz kmd grbnn, Mnty
# Pythn's Flyng Crcs dl gstrsndn snlnrk dlndrmştr. nck
# hr n kdr grçk byl ls d, Pythn prgrmlm dlnn pk çk yrd
# br yln fgr l tmsl dlms nrdys br glnk hln lmştr
# dyblrz.
# --ÇIKTI--
