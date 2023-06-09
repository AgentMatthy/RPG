print('The beginning, press enter always to continue')
import random
import time

#functions

def advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp):
    print('+',xpgain,'xp (',xp,')')
    print('+',goldgain,'gold (',treasury,')')
    print('')

def advlose(xp, xpgain, hp, hploss, maxhp):
    print('+',xpgain,'xp (',xp,')')
    print('-',hploss,'HP (',hp,'/',maxhp,')')

def armorequip(leatherarmoramount, catarmoramount, copperarmoramount, maxhp, type, equippedarmor):
                if equippedarmor=='Leather armor':
                    leatherarmoramount=leatherarmoramount+1
                    print('Leather armor unequipped')
                    print("")
                if equippedarmor=='Copper armor':
                    copperarmoramount=copperarmoramount+1
                    print('Copper armor unequipped')
                    print('')
                if equippedarmor=='Maxwell armor':
                    catarmoramount=catarmoramount+1
                    print('Maxwell armor unequipped')
                    print('')
                else:
                    print('')
                if block1a==1:
                    block1a=block1a-1
                if block2a==1:
                    block2a=block2a-1
                if block3a==1:
                    block3a=block3a-1

def weaponequip(woodendaggeramount, woodenswordamount, catswordamount, copperswordamount, power, equippedweapon):
                if equippedweapon=='Wooden dagger':
                    woodendaggeramount=woodendaggeramount+1
                    print('Wooden dagger unequipped')
                    print("")
                if equippedweapon=='Wooden sword':
                    woodenswordamount=woodenswordamount+1
                    print('Wooden sword unequipped')
                    print('')
                if equippedweapon=='Copper sword':
                    copperswordamount=copperswordamount+1
                    print('Copper sword unequipped')
                    print('')
                if equippedweapon=='Maxwell sword':
                    catswordamount=catswordamount+1
                    print('Maxwell sword unequipped')
                    print('')
                else:
                    print('')
                if loot1==1:
                    loot1=loot1-1
                if loot2==1:
                    loot2=loot2-1
                if loot3==1:
                    loot3=loot3-1
                if block1w==1:
                    block1w=block1w-1
                if block2w==1:
                    block2w=block2w-1
                if block3w==1:
                    block3w=block3w-1

#stats

xp=0
treasury=0
maxhp=10
hp=10
power=1
hploss=0
strength=hp*power

strengthuse=0
resistanceuse=0

equippedweapon=''
equippedarmor=''

skillpoint=0

#potions

revivepotionamount=0
healthpotionamount=0
resistancepotionamount=0
strengthpotionamount=0

#armors

leatherarmoramount=0
copperarmoramount=0
catarmoramount=0

#weapons

woodendaggeramount=0
woodenswordamount=0
catswordamount=0
copperswordamount=0

#enchants

loot1=0
loot2=0
loot3=0
block1a=0
block2a=0
block3a=0
block1w=0
block2w=0
block3w=0
sharp1=0
sharp2=0
sharp3=0
curse1=0
curse2=0
curse3=0

enchantmentscroll=0

#special

point=300

#skills

focus=0
vampire=0
advancedlooting=0
laststand=0
learning=0
shield=0

#classes

while True:
    type=input('Choose a class: \n 1=Healer: +5 Health potion; -20% power \n 2=Swordsman: +Wooden sword; -15% maxHP \n 3=Trader: +10 gold; -30% maxHP \n 4=Wizard: Enchanting only costs 15 XP; -30% maxHP \n 5=Warrior: +Copper sword; +leather armor; +25% maxHP; -50% gold gain')
    print('')
    if type=='1':
        healthpotionamount=5
        power=power*0.8
        type='Healer'
        print('Class selected: Healer')
        break
    if type=='2':
        equippedweapon='Wooden sword'
        maxhp=maxhp*0.85
        hp=8.5
        type='Swordsman'
        print('Class selected: Swordsman')
        break
    if type=='3':
        treasury=10
        maxhp=maxhp*0.7
        hp=7
        type='Trader'
        print('Class selected: Trader')
        break
    if type=='4':
        maxhp=maxhp*0.7
        hp=7
        type='Wizard'
        print('Class selected: Wizard')
        break
    if type=='5':
        maxhp=maxhp*1.25
        hp=12.5
        equippedarmor='Leather armor'
        equippedweapon='Copper sword'
        type='Warrior'
        print('Class selected: Warrior')
        break
    else:
        print('I said choose a class')
        continue

#game

while True:

    maxhp=round(maxhp,3)
    if point<21:
        print('')
        skillpoint=skillpoint+1
        print('+ Skill point (',skillpoint,')')
        print('')
        point=100
    else:
        skillpoint=skillpoint

    power=1
    if equippedweapon=='Wooden dagger':
        power=1.3
    if equippedweapon=='Wooden sword':
        power=1.5
    if equippedweapon=='Copper sword':
        power=1.7
    if equippedweapon=='Maxwell sword':
        power=2
    if type=='Healer':
        power=power*0.8
    if sharp1==1:
        power=power*1.15
    if sharp2==1:
        power=power*1.3
    if sharp3==1:
        power=power*1.5
    if curse1==1:
        power=power*0.85
    if curse2==1:
        power=power*0.7
    if curse3==1:
        power=power*0.5
    chance=random.randint (0,100)
    loot=random.randint (0,100)
    event=random.randint (0,100)
    if strengthuse>0:
            print('')
            print('Strength potion active')
            print('')
            power=power*1.5
    if resistanceuse>0:
            print('')
            print('Resistance potion active')
            print('')

    print('Options: 1=Adventure, 2=Profile, 3=Inventory, 4=Shop, 5=Help, 6=Item list, 7=Gamble, 8=Enchanting, 9=Skills')
    choice=input('')

    if choice=='1':
        strengthuse=strengthuse-1
        resistanceuse=resistanceuse-1
        point=random.randint(1,100)
        laststandskill='Not used'

        if event<3:
            print('')
            print('A strange scientist appears and asks you to solve a math problem, if you are correct then you get a reward')
            num1=random.randint(0,1000)
            num2=random.randint(0,1000)
            print('What is ',num1,'+',num2,'?')
            answer=int(input(''))
            if answer==num1+num2:
                print('That is correct, the scientist gives you a enchantment scroll, with which it is free to enchant items')
                print('')
                enchantmentscroll=enchantmentscroll+1
            else:
                print('You are bad at maths bruh')
                print('')

        if xp<50 or xp==50:
            if 0<chance and chance<50:
                print('')
                enemymaxhp=3
                enemyhp=3
                print('Wolf encounter:')
                print('Enemy HP:',enemyhp,'')
                battle=input('1=Run, 2=Fight')
                if battle=='1':
                    hploss=random.randint(0,1)
                    if block1a==1:
                        hploss=hploss*0.85
                    if block2a==1:
                        hploss=hploss*0.7
                    if block3a==1:
                        hploss=hploss*0.5
                    if block1w==1:
                        hploss=hploss*0.85
                    if block2w==1:
                        hploss=hploss*0.7
                    if block3w==1:
                        hploss=hploss*0.5
                    if resistanceuse>0:
                        hploss=hploss*0.5
                    else:
                        hploss=hploss
                    xpgain=random.randint(1,5)
                    if learning==1:
                        xpgain=xpgain*1.2
                    if learning==2:
                        xpgain=xpgain*1.4
                    if learning==3:
                        xpgain=xpgain*1.6
                    xp=xp+xpgain
                    protection=random.randint(1,100)
                    if shield==1:
                        if protection<6:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==2:
                        if protection<11:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==3:
                        if protection<16:
                            hploss=0
                        else:
                            hploss=hploss
                    hp=hp-hploss
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    while True:
                        if focus==1:
                            enemycrit=random.randint(1,134)
                        if focus==2:
                            enemycrit=random.randint(1,200)
                        if focus==3:
                            enemycrit=random.randint(1,400)
                        else:
                            enemycrit=random.randint(1,100)
                        crit=random.randint(1,100)
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        if block1a==1:
                            hploss=hploss*0.85
                        if block2a==1:
                            hploss=hploss*0.7
                        if block3a==1:
                            hploss=hploss*0.5
                        if block1w==1:
                            hploss=hploss*0.85
                        if block2w==1:
                            hploss=hploss*0.7
                        if block3w==1:
                            hploss=hploss*0.5
                        if resistanceuse>0:
                            hploss=hploss*0.5
                        if enemycrit<21:
                            hploss=hploss*1.5
                        else:
                            hploss=hploss
                        enemyhploss=random.randint(0,2)
                        if equippedweapon=='Wooden dagger':
                            enemyhploss=random.randint(0,3)
                        if equippedweapon=='Wooden sword':
                            enemyhploss=random.randint(0,5)
                        if equippedweapon=='Copper sword':
                            enemyhploss=random.randint(0,7)
                        if equippedweapon=='Maxwell sword':
                            enemyhploss=random.randint(0,10)
                        if strengthuse>0:
                            enemyhploss=enemyhploss*1.5
                        if type=='Healer':
                            enemyhploss=enemyhploss*0.8
                        if sharp1==1:
                            enemyhploss=enemyhploss*1.15
                        if sharp2==1:
                            enemyhploss=enemyhploss*1.4
                        if sharp3==1:
                            enemyhploss=enemyhploss*1.5
                        if curse1==1:
                            enemyhploss=enemyhploss*0.85
                        if curse2==1:
                            enemyhploss=enemyhploss*0.7
                        if curse3==1:
                            enemyhploss=enemyhploss*0.5
                        crit=random.randint(1,100)
                        if crit<21:
                            enemyhploss=enemyhploss*1.5
                        if vampire>0:
                            vam=random.randint(1,100)
                            if vampire==1:
                                corrvam=16
                            if vampire==2:
                                corrvam=31
                            if vampire==3:
                                corrvam=51
                            else:
                                treasury=treasury
                            if vam<corrvam:
                                enemyhploss=enemyhploss+(enemymaxhp*0.3)
                                hp=hp+(enemymaxhp*0.3)
                            else:
                                treasury=treasury
                        enemyhp=enemyhp-enemyhploss
                        protection=random.randint(1,100)
                        if shield==1:
                            if protection<6:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                            else:
                                hploss=hploss
                        hp=hp-hploss
                        print('')
                        if crit<21:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
                        else:
                            print('Enemy HP: -',round(enemyhploss,2),'(',round(enemyhp,2),'/',enemymaxhp,')')
                        if enemycrit<21:
                            print('Your HP: -',round(hploss,2),' Critical hit! (',round(hp,2),'/',maxhp,')')
                        else:
                            print('Your HP: -',round(hploss,2),'(',round(hp,2),'/',maxhp,')')
                        print('')
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',hp,'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                print('You do not have a revive potion, the game is over :c')
                                break
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        else:
                            time.sleep(3)
                            continue
                    if hp<0 or hp==0:
                        break
                    else:
                        xpgain=random.randint(1,8)
                        if learning==1:
                            xpgain=xpgain*1.2
                        if learning==2:
                            xpgain=xpgain*1.4
                        if learning==3:
                            xpgain=xpgain*1.6
                        goldgain=random.randint(0,5)
                        xp=xp+xpgain
                        if loot1==1:
                            goldgain=goldgain*1.25
                        if loot2==1:
                            goldgain=goldgain*1.5
                        if loot3==1:
                            goldgain=goldgain*1.75
                        if type=='Warrior':
                            goldgain=goldgain*0.5
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        if 0<loot and loot<20:
                            woodendaggeramount=woodendaggeramount+1
                            print('+ Wooden dagger (',woodendaggeramount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        else:
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                else:
                    continue
            if 50<chance:
                print('')
                enemymaxhp=5
                enemyhp=5
                print('Bear encounter:')
                print('Enemy HP:',enemyhp,'')
                battle=input('1=Run, 2=Fight')
                if battle=='1':
                    hploss=random.randint(0,2)
                    if block1a==1:
                        hploss=hploss*0.85
                    if block2a==1:
                        hploss=hploss*0.7
                    if block3a==1:
                        hploss=hploss*0.5
                    if block1w==1:
                        hploss=hploss*0.85
                    if block2w==1:
                        hploss=hploss*0.7
                    if block3w==1:
                        hploss=hploss*0.5
                    if resistanceuse>0:
                        hploss=hploss*0.5
                    else:
                        hploss=hploss
                    xpgain=random.randint(1,7)
                    if learning==1:
                        xpgain=xpgain*1.2
                    if learning==2:
                        xpgain=xpgain*1.4
                    if learning==3:
                        xpgain=xpgain*1.6
                    xp=xp+xpgain
                    protection=random.randint(1,100)
                    if shield==1:
                        if protection<6:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==2:
                        if protection<11:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==3:
                        if protection<16:
                            hploss=0
                        else:
                            hploss=hploss
                    hp=hp-hploss
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    while True:
                        if focus==1:
                            enemycrit=random.randint(1,134)
                        if focus==2:
                            enemycrit=random.randint(1,200)
                        if focus==3:
                            enemycrit=random.randint(1,400)
                        else:
                            enemycrit=random.randint(1,100)
                        crit=random.randint(1,100)
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        if block1a==1:
                            hploss=hploss*0.85
                        if block2a==1:
                            hploss=hploss*0.7
                        if block3a==1:
                            hploss=hploss*0.5
                        if block1w==1:
                            hploss=hploss*0.85
                        if block2w==1:
                            hploss=hploss*0.7
                        if block3w==1:
                            hploss=hploss*0.5
                        if resistanceuse>0:
                            hploss=hploss*0.5
                        if enemycrit<21:
                            hploss=hploss*1.5
                        else:
                            hploss=hploss
                        enemyhploss=random.randint(0,2)
                        if equippedweapon=='Wooden dagger':
                            enemyhploss=random.randint(0,3)
                        if equippedweapon=='Wooden sword':
                            enemyhploss=random.randint(0,5)
                        if equippedweapon=='Copper sword':
                            enemyhploss=random.randint(0,7)
                        if equippedweapon=='Maxwell sword':
                            enemyhploss=random.randint(0,10)
                        if strengthuse>0:
                            enemyhploss=enemyhploss*1.5
                        if type=='Healer':
                            enemyhploss=enemyhploss*0.8
                        if sharp1==1:
                            enemyhploss=enemyhploss*1.15
                        if sharp2==1:
                            enemyhploss=enemyhploss*1.4
                        if sharp3==1:
                            enemyhploss=enemyhploss*1.5
                        if curse1==1:
                            enemyhploss=enemyhploss*0.85
                        if curse2==1:
                            enemyhploss=enemyhploss*0.7
                        if curse3==1:
                            enemyhploss=enemyhploss*0.5
                        if crit<21:
                            enemyhploss=enemyhploss*1.5
                        if vampire>0:
                            vam=random.randint(1,100)
                            if vampire==1:
                                corrvam=16
                            if vampire==2:
                                corrvam=31
                            if vampire==3:
                                corrvam=51
                            else:
                                treasury=treasury
                            if vam<corrvam:
                                enemyhploss=enemyhploss+(enemymaxhp*0.3)
                                hp=hp+(enemymaxhp*0.3)
                            else:
                                treasury=treasury
                        enemyhp=enemyhp-enemyhploss
                        protection=random.randint(1,100)
                        if shield==1:
                            if protection<6:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                            else:
                                hploss=hploss
                        hp=hp-hploss
                        print('')
                        if crit<21:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
                        else:
                            print('Enemy HP: -',round(enemyhploss,2),'(',round(enemyhp,2),'/',enemymaxhp,')')
                        if enemycrit<21:
                            print('Your HP: -',round(hploss,2),' Critical hit! (',round(hp,2),'/',maxhp,')')
                        else:
                            print('Your HP: -',round(hploss,2),'(',round(hp,2),'/',maxhp,')')
                        print('')
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',hp,'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                print('You do not have a revive potion, the game is over :c')
                                break
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        else:
                            time.sleep(3)
                            continue
                    if hp<0 or hp==0:
                        break
                    else:
                        xpgain=random.randint(1,10)
                        goldgain=random.randint(0,6)
                        xp=xp+xpgain
                        if learning==1:
                            xpgain=xpgain*1.2
                        if learning==2:
                            xpgain=xpgain*1.4
                        if learning==3:
                            xpgain=xpgain*1.6
                        if loot1==1:
                            goldgain=goldgain*1.25
                        if loot2==1:
                            goldgain=goldgain*1.5
                        if loot3==1:
                            goldgain=goldgain*1.75
                        if type=='Warrior':
                            goldgain=goldgain*0.5
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        if 0<loot and loot<20:
                            leatherarmoramount=leatherarmoramount+1
                            print('+ Leather armor (',leatherarmoramount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        else:
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                else:
                    continue

            if chance==0:
                prize=random.randint(4,10)
                treasury=treasury+prize
                print('Gold box:')
                print('+',prize,'gold (',treasury,')')
                cont=input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            if chance==50:
                prize=random.randint(1,6)
                if prize==1:
                    print('Item box:')
                    if advancedlooting==1:
                        healthpotionamount=healthpotionamount+2
                        print('+ 2 Health potion (',healthpotionamount,')')
                    else:
                        healthpotionamount=healthpotionamount+1
                        print('+ Health potion (',healthpotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==2:
                    revivepotionamount=revivepotionamount+1
                    print('Item box:')
                    print('+ 1 Revive potion (',revivepotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==3:
                    leatherarmoramount=leatherarmoramount+1
                    print('Item box:')
                    print('+ 1 Leather armor (',leatherarmoramount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==4:
                    woodendaggeramount=woodendaggeramount+1
                    print('Item box:')
                    print('+ 1 Leather armor (',leatherarmoramount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==5:
                    resistancepotionamount=resistancepotionamount+1
                    print('Item box:')
                    print('+ 1 Resistance potion (',resistancepotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==6:
                    strengthpotionamount=strengthpotionamount+1
                    print('Item box:')
                    print('+ 1 Strength potion (',strengthpotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue

            else:
                continue
        
        if xp>50 and xp<101:
            if chance==0:
                prize=random.randint(4,10)
                treasury=treasury+prize
                print('Gold box:')
                print('+',prize,'gold (',treasury,')')
                cont=input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue 
            if chance>1 and chance<5:
                prize=random.randint(1,9)
                if prize==1:
                    print('Item box:')
                    if advancedlooting==1:
                        healthpotionamount=healthpotionamount+2
                        print('+ 2 Health potion (',healthpotionamount,')')
                    else:
                        healthpotionamount=healthpotionamount+1
                        print('+ Health potion (',healthpotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==2:
                    revivepotionamount=revivepotionamount+1
                    print('Item box:')
                    print('+ 1 Revive potion (',revivepotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==3:
                    leatherarmoramount=leatherarmoramount+1
                    print('Item box:')
                    print('+ 1 Leather armor (',leatherarmoramount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==4:
                    woodendaggeramount=woodendaggeramount+1
                    print('Item box:')
                    print('+ 1 Wooden dagger (',woodendaggeramount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==5:
                    copperarmoramount=copperarmoramount+1
                    print('Item box:')
                    print('+ 1 Copper armor (',copperarmoramount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==6:
                    copperswordamount=copperswordamount+1
                    print('Item box:')
                    print('+ 1 Copper sword (',copperswordamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==7:
                    revivepotionamount=revivepotionamount+1
                    print('Item box:')
                    print('+ 1 Revive potion (',revivepotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==8:
                    resistancepotionamount=resistancepotionamount+1
                    print('Item box:')
                    print('+ 1 Resistance potion (',resistancepotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if prize==9:
                    strengthpotionamount=strengthpotionamount+1
                    print('Item box:')
                    print('+ 1 Strength potion (',strengthpotionamount,')')
                    cont=input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
            if 5<chance and chance<50:
                print('')
                enemymaxhp=7
                enemyhp=7
                print('Bandit encounter:')
                print('Enemy HP:',enemyhp,'')
                battle=input('1=Run, 2=Fight')
                if battle=='1':
                    hploss=random.randint(0,3)
                    if block1a==1:
                        hploss=hploss*0.85
                    if block2a==1:
                        hploss=hploss*0.7
                    if block3a==1:
                        hploss=hploss*0.5
                    if block1w==1:
                        hploss=hploss*0.85
                    if block2w==1:
                        hploss=hploss*0.7
                    if block3w==1:
                        hploss=hploss*0.5
                    if resistanceuse>0:
                        hploss=hploss*0.5
                    else:
                        hploss=hploss
                    xpgain=random.randint(1,7)
                    if learning==1:
                        xpgain=xpgain*1.2
                    if learning==2:
                        xpgain=xpgain*1.4
                    if learning==3:
                        xpgain=xpgain*1.6
                    xp=xp+xpgain
                    protection=random.randint(1,100)
                    if shield==1:
                        if protection<6:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==2:
                        if protection<11:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==3:
                        if protection<16:
                            hploss=0
                        else:
                            hploss=hploss
                    hp=hp-hploss
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    while True:
                        if focus==1:
                            enemycrit=random.randint(1,134)
                        if focus==2:
                            enemycrit=random.randint(1,200)
                        if focus==3:
                            enemycrit=random.randint(1,400)
                        else:
                            enemycrit=random.randint(1,100)
                        crit=random.randint(1,100)
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,5)
                        if block1a==1:
                            hploss=hploss*0.85
                        if block2a==1:
                            hploss=hploss*0.7
                        if block3a==1:
                            hploss=hploss*0.5
                        if block1w==1:
                            hploss=hploss*0.85
                        if block2w==1:
                            hploss=hploss*0.7
                        if block3w==1:
                            hploss=hploss*0.5
                        if resistanceuse>0:
                            hploss=hploss*0.5
                        if enemycrit<21:
                            hploss=hploss*1.5
                        else:
                            hploss=hploss
                        enemyhploss=random.randint(0,2)
                        if equippedweapon=='Wooden dagger':
                            enemyhploss=random.randint(0,3)
                        if equippedweapon=='Wooden sword':
                            enemyhploss=random.randint(0,5)
                        if equippedweapon=='Copper sword':
                            enemyhploss=random.randint(0,7)
                        if equippedweapon=='Maxwell sword':
                            enemyhploss=random.randint(0,10)
                        if strengthuse>0:
                            enemyhploss=enemyhploss*1.5
                        if type=='Healer':
                            enemyhploss=enemyhploss*0.8
                        if sharp1==1:
                            enemyhploss=enemyhploss*1.15
                        if sharp2==1:
                            enemyhploss=enemyhploss*1.4
                        if sharp3==1:
                            enemyhploss=enemyhploss*1.5
                        if curse1==1:
                            enemyhploss=enemyhploss*0.85
                        if curse2==1:
                            enemyhploss=enemyhploss*0.7
                        if curse3==1:
                            enemyhploss=enemyhploss*0.5
                        if crit<21:
                            enemyhploss=enemyhploss*1.5
                        if vampire>0:
                            vam=random.randint(1,100)
                            if vampire==1:
                                corrvam=16
                            if vampire==2:
                                corrvam=31
                            if vampire==3:
                                corrvam=51
                            else:
                                treasury=treasury
                            if vam<corrvam:
                                enemyhploss=enemyhploss+(enemymaxhp*0.3)
                                hp=hp+(enemymaxhp*0.3)
                            else:
                                treasury=treasury
                        enemyhp=enemyhp-enemyhploss
                        protection=random.randint(1,100)
                        if shield==1:
                            if protection<6:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                            else:
                                hploss=hploss
                        hp=hp-hploss
                        print('')
                        if crit<21:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
                        else:
                            print('Enemy HP: -',round(enemyhploss,2),'(',round(enemyhp,2),'/',enemymaxhp,')')
                        if enemycrit<21:
                            print('Your HP: -',round(hploss,2),' Critical hit! (',round(hp,2),'/',maxhp,')')
                        else:
                            print('Your HP: -',round(hploss,2),'(',round(hp,2),'/',maxhp,')')
                        print('')
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',hp,'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                print('You do not have a revive potion, the game is over :c')
                                break
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        else:
                            time.sleep(3)
                            continue
                    if hp<0 or hp==0:
                        break
                    else:
                        xpgain=random.randint(1,12)
                        goldgain=random.randint(0,8)
                        if learning==1:
                            xpgain=xpgain*1.2
                        if learning==2:
                            xpgain=xpgain*1.4
                        if learning==3:
                            xpgain=xpgain*1.6
                        xp=xp+xpgain
                        if loot1==1:
                            goldgain=goldgain*1.25
                        if loot2==1:
                            goldgain=goldgain*1.5
                        if loot3==1:
                            goldgain=goldgain*1.75
                        if type=='Warrior':
                            goldgain=goldgain*0.5
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        if 0<loot and loot<20:
                            prize=random.randint(1,7)
                            if prize==1:
                                if advancedlooting==1:
                                    healthpotionamount=healthpotionamount+2
                                    print('+ 2 Health potion (',healthpotionamount,')')
                                else:
                                    healthpotionamount=healthpotionamount+1
                                    print('+ Health potion (',healthpotionamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==2:
                                revivepotionamount=revivepotionamount+1
                                print('+ 1 Revive potion (',revivepotionamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==3:
                                leatherarmoramount=leatherarmoramount+1
                                print('+ 1 Leather armor (',leatherarmoramount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==4:
                                woodendaggeramount=woodendaggeramount+1
                                print('+ 1 Wooden dagger (',woodendaggeramount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==5:
                                copperarmoramount=copperarmoramount+1
                                print('+ 1 Copper armor (',copperarmoramount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==6:
                                copperswordamount=copperswordamount+1
                                print('+ 1 Copper sword (',copperswordamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==7:
                                revivepotionamount=revivepotionamount+1
                                print('+ 1 Revive potion (',revivepotionamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue

                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        else:
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                else:
                    continue
            if chance==1 or chance==5:
                print('MAXWELL THE CAT appears and asks you too choose a number:')
                szám=input('1 or 2 (Answer with the number)')
                correct=random.randint(1,2)
                if szám=='1':
                    if correct==1:
                        print('')
                        print('You guessed it! It is 1!')
                        választás=input('MAXWELL THE CAT asks you to choose: 1=Maxwell sword, 2=Maxwell armor')
                        if választás==1:
                            print('')
                            catswordamount=catswordamount+1
                            print('+ Maxwell sword ')
                            print('')
                            continue
                        if választás==2:
                            print('')
                            catarmoramount=catarmoramount+1
                            print('+ Maxwell armor ')
                            print('')
                            continue
                        else:
                            print('You did not answer correctly! But MAXWELL THE CAT gives you 2 revive potions anyway')
                            print('')
                            revivepotionamount=revivepotionamount+2
                    if correct==2:
                        print('')
                        print('You did not guess correctly, but MAXWELL THE CAT is kind and gives you nothing')
                        print('')
                        continue
                if szám=='2':
                    if correct==2:
                        print('')
                        print('You guessed it! It is 2!')
                        választás=input('MAXWELL THE CAT asks you to choose: 1=Maxwell sword, 2=Maxwell armor')
                        if választás==1:
                            print('')
                            catswordamount=catswordamount+1
                            print('+ Maxwell sword ')
                            print('')
                            continue
                        if választás==2:
                            print('')
                            catarmoramount=catarmoramount+1
                            print('+ Maxwell armor ')
                            print('')
                            continue
                        else:
                            print('You did not answer correctly! But MAXWELL THE CAT gives you 2 revive potions anyway')
                            print('')
                            revivepotionamount=revivepotionamount+2
                    if correct==1:
                        print('')
                        print('You did not guess correctly, but MAXWELL THE CAT is kind and gives you nothing')
                        print('')
                        continue
                else:
                    print('')
                    print('What')
                    print('MAXWELL THE CAT does not understand you and leaves, why did you miss this chance?')
                    print('')
                    continue
            if 80<chance and chance<90:
                print('')
                enemymaxhp=3
                enemyhp=3
                print('Wolf encounter:')
                print('Enemy HP:',enemyhp,'')
                battle=input('1=Run, 2=Fight')
                if battle=='1':
                    hploss=random.randint(0,1)
                    if block1a==1:
                        hploss=hploss*0.85
                    if block2a==1:
                        hploss=hploss*0.7
                    if block3a==1:
                        hploss=hploss*0.5
                    if block1w==1:
                        hploss=hploss*0.85
                    if block2w==1:
                        hploss=hploss*0.7
                    if block3w==1:
                        hploss=hploss*0.5
                    if resistanceuse>0:
                        hploss=hploss*0.5
                    else:
                        hploss=hploss
                    xpgain=random.randint(1,5)
                    if learning==1:
                        xpgain=xpgain*1.2
                    if learning==2:
                        xpgain=xpgain*1.4
                    if learning==3:
                        xpgain=xpgain*1.6
                    xp=xp+xpgain
                    protection=random.randint(1,100)
                    if shield==1:
                        if protection<6:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==2:
                        if protection<11:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==3:
                        if protection<16:
                            hploss=0
                        else:
                            hploss=hploss
                    hp=hp-hploss
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    while True:
                        if focus==1:
                            enemycrit=random.randint(1,134)
                        if focus==2:
                            enemycrit=random.randint(1,200)
                        if focus==3:
                            enemycrit=random.randint(1,400)
                        else:
                            enemycrit=random.randint(1,100)
                        crit=random.randint(1,100)
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        if block1a==1:
                            hploss=hploss*0.85
                        if block2a==1:
                            hploss=hploss*0.7
                        if block3a==1:
                            hploss=hploss*0.5
                        if block1w==1:
                            hploss=hploss*0.85
                        if block2w==1:
                            hploss=hploss*0.7
                        if block3w==1:
                            hploss=hploss*0.5
                        if resistanceuse>0:
                            hploss=hploss*0.5
                        if enemycrit<21:
                            hploss=hploss*1.5
                        else:
                            hploss=hploss
                        enemyhploss=random.randint(0,2)
                        if equippedweapon=='Wooden dagger':
                            enemyhploss=random.randint(0,3)
                        if equippedweapon=='Wooden sword':
                            enemyhploss=random.randint(0,5)
                        if equippedweapon=='Copper sword':
                            enemyhploss=random.randint(0,7)
                        if equippedweapon=='Maxwell sword':
                            enemyhploss=random.randint(0,10)
                        if strengthuse>0:
                            enemyhploss=enemyhploss*1.5
                        if type=='Healer':
                            enemyhploss=enemyhploss*0.8
                        if sharp1==1:
                            enemyhploss=enemyhploss*1.15
                        if sharp2==1:
                            enemyhploss=enemyhploss*1.4
                        if sharp3==1:
                            enemyhploss=enemyhploss*1.5
                        if curse1==1:
                            enemyhploss=enemyhploss*0.85
                        if curse2==1:
                            enemyhploss=enemyhploss*0.7
                        if curse3==1:
                            enemyhploss=enemyhploss*0.5
                        if crit<21:
                            enemyhploss=enemyhploss*1.5
                        if vampire>0:
                            vam=random.randint(1,100)
                            if vampire==1:
                                corrvam=16
                            if vampire==2:
                                corrvam=31
                            if vampire==3:
                                corrvam=51
                            else:
                                treasury=treasury
                            if vam<corrvam:
                                enemyhploss=enemyhploss+(enemymaxhp*0.3)
                                hp=hp+(enemymaxhp*0.3)
                            else:
                                treasury=treasury
                        enemyhp=enemyhp-enemyhploss
                        protection=random.randint(1,100)
                        if shield==1:
                            if protection<6:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                            else:
                                hploss=hploss
                        hp=hp-hploss
                        print('')
                        if crit<21:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
                        else:
                            print('Enemy HP: -',round(enemyhploss,2),'(',round(enemyhp,2),'/',enemymaxhp,')')
                        if enemycrit<21:
                            print('Your HP: -',round(hploss,2),' Critical hit! (',round(hp,2),'/',maxhp,')')
                        else:
                            print('Your HP: -',round(hploss,2),'(',round(hp,2),'/',maxhp,')')
                        print('')
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',hp,'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                print('You do not have a revive potion, the game is over :c')
                                break
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        else:
                            time.sleep(3)
                            continue
                    if hp<0 or hp==0:
                        break
                    else:
                        xpgain=random.randint(1,8)
                        goldgain=random.randint(0,5)
                        if learning==1:
                            xpgain=xpgain*1.2
                        if learning==2:
                            xpgain=xpgain*1.4
                        if learning==3:
                            xpgain=xpgain*1.6
                        xp=xp+xpgain
                        if loot1==1:
                            goldgain=goldgain*1.25
                        if loot2==1:
                            goldgain=goldgain*1.5
                        if loot3==1:
                            goldgain=goldgain*1.75
                        if type=='Warrior':
                            goldgain=goldgain*0.5
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        if 0<loot and loot<20:
                            woodendaggeramount=woodendaggeramount+1
                            print('+ Wooden dagger (',woodendaggeramount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        else:
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                else:
                    continue
            if 90<chance and chance<100:
                print('')
                enemymaxhp=5
                enemyhp=5
                print('Bear encounter:')
                print('Enemy HP:',enemyhp,'')
                battle=input('1=Run, 2=Fight')
                if battle=='1':
                    hploss=random.randint(0,2)
                    if block1a==1:
                        hploss=hploss*0.85
                    if block2a==1:
                        hploss=hploss*0.7
                    if block3a==1:
                        hploss=hploss*0.5
                    if block1w==1:
                        hploss=hploss*0.85
                    if block2w==1:
                        hploss=hploss*0.7
                    if block3w==1:
                        hploss=hploss*0.5
                    if resistanceuse>0:
                        hploss=hploss*0.5
                    else:
                        hploss=hploss
                    xpgain=random.randint(1,7)
                    if learning==1:
                        xpgain=xpgain*1.2
                    if learning==2:
                        xpgain=xpgain*1.4
                    if learning==3:
                        xpgain=xpgain*1.6
                    xp=xp+xpgain
                    protection=random.randint(1,100)
                    if shield==1:
                        if protection<6:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==2:
                        if protection<11:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==3:
                        if protection<16:
                            hploss=0
                        else:
                            hploss=hploss
                    hp=hp-hploss
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    while True:
                        if focus==1:
                            enemycrit=random.randint(1,134)
                        if focus==2:
                            enemycrit=random.randint(1,200)
                        if focus==3:
                            enemycrit=random.randint(1,400)
                        else:
                            enemycrit=random.randint(1,100)
                        crit=random.randint(1,100)
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        if block1a==1:
                            hploss=hploss*0.85
                        if block2a==1:
                            hploss=hploss*0.7
                        if block3a==1:
                            hploss=hploss*0.5
                        if block1w==1:
                            hploss=hploss*0.85
                        if block2w==1:
                            hploss=hploss*0.7
                        if block3w==1:
                            hploss=hploss*0.5
                        if resistanceuse>0:
                            hploss=hploss*0.5
                        if enemycrit<21:
                            hploss=hploss*1.5
                        else:
                            hploss=hploss
                        enemyhploss=random.randint(0,2)
                        if equippedweapon=='Wooden dagger':
                            enemyhploss=random.randint(0,3)
                        if equippedweapon=='Wooden sword':
                            enemyhploss=random.randint(0,5)
                        if equippedweapon=='Copper sword':
                            enemyhploss=random.randint(0,7)
                        if equippedweapon=='Maxwell sword':
                            enemyhploss=random.randint(0,10)
                        if strengthuse>0:
                            enemyhploss=enemyhploss*1.5
                        if type=='Healer':
                            enemyhploss=enemyhploss*0.8
                        if sharp1==1:
                            enemyhploss=enemyhploss*1.15
                        if sharp2==1:
                            enemyhploss=enemyhploss*1.4
                        if sharp3==1:
                            enemyhploss=enemyhploss*1.5
                        if curse1==1:
                            enemyhploss=enemyhploss*0.85
                        if curse2==1:
                            enemyhploss=enemyhploss*0.7
                        if curse3==1:
                            enemyhploss=enemyhploss*0.5
                        if crit<21:
                            enemyhploss=enemyhploss*1.5
                        if vampire>0:
                            vam=random.randint(1,100)
                            if vampire==1:
                                corrvam=16
                            if vampire==2:
                                corrvam=31
                            if vampire==3:
                                corrvam=51
                            else:
                                treasury=treasury
                            if vam<corrvam:
                                enemyhploss=enemyhploss+(enemymaxhp*0.3)
                                hp=hp+(enemymaxhp*0.3)
                            else:
                                treasury=treasury
                        enemyhp=enemyhp-enemyhploss
                        protection=random.randint(1,100)
                        if shield==1:
                            if protection<6:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                            else:
                                hploss=hploss
                        hp=hp-hploss
                        print('')
                        if crit<21:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
                        else:
                            print('Enemy HP: -',round(enemyhploss,2),'(',round(enemyhp,2),'/',enemymaxhp,')')
                        if enemycrit<21:
                            print('Your HP: -',round(hploss,2),' Critical hit! (',round(hp,2),'/',maxhp,')')
                        else:
                            print('Your HP: -',round(hploss,2),'(',round(hp,2),'/',maxhp,')')
                        print('')
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',hp,'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                print('You do not have a revive potion, the game is over :c')
                                break
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        else:
                            time.sleep(3)
                            continue
                    if hp<0 or hp==0:
                        break
                    else:
                        xpgain=random.randint(1,10)
                        goldgain=random.randint(0,6)
                        if learning==1:
                            xpgain=xpgain*1.2
                        if learning==2:
                            xpgain=xpgain*1.4
                        if learning==3:
                            xpgain=xpgain*1.6
                        xp=xp+xpgain
                        if loot1==1:
                            goldgain=goldgain*1.25
                        if loot2==1:
                            goldgain=goldgain*1.5
                        if loot3==1:
                            goldgain=goldgain*1.75
                        if type=='Warrior':
                            goldgain=goldgain*0.5
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        if 0<loot and loot<20:
                            leatherarmoramount=leatherarmoramount+1
                            print('+ Leather armor (',leatherarmoramount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        else:
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                else:
                    continue
            else:
                print('')
                enemymaxhp=10
                enemyhp=10
                print('Slime encounter:')
                print('Enemy HP:',enemyhp,'')
                battle=input('1=Run, 2=Fight')
                if battle=='1':
                    hploss=random.randint(0,4)
                    if block1a==1:
                        hploss=hploss*0.85
                    if block2a==1:
                        hploss=hploss*0.7
                    if block3a==1:
                        hploss=hploss*0.5
                    if block1w==1:
                        hploss=hploss*0.85
                    if block2w==1:
                        hploss=hploss*0.7
                    if block3w==1:
                        hploss=hploss*0.5
                    if resistanceuse>0:
                        hploss=hploss*0.5
                    else:
                        hploss=hploss
                    xpgain=random.randint(1,8)
                    if learning==1:
                        xpgain=xpgain*1.2
                    if learning==2:
                        xpgain=xpgain*1.4
                    if learning==3:
                        xpgain=xpgain*1.6
                    xp=xp+xpgain
                    protection=random.randint(1,100)
                    if shield==1:
                        if protection<6:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==2:
                        if protection<11:
                            hploss=0
                        else:
                            hploss=hploss
                    if shield==3:
                        if protection<16:
                            hploss=0
                        else:
                            hploss=hploss
                    hp=hp-hploss
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    while True:
                        if focus==1:
                            enemycrit=random.randint(1,134)
                        if focus==2:
                            enemycrit=random.randint(1,200)
                        if focus==3:
                            enemycrit=random.randint(1,400)
                        else:
                            enemycrit=random.randint(1,100)
                        crit=random.randint(1,100)
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,6)
                        if block1a==1:
                            hploss=hploss*0.85
                        if block2a==1:
                            hploss=hploss*0.7
                        if block3a==1:
                            hploss=hploss*0.5
                        if block1w==1:
                            hploss=hploss*0.85
                        if block2w==1:
                            hploss=hploss*0.7
                        if block3w==1:
                            hploss=hploss*0.5
                        if resistanceuse>0:
                            hploss=hploss*0.5
                        if enemycrit<21:
                            hploss=hploss*1.5
                        else:
                            hploss=hploss
                        enemyhploss=random.randint(0,2)
                        if equippedweapon=='Wooden dagger':
                            enemyhploss=random.randint(0,3)
                        if equippedweapon=='Wooden sword':
                            enemyhploss=random.randint(0,5)
                        if equippedweapon=='Copper sword':
                            enemyhploss=random.randint(0,7)
                        if equippedweapon=='Maxwell sword':
                            enemyhploss=random.randint(0,10)
                        if strengthuse>0:
                            enemyhploss=enemyhploss*1.5
                        if type=='Healer':
                            enemyhploss=enemyhploss*0.8
                        if sharp1==1:
                            enemyhploss=enemyhploss*1.15
                        if sharp2==1:
                            enemyhploss=enemyhploss*1.4
                        if sharp3==1:
                            enemyhploss=enemyhploss*1.5
                        if curse1==1:
                            enemyhploss=enemyhploss*0.85
                        if curse2==1:
                            enemyhploss=enemyhploss*0.7
                        if curse3==1:
                            enemyhploss=enemyhploss*0.5
                        if crit<21:
                            enemyhploss=enemyhploss*1.5
                        if vampire>0:
                            vam=random.randint(1,100)
                            if vampire==1:
                                corrvam=16
                            if vampire==2:
                                corrvam=31
                            if vampire==3:
                                corrvam=51
                            else:
                                treasury=treasury
                            if vam<corrvam:
                                enemyhploss=enemyhploss+(enemymaxhp*0.3)
                                hp=hp+(enemymaxhp*0.3)
                            else:
                                treasury=treasury
                        enemyhp=enemyhp-enemyhploss
                        protection=random.randint(1,100)
                        if shield==1:
                            if protection<6:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                            else:
                                hploss=hploss
                        hp=hp-hploss
                        print('')
                        if crit<21:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
                        else:
                            print('Enemy HP: -',round(enemyhploss,2),'(',round(enemyhp,2),'/',enemymaxhp,')')
                        if enemycrit<21:
                            print('Your HP: -',round(hploss,2),' Critical hit! (',round(hp,2),'/',maxhp,')')
                        else:
                            print('Your HP: -',round(hploss,2),'(',round(hp,2),'/',maxhp,')')
                        print('')
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',hp,'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                print('You do not have a revive potion, the game is over :c')
                                break
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        else:
                            time.sleep(3)
                            continue
                    if hp<0 or hp==0:
                        break
                    else:
                        xpgain=random.randint(1,15)
                        goldgain=random.randint(0,10)
                        if learning==1:
                            xpgain=xpgain*1.2
                        if learning==2:
                            xpgain=xpgain*1.4
                        if learning==3:
                            xpgain=xpgain*1.6
                        xp=xp+xpgain
                        if loot1==1:
                            goldgain=goldgain*1.25
                        if loot2==1:
                            goldgain=goldgain*1.5
                        if loot3==1:
                            goldgain=goldgain*1.75
                        if type=='Warrior':
                            goldgain=goldgain*0.5
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        if 0<loot and loot<20:
                            prize=random.randint(1,7)
                            if prize==1:
                                if advancedlooting==1:
                                    healthpotionamount=healthpotionamount+2
                                    print('+ 2 Health potion (',healthpotionamount,')')
                                else:
                                    healthpotionamount=healthpotionamount+1
                                    print('+ Health potion (',healthpotionamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==2:
                                revivepotionamount=revivepotionamount+1
                                print('+ 1 Revive potion (',revivepotionamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==3:
                                leatherarmoramount=leatherarmoramount+1
                                print('+ 1 Leather armor (',leatherarmoramount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==4:
                                woodendaggeramount=woodendaggeramount+1
                                print('+ 1 Wooden dagger (',woodendaggeramount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==5:
                                copperarmoramount=copperarmoramount+1
                                print('+ 1 Copper armor (',copperarmoramount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==6:
                                copperswordamount=copperswordamount+1
                                print('+ 1 Copper sword (',copperswordamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue
                            if prize==7:
                                revivepotionamount=revivepotionamount+1
                                print('+ 1 Revive potion (',revivepotionamount,')')
                                if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        hp=maxhp
                                        continue
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                                else:
                                    cont=input('')
                                    if cont=='':
                                        continue
                                    elif cont=='stop':
                                        break
                                    else:
                                        print('There is no such command as [',cont,']')
                                        continue

                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                        else:
                            if hp<0 or hp==0:
                                print('')
                                print('You died')
                                if revivepotionamount>0:
                                    revivepotionamount=revivepotionamount-1
                                    print('Revive potion used (',revivepotionamount,'remaining)')
                                    hp=maxhp
                                    continue
                                else:
                                    print('You do not have a revive potion, the game is over :c')
                                    break
                            else:
                                cont=input('')
                                if cont=='':
                                    continue
                                elif cont=='stop':
                                    break
                                else:
                                    print('There is no such command as [',cont,']')
                                    continue
                else:
                    continue

        if 100<xp:
            print('')
            boss=input('You reached 100 xp, do you want to fight the final boss? Yes or no?')
            if boss=='no':
                xp=100
                print('')
                continue
            if boss=='yes':
                for i in range(3):
                    correct=random.randint(1,2)
                    print('')
                    num=input('Choose a number: 1 or 2?')
                    if correct==1:
                        if num=='1':
                            print('Correct!')
                            print('')
                            continue
                        else:
                            hploss=random.randint(5,10)
                            print('Incorrect!')
                            hp=hp-hploss
                            print('-',hploss,'HP (',hp,'/',maxhp,')')
                            if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if laststand==1:
                                        if laststandskill=='In use':
                                            laststand=laststand
                                        else:
                                            hp=maxhp*0.2
                                            print('Last stand skill in use, HP:',hp,'')
                                            laststandskill='In use'
                                            continue
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        print('')
                                        hp=maxhp
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                            else:
                                print('')
                                continue
                    if correct==2:
                        if num=='2':
                            print('Correct!')
                            print('')
                            continue
                        else:
                            hploss=random.randint(5,10)
                            print('Incorrect!')
                            hp=hp-hploss
                            print('-',hploss,'HP (',hp,'/',maxhp,')')
                            if hp<0 or hp==0:
                                    print('')
                                    print('You died')
                                    if laststand==1:
                                        if laststandskill=='In use':
                                            laststand=laststand
                                        else:
                                            hp=maxhp*0.2
                                            print('Last stand skill in use, HP:',hp,'')
                                            laststandskill='In use'
                                            continue
                                    if revivepotionamount>0:
                                        revivepotionamount=revivepotionamount-1
                                        print('Revive potion used (',revivepotionamount,'remaining)')
                                        print('')
                                        hp=maxhp
                                    else:
                                        print('You do not have a revive potion, the game is over :c')
                                        break
                            else:
                                print('')
                                continue
                if hp<0 or hp==0:
                    break 
                print('You defeated MUFTOSZ, you spent some of your time to do this so shame on you')
                break               
            else:
                continue
        
        else:
            continue

    if choice=='2':
        if xp<50:
            print('')
            print('LVL 1 (',xp,'xp )')
            print('Class:',type,'')
            print('Treasury:',treasury,'')
            print('HP:',round(hp,2),'/',maxhp, equippedarmor,'')
            print('Strength:',round(power,2), equippedweapon,'')
            print('')
            print('Skills:')
            print('')
            if vampire==1:
                print('Vampire I')
                print('')
            if vampire==2:
                print('Vampire II')
                print('')
            if vampire==3:
                print('Vampire III')
                print('')
            if focus==1:
                print('Focus I')
                print('')
            if focus==2:
                print('Focus II')
                print('')
            if focus==3:
                print('Focus III')
                print('')
            if advancedlooting==1:
                print('Advanced looting I')
                print('')
            if learning==1:
                print('Improved learning I')
                print('')
            if learning==2:
                print('Improved learning II')
                print('')
            if learning==3:
                print('Improved learning III')
                print('')
            if shield==1:
                print('Shield I')
                print('')
            if shield==2:
                print('Shield II')
                print('')
            if shield==3:
                print('Shield III')
                print('')
            if laststand==1:
                print('Last stand I')
                print('')
            if skillpoint>0:
                print('Skill points:',skillpoint,'')
            cont=input('')
            if cont=='':
                continue
            elif cont=='stop':
                break
            else:
                print('There is no such command as [',cont,']')
                continue
        if 50<xp or xp<100:
            print('')
            print('LVL 2 (',xp,'xp )')
            print('Class:',type,'')
            print('Treasury:',treasury,'')
            print('HP:',round(hp,2),'/',maxhp, equippedarmor,'')
            print('Strength:',round(power,2), equippedweapon,'')
            print('')
            print('Skills:')
            print('')
            if vampire==1:
                print('Vampire I')
                print('')
            if vampire==2:
                print('Vampire II')
                print('')
            if vampire==3:
                print('Vampire III')
                print('')
            if focus==1:
                print('Focus I')
                print('')
            if focus==2:
                print('Focus II')
                print('')
            if focus==3:
                print('Focus III')
                print('')
            if advancedlooting==1:
                print('Advanced looting I')
                print('')
            if learning==1:
                print('Improved learning I')
                print('')
            if learning==2:
                print('Improved learning II')
                print('')
            if learning==3:
                print('Improved learning III')
                print('')
            if shield==1:
                print('Shield I')
                print('')
            if shield==2:
                print('Shield II')
                print('')
            if shield==3:
                print('Shield III')
                print('')
            if laststand==1:
                print('Last stand I')
                print('')
            if skillpoint>0:
                print('Skill points:',skillpoint,'')
            cont=input('')
            if cont=='':
                continue
            elif cont=='stop':
                break
            else:
                print('There is no such command as [',cont,']')
                continue

    if choice=='3':
        print('')
        print('Potions:')
        print('')
        if healthpotionamount>0:
            print('(1) Health potion:',healthpotionamount,'')
        if revivepotionamount>0:
            print('(2) Revive potion:',revivepotionamount,'')
        if resistancepotionamount>0:
            print('(10) Resistance potion:',resistancepotionamount,'')
        if strengthpotionamount>0:
            print('(11) Strength potion:',strengthpotionamount,'')
        else:
            treasury=treasury
        print('')
        print('Armors:')
        print('')
        if leatherarmoramount>0:
            print('(3) Leather armor:',leatherarmoramount,'')
        if copperarmoramount>0:
            print('(6) Copper armor:',copperarmoramount,'')
        if catarmoramount>0:
            print('(5) Maxwell armor:',catarmoramount,'')
        else:
            treasury=treasury
        print('')
        print('Weapons:')
        print('')
        if woodendaggeramount>0:
            print('(4) Wooden dagger:',woodendaggeramount,'')
        if woodenswordamount>0:
            print('(7) Wooden sword:',woodenswordamount,'')
        if copperswordamount>0:
            print('(8) Copper sword:',copperswordamount,'')
        if catswordamount>0:
            print('(9) Maxwell sword:',catswordamount,'')
        else:
            treasury=treasury
        print('')
        print('Items')
        if enchantmentscroll>0:
            print('Enchantment scroll:',enchantmentscroll,'')
        else:
            treasury=treasury
        print('')
        use=input('What do you want to do?')
        if use=='1':
            print('')
            if healthpotionamount>0:
                healthpotionamount=healthpotionamount-1
                hp=hp+(0.3*maxhp)
                if hp>maxhp:
                    hp=hp-(hp-maxhp)
                    print('+',round(maxhp*0.3,3),'HP (',round(hp,3),'/',maxhp,')')
                else:
                    print('+',round(maxhp*0.3,3),'HP (',round(hp,3),'/',maxhp,')')
            else:
                print('You do not have a health potion :c')
                continue
        if use=='2':
            print('')
            if revivepotionamount>0:
                print('You can only use a revive potion when you die during an adventure')
            else:
                print('You do not have a revive potion :c')
                continue
        if use=='3':
            print('')
            if leatherarmoramount>0:
                print('Leather armor equipped')
                maxhp=15
                if equippedarmor=='Leather armor':
                    leatherarmoramount=leatherarmoramount+1
                    print('Leather armor unequipped')
                    print("")
                if equippedarmor=='Copper armor':
                    copperarmoramount=copperarmoramount+1
                    print('Copper armor unequipped')
                    print('')
                if equippedarmor=='Maxwell armor':
                    catarmoramount=catarmoramount+1
                    print('Maxwell armor unequipped')
                    print('')
                else:
                    print('')
                if block1a==1:
                    block1a=block1a-1
                if block2a==1:
                    block2a=block2a-1
                if block3a==1:
                    block3a=block3a-1
                equippedarmor='Leather armor'
                leatherarmoramount=leatherarmoramount-1
                if type=='Swordsman':
                    maxhp=maxhp*0.85
                if type=='Trader' or type=='Wizard':
                    maxhp=maxhp*0.7
                if type=='Warrior':
                    maxhp=maxhp*1.25
                continue
            else:
                print('You do not have a leather armor :c')
                continue
        if use=='4':
            print('')
            if woodendaggeramount>0:
                print('Wooden dagger equipped')
                power=1.3
                if equippedweapon=='Wooden dagger':
                    woodendaggeramount=woodendaggeramount+1
                    print('Wooden dagger unequipped')
                    print("")
                if equippedweapon=='Wooden sword':
                    woodenswordamount=woodenswordamount+1
                    print('Wooden sword unequipped')
                    print('')
                if equippedweapon=='Copper sword':
                    copperswordamount=copperswordamount+1
                    print('Copper sword unequipped')
                    print('')
                if equippedweapon=='Maxwell sword':
                    catswordamount=catswordamount+1
                    print('Maxwell sword unequipped')
                    print('')
                else:
                    print('')
                if loot1==1:
                    loot1=loot1-1
                if loot2==1:
                    loot2=loot2-1
                if loot3==1:
                    loot3=loot3-1
                if block1w==1:
                    block1w=block1w-1
                if block2w==1:
                    block2w=block2w-1
                if block3w==1:
                    block3w=block3w-1
                if sharp1==1:
                    sharp1=sharp1-1
                if sharp2==1:
                    sharp2=sharp2-1
                if sharp3==1:
                    sharp3=sharp3-1
                if curse1==1:
                    curse1=curse1-1
                if curse2==1:
                    curse2=curse2-1
                if curse3==1:
                    curse3=curse3-1
                equippedweapon='Wooden dagger'
                woodendaggeramount=woodendaggeramount-1
                if type=='Healer':
                    power=power*0.8
                continue
            else:
                print('You do not have a woodendagger :c')
                continue
        if use=='5':
            print('')
            if catarmoramount>0:
                print('Maxwell armor equipped')
                maxhp=30
                if equippedarmor=='Leather armor':
                    leatherarmoramount=leatherarmoramount+1
                    print('Leather armor unequipped')
                    print("")
                if equippedarmor=='Copper armor':
                    copperarmoramount=copperarmoramount+1
                    print('Copper armor unequipped')
                    print('')
                if equippedarmor=='Maxwell armor':
                    catarmoramount=catarmoramount+1
                    print('Maxwell armor unequipped')
                    print('')
                else:
                    print('')
                if block1a==1:
                    block1a=block1a-1
                if block2a==1:
                    block2a=block2a-1
                if block3a==1:
                    block3a=block3a-1
                equippedarmor='Maxwell armor'
                catarmoramount=catarmoramount-1
                if type=='Swordsman':
                    maxhp=maxhp*0.85
                if type=='Trader' or type=='Wizard':
                    maxhp=maxhp*0.7
                if type=='Warrior':
                    maxhp=maxhp*1.25
                continue
            else:
                print('You do not have a Maxwell armor :c')
                continue
        if use=='6':
            print('')
            if copperarmoramount>0:
                print('Copper armor equipped')
                maxhp=20
                if equippedarmor=='Leather armor':
                    leatherarmoramount=leatherarmoramount+1
                    print('Leather armor unequipped')
                    print("")
                if equippedarmor=='Copper armor':
                    copperarmoramount=copperarmoramount+1
                    print('Copper armor unequipped')
                    print('')
                if equippedarmor=='Maxwell armor':
                    catarmoramount=catarmoramount+1
                    print('Maxwell armor unequipped')
                    print('')
                else:
                    print('')
                if block1a==1:
                    block1a=block1a-1
                if block2a==1:
                    block2a=block2a-1
                if block3a==1:
                    block3a=block3a-1
                equippedarmor='Copper armor'
                copperarmoramount=copperarmoramount-1
                if type=='Swordsman':
                    maxhp=maxhp*0.85
                if type=='Trader' or type=='Wizard':
                    maxhp=maxhp*0.7
                if type=='Warrior':
                    maxhp=maxhp*1.25
                continue
            else:
                print('You do not have a copper armor :c')
                continue
        if use=='7':
            print('')
            if woodenswordamount>0:
                print('Wooden sword equipped')
                power=1.5
                if equippedweapon=='Wooden dagger':
                    woodendaggeramount=woodendaggeramount+1
                    print('Wooden dagger unequipped')
                    print("")
                if equippedweapon=='Wooden sword':
                    woodenswordamount=woodenswordamount+1
                    print('Wooden sword unequipped')
                    print('')
                if equippedweapon=='Copper sword':
                    copperswordamount=copperswordamount+1
                    print('Copper sword unequipped')
                    print('')
                if equippedweapon=='Maxwell sword':
                    catswordamount=catswordamount+1
                    print('Maxwell sword unequipped')
                    print('')
                else:
                    print('')
                if loot1==1:
                    loot1=loot1-1
                if loot2==1:
                    loot2=loot2-1
                if loot3==1:
                    loot3=loot3-1
                if block1w==1:
                    block1w=block1w-1
                if block2w==1:
                    block2w=block2w-1
                if block3w==1:
                    block3w=block3w-1
                if sharp1==1:
                    sharp1=sharp1-1
                if sharp2==1:
                    sharp2=sharp2-1
                if sharp3==1:
                    sharp3=sharp3-1
                if curse1==1:
                    curse1=curse1-1
                if curse2==1:
                    curse2=curse2-1
                if curse3==1:
                    curse3=curse3-1
                equippedweapon='Wooden sword'
                woodenswordamount=woodenswordamount-1
                if type=='Healer':
                    power=power*0.8
                continue
            else:
                print('You do not have a wooden sword :c')
                continue
        if use=='8':
            print('')
            if copperswordamount>0:
                print('Copper sword equipped')
                power=1.7
                if equippedweapon=='Wooden dagger':
                    woodendaggeramount=woodendaggeramount+1
                    print('Wooden dagger unequipped')
                    print("")
                if equippedweapon=='Wooden sword':
                    woodenswordamount=woodenswordamount+1
                    print('Wooden sword unequipped')
                    print('')
                if equippedweapon=='Copper sword':
                    copperswordamount=copperswordamount+1
                    print('Copper sword unequipped')
                    print('')
                if equippedweapon=='Maxwell sword':
                    catswordamount=catswordamount+1
                    print('Maxwell sword unequipped')
                    print('')
                else:
                    print('')
                if loot1==1:
                    loot1=loot1-1
                if loot2==1:
                    loot2=loot2-1
                if loot3==1:
                    loot3=loot3-1
                if block1w==1:
                    block1w=block1w-1
                if block2w==1:
                    block2w=block2w-1
                if block3w==1:
                    block3w=block3w-1
                if sharp1==1:
                    sharp1=sharp1-1
                if sharp2==1:
                    sharp2=sharp2-1
                if sharp3==1:
                    sharp3=sharp3-1
                if curse1==1:
                    curse1=curse1-1
                if curse2==1:
                    curse2=curse2-1
                if curse3==1:
                    curse3=curse3-1
                equippedweapon='Copper sword'
                copperswordamount=copperswordamount-1
                if type=='Healer':
                    power=power*0.8
                continue
            else:
                print('You do not have a copper sword :c')
                continue
        if use=='9':
            print('')
            if catswordamount>0:
                print('Maxwell sword equipped')
                power=2
                if equippedweapon=='Wooden dagger':
                    woodendaggeramount=woodendaggeramount+1
                    print('Wooden dagger unequipped')
                    print("")
                if equippedweapon=='Wooden sword':
                    woodenswordamount=woodenswordamount+1
                    print('Wooden sword unequipped')
                    print('')
                if equippedweapon=='Copper sword':
                    copperswordamount=copperswordamount+1
                    print('Copper sword unequipped')
                    print('')
                if equippedweapon=='Maxwell sword':
                    catswordamount=catswordamount+1
                    print('Maxwell sword unequipped')
                    print('')
                else:
                    print('')
                if loot1==1:
                    loot1=loot1-1
                if loot2==1:
                    loot2=loot2-1
                if loot3==1:
                    loot3=loot3-1
                if block1w==1:
                    block1w=block1w-1
                if block2w==1:
                    block2w=block2w-1
                if block3w==1:
                    block3w=block3w-1
                if sharp1==1:
                    sharp1=sharp1-1
                if sharp2==1:
                    sharp2=sharp2-1
                if sharp3==1:
                    sharp3=sharp3-1
                if curse1==1:
                    curse1=curse1-1
                if curse2==1:
                    curse2=curse2-1
                if curse3==1:
                    curse3=curse3-1
                equippedweapon='Maxwell sword'
                catswordamount=catswordamount-1
                if type=='Healer':
                    power=power*0.8
                continue
            else:
                print('You do not have a Maxwell sword :c')
                continue
        if use=='10':
            print('')
            if resistancepotionamount>0:
                print('Resistance potion activated for 3 adventures')
                resistancepotionamount=resistancepotionamount-1
                resistanceuse=4
            else:
                print('You do not have a resistance potion :c')
                continue
        if use=='11':
            print('')
            if strengthpotionamount>0:
                strengthpotionamount=strengthpotionamount-1
                print('Strength potion activated for 3 adventures')
                strengthuse=4
                continue
            else:
                print('You do not have a strength potion :c')
                used=0
                continue
        cont = input('')
        if cont=='':
            continue
        elif cont=='stop':
            break
        else:
            print('There is no such command as [',cont,']')
            continue
    
    if choice=='4':
        print('')
        print('Potions:')
        print('')
        print('(1) Health potion = 3 gold (2 gold for sell)')
        print('(2) Revive potion = 10 gold (7 gold for sell)')
        print('(10) Resistance potion = 6 gold (4 gold for sell)')
        print('(11) Strength potion = 6 gold (4 gold for sell)')
        print('')
        print('Armors:')
        print('')
        print('(3) Leather armor (15 HP) = 6 gold (4 gold for sell)')
        print('(9) Copper armor (20 HP) = 8 gold (Only for sell)')
        print('Weapons:')
        print('')
        print('(4) Wooden dagger (1.3 Power) = 5 gold (3 gold for sell)')
        print('(5) Wooden sword (1.5 Power) = 7 gold (5 gold for sell)')
        print('(8) Copper sword (1.7 Power) = 9 gold (Only for sell)')
        print('')
        print('Lootboxes:')
        print('')
        print('(6) Common lootbox = 5 gold')
        print('(7) Rare lootbox = 12 gold')
        purchase=input('')
        if purchase=='1':
            if treasury>2.99:
                print('')
                print('Purchase succesfull')
                print('+ 1 Health potion (',healthpotionamount+1,')')
                print('- 3 gold (',treasury-3,')')
                treasury=treasury-3
                healthpotionamount=healthpotionamount+1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            
        if purchase=='sell 1':
            if healthpotionamount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Health potion (',healthpotionamount-1,')')
                print('+ 2 gold (',treasury+2,')')
                treasury=treasury+2
                healthpotionamount=healthpotionamount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a health potion')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='2':
            if treasury>9.99:
                print('')
                print('Purchase succesfull')
                print('+ 1 Revive potion (',revivepotionamount+1,')')
                print('- 10 gold (',treasury-10,')')
                treasury=treasury-10
                revivepotionamount=revivepotionamount+1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='sell 2':
            if revivepotionamount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Revive potion (',revivepotionamount-1,')')
                print('+ 7 gold (',treasury+7,')')
                treasury=treasury+7
                revivepotionamount=revivepotionamount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a revive potion')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='3':
            if treasury>5.99:
                print('')
                print('Purchase succesfull')
                print('+ 1 Leather armor (',leatherarmoramount+1,')')
                print('- 6 gold (',treasury-6,')')
                treasury=treasury-6
                leatherarmoramount=leatherarmoramount+1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='sell 3':
            if leatherarmoramount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Leather armor (',leatherarmoramount-1,')')
                print('+ 4 gold (',treasury+4,')')
                treasury=treasury+4
                leatherarmoramount=leatherarmoramount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a leather armor')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='4':
            if treasury>4.99:
                print('')
                print('Purchase succesfull')
                print('+ 1 Wooden dagger (',woodendaggeramount+1,')')
                print('- 5 gold (',treasury-5,')')
                treasury=treasury-5
                woodendaggeramount=woodendaggeramount+1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='sell 4':
            if woodendaggeramount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Wooden dagger (',woodendaggeramount-1,')')
                print('+ 3 gold (',treasury+3,')')
                treasury=treasury+3
                woodendaggeramount=woodendaggeramount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a wooden dagger')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='5':
            if treasury>6.99:
                print('')
                print('Purchase succesfull')
                print('+ 1 Wooden sword (',woodenswordamount+1,')')
                print('- 7 gold (',treasury-7,')')
                treasury=treasury-7
                woodenswordamount=woodenswordamount+1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='sell 5':
            if woodenswordamount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Wooden sword (',woodenswordamount-1,')')
                print('+ 5 gold (',treasury+5,')')
                treasury=treasury+5
                woodenswordamount=woodenswordamount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a wooden sword')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='6':
            if treasury>5.99:
                print('')
                print('Purchase succesfull')
                print('- 5 gold (',treasury-5,')')
                treasury=treasury-5
                item=random.randint(1,6)
                if item==1:
                    woodendaggeramount=woodendaggeramount+1
                    print('+ Wooden dagger (',woodendaggeramount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if item==2:
                    woodenswordamount=woodenswordamount+1
                    print('+ Wooden sword (',woodenswordamount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if item==3:
                    leatherarmoramount=leatherarmoramount+1
                    print('+ Leather armor (',leatherarmoramount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if item==4:
                    healthpotionamount=healthpotionamount+1
                    print('+ Leather armor (',healthpotionamount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if item==5:
                    resistancepotionamount=resistancepotionamount+1
                    print('+ Resistance potion (',resistancepotionamount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if item==6:
                    strengthpotionamount=strengthpotionamount+1
                    print('+ Strength potion (',strengthpotionamount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='7':
            if treasury>11.99:
                print('')
                print('Purchase succesfull')
                print('- 12 gold (',treasury-12,')')
                treasury=treasury-12
                item=random.randint(1,3)
                if item==1:
                    copperarmoramount=copperarmoramount+1
                    print('+ Copper armor (',copperarmoramount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if item==2:
                    copperswordamount=copperswordamount+1
                    print('+ Copper sword (',copperswordamount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
                if item==3:
                    revivepotionamount=revivepotionamount+1
                    print('+ Revive potion (',revivepotionamount,') ')
                    cont = input('')
                    if cont=='':
                        continue
                    elif cont=='stop':
                        break
                    else:
                        print('There is no such command as [',cont,']')
                        continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='8':
            print('')
            print('You cannot buy a copper sword in the shop, maybe try to get it from the rare lootbox')
            print('')
            continue

        if purchase=='9':
            print('')
            print('You cannot buy a copper armor in the shop, maybe try to get it from the rare lootbox')
            print('')
            continue

        if purchase=='sell 8':
            if copperswordamount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Copper sword (',copperswordamount-1,')')
                print('+ 9 gold (',treasury+9,')')
                treasury=treasury+9
                copperswordamount=copperswordamount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a copper sword')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='sell 9':
            if copperarmoramount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Copper armor (',copperarmoramount-1,')')
                print('+ 8 gold (',treasury+8,')')
                treasury=treasury+8
                copperarmoramount=copperarmoramount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a copper armor')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='10':
            if treasury>5.99:
                print('')
                print('Purchase succesfull')
                print('+ 1 Resistance potion (',resistancepotionamount+1,')')
                print('- 6 gold (',treasury-6,')')
                treasury=treasury-6
                resistancepotionamount=resistancepotionamount+1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            
        if purchase=='sell 10':
            if resistancepotionamount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Resistance potion (',resistancepotionamount-1,')')
                print('+ 4 gold (',treasury+4,')')
                treasury=treasury+4
                resistancepotionamount=resistancepotionamount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a resistance potion')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='11':
            if treasury>5.99:
                print('')
                print('Purchase succesfull')
                print('+ 1 Strength potion (',strengthpotionamount+1,')')
                print('- 6 gold (',treasury-6,')')
                treasury=treasury-6
                strengthpotionamount=strengthpotionamount+1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            
        if purchase=='sell 11':
            if healthpotionamount>0:
                print('')
                print('Sell succesfull')
                print('- 1 Strength potion (',strengthpotionamount-1,')')
                print('+ 4 gold (',treasury+4,')')
                treasury=treasury+4
                strengthpotionamount=strengthpotionamount-1
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a strength potion')
                cont = input('')
                if cont=='':
                    continue
                elif cont=='stop':
                    break
                else:
                    print('There is no such command as [',cont,']')
                    continue

        if purchase=='':
            continue
        else:
            print('There is no such command as [',purchase,']')
            continue
    
    if choice=='5':
        print('')
        print('Adventure:')
        print('')
        print('In adventure, you can fight and get xp and gold but it comes with a price: HPloss')
        print('The more xp you have, the harder the fights get')
        print('Here you can decide to run or fight: if you run, then you get some XP and lose some HP, if you fight, you will deal damage to the enemy according to your weapon, you will also lose HP, if your HP gets below 0 or is 0, then you die and if the enemys HP is down then you win, in fights you get more XP than running and also get gold')
        print('')
        print('Shop:')
        print('')
        print('In the shop, enter the number of the item to buy it, if you want to sell something, just put sell before it like sell 1 ')
        print('')
        print('Profile & Inventory:')
        print('')
        print('In the inventory you can view your items and in the profile you can check your stats')
        print('In the inventory, write the number of the item to use it or equip it')
        print('When you equip something, you cannot sell it anymore, so equip them wisely! (You can unequip them by equipping another stuff)')
        print('')
        print('Gamble:')
        print('')
        print('Here you can bet an amount of gold and maybe lose the half it or win +50% DO NOT WRITE A LETTER HERE, JUST NUMBERS OR ELSE THE GAME WILL BREAK')
        print('')
        print('Enchanting:')
        print('Here you can get enchantments to your weapons or to your armors. Unequipping an enchanted armor will result in losing the enchantment, enchanting costs 30xp, use it wisely!')
        print('')
        print('Gameplay:')
        print('')
        print('The goal of the game is to reach 100 xp and to survive, there are many rare events to help your journey')
        print('The game is made up of two section, one is before reaching 50 xp and the other is after 50 xp, this section is harder')

        cont=input('')
        if cont=='':
            continue
        elif cont=='stop':
            break
        else:
            print('There is no such command as [',cont,']')
            continue

    if choice=='6':
        print('')
        print('Potions:')
        print('')
        print('Health potion - Common (+30% HP) - Source: Adventure loot, Common lootbox, Shop')
        print('Revive potion - Rare! (Allows to continue the game with full HP after dying) - Source: Adventure loot, Rare lootbox, Shop')
        print('Resistance potion - Common (-50% HP loss for 3 adventures) - Source: Adventure loot, Common lootbox, Shop')
        print('Strength potion - Common (+50% Strength for 3 adventures) - Source: Adventure loot, Common lootbox, Shop')
        print('')
        print('Armors:')
        print('')
        print('Leather armor - Common (15 HP) - Source: Adventure loot, Common lootbox, Shop')
        print('Copper armor - Rare! (20 HP) - Source: Adventure loot, Rare lootbox')
        print('Maxwell armor - Epic!! (30 HP) - Source: Maxwell event')
        print('')
        print('Weapons:')
        print('')
        print('Wooden dagger - Common (1.3 Power) - Source: Adventure loot, Common lootbox, Shop')
        print('Wooden sword - Common (1.5 Power) - Source: Adventure loot, Common lootbox, Shop')
        print('Copper sword - Rare! (1.7 Power) - Source: Adventure loot, Rare lootbox')
        print('Maxwell sword - Epic!! (2 Power) - Source: Maxwell event')

    if choice=='7':
        odd=random.randint(1,2)
        print("")
        print('50-50%, double or half')
        bet= float(input('Make a bet: '))
        if bet>treasury:
            print('')
            print('Eyo you do not even have that many gold')
            print('')
            continue
        if bet<treasury or bet==treasury:
            if odd==1:
                print('')
                print('Win - +50%')
                goldgain=0.5*bet
                treasury=goldgain+treasury
                print('+',goldgain,'gold (',treasury,')')
                print('')
                continue
            else:
                print('')
                print('Lose - -50%')
                goldgain=0.5*bet
                treasury=treasury-goldgain
                print('-',goldgain,'gold (',treasury,')')
                print('')
                continue
        else:
            continue

    if choice=='8':
        if xp>29:
            print('')
            entype=input('What would you like to enchant? 1=Equipped weapon, 2=Equipped armor')
            enchant=random.randint(1,100)
            if entype=='1':
                if enchantmentscroll>0:
                    print('Enchantmentscroll used')
                    enchantmentscroll=enchantmentscroll-1
                else:
                    if type=='Wizard':
                        xpgain=15
                        xp=xp-xpgain
                        print('- 15 XP (',xp,')')
                    else:
                        xpgain=30
                        xp=xp-xpgain
                        print('- 30 XP (',xp,')')
                if enchant>0 and enchant<16:
                    enchant='Sharpness I'
                    print('Your weapon got enchanted with:',enchant,'\n+15% Power')
                    print('')
                    power=power*1.15
                    sharp1=1
                    continue
                if enchant>15 and enchant<23:
                    enchant='Sharpness II'
                    print('Your weapon got enchanted with:',enchant,'\n+30% Power')
                    print('')
                    power=power*1.3
                    sharp2=1
                    continue
                if enchant>22 and enchant<26:
                    enchant='Sharpness III'
                    print('Your weapon got enchanted with:',enchant,'\n+50% Power')
                    print('')
                    power=power*1.5
                    sharp3=1
                    continue
                if enchant>25 and enchant<41:
                    enchant='Curse I'
                    print('Your weapon got enchanted with:',enchant,'\n-15% Power')
                    print('')
                    power=power*0.85
                    curse1=1
                    continue
                if enchant>40 and enchant<48:
                    enchant='Curse II'
                    print('Your weapon got enchanted with:',enchant,'\n-30% Power')
                    print('')
                    power=power*0.7
                    curse2=1
                    continue
                if enchant>47 and enchant<51:
                    enchant='Curse III'
                    print('Your weapon got enchanted with:',enchant,'\n-50% Power')
                    print('')
                    power=power*0.5
                    curse3=1
                    continue
                if enchant>50 and enchant<66:
                    enchant='Looting I'
                    print('Your weapon got enchanted with:',enchant,'\n+25% Goldgain')
                    print('')
                    loot1=1
                if enchant>65 and enchant<73:
                    enchant='Looting II'
                    print('Your weapon got enchanted with:',enchant,'\n+50% Goldgain')
                    print('')
                    loot2=1
                    continue
                if enchant>72 and enchant<76:
                    enchant='Looting III'
                    print('Your weapon got enchanted with:',enchant,'\n+75% Goldgain')
                    print('')
                    loot3=1
                    continue
                if enchant>75 and enchant<91:
                    enchant='Blocking I'
                    print('Your weapon got enchanted with:',enchant,'\n-15% HPloss')
                    print('')
                    block1w=1
                    continue
                if enchant>90 and enchant<98:
                    enchant='Blocking II'
                    print('Your weapon got enchanted with:',enchant,'\n-30% HPloss')
                    print('')
                    block2w=1
                    continue
                else:
                    enchant='Blocking III'
                    print('Your weapon got enchanted with:',enchant,'\n-50% HPloss')
                    print('')
                    block3w=1
                    continue
            if entype=='2':
                if enchantmentscroll>0:
                    print('Enchantmentscroll used')
                    enchantmentscroll=enchantmentscroll-1
                else:
                    xpgain=30
                    xp=xp-xpgain
                    print('- 30 XP (',xp,')')
                if enchant>0 and enchant<16:
                    enchant='Resistance I'
                    print('Your armor got enchanted with:',enchant,'\n+15% MaxHP')
                    print('')
                    maxhp=maxhp*1.15
                    continue
                if enchant>15 and enchant<23:
                    enchant='Resistance II'
                    print('Your armor got enchanted with:',enchant,'\n+30% MaxHP')
                    print('')
                    maxhp=maxhp*1.3
                    continue
                if enchant>22 and enchant<26:
                    enchant='Resistance III'
                    print('Your armor got enchanted with:',enchant,'\n+50% MaxHP')
                    print('')
                    maxhp=maxhp*1.5
                    continue
                if enchant>25 and enchant<41:
                    enchant='Curse I'
                    print('Your armor got enchanted with:',enchant,'\n-15% MaxHP')
                    print('')
                    maxhp=maxhp*0.85
                    continue
                if enchant>40 and enchant<48:
                    enchant='Curse II'
                    print('Your armor got enchanted with:',enchant,'\n-30% MaxHP')
                    print('')
                    maxhp=maxhp*0.7
                    continue
                if enchant>47 and enchant<51:
                    enchant='Curse III'
                    print('Your armor got enchanted with:',enchant,'\n-50% MaxHP')
                    print('')
                    maxhpx=maxhp*0.5
                    continue
                if enchant>75 and enchant<91:
                    enchant='Blocking III'
                    print('Your armor got enchanted with:',enchant,'\n-50% HPloss')
                    print('')
                    block3a=1
                    continue
                if enchant>90 and enchant<98:
                    enchant='Blocking II'
                    print('Your armor got enchanted with:',enchant,'\n-30% HPloss')
                    print('')
                    block2a=1
                    continue
                else:
                    enchant='Blocking I'
                    print('Your armor got enchanted with:',enchant,'\n-15% HPloss')
                    print('')
                    block1a=1
                    continue
            else:
                continue

        else:
            print('')
            print('You did not reach 30XP :c')
            continue

    if choice=='9':
        if type=='Healer':
            if vampire==0:
                print('1 = Vampire I: 15% chance to damage 30% of your enemys max HP and heal by that amount - 2 skill points required')
            if vampire==1:
                print('1 = Vampire II: 30% chance to damage 30% of your enemys max HP and heal by that amount - 2 skill points required')
            if vampire==2:
                print('1 = Vampire III: 50% chance to damage 30% of your enemys max HP and heal by that amount - 2 skill points required')
            if focus==0:
                print('2 = Focus I: Decrease enemy critical hit chance by 5% - 1 skill point required')
            if focus==1:
                print('2 = Focus II: Decrease enemy critical hit chance by 10% - 1 skill point required')
            if focus==2:
                print('2 = Focus III: Decrease enemy critical hit chance by 15% - 1 skill point required')
            if advancedlooting==0:
                print('3 = Advanced looting: Extra health potion in adventures if you get one - 1 skill point required')
            skillchoice=input('')
            if skillchoice=='1':
                if vampire==0:
                    if skillpoint>1:
                        print('')
                        print('Vampire I skill learned')
                        print('')
                        vampire=1
                        skillpoint=skillpoint-2
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if vampire==1:
                    if skillpoint>1:
                        print('')
                        print('Vampire II skill learned')
                        print('')
                        vampire=2
                        skillpoint=skillpoint-2
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if vampire==2:
                    if skillpoint>1:
                        print('')
                        print('Vampire III skill learned')
                        print('')
                        vampire=3
                        skillpoint=skillpoint-2
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='2':
                if focus==0:
                    if skillpoint>0:
                        print('')
                        print('Focus I skill learned')
                        print('')
                        focus=1
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if focus==1:
                    if skillpoint>0:
                        print('')
                        print('Focus II skill learned')
                        print('')
                        focus=2
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if focus==2:
                    if skillpoint>0:
                        print('')
                        print('Focus III skill learned')
                        print('')
                        focus=3
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='3':
                if advancedlooting==0:
                    if skillpoint>0:
                        print('')
                        print('Advanced looting skill learned')
                        print('')
                        advancedlooting=1
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            else:
                continue
        if type=='Swordsman':
            if learning==0:
                print('1 = Improved learning I: Increase XP gain by 20% - 2 skill points required')
            if learning==1:
                print('1 = Improved learning II: Increase XP gain by 40% - 2 skill points required')
            if learning==2:
                print('1 = Improved learning III: Increase XP gain by 60% - 2 skill points required')
            if shield==0:
                print('2 = Shield I: 5% to not lose HP during a turn of a fight - 1 skill point required')
            if shield==1:
                print('2 = Shield II: 10% to not lose HP during a turn of a fight - 1 skill point required')
            if shield==2:
                print('2 = Shield III: 15% to not lose HP during a turn of a fight - 1 skill point required')
            if laststand==0:
                print('3 = Last stand: If you die, you return back with 20% HP - 3 skill points required')
            skillchoice=input('')
            if skillchoice=='1':
                if learning==0:
                    if skillpoint>1:
                        print('')
                        print('Improved learning I skill learned')
                        print('')
                        learning=1
                        skillpoint=skillpoint-2
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if learning==1:
                    if skillpoint>1:
                        print('')
                        print('Improved learning II skill learned')
                        print('')
                        learning=2
                        skillpoint=skillpoint-2
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if learning==2:
                    if skillpoint>1:
                        print('')
                        print('Learning III skill learned')
                        print('')
                        learning=3
                        skillpoint=skillpoint-2
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='2':
                if shield==0:
                    if skillpoint>0:
                        print('')
                        print('Shield I skill learned')
                        print('')
                        shield=1
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if shield==1:
                    if skillpoint>0:
                        print('')
                        print('Shield II skill learned')
                        print('')
                        shield=2
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if shield==2:
                    if skillpoint>0:
                        print('')
                        print('Shield III skill learned')
                        print('')
                        shield=3
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='3':
                if laststand==0:
                    if skillpoint>0:
                        print('')
                        print('Last stand looting skill learned')
                        print('')
                        laststand=1
                        skillpoint=skillpoint-3
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            else:
                continue

    if choice=='cheat':
        treasury=10000
        xp=101
        skillpoint=1000
        continue

    else:
        print('There is no such command as [',choice,']')
        continue
        
        
                    