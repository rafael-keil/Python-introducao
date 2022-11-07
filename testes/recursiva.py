# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 19:48:39 2021

@author: rafak
"""

def contagemRegressiva(n):
    if (n == 0):
        print("Fogo!")
    else:
        print(n)
        contagemRegressiva(n-1)
    print("Fim")    

def main():
    contagemRegressiva(5)

if __name__ == "__main__":
    main()