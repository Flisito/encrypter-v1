import encryter

while True:
    print("Menú:")
    print("1. Encriptar")
    print("2. Desencriptar")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        mensaje = input("Ingrese el mensaje a encriptar: ")
        llave = encryter.generadorllave(mensaje)
        print("Su llave para desencriptar: " + str(llave))
        mensaje_encriptado = encryter.encriptar(mensaje, llave)
        print("Mensaje encriptado: ", mensaje_encriptado)

    elif opcion == "2":
        mensaje_encriptado = input("Ingrese el mensaje encriptado: ")
        llave = input("Ingrese la llave: ")
        mensaje_original = encryter.desencriptar(mensaje_encriptado, llave)
        print("Mensaje desencriptado: ", mensaje_original)

    elif opcion == "3":
        break
    else:
        print("Opción no válida")