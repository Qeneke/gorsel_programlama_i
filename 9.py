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

sesli_harfler = "aeıioöuüAEIİOÖUÜ"  # Sesli harflerimiz

# Yeni metin için oluşturulan değişken (Sesli harfler olmadan metni aktaracağız)
yeni_metin = ""

for i in metin:  # Metin için for döngüsü
    if not i in sesli_harfler:  # Eğer döngüdeki harf sesli harfler içinde değilse
        yeni_metin += i  # Yeni metin char dizisine döngüdeki harfi ekle

print(yeni_metin)  # Yeni metni bastır
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
