message=input("Введите сообщение:")
#print(message)
length = len(message)
#print(length)
#print(message[:3])
#print(message[3:])
print("\033[34m\033[43m{message}\033[0m")
cipher_one=message
cipher_one=cipher_one.replace('и','с')
cipher_one=cipher_one.replace('п','м')
cipher_one=cipher_one.replace('т','х')
cipher_one=cipher_one.replace('в','г')
print("Шифр 1", cipher_one)
cipher_two=message[::-1]
print("Шифр 2", cipher_two)
cipher_three=message
odd= message[::2]
even=message[1::2]
cipher_three=odd+even
print("Шифр 3", cipher_three)
cipher_four=message
first_letter =cipher_four[0]
last_letter=cipher_four[-1]
length = len(message)
cipher_four = last_letter + cipher_four[1:length-1] + first_letter


print("Шифр 4", cipher_four)
cipher_five=message
half_length = len(message)//2
cipher_five = message[half_length:] + message[:half_length]
print("Шифр 5", cipher_five)
decipher_one=cipher_one.replace('с','и')
decipher_one=decipher_one.replace('х','т')
decipher_one=decipher_one.replace('м','п')
decipher_one=decipher_one.replace('г','в')
print("Расшифровка 1", decipher_one)
decipher_two=cipher_two[::-1]
print("Расшифровка 2", decipher_two)
zero_line=""
one_line=odd
two_line=even
for symbol in range(len(one_line)):
    zero_line+=one_line[symbol]
    if symbol < len (two_line):
        zero_line+=two_line[symbol]
print("Расшифровка 3", zero_line)
decipher_four =  first_letter + message[1:length-1] + last_letter
print("Расшифровка 4", decipher_four)
decipher_five=cipher_five
decipher_five =cipher_five[half_length:] + cipher_five[:half_length]
print("Расшифровка 5", decipher_five)
