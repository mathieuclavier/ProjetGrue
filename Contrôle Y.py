from math import*

def mouvy(y, Lbras):
    alpha=degrees(asin(y/Lbras))
    return alpha

if __name__=="__main__":
    while True:
        y=float(input("Axe Y: "))
        Lbras=float(input("Longueur 2eme Segment: "))
        print("Alpha:", mouvy(y,Lbras))

        continuer = input("Voulez vous continuer? [o/N]").strip().lower()
        if not continuer.startswith('o'):