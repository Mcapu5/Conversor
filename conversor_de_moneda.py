usuario = input("Introduce tu nombre de usuario: ")
def convert(tipo_moneda, valor_moneda):
    dinero = int(input("¿Cuanto dinero desea convertir?: "))
    moneda = dinero / valor_moneda
    moneda = round(moneda, 2)
    moneda = str(moneda) 
    print(usuario + ", tienes $" + moneda, tipo_moneda)

menu = """
Bienvenido al conversor de monedas """ + usuario + """

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