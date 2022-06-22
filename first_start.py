print('LICENSE CHECK!')

file=open('.git\objects\info\lic.md', 'r')
l1=file.readline(20)
l2=file.readline(20)
l3=file.readline(20)
l4=file.readline(20)
l5=file.readline(20)
l6=file.readline(20)
file.close()

a1=input('enter battle code: ')
a2=input('enter magazine code: ')
a3=input('enter bazare code: ')
a4=input('enter save code: ')
a5=input('enter subfunc code: ')
a6=input('enter check code: ')

if a1==l1:
    file=open('licence_c.md')
    file.write('battle true\n')
    file.close()
elif a2==l2:
    file=open('licence_c.md')
    file.write('magazine true\n')
    file.close()
elif a3==l3:
    file=open('licence_c.md')
    file.write('bazar true\n')
    file.close()
elif a4==l4:
    file=open('licence_c.md')
    file.write('save true\n')
    file.close()
elif a5==l5:
    file=open('licence_c.md')
    file.write('subfunc true\n')
    file.close()
elif a6==l6:
    file=open('licence_c.md')
    file.write('check true')
    file.close()
else:
    print("you don't have licence")