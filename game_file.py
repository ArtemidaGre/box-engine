#this is file with scenario and any things ;)



print('choose language\n1.русский\n2.english')
language=input('>>>')

if language==1 or 'русский':
    language='rus'
if language==2 or 'english':
    language='eng'

hp=100
damage=15
defence=1

if language=='rus':
    print('Добро пожаловать в симулятор квеста 2!')
    name=str(input('Как ваш называть?\n>>>'))
    if name=='Debug':
        DebugMode=True
        print('Включен режим разработчика')
    print('После победы над боссом из первой части вы пошли по дороге\nВдруг на вас выскочила собака!')
    choise=input('дать ей отпор?\n(да или нет, такой выбор будет практически во всей игре)\n>>>')
    if choise=='да':
        game.battle(damage, 15, 5, defence, 1.5)
    






















if language=='eng':
    print('Welcome to Quest Simulator 2!')
    name=str(input("What's your name?\n>>>"))
    if name=='Debug':
        DebugMode=True
        print('Debug mode enabled')