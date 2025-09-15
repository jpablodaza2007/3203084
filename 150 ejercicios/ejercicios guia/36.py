while True:
    print("\n" + "="*40)
    print("  CALCULADORA CIENTÍFICA")
    print("="*40)
    print("1.  Suma")
    print("2.  Resta") 
    print("3.  Multiplicación")
    print("4.  División")
    print("5.  Potencia (x^y)")
    print("6.  Raíz cuadrada")
    print("7.  Raíz cúbica")
    print("8.  Factorial")
    print("9. Seno")
    print("10. Coseno")
    print("11. Tangente")
    print("0.  Salir")
    print("="*40)
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == '0':
        print("Fin")
        break
    
    elif opcion == '1':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        resultado = a + b
        print(f"Resultado: {a} + {b} = {resultado}")
    
    elif opcion == '2':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        resultado = a - b
        print(f"Resultado: {a} - {b} = {resultado}")
    
    elif opcion == '3':
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        resultado = a * b
        print(f"Resultado: {a} × {b} = {resultado}")
    
    elif opcion == '4':
        a = float(input("Dividendo: "))
        b = float(input("Divisor: "))
        if b == 0:
            print("Error: No se puede dividir por cero")
        else:
            resultado = a / b
            print(f"Resultado: {a} ÷ {b} = {resultado}")
    
    elif opcion == '5':
        base = float(input("Base: "))
        exponente = float(input("Exponente: "))
        resultado = base ** exponente
        print(f"Resultado: {base}^{exponente} = {resultado}")
    
    elif opcion == '6':
        numero = float(input("Número: "))
        if numero < 0:
            print("Error: No se puede calcular raíz cuadrada de número negativo")
        else:

            if numero == 0:
                resultado = 0
            else:
                x = numero
                for _ in range(10):
                    x = (x + numero / x) / 2
                resultado = x
            print(f"Resultado: √{numero} = {resultado}")
    
    elif opcion == '7':
        numero = float(input("Número: "))
        if numero >= 0:
            resultado = numero ** (1/3)
        else:
            resultado = -((-numero) ** (1/3))
        print(f"Resultado: ∛{numero} = {resultado}")
    
    
    elif opcion == '8':
        numero = int(input("Número entero positivo: "))
        if numero < 0:
            print("Error: El factorial solo está definido para números enteros no negativos")
        else:
            factorial = 1
            i = 1
            while i <= numero:
                factorial *= i
                i += 1
            print(f"Resultado: {numero}! = {factorial}")
    
    elif opcion == '9':
        angulo = float(input("Ángulo en radianes: "))

        pi = 3.14159265359
        while angulo > 2 * pi:
            angulo -= 2 * pi
        while angulo < -2 * pi:
            angulo += 2 * pi
        
        seno = 0
        termino = angulo
        n = 1
        
        for i in range(15):
            seno += termino
            termino *= -angulo * angulo / ((n + 1) * (n + 2))
            n += 2
        
        print(f"Resultado: sen({angulo:.4f}) = {seno:.6f}")
    
    elif opcion == '10':
        angulo = float(input("Ángulo en radianes: "))

        pi = 3.14159265359
        while angulo > 2 * pi:
            angulo -= 2 * pi
        while angulo < -2 * pi:
            angulo += 2 * pi
        
        coseno = 1
        termino = 1
        n = 0
        
        for i in range(15):
            termino *= -angulo * angulo / ((n + 1) * (n + 2))
            coseno += termino
            n += 2
        
        print(f"Resultado: cos({angulo:.4f}) = {coseno:.6f}")
    
    elif opcion == '11':
        angulo = float(input("Ángulo en radianes: "))

        pi = 3.14159265359
        while angulo > 2 * pi:
            angulo -= 2 * pi
        while angulo < -2 * pi:
            angulo += 2 * pi
        
        seno = 0
        termino = angulo
        n = 1
        
        for i in range(15):
            seno += termino
            termino *= -angulo * angulo / ((n + 1) * (n + 2))
            n += 2
        
        coseno = 1
        termino = 1
        n = 0
        
        for i in range(15):
            termino *= -angulo * angulo / ((n + 1) * (n + 2))
            coseno += termino
            n += 2
        
        if coseno == 0:
            print("Error: Tangente no definida (coseno = 0)")
        else:
            tangente = seno / coseno
            print(f"Resultado: tan({angulo:.4f}) = {tangente:.6f}")
    
    else:
        print("Opción no válida.")
    
    input("\nPresiona Enter para continuar...")