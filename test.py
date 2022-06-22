from engine import subfunc

subfunc.save('amogus\n', 'save.txt')
subfunc.save('amogus2', 'save.txt')

file=open('save.txt')

amogus=file.read()

print(amogus)

subfunc.clearsave('save.txt')