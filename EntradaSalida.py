import datetime

while True:
    try:
        fecha = input("Introducir Fecha dd-mm-aaaa: ")
        fecha = datetime.datetime.strptime(fecha, "%d-%m-%Y")
        break

    except:
        print ("Fecha incorrecta\n")

print(fecha)
