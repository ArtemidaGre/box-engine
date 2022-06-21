#file with modules and func :)

from game_file import hp, language

class game:
    def battle(damage, ehp, edamage, defe, edef):   
        from random import randint
        from time import sleep
        global hp, win, language
        while True:
            luck=randint(0, 100)
            if luck>=21:
                if hp>=1:
                    hp=hp-(edamage*edef)
                    sleep(0.2)
            if luck<=80:
                if ehp>=1:
                    ehp=ehp-(damage*defe)
                    sleep(0.2)
            if hp<=0:
                win=0
                if language=='rus':
                    print('вы проиграли :(')
                elif language=='eng':
                    print('you lose :(')
                break
            if ehp<=0:
                win=1
                if  language=='rus':
                    print('Вы победили :)')
                elif language=='eng':
                    print('you win :)')
                break
    def magazine(i1, c1, i2, c2, i3, c3):
        global coins, language, a1, a2, a3
        a1=a2=a3=0
        if language=='rus' or 1:
            while True:
                print('у вас', coins, 'монет.')
                print('Вы можете купить:\n1.', i1, 'за', c1, 'монет.\n2.', i2, 'за', c2, 'монет.\n3.', i3, 'за', c3, 'монет.')
                choise=input('>>>')
                if choise==1 or i1:
                    if coins>=c1 and a1==0:
                        print('вы купили', i1)
                        a1=1
                    else:
                        print('вы не можете купить', i1)
                if choise==2 or i2:
                    if coins>=c2 and a2==0:
                        print('вы купили', i2)
                        a2=1
                    else:
                        print('вы не можете купить', i2)
                if choise==3 or i3:
                    if coins>=c3 and a3==0:
                        print('вы купили',i3)
                        a3=3
                    else:
                        print('вы не можете купить', i3)
                c_buy=input('продолжить покупки?\n>>>')
        if language=='eng' or 2:
            while True:
                print('you can buy:\n1.', i1, 'it costs', c1, 'coins.\n2.', i2, 'it costs', c2, 'coins.\n3.', i3, 'it costs', c3, 'coins.')
                choise=input('>>>')
                if choise==1 or i1:
                    if coins>=c1 and a1==0:
                        print('you buy', i1)
                        a1=1
                    else:
                        print("you don't buy", i1)
                if choise==2 or i2:
                    if coins>=c2 and a2==0:
                        print('you buy', i2)
                        a2=1
                    else:
                        print("you don't buy", i2)
                if choise==3 or i3:
                    if coins>=c3 and a3==0:
                        print('you buy',i3)
                        a3=3
                    else:
                        print("you don't buy", i3)
                c_buy=input('continue buying?\n>>>')
    