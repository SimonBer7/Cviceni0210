import re


def password_policy(username, password):
    if len(password) < 10:  #delka
        return False

    if not re.search(r"\d", password):  #obsahuje cislo
        return False

    if not re.search(r"[a-z]", password):   #obsahuje male pismeno
        return False

    if not re.search(r"[A-Z]", password):     #obsahuje velke pismeno
        return False

    if username in password:
        return False

    return True









username = input("Zadej username: ")
password = input("Zadej password: ")

if password_policy(username, password):
    print("Username: "+str(username)+", password: "+str(password))
else:
    raise ValueError
