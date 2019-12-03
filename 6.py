# q klavyesde soldan sağa tuşlar
q_klavye_düzeni = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
# f klavyede soldan sağa tuşlar
f_klavye_düzeni = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"

# f klavyede yanlışıkla yazılan,
# aslında q klavyedeymiş gibi yazılan metin
metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

çeviri_tablosu = str.maketrans(q_klavye_düzeni, f_klavye_düzeni)
print(çeviri_tablosu)
# --ÇIKTI--
# {113: 102, 119: 103, 101: 287, 114: 305, 116: 111, 121: 100, 117: 114, 305: 110,
# 111: 104, 112: 112, 287: 113, 252: 119, 97: 117, 115: 105, 100: 101,
# 102: 97, 103: 252, 104: 116, 106: 107, 107: 109, 108: 108,
# 351: 121, 105: 351, 44: 120, 122: 106, 120: 246, 99: 118,
# 118: 99, 98: 231, 110: 122, 109: 115, 246: 98, 231: 46, 46: 44}
# --ÇIKTI--

print(metin.translate(çeviri_tablosu))
# --ÇIKTI--
# Bakalım bu metin doğru şekilde çevrilecek mi?
# --ÇIKTI--
