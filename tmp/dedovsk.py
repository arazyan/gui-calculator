import numbersystem as ns
from converter import binchecker, octchecker, decchecker, hexchecker
def convert(number : int, input_system : str = '10', output_system : str = '10'):
    if input_system == '2':
        try:
            binchecker(abs(number))
        except:
            print('Incorrect binary number')
        if output_system == '8':
            number = ns.binaryToOctal(str(number))
        elif output_system == '10':
            number = ns.binaryToDecimal(str(number))
        elif output_system == '16':
            number = ns.binaryToHexa(str(number))
    elif input_system == '8':
        try:
            octchecker(abs(number))
        except:
            print('Incorrect octal number')
        if output_system == '2':
            number = ns.octalToBinary(str(number))
        elif output_system == '10':
            number = ns.octalToDecimal(str(number))
        elif output_system == '16':
            number = ns.octalToHexa(str(number))
    elif input_system == '16':
        try:
            hexchecker(abs(number))
        except:
            print('Incorrect hexa number')
        if output_system == '2':
            number = ns.hexaToBinary(str(number))
        elif output_system == '8':
            number = ns.hexaToOctal(str(number))
        elif output_system == '10':
            number = ns.hexaToDecimal(str(number))
    else:
        try:
            decchecker(abs(number))
        except:
            print('Incorrect decimal number')
        if output_system == '2':
            number = ns.decimalToBinary(str(number))
        elif output_system == '8':
            number = ns.decimalToOctal(str(number))
        elif output_system == '16':
            number = ns.decimalToHexa(str(number))
    return number