#Box engine to console quests, work in russian and english language.

from random import randint


file=open('language.txt', 'r')
language=file.read()

class game:
    def battle(hp, damage, ehp, edamage, defe, edefe, lic_code):
        global win, language
        if language=='rus':
            start_hp=hp
            import time as t
            print('Бой начинается!')
            print('у вас', hp, 'hp, и', damage, 'урона\nу врага', ehp, 'hp, и', edamage, 'урона')
            t.sleep(0.5)
            import random as r
            while hp>=1 and ehp>=1:
                if hp>=1:
                    luck=r.randint(0, 100)
                    if luck>=21:
                        to_damage=r.randint(0, damage)*edefe
                        ehp=ehp-to_damage
                        print('вы ударили противника на', to_damage, 'урона, у него осталость', ehp, 'hp')
                        t.sleep(0.2)
                    elif luck<=20:
                        print('Вы промахнулисть')
                        t.sleep(0.2)
                    luck2=r.randint(0, 100)
                if ehp>=1:
                    if luck2>=41:
                        to_damage2=r.randint(0, edamage)*defe
                        hp=hp-to_damage2
                        print('враг вас ударил на', to_damage2, 'урона, у вас осталость', hp, 'hp')
                        t.sleep(0.2)
                    elif luck2<=40:
                        print('враг промахнулся')
                        t.sleep(0.2)
            if hp<=0.1:
                win=0
                print('вы проиграли!!!')
            elif hp>=0.0:
                win=1
                print('Победа!!!')
        if language=='eng':
            start_hp=hp
            import time as t
            print('fight has been started')
            print('you have', hp, 'hp, and', damage, 'damage\nenemy have', ehp, 'hp, and', edamage, 'damage')
            t.sleep(0.5)
            import random as r
            while hp>=1 and ehp>=1:
                if hp>=1:
                    luck=r.randint(0, 100)
                    if luck>=21:
                        to_damage=r.randint(0, damage)*edefe
                        ehp=ehp-to_damage
                        print('you beat enemy on', to_damage, 'damage, he had', ehp, 'hp')
                        t.sleep(0.2)
                    elif luck<=20:
                        print('you missed')
                        t.sleep(0.2)
                    luck2=r.randint(0, 100)
                if ehp>=1:
                    if luck2>=41:
                        to_damage2=r.randint(0, edamage)*defe
                        hp=hp-to_damage2
                        print('enemy beats you on', to_damage2, 'damage, you have', hp, 'hp')
                        t.sleep(0.2)
                    elif luck2<=40:
                        print('enemy missed')
                        t.sleep(0.2)
            if hp<=0.1:
                win=0
                print('You lose!!!')
            elif hp>=0.0:
                win=1
                print('You win!!!')
        else:
            print("you don't get licence!")
        t.sleep(0.5)
        
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
    def bazar(wish1, w1c, coins):
        global language, tryis
        if language=='rus':
            import random as r
            torg=0
            print('Вы можете купить', wish1, 'за', w1c,'рублей!')
            choise=str(input('Купить '+wish1+'?\n>>>'))
            if choise=='да':
                if coins>=w1c:
                    print('Вы можете купить это!')
                    choise=str(input('торговаться?\n>>>'))
                    if choise=='да':
                        while True:
                            torgm=int(input('до скольки вы хотите скинуть цену?\n>>>'))
                            if torgm>=(w1c/2.1):
                                print('Вы начали торги!')
                                torg=r.randint(0,100)
                                if torg>=80:
                                    print('У вас получилось!')
                                    w1c=torgm
                                    if coins>=w1c:
                                        coins=coins-w1c
                                        torg=1
                                        break
                                    elif coins<<w1c:
                                        print("у вас слишком мало денег!")
                                elif torg>=50:
                                    print('У вас почти получиось!')
                                    w1c=torgm+(w1c/5)
                                elif torg<=50:
                                    print('У вас не получилось')
                    elif choise=="нет":
                        print("♂fuck you♂")
            elif choise=="нет":
                print("♂fuck you♂")
                torg=0
        if language=='eng':
            import random as r
            torg=0
            print('you can buy', wish1, 'it costs', w1c,'coins')
            choise=str(input('buy '+wish1+'?\n>>>'))
            if choise=='yes':
                if coins>=w1c:
                    print('You can buy it!')
                    choise=str(input('bargain?\n>>>'))
                    if choise=='yes':
                        while True:
                            torgm=int(input('how much do you want to drop the price?\n>>>'))
                            if torgm>=(w1c/2.1):
                                print('You have started bidding!')
                                torg=r.randint(0,100)
                                if torg>=80:
                                    print('You did it!')
                                    w1c=torgm
                                    if coins>=w1c:
                                        coins=coins-w1c
                                        tryis=1
                                        break
                                    elif coins<<w1c:
                                        print("you have too little money!")
                                elif torg>=50:
                                    print('You almost did it!')
                                    w1c=torgm+(w1c/5)
                                elif torg<=50:
                                    print("You didn't succeed")
                    elif choise=="no":
                        print("♂fuck you♂")
            elif choise=="no":
                print("♂fuck you♂")
                tryis
    def new_battle(hp, ehp, damage, edamage, defence, edefence, ename):
        from random import randint
        from time import sleep
        file=open('language.txt', 'r')
        lang=file.readline(3)
        battle_f=True
        global win
        if lang=='rus':
            print('у вас', hp, 'hp и',damage, 'урона')
            print('Вы будите бится с', ename, 'Вот его статы:')
            print(ehp, 'hp и', damage, 'урона')
            first_kick=randint(1, 10)
            stun=estun=0
            while battle_f:
                if first_kick>=5:
                    estun=0
                    if hp>=1 and stun==0:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, damage)
                            print('вы ударили', ename, 'на', dam_tru, 'но', ename,'получил', dam_tru*edefence)
                            ehp-=dam_tru*edefence
                            sleep(0.2)
                        if luck<=199:
                            print('вы не попали по', ename)
                            sleep(0.2)
                        if luck>=850:
                            print(ename, 'оглушен')
                            estun=1
                            sleep(0.2)
                    elif hp>=1 and stun==1:
                        sleep(0.1)
                    elif hp<=0:
                        battle_f=False
                        win=0
                        print('вы проиграли(')
                    stun=0
                    if ehp>=1 and estun==0:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, edamage)
                            print(ename, 'ударил вас на', dam_tru, 'но вы получили', dam_tru*defence)
                            hp-=dam_tru*defence
                            sleep(0.2)
                        if luck<=199:
                            print(ename, 'не попал по вам!')
                            sleep(0.2)
                        if luck>=870:
                            print(ename, 'оглушил вас!')
                            stun=1
                    elif ehp>=1 and estun==1:
                        sleep(0.1)
                    elif ehp<=0:
                        battle_f=False
                        win=1
                        print('вы выиграли!!')
                else:
                    if ehp>=1:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, edamage)
                            print(ename, 'ударил вас на', dam_tru, 'но вы получили', dam_tru*defence)
                            hp-=dam_tru*defence
                        if luck<=199:
                            print(ename, 'не попал по вам!')
                    elif ehp<=0:
                        battle_f=False
                        win=1
                        print('вы выиграли!')
                    if hp>=1:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, damage)
                            print('вы ударили', ename, 'на', dam_tru, 'но', ename,'получил', dam_tru*edefence)
                            ehp-=dam_tru*edefence
                        if luck<=199:
                            print('вы не попали по', ename)
                    elif hp<=0:
                        battle_f=False
                        win=0
                        print('вы проиграли:(')
        if lang=='eng':
            print('you have', hp, 'hp, and',damage, 'damage')
            print('you will fight with', ename, 'here are his characteristics:')
            print(ehp, 'hp and', damage, 'damage')
            first_kick=randint(1, 10)
            stun=estun=0
            while battle_f:
                if first_kick>=5:
                    estun=0
                    if hp>=1 and stun==0:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, damage)
                            print('you beat', ename, 'on', dam_tru+',but', ename,'get', dam_tru*edefence)
                            ehp-=dam_tru*edefence
                            sleep(0.2)
                        if luck<=199:
                            print('MISS')
                            sleep(0.2)
                        if luck>=850:
                            print(ename, 'get stun')
                            estun=1
                            sleep(0.2)
                    elif hp>=1 and stun==1:
                        sleep(0.1)
                    elif hp<=0:
                        battle_f=False
                        win=0
                        print('you lose(')
                    stun=0
                    if ehp>=1 and estun==0:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, edamage)
                            print(ename, 'hit you on', dam_tru, 'but you get', dam_tru*defence)
                            hp-=dam_tru*defence
                            sleep(0.2)
                        if luck<=199:
                            print(ename, 'missed')
                            sleep(0.2)
                        if luck>=870:
                            print(ename, 'stunned you')
                            stun=1
                    elif ehp>=1 and estun==1:
                        sleep(0.1)
                    elif ehp<=0:
                        battle_f=False
                        win=1
                        print('you win!')
                else:
                    if ehp>=1:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, edamage)
                            print(ename, 'bit you on', dam_tru, ', but you get', dam_tru*defence)
                            hp-=dam_tru*defence
                            sleep(0.1)
                        if luck<=199:
                            print(ename, 'missed')
                            sleep(0.1)
                    elif ehp<=0:
                        battle_f=False
                        win=1
                        print('you win!')
                    if hp>=1:
                        luck=randint(1, 1000)
                        if luck>=200:
                            dam_tru=randint(1, damage)
                            print('you bit', ename, 'on', dam_tru, ', but', ename,'get', dam_tru*edefence)
                            ehp-=dam_tru*edefence
                            sleep(0.1)
                        if luck<=199:
                            print('you missed')
                            sleep(0.1)
                    elif hp<=0:
                        battle_f=False
                        win=0
                        print('you lose(')
        global win
    def battle_v3(hp, damage, defence, enemy_hp, enemy_damage, enemy_defence, enemy_name, accuracy, enemy_accuracy):
        file=open('language.txt', 'r')
        from os import system
        from random import randint
        sehp=enemy_hp
        sedamage=enemy_damage
        sedefence=enemy_defence
        def __ai__(my_hp, my_damage, my_defence, my_accuracy):
            global ai_choose
            if my_hp>=sehp*0.7:
                if my_accuracy<=41:
                    if my_defence>=0.90:
                        ai_cl=randint(1, 1000)
                        if ai_cl>=501:
                            ai_choose='attack'
                        else:
                            ai_choose='defence'
                    if my_defence<=0.89 and my_defence>=0.61:
                        ai_cl=randint(1, 1000)
                        if ai_cl>=801:
                            ai_choose='attack'
                        else:
                            ai_choose='defence'
                    if my_defence<=0.60 and my_defence>=0.31:
                        ai_cl=randint(1, 1000)
                        if ai_cl>=921:
                            ai_choose='attack'
                        elif ai_cl<<921 and ai_cl>=101:
                            ai_choose='defense'
                        else:
                            ai_choose='lost'
                    if my_defence<<0.31:
                        ai_cl=randint(0, 100)
                        if ai_cl>=91:
                            ai_choose='defence'
                        else:
                            ai_choose='attack'
                if my_accuracy>>40 and my_accuracy<=65:
                    if my_defence>=0.81:
                        ai_cl=randint(1, 1000)
                        if ai_cl>=501:
                            ai_choose='attack'
                        else:
                            ai_choose='defence'
                    if my_defence<=0.80 and my_defence>=0.51:
                        ai_cl=randint(1, 1000)
                        if ai_cl>=801:
                            ai_choose='attack'
                        else:
                            ai_choose='defence'
                    if my_defence<=0.50 and my_defence>=0.21:
                        ai_cl=randint(1, 1000)
                        if ai_cl>=921:
                            ai_choose='attack'
                        elif ai_cl<<921 and ai_cl>=101:
                            ai_choose='defense'
                        else:
                            ai_choose='lost'
                    if my_defence<<0.21:
                        ai_cl=randint(0, 100)
                        if ai_cl>=91:
                            ai_choose='defence'
                        else:
                            ai_choose='attack'
                if my_accuracy<=40:
                    if my_damage*5>=my_hp and my_defence<=0.80:
                        ai_cl=randint(0,1000)
                        if ai_cl>=801:
                            ai_choose='attack'
                        elif ai_cl<=599:
                            ai_choose='defence'
                        else:
                            ai_choose='lost'
                            
        lang=file.readline(3)
        system('cls||clear')
        if lang=='rus':
            print('Бой начинается!\nВот ваши характеристики:\n'+hp+'hp\n'+damage+'урона\n'+defence+' коэф. защиты')
            print('характеристики врага:\n'+enemy_hp+'hp\n'+enemy_damage+'урона\n'+enemy_defence+' коэф. защиты')
            while hp>=1 and enemy_hp>=1:
                battle_choise=str(input("Выбирите действие:\n1.атака\n2.защита\n3.пропуск\n4.обучение"))


class subfunc():
    global inventory, inventory_eff, inventory_use
    global hp, damage, defence, coins
    def save(to_save, save_name):
        file=open("saves/"+save_name, 'a+')
        file.write(str(to_save))
        file.newlines
        file.close()
    def clearsave(save_name):
        from os import remove
        file=open(save_name, 'w')
        file.close()
    def inventory_u(to_do, to_fl, num, eff, use):
        language=file.read()
        if language == 'rus':
            if to_do=='first':
                inventory=['пустая ячейка', 'пустая ячейка', 'пустая ячейка', 'пустая ячейка', 'пустая ячейка', 'пустая ячейка', 'пустая ячейка', 'пустая ячейка', 'пустая ячейка', 'пустая ячейка']
                inventory_use=['none', 'none', 'none, none', 'none', 'none, none', 'none', 'none,', 'none']
                inventory_eff=[0,0,0,0,0,0,0,0,0,0]
            if to_do=='remove':
                inventory[num] = 'пустая ячейка'
            if to_do=='check':
                print(inventory[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            if to_do=='add':
                num=input('на какое место поставить?\n>>>')
                print(inventory[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                inventory[num] = to_fl
                inventory_eff[num] = eff
                inventory_use[num] = use
            if to_do=='use':
                inventory[num] = 'пустая ячейка'
                if inventory_use[num]=='hal':
                    hp=hp+inventory_eff[num]
                if inventory_use[num]=='def':
                    defence=defence-inventory_eff[num]
                if inventory_use[num]=='dmg':
                    damage=damage+inventory_eff[num]
                if inventory_use[num]=='mny':
                    coins=coins+inventory_eff[num]
                else:
                    print('эффектов нет  :{')
            else:
                print('error')
        if language == 'eng':
            if to_do=='first':
                inventory=['none', 'none', 'none, none', 'none', 'none, none', 'none', 'none,', 'none']
                inventory_use=['none', 'none', 'none, none', 'none', 'none, none', 'none', 'none,', 'none']
                inventory_eff=[0,0,0,0,0,0,0,0,0,0]
            if to_do=='remove':
                inventory[num] = 'none'
            if to_do=='check':
                print(inventory[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            if to_do=='add':
                num=input('choose place to put?\n>>>')
                inventory[num] = to_fl
                inventory_eff[num] = eff
                inventory_use[num] = use
            if to_do=='use':
                inventory[num] = 'none'
                if inventory_use[num]=='hal':
                    hp=hp+inventory_eff[num]
                if inventory_use[num]=='def':
                    defence=defence-inventory_eff[num]
                if inventory_use[num]=='dmg':
                    damage=damage+inventory_eff[num]
                if inventory_use[num]=='mny':
                    coins=coins+inventory_eff[num]
                else:
                    print('you have no effects  :{')
            else:
                print('error')