print("Hola usuario, inicia con nuestro menú llamado MenSys, elije la opcion que quieras para interactuar con este programa.")
print("Menú principal")
print("1. Imprimir")
print("2. Operaciones")
print("3. Salir")
op = input("Ingresa el numero de la opción deseada: ")
if op == "3":
    print(" Gracias por usar el programa")
if op =="1":
    print("Mp / Imprimir")
    print("Elije a un gran programador")
    print("1. Dennis Ritchie")
    print("2. Linus Torvalds")
    print("3. Volver al menú principal ")
else:
    ("Error")
    op2= input("Ingrese el número de la opción deseada: ")
    while op2 == "3":
        print("Has sido redirigido al menú principal")
        print("1. Imprimir")
        print("2. Operaciones")
        print("3. Salir")
        op = input("Ingresa el numero de la opción deseada: ")
        break
    if op2 == "1":
        print("Dennis Ritchie  (1941-2011) fue un influyente científico de la computación estadounidense, reconocido como el creador del lenguaje de programación C y co-desarrollador del sistema operativo Unix en Bell Labs. ")
        input("Ingresa 3 para volver al menú principal: ")
    elif op2 == "2":
        print("Nacido en 1969 es un ingeniero de software finlandés, mundialmente reconocido por crear el núcleo (kernel) Linux en 1991, base de la mayoría de los sistemas operativos libres.")
        input("Ingresa 3 para volver al menú principal: ")
    elif op == "2":
        print("MP / Operaciones")
    print("elija una de las operaciones con el numero indicado")
    print("1.Suma")
    print("2.Resta")
    print("3.volver al menu principal")
    op3=input("Ingrese el numero de numero de la opcion: ")
    if op3=="1":
        num1=float(input("Ingrese el primer numero: "))
        num2=float(input("ingrese el segundo numero: "))
        print("El resultado de la suma es", num1+num2)
        input("Ingresa 3 para volver al menú principal: ")
    elif op3=="2":
        num3=float(input("Ingrese el primer numero: "))
        num4=float(input("ingrese el segundo numero: "))
        print("El resultado de la resta es", num3+num4)
        input("Ingresa 3 para volver al menú principal: ")
    while op3 == "3":
        print("Has sido redirigido al menú principal")
        print("1. Imprimir")
        print("2. Operaciones")
        print("3. Salir")
        op = input("Ingresa el numero de la opción deseada: ")
        break
    else:
        ("Error")

