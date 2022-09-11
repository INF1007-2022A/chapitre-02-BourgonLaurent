#!/usr/bin/env python
from typing import List


def majuscule(mot: str) -> str:
    return "".join([chr(ord(char) - 32) for char in mot])


if __name__ == "__main__":
    mots: List[str] = [
        "riz",
        "cours",
        "voiture",
        "oiseau",
        "bonjour",
        "églantier",
        "arbre",
    ]
    mots_majuscules: List[str] = [majuscule(mot) for mot in mots]
