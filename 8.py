metin = "Bfjflrk öa kdhsı yteua idjslyd bdcusldvdj ks?"

çeviri_tablosu = str.maketrans({"q": "f", "w": "g", "e": "ğ", "r": "ı", "t": "o", "y": "d", "u": "r",
                                "ı": "n", "o": "h", "p": "p", "ğ": "q", "ü": "w", "a": "u", "s": "i",
                                "d": "e", "f": "a", "g": "ü", "h": "t", "j": "k", "k": "m", "l": "l",
                                "ş": "y", "i": "ş", ",": "x", "z": "j", "x": "ö", "c": "v", "v": "c",
                                "b": "ç", "n": "z", "m": "s", "ö": "b", "ç": ".", ".": ","})  # Direkt sözlüğümüzü verdik
print(metin.translate(çeviri_tablosu))
