from foo import xor_encode


print('Exercise 5.3')

message = '1110001010101110100100111'
code = '0010010100111'

print(f'Original message is \'{message}\'')

coded_message = xor_encode(message, code)
print(f'Coded message is \'{coded_message}\'')

decoded_message = xor_encode(coded_message, code)
print(f'Decoded message is \'{decoded_message}\'')