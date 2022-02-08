# temps[0] : jours / temps[1]: heures / temps[2]: minutes / temps[3]: secondes
temps = (3, 23, 1, 34)


def tempsEnSeconde(temps):
    seconde = (temps[0] * (60*60*24)) + (temps[1] * (60*60)) + (temps[2] * 60) + temps[3]
    return seconde


print(type(temps))
print("1 - Il y a", tempsEnSeconde(temps), "secondes.")


def secondeEnTemps(seconde):
    jour = seconde // (60*60*24)
    heure = (seconde % (24 * 3600)) // 3600
    minute = ((seconde % (24 * 3600)) // 60) % 60
    seconde = ((seconde % (24 * 3600)) % 60) % 60
    temps = (jour, heure, minute, seconde)
    return temps


temps = secondeEnTemps(10000)
print("2 - Cela fait", temps[0], "jour(s)", temps[1], "heure(s)", temps[2], "minute(s)", temps[3], "seconde(s)")


def afficheTemps(temps):
    print("3 - Il y a ", end=" ")
    if temps[0] == 0:
        print(end=" ")
    elif temps[0] == 1:
        print(temps[0], "jour,", end=" ")
    else:
        print(temps[0], "jours", end=" ")

    if temps[1] == 0:
        print(end=" ")
    elif temps[1] == 1:
        print(temps[1], "heure,", end=" ")
    else:
        print(temps[1], "heures,", end=" ")

    if temps[2] == 0:
        print(end=" ")
    elif temps[2] == 1:
        print(temps[2], "minute,", end=" ")
    else:
        print(temps[2], "minutes,", end=" ")

    if temps[3] == 0:
        print(end=" ")
    elif temps[3] == 1:
        print(temps[3], "seconde.")
    else:
        print(temps[3], "secondes.")


afficheTemps((1, 0, 14, 23))


def demandeTemps():
    jour = int(input("Entrée un nombre de jour(s)"))
    heure = int(input("Entrée un nombre d'heure(s)"))
    minute = int(input("Entrée un nombre de minute(s)"))
    seconde = int(input("Entrée un nombre de seconde(s)"))
    while jour>31 or jour<0 :
        jour = int(input("Entrée un nombre de jour(s) compris entre 0 et 31 :"))
    while heure>23 or heure<0 : 
        heure = int(input("Entrée un nombre d'heure(s) compris entre 0 et 23 :"))
    while minute>59 or minute<0 :
        minute = int(input("Entrée un nombre de minute(s) compris entre 0 et 59 :"))
    while seconde>59 or seconde<0 :
        seconde = int(input("Entrée un nombre de seconde(s) compris entre 0 et 59 :"))
    temps = (jour, heure, minute, seconde)
    return temps


afficheTemps(demandeTemps())
