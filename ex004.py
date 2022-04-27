expr = input('Digite algo: ')
msg = ''
exp = list(expr)
print('\nA expressão possui {} caracteres: {}'.format(len(expr), exp))
num = 0
spc = 0
m = 0
M = 0
for x in exp:
    if x.isnumeric():
        num = num + 1
    if x.isspace():
        spc = spc + 1
    if x.islower():
        m = m + 1
    if x.isupper():
        M = M + 1
msg = ''
if num > 0:
    msg = msg + str(num) + ' número(s), '
if spc > 0:
    msg = msg + str(spc) + ' espaço(s), '
if m > 0:
    msg = msg +str(m) + ' letra(s) minúscula(s), '
if M > 0:
    msg = msg + str(M) + ' letra(s) maiúscula(s), '

cesp = len(expr) - (num + spc + m + M)

if cesp > 0:
    msg = msg + str(cesp) + ' caracter(es) especial(is)'

print('\nEntre eles: ', msg)
