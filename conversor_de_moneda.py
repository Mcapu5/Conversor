#Valores
usuario = input("Introduce tu nombre de Usuario: ")
dinero = float(input("Introduce el dinero a convertir: "))
eth = 3493.47
dolar = 111.34
euro = 122.84
btc = 46390.30
#Calculo a dolar
dolares = dinero / dolar
dolares = round(dolares, 2)
dolares = str(dolares)
#Calculo a euro
euros = dinero / euro
euros = round(euros, 2)
euros = str(euros)
#Calculo a eth
eths = dinero / eth
eths = round(eths, 2)
eths = str(eths)
#Calculo a BTC
btcs = dinero / btc
btcs = round(btcs, 2)
btcs = str(btcs)
#Input del Usuario
print("1.Dolar")
print("2.Euro")
print("3.ETH")
print("4.BTC")
moneda = input("Introduce a la moneda que deseas convertir: ")
moneda = int(moneda)
if moneda == 1:
    print(usuario + " Tienes $"+ dolares + " dolares")
elif moneda == 2:
    print(usuario + " Tienes €"+ euros + " euros")
elif moneda == 3:
    print(usuario + " Tienes $"+ eths + " ethereum")
elif moneda == 4:
    print(usuario + " Tienes $"+ btcs + " bitcoins")
else:
    print("La opcion ingresada no es valida, vuelva a intentarlo.")