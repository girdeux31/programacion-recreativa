from foo import xor_encoder, xor_decoder


print('Exercise 5.3')

message = '1110001010101110100100111'
code = '0010010100111'

print(f'Original message is \'{message}\'')

coded_message = xor_encoder(message, code)
print(f'Coded message is \'{coded_message}\'')

decoded_message = xor_decoder(coded_message, code)
print(f'Decoded message is \'{decoded_message}\'')