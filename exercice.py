#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ne pas utiliser replace ou count

def is_even_len(string: str) -> bool:
    if (len(string)%2==0):
        return True
    else:
        return False
    pass

def remove_third_char(string: str) -> str:
    avant_trois = string[0:2]
    apres_trois = string [3:]
    mot = avant_trois+apres_trois
    return mot
    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    #vieux = string.index (old_char)
    #avant_old = string [0:vieux]
    #apres_old = string [vieux+1:]
    #nouveau = avant_old+new_char+apres_old
    mot = ""
    lettre= ""
    for i in string:
        if (i!= old_char):
            lettre = i
        else:
            lettre = new_char
        mot += lettre

    return mot
    pass


def get_number_of_char(string: str, char: str) -> int:
    counter = 0
    for i in string:
        if (i==char):
            counter+=1
    return counter
    pass


def get_number_of_words(sentence: str, word: str) -> int:
    mots = sentence.split()
    counter = 0
    for mot in mots:
        if mot == word:
            counter+= 1
    return counter
    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'l', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world! est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
