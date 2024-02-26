
def binary_to_decimal_ieee754(binary):
    sign = -1 if binary[0] == '1' else 1
    exponent = int(binary[1:9], 2) - 127
    mantissa = 1 + sum(int(binary[i]) * 2 ** -(i - 8) for i in range(9, 32))
    decimal = sign * mantissa * 2 ** exponent
    return decimal

def decimal_to_binary_ieee754(decimal):
    # Obteniendo el signo
    sign = '1' if decimal < 0 else '0'
    # Convirtiendo el número a su representación binaria normalizada
    integer_part, fractional_part = str(decimal).split('.')
    integer_part = bin(int(integer_part))[2:]

    fractional_binary = ''
    fractional_part = '0.' + fractional_part
    while len(fractional_binary) < 23 and fractional_part != '0.0':
        fractional_part = str(float(fractional_part) * 2)
        int_part, frac_part = fractional_part.split('.')
        fractional_binary += int(int_part)

    normalized_binary = integer_part + '.' + fractional_binary

    # Ajustando la mantisa a 23 bits
    mantissa = normalized_binary[:23].ljust(23, '0')
    # Calculando el exponente
    exponent = len(integer_part) - 1 + 127
    # Convirtiendo el exponente a binario de 8 bits
    exponent_binary = bin(exponent)[2:].rjust(8, '0')
    # Combinando los componentes para formar el número en formato IEEE 754
    ieee754_binary = sign + exponent_binary + mantissa
    return ieee754_binary


def main():
    while True:
        print("Menú")
        print("1. Binario a Decimal (IEEE 754)")
        print("2. Decimal a Binario (IEEE 754)")
        print("3. Salir")
        option = input("Opción: ")

        if option == '1':
            binary_input = input("Ingrese el número binario en formato IEEE 754 de precisión simple: ")
            decimal_output = binary_to_decimal_ieee754(binary_input)
            print("El número decimal es:", decimal_output)
        elif option == '2':
            decimal_input = float(input("Ingrese el número decimal: "))
            binary_output = decimal_to_binary_ieee754(decimal_input)
            print("El número binario en formato IEEE 754 de precisión simple es:", binary_output)
        elif option == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
