#!/usr/bin/env python
def majuscule(mot: str) -> str:
    return "".join([chr(ord(char) - 32) for char in mot])


if __name__ == "__main__":
    mots: list[str] = [
        "riz",
        "cours",
        "voiture",
        "oiseau",
        "bonjour",
        "églantier",
        "arbre",
    ]
    mots_majuscules: list[str] = [majuscule(mot) for mot in mots]
