from foo import vigenere_encode


print('Exercise 5.4')

message = 'Th1s 1s V1g3n3r3 c0d3!_9'
key = 'hack! $'

print(f'Original message is \'{message}\'')

coded_message = vigenere_encode(message, key)
print(f'Coded message is \'{coded_message}\'')

decoded_message = vigenere_encode(coded_message, key, decode=True)
print(f'Decoded message is \'{decoded_message}\'')