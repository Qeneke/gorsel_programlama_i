import envs

metin = "buraK haYrettin abDullah BarıŞ"

kaynak = envs.kaynak+"KYDBŞ"  # ş önemli
hedef = envs.hedef+"kydbş"
silinecek = "rtl "

çeviri_tablosu = str.maketrans(kaynak, hedef, silinecek)

print(metin.translate(çeviri_tablosu))
# --ÇIKTI--
# buakhayeinabduahbais
# --ÇIKTI--
