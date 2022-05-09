user = input("Introduce tu nombre de usuario: ")
def convert(money_type, money_value):
    money = int(input("¿Cuanto dinero desea convertir?: "))
    coin = money / money_value
    coin = round(coin, 2)
    coin = str(coin) 
    print(user + ", tienes $" + coin, money_type)

menu = """
Bienvenido al conversor de monedas """ + user + """

1 - Dolar
2 - Euro
3 - Ethereum
4 - Bitcoin

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    convert("dolares", 111.34)
elif opcion == 2:
    convert("euros", 122.84)
elif opcion == 3:
    convert("ethereum", 388962.94)
elif opcion == 4:
    convert("bitcoins", 5165096.0)
else:
    print("Ingresa una opcion valida por favor")