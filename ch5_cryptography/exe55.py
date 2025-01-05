from foo import roman_encoder, roman_decoder


print('Exercise 5.5')

message = '3999'

print(f'Original message is \'{message}\'')

coded_message = roman_encoder(message)
print(f'Coded message is \'{coded_message}\'')

decoded_message = roman_decoder(coded_message)
print(f'Decoded message is \'{decoded_message}\'')