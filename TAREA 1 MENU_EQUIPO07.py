def decimal_to_binary(decimal):
    integer_part = int(decimal)
    fractional_part = decimal - integer_part

    integer_binary = bin(integer_part)[2:]
    fractional_binary = ""
    while len(fractional_binary) < 4:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit

    return f"{integer_binary}.{fractional_binary}"

def binary_to_decimal(binary):
    integer_part, fractional_part = binary.split(".")

    decimal_integer = int(integer_part, 2)
    decimal_fractional = 0
    for i in range(min(len(fractional_part), 4)):
        decimal_fractional += int(fractional_part[i]) * 2 ** -(i + 1)

    return decimal_integer + decimal_fractional

def decimal_to_octal(decimal):
    return oct(int(decimal))

def octal_to_decimal(octal):
    return int(octal, 8)

def decimal_to_hexadecimal(decimal):
    return hex(int(decimal))

def hexadecimal_to_binary(hexadecimal):
    return bin(int(hexadecimal, 16))[2:]

def hexadecimal_to_decimal(hexadecimal):
    return int(hexadecimal, 16)

def binary_to_octal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_octal(decimal)

def octal_to_binary(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_binary(decimal)

def binary_to_hexadecimal(binary):
    decimal = binary_to_decimal(binary)
    return decimal_to_hexadecimal(decimal)

def octal_to_hexadecimal(octal):
    decimal = octal_to_decimal(octal)
    return decimal_to_hexadecimal(decimal)

def hexadecimal_to_octal(hexadecimal):
    decimal = hexadecimal_to_decimal(hexadecimal)
    return decimal_to_octal(decimal)

def main():
    while True:
        print("1. Convertir de decimal a binario")
        print("2. Convertir de binario a decimal")
        print("3. Convertir de decimal a octal")
        print("4. Convertir de octal a decimal")
        print("5. Convertir de decimal a hexadecimal")
        print("6. Convertir de hexadecimal a decimal")
        print("7. Convertir de hexadecimal a binario")
        print("8. Convertir de binario a hexadecimal")
        print("9. Convertir de octal a binario")
        print("10. Convertir de binario a octal")
        print("11. Convertir de octal a hexadecimal")
        print("12. Convertir de hexadecimal a octal")
        print("13. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            decimal = float(input("Ingresa el número en base decimal: "))
            print("El número en binario es:", decimal_to_binary(decimal))
        elif opcion == "2":
            binary = input("Ingresa el número en base binario: ")
            print("El número en decimal es:", binary_to_decimal(binary))
        elif opcion == "3":
            decimal = float(input("Ingresa el número en base decimal: "))
            print("El número en octal es:", decimal_to_octal(decimal))
        elif opcion == "4":
            octal = input("Ingresa el número en base octal: ")
            print("El número en decimal es:", octal_to_decimal(octal))
        elif opcion == "5":
            decimal = float(input("Ingresa el número en base decimal: "))
            print("El número en hexadecimal es:", decimal_to_hexadecimal(decimal))
        elif opcion == "6":
            hexadecimal = input("Ingresa el número en base hexadecimal: ")
            print("El número en decimal es:", hexadecimal_to_decimal(hexadecimal))
        elif opcion == "7":
            hexadecimal = input("Ingresa el número en base hexadecimal: ")
            print("El número en binario es:", hexadecimal_to_binary(hexadecimal))
        elif opcion == "7":
            hexadecimal = input("Ingresa el número en base hexadecimal: ")
            print("El número en decimal es:", hexadecimal_to_decimal(hexadecimal))
        elif opcion == "8":
            binary = input("Ingresa el número en base binario: ")
            print("El número en hexadecimal es:", binary_to_hexadecimal(binary))
        elif opcion == "9":
            octal = input("Ingresa el número en base octal: ")
            print("El número en binario es:", octal_to_binary(octal))
        elif opcion == "10":
            binary = input("Ingresa el número en base binario: ")
            print("El número en octal es:", binary_to_octal(binary))
        elif opcion == "11":
            octal = input("Ingresa el número en base octal: ")
            print("El número en hexadecimal es:", octal_to_hexadecimal(octal))
        elif opcion == "12":
            hexadecimal = input("Ingresa el número en base hexadecimal: ")
            print("El número en octal es:", hexadecimal_to_octal(hexadecimal))
        elif opcion == "13":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
    