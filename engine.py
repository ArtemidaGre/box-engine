#Box engine to console quests, work in russian and english language.

from random import randint


file=open('language.txt', 'r')
language=file.read()

class game:
    def battle(hp, damage, ehp, edamage, defe, edefe, lic_code):
        global win, language
        subfunc.lic_c(lic_code)
        if language=='rus' and licence_check:
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
        if language=='eng' and licence_check:
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
        file=open('language')
        lang=file.readline(3)
        battle_f=True
        if lang=='rus':
            print('у вас', hp, 'hp и',damage, 'урона')
            print('Вот ваш инвентарь: ')
            subfunc.inventory('check', 1, 1)
            print('Вы будите бится с', ename, 'Вот его статы:')
            print(ehp, 'hp и', damage, 'урона')
            while battle_f:
                print('Вы можете:\n1.бится\n2.ипользовать инвентарь\n3.обхитрить врага')
                battle_use=input('>>>')
                if battle_use==1 or 'бится':
                    lucky=randint(0, 1000)
                    if lucky<=199:
                        print('Вы промахнулись!')
                    elif lucky>=200:
                        print('Вы попали!', end='')
                        damage_i=randint(1, damage)
                        print('. Вы ударили его на', damage_i)
                    
                        
                    
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
    def lic_c(code):
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
        a1P=file.readline(1)
        l6=file.readline(19)
        file.close()
        if code==l1 or code==l2 or code==l3 or code==l4 or code==l5 or code==l6:
            licence_i=True
        elif code!=l1 or code!=l2 or code!=l3 or code!=l4 or code!=l5 or code!=l6:
            licence_i=False
        if code=='testing':
            licence_i=0
        global licence_check
        licence_check=licence_i
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