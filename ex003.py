expr = input('Digite algo: ')
msg = ''
print('A expressão {}: '.format(expr))
print('possui {} caracteres'.format(len(expr)))

if expr.isnumeric():
    msg = 'contém somente números;'
elif expr.isalpha():
    msg = 'contém somente letras;'
elif expr.isalnum():
    msg = 'contém letras e números;'

print(msg)
if expr.islower():
    msg = 'possui letras minúsculas;'
elif expr.isupper():
    msg = 'possui letras maiúsculas;'
else:
    msg = 'possui letras maiúsculas e minúsculas;'
print(msg)
