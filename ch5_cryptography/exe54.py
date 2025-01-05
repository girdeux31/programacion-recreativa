from foo import vigenere_encoder, vigenere_decoder


print('Exercise 5.4')

message = 'Th1s 1s V1g3n3r3 c0d3!_9'
key = 'hack! $'

print(f'Original message is \'{message}\'')

coded_message = vigenere_encoder(message, key)
print(f'Coded message is \'{coded_message}\'')

decoded_message = vigenere_decoder(coded_message, key)
print(f'Decoded message is \'{decoded_message}\'')