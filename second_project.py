import re


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False



def get_sql_commant(username, email):
    if isValid(email):
        sql_commant = f"update account set email = '{email}' where username = '{username}'"
        print(sql_commant)
    else:
        print("Email neni validni :(")



username = input("Zadej username: ")
email = input("Zadej email: ")

print(get_sql_commant(username, email))
