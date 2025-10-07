def trim(s: str) -> str:
    return s.strip()

def normalizo_hapesirat(s: str) -> str:
    rezultat = ""
    ne_hapesire = False
    for c in s:
        if c == " ":
            if not ne_hapesire:
                rezultat += " "
                ne_hapesire = True
        else:
            rezultat += c
            ne_hapesire = False
    return rezultat

def format_card_title(s: str) -> str:
    s = trim(s)
    s = normalizo_hapesirat(s)
    if s == "":
        return ""
    return s[0].upper() + s[1:]

teksti = input("Teksti: ")
titulli = format_card_title(teksti)
print(f"Titulli: {titulli}")
