print('LICENSE CHECK!')

file=open('saves\licenze', 'r')
l1=file.readline(19)
am1=file.readline(1)
l2=file.readline(19)
am1=file.readline(1)
l3=file.readline(19)
am1=file.readline(1)
l4=file.readline(19)
am1=file.readline(1)
l5=file.readline(19)
am1=file.readline(1)
l6=file.readline(19)
file.close()

a1=input('enter battle code: ')
a2=input('enter magazine code: ')
a3=input('enter bazare code: ')
a4=input('enter save code: ')
a5=input('enter subfunc code: ')
a6=input('enter check code: ')

if a1==l1:
    file=open('licence_c.md', 'w+')
    file.write('battle true\n')
    file.close()
if a2==l2:
    file=open('licence_c.md', 'w+')
    file.write('magazine true\n')
    file.close()
if a3==l3:
    file=open('licence_c.md', 'w+')
    file.write('bazar true\n')
    file.close()
if a4==l4:
    file=open('licence_c.md', 'w+')
    file.write('save true\n')
    file.close()
if a5==l5:
    file=open('licence_c.md', 'w+')
    file.write('subfunc true\n')
    file.close()
if a6==l6:
    file=open('licence_c.md', 'w+')
    file.write('check true')
    file.close()
else:
    print("you don't have licence")