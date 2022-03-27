# -*- coding: utf-8 -*-

from pathlib import Path
def main():
    """"""
    fname = Path("problem13.txt")
    somme = 0
    with open(fname, 'r') as f:
        ligne = f.readline()
        i = 0
        while ligne:
            i +=1
            print(i,end="\r")
            somme += int(ligne[:-1])
            ligne = f.readline()
    return somme

if __name__ == "__main__":
    print(main())
