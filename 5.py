import envs  # envs modülümüzü içeri aktarıyoruz (import)
print(str.maketrans("a", "A"))
print(''.maketrans(envs.kaynak, envs.hedef))
# envs.kaynak="şçöğüıŞÇÖĞÜİ"
# envs.hedef="scoguiSCOGUI"
