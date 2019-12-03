import envs  # envs modülümüzü içeri aktarıyoruz (import)
print(str.maketrans("a", "A"))
# --ÇIKTI--
#{97: 65}
# --ÇIKTI--

# envs.hedef="scoguiSCOGUI"
# envs.kaynak="şçöğüıŞÇÖĞÜİ"
print(''.maketrans(envs.kaynak, envs.hedef))
# --ÇIKTI--
# {351: 115, 231: 99, 246: 111, 287: 103, 252: 117, 305: 105, 350: 83, 199: 67, 214: 79, 286: 71, 220: 85, 304: 73}
# --ÇIKTI--
