from os import startfile

print('LICENSE CHECK!')

file=open('saves\licenze', 'r')
l1=file.readline(19)
a1P=file.readline(1)
l2=file.readline(19)
a1P=file.readline(1)
l3=file.readline(19)
a1P=file.readline(1)
l4=file.readline(19)
a1P=file.readline(1)
l5=file.readline(19)
file.close()

a1=input('enter battle code: ')
a2=input('enter magazine code: ')
a3=input('enter bazare code: ')
a4=input('enter save code: ')
a5=input('enter subfunc code: ')

if a1==l1:
    file=open('licence_c.md', 'w+')
    file.write('battle true\n')
    file.close()
elif a2==l2:
    file=open('licence_c.md', 'w+')
    file.write('magazine true\n')
    file.close()
elif a3==l3:
    file=open('licence_c.md', 'w+')
    file.write('bazar true\n')
    file.close()
elif a4==l4:
    file=open('licence_c.md', 'w+')
    file.write('save true\n')
    file.close()
elif a5==l5:
    file=open('licence_c.md', 'w+')
    file.write('subfunc true\n')
    file.close()
else:
    print("you don't have licence")

startfile('language.pyw')

a=input('\nenter something to finish\n>>>')