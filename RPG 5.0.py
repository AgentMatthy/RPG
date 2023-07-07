import random
import time

#-----------------------Functions-----------------------#

def advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp):
    time.sleep(3)
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
                enchantcheckarmor()

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
                enchantcheckweapon()

def run_modifiers():
                    global block1a
                    global block2a
                    global block3a
                    global block1w
                    global block2w
                    global block3w
                    global resistanceuse
                    global hploss
                    global learning
                    global xpgain
                    global protection
                    global shield
                    global enemylvl
                    hploss=((enemylvl/10)*hploss)+hploss
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
                    if learning==1:
                        xpgain=xpgain*1.2
                    if learning==2:
                        xpgain=xpgain*1.4
                    if learning==3:
                        xpgain=xpgain*1.6
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

def fight():                      
                        global enemyhploss
                        global crit
                        global focus
                        global enemycrit
                        global block1a
                        global block2a
                        global block3a
                        global block1w
                        global block2w
                        global block3w
                        global hploss
                        global equippedweapon
                        global hp
                        global enemymaxhp
                        global protection
                        global vampire
                        global vam
                        global corrvam
                        global type
                        global sharp1
                        global sharp2
                        global sharp3
                        global curse1
                        global curse2
                        global curse3
                        global maxhp
                        global enemyhp
                        global shield
                        global treasury
                        global critcount
                        global weaken
                        global stun
                        global sabotage
                        global stunning
                        global tearing
                        global downfall
                        global finish
                        global finishchance
                        global stamina
                        global block
                        global blockchance
                        global blocktype
                        global staminatype
                        global movement
                        global staminaloss
                        global blockloss
                        global staminaplus
                        global blockplus
                        global stamina
                        global enemystamina
                        global enemyblock
                        global enemyblockchance
                        global enemymovement
                        global enemystaminaloss
                        global enemyblockloss
                        global enemystaminaplus
                        global enemyblockplus
                        global armorresistance
                        global enemylvl
                        global healing
                        global turncount
                        global tearingdive
                        global tearingdiveskill
                        global fireauracrit
                        global healthpotionamount
                        global staminapotionamount
                        global strengthpotionamount
                        global resistancepotionamount
                        global doing12
                        global doing13
                        global progress
                        global potions
                        turncount=turncount+1
                        fireauracrit=fireauracrit-1
                        if turncount>3 and healing==1:
                            printB('type heal to heal')
                            heal=input('')
                            if heal=='heal':
                                hp=hp+(0.2*maxhp)
                                if hp>maxhp:
                                    hp=maxhp
                                print('')
                                print('Healing: +',round((maxhp*0.2),3),'HP (',round(hp,3),'/',round(maxhp,3),')')
                                print('')
                                turncount=turncount-4
                        if turncount>3 and tearingdive==1:
                            printB('type tearing dive to active the skill')
                            dive=input('')
                            if dive=='tearing dive':
                                tearingdiveskill=1
                                turncount=turncount-4
                        hploss=((enemylvl/10)*hploss)+hploss
                        enemyhploss=random.randint(0,2)
                        if tearing==1:
                            crit=random.randint(1,80)
                        if tearing==2:
                            crit=random.randint(1,66)
                        if tearing==3:
                            crit=random.randint(1,57)
                        else:
                            crit=random.randint(1,100)                     
                        if focus==1:
                            enemycrit=random.randint(1,134)
                        if focus==2:
                            enemycrit=random.randint(1,200)
                        if focus==3:
                            enemycrit=random.randint(1,400)
                        else:
                            enemycrit=random.randint(1,100)
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
                        if equippedweapon=='Wooden dagger':
                            enemyhploss=random.randint(0,3)
                            if tearingdiveskill==1:
                                enemyhploss=random.randint(1,3)
                        if equippedweapon=='Wooden sword':
                            enemyhploss=random.randint(0,5)
                            if tearingdiveskill==1:
                                enemyhploss=random.randint(1,5)
                        if equippedweapon=='Copper sword':
                            enemyhploss=random.randint(0,7)
                            if tearingdiveskill==1:
                                enemyhploss=random.randint(1,7)
                        if equippedweapon=='Maxwell sword':
                            enemyhploss=random.randint(0,10)
                            if tearingdiveskill==1:
                                enemyhploss=random.randint(1,10)
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
                                if maxhp<hp:
                                    hp=maxhp
                                else:
                                    hp=hp
                            else:
                                treasury=treasury
                        protection=random.randint(1,100)
                        if weaken==1:
                            hploss=hploss*0.93
                        if weaken==2:
                            hploss=hploss*0.86
                        if weaken==3:
                            hploss=hploss*0.8
                        stun=stun-1
                        if stun>0:
                            hploss=0
                        if finish==1:
                            finishchance=random.randint(1,100)
                            if finishchance<11:
                                enemyhploss=enemyhploss*5
                        if stamina<101 and stamina>79:
                            staminatype='High'
                            crit=random.randint(1,40)
                        if stamina<80 and stamina>39:
                            staminatype='Medium'
                            enemyhploss=enemyhploss
                        if stamina<40:
                            staminatype='Low'
                            enemyhploss=enemyhploss*0.5
                        blockchance=100
                        enemyblockchance=100
                        if block<101 and block>79:
                            blocktype='High'
                            blockchance=random.randint(1,2)
                        if block<80 and block>39:
                            blocktype='Medium'
                            hploss=hploss
                        if block<40:
                            blocktype='Low'
                            hploss=hploss*1.5
                        if enemystamina<101 and enemystamina>79:
                            enemycrit=random.randint(1,40)
                        if enemystamina<80 and enemystamina>39:
                            hploss=hploss
                        if enemystamina<40:
                            hploss=hploss*0.5
                        if enemyblock<101 and enemyblock>79:
                            enemyblockchance=random.randint(1,2)
                        if enemyblock<80 and enemyblock>39:
                            enemyhploss=enemyhploss
                        if block<40:
                            enemyhploss=enemyhploss*1.5
                        print('')
                        print('Stamina:',staminatype,'')
                        print('Block:',blocktype,'')
                        print('')
                        potions=healthpotionamount+staminapotionamount
                        if potions>0:
                            printB('Potions:')
                            print('')
                            if healthpotionamount>0:
                                print('(1) Health potion:',healthpotionamount,'')
                            if staminapotionamount>0:
                                print('(2) Stamina potion:',staminapotionamount,'')
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
                                    printR('You do not have a health potion :c')
                            if use=='2':
                                print('')
                                if staminapotionamount>0:
                                    staminapotionamount=staminapotionamount-1
                                    printG('Stamina and block replenished')
                                    stamina=100
                                    block=100
                                else:
                                    printR('You do not have a stamina potion :c')
                                    used=0
                        printB('1=Defend, 2=Attack')
                        movement=input('')
                        if movement=='1':
                            blockloss=random.randint(10,40)
                            staminaplus=random.randint(10,40)
                            block=block-blockloss
                            stamina=stamina+staminaplus
                            hploss=hploss*0.5
                            enemyhploss=enemyhploss*0.5
                        else:
                            staminaloss=random.randint(10,40)
                            blockplus=random.randint(10,40)
                            stamina=stamina-staminaloss
                            block=block+blockplus
                            hploss=hploss*1.5
                            enemyhploss=enemyhploss*1.5
                        if stamina<0:
                            stamina=0
                        if block<0:
                            block=0
                        enemymovement=random.randint(1,2)
                        if enemymovement==1:
                            enemyblockloss=random.randint(10,40)
                            enemystaminaplus=random.randint(10,40)
                            enemyblock=enemyblock-enemyblockloss
                            enemystamina=enemystamina+enemystaminaplus
                            enemyhploss=enemyhploss*0.5
                            hploss=hploss*0.5
                        else:
                            enemystaminaloss=random.randint(10,40)
                            enemyblockplus=random.randint(10,40)
                            enemystamina=enemystamina-enemystaminaloss
                            enemyblock=enemyblock+enemyblockplus
                            enemyhploss=enemyhploss*1.5
                            hploss=hploss*1.5
                        if enemystamina<0:
                            enemystamina=0
                        if enemyblock<0:
                            enemyblock=0
                        if shield==1:
                            if protection<6:
                                hploss=0
                                print('')
                                printG('SHIELD ACTIVE')
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                                print('')
                                printG('SHIELD ACTIVE')
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                                print('')
                                printG('SHIELD ACTIVE')
                            else:
                                hploss=hploss
                        if tearingdiveskill==1:
                            crit=10
                        if crit<21:
                            if downfall==1:
                                enemyhploss=enemyhploss*1.65
                            if downfall==2:
                                enemyhploss=enemyhploss*1.8
                            if downfall==3:
                                enemyhploss=enemyhploss*2
                            else:
                                enemyhploss=enemyhploss*1.5
                            critcount=critcount+1
                            if stunning==1 and enemyhploss==0:
                                print('')
                                printY('ENEMY STUNNED')
                                stun=3
                            if fireaura==1:
                                print('')
                                printR('FIRE AURA triggered for 3 turns')
                                fireauracrit=3
                        if armorresistance==1:
                            hploss=hploss-1
                        if armorresistance==2:
                            hploss=hploss-2
                        if armorresistance==3:
                            hploss=hploss-3
                        else:
                            hploss=hploss
                        if hploss<0:
                            hploss=0
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
                                if maxhp<hp:
                                    hp=maxhp
                                else:
                                    hp=hp
                            else:
                                treasury=treasury
                        if blockchance==1 or hploss==0:
                            print('')
                            printG('HIT BLOCKED')
                            print('')
                            if doing13=='Yes':
                                progress=progress+1
                            hploss=0
                        else:
                            hploss=hploss
                        if enemyblockchance==1 or enemyhploss==0:
                            if tearingdiveskill==1:
                                enemyhploss=enemyhploss
                            else:
                                enemyhploss=0
                                print('')
                                printR('ENEMY BLOCKED HIT')
                                print('')
                        else:
                            enemyhploss=enemyhploss
                        if fireauracrit>0:
                            enemyhploss=enemyhploss+(enemymaxhp*0.1)
                        hp=hp-hploss
                        enemyhp=enemyhp-enemyhploss
                        tearingdiveskill=0
                        if sabotage==1:
                            enemycrit=100
                        if enemycrit<21:
                            hploss=hploss*1.5  
                        print('')
                        if crit<21 and enemyhploss>0:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
                            if doing12=='Yes':
                                progress=progress+1
                        else:
                            print('Enemy HP: -',round(enemyhploss,2),'(',round(enemyhp,2),'/',enemymaxhp,')')
                        if enemycrit<21 and hploss>0:
                            print('Your HP: -',round(hploss,2),' Critical hit! (',round(hp,2),'/',maxhp,')')
                        else:
                            print('Your HP: -',round(hploss,2),'(',round(hp,2),'/',maxhp,')')
                        print('')

def win():
                        global learning
                        global xpgain
                        global goldgain
                        global type
                        global loot1
                        global loot2
                        global loot3
                        global critcount
                        global stealing
                        global moneyrain
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
                        if stealing==1:
                            goldgain=goldgain+(3*critcount)
                        if moneyrain==1:
                            rain=random.randint(1,2)
                            if rain==2:
                                goldgain=goldgain*1.5
                            else:
                                goldgain=goldgain

def wolf_loot():
                        global loot
                        global woodendaggeramount
                        global revivepotionamount
                        global advancedlooting
                        global healthpotionamount
                        global resistancepotionamount
                        global strengthpotionamount
                        global staminapotionamount
                        global inprogress1
                        global inprogress2
                        global inprogress3
                        global questtype1
                        global questtype2
                        global questtype3
                        global doing11
                        if 0<loot and loot<20:
                            woodendaggeramount=woodendaggeramount+1
                            print('+ Wooden dagger (',woodendaggeramount,')')
                            if inprogress1=='Yes':
                                if doing11=='Yes' and questtype1=='Wooden dagger':
                                    progress=progress+1
                            if inprogress2=='Yes':
                                if doing11=='Yes' and questtype2=='Wooden dagger':
                                    progress=progress+1
                            if inprogress3=='Yes':
                                if doing11=='Yes' and questtype3=='Wooden dagger':
                                    progress=progress+1
                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                        if loot>49 and loot<53:
                            staminapotionamount=staminapotionamount+1
                            print('+ Stamina potion (',staminapotionamount,')')
                        print('')

def bear_loot():
                        global loot
                        global leatherarmoramount
                        global revivepotionamount
                        global advancedlooting
                        global healthpotionamount
                        global resistancepotionamount
                        global strengthpotionamount
                        global staminapotionamount
                        global inprogress1
                        global inprogress2
                        global inprogress3
                        global questtype1
                        global questtype2
                        global questtype3
                        global doing11
                        if 0<loot and loot<20:
                            leatherarmoramount=leatherarmoramount+1
                            print('+ Leather armor (',leatherarmoramount,')')
                            if inprogress1=='Yes':
                                if doing11=='Yes' and questtype1=='Leather armor':
                                    progress=progress+1
                            if inprogress2=='Yes':
                                if doing11=='Yes' and questtype2=='Leather armor':
                                    progress=progress+1
                            if inprogress3=='Yes':
                                if doing11=='Yes' and questtype3=='Leather armor':
                                    progress=progress+1
                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                        if loot>49 and loot<53:
                            staminapotionamount=staminapotionamount+1
                            print('+ Stamina potion (',staminapotionamount,')')
                        print('')

def rare_loot():
                        global loot
                        global prize
                        global advancedlooting
                        global healthpotionamount
                        global resistancepotionamount
                        global revivepotionamount
                        global strengthpotionamount
                        global woodendaggeramount
                        global woodenswordamount
                        global copperswordamount
                        global leatherarmoramount
                        global copperarmoramount
                        global staminapotionamount
                        global inprogress1
                        global inprogress2
                        global inprogress3
                        global questtype1
                        global questtype2
                        global questtype3
                        global doing11
                        if 0<loot and loot<20:
                            prize=random.randint(1,8)
                            if prize==1:
                                if advancedlooting==1:
                                    healthpotionamount=healthpotionamount+2
                                    print('+ 2 Health potion (',healthpotionamount,')')
                                else:
                                    healthpotionamount=healthpotionamount+1
                                    print('+ Health potion (',healthpotionamount,')')
                            if prize==2:
                                revivepotionamount=revivepotionamount+1
                                print('+ 1 Revive potion (',revivepotionamount,')')
                            if prize==3:
                                leatherarmoramount=leatherarmoramount+1
                                print('+ 1 Leather armor (',leatherarmoramount,')')
                                if inprogress1=='Yes':
                                    if doing11=='Yes' and questtype1=='Leather armor':
                                        progress=progress+1
                                if inprogress2=='Yes':
                                    if doing11=='Yes' and questtype2=='Leather armor':
                                        progress=progress+1
                                if inprogress3=='Yes':
                                    if doing11=='Yes' and questtype3=='Leather armor':
                                        progress=progress+1
                            if prize==4:
                                woodendaggeramount=woodendaggeramount+1
                                print('+ 1 Wooden dagger (',woodendaggeramount,')')
                                if inprogress1=='Yes':
                                    if doing11=='Yes' and questtype1=='Wooden dagger':
                                        progress=progress+1
                                if inprogress2=='Yes':
                                    if doing11=='Yes' and questtype2=='Wooden dagger':
                                        progress=progress+1
                                if inprogress3=='Yes':
                                    if doing11=='Yes' and questtype3=='Wooden dagger':
                                        progress=progress+1
                            if prize==5:
                                copperarmoramount=copperarmoramount+1
                                print('+ 1 Copper armor (',copperarmoramount,')')
                                if inprogress1=='Yes':
                                    if doing11=='Yes' and questtype1=='Copper armor':
                                        progress=progress+1
                                if inprogress2=='Yes':
                                    if doing11=='Yes' and questtype2=='Copper armor':
                                        progress=progress+1
                                if inprogress3=='Yes':
                                    if doing11=='Yes' and questtype3=='Copper armor':
                                        progress=progress+1
                            if prize==6:
                                copperswordamount=copperswordamount+1
                                print('+ 1 Copper sword (',copperswordamount,')')
                                if inprogress1=='Yes':
                                    if doing11=='Yes' and questtype1=='Copper sword':
                                        progress=progress+1
                                if inprogress2=='Yes':
                                    if doing11=='Yes' and questtype2=='Copper sword':
                                        progress=progress+1
                                if inprogress3=='Yes':
                                    if doing11=='Yes' and questtype3=='Copper sword':
                                        progress=progress+1                               
                            if prize==7:
                                revivepotionamount=revivepotionamount+1
                                print('+ 1 Revive potion (',revivepotionamount,')')
                            if prize==8:
                                staminapotionamount=staminapotionamount+1
                                print('+ Stamina potion (',staminapotionamount,')')
                        if loot==20:
                            revivepotionamount=revivepotionamount+1
                            print('+ Revive potion (',revivepotionamount,')')
                        if loot>20 and loot<40:
                            if advancedlooting==1:
                                healthpotionamount=healthpotionamount+2
                                print('+ 2 Health potion (',healthpotionamount,')')
                            else:
                                healthpotionamount=healthpotionamount+1
                                print('+ Health potion (',healthpotionamount,')')
                        if loot>40 and loot<45:
                            resistancepotionamount=resistancepotionamount+1
                            print('+ Resistance potion (',resistancepotionamount,')')
                        if loot>45 and loot<50:
                            strengthpotionamount=strengthpotionamount+1
                            print('+ Strength potion (',strengthpotionamount,')')
                        if loot>49 and loot<53:
                            staminapotionamount=staminapotionamount+1
                            print('+ Stamina potion (',staminapotionamount,')')
                        print('')

def gold_box():
                global prize
                global treasury
                prize=random.randint(4,10)
                treasury=treasury+prize
                printY('Gold box:')
                print('+',prize,'gold (',treasury,')')
                print('')

def profile():
            global type
            global treasury
            global hp
            global maxhp
            global equippedweapon
            global equippedarmor
            global vampire
            global skillpoint
            global shield
            global laststand
            global focus
            global learning
            global advancedlooting
            global healing
            global tearingdive
            global business
            global fireaura
            global perfecthealth
            global value
            global enemieskilled
            global score
            print('Class:',type,'')
            print('Treasury:',treasury,'')
            print('HP:',round(hp,2),'/',maxhp, equippedarmor,'-',armorenchant,'')
            print('Strength:',round(power,2), equippedweapon,'-',weaponenchant,'')
            print('Stamina:',staminatype,'')
            print('Block:',blocktype,'')
            print('')
            printB('Skills:')
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
            if healing==1:
                print('Healing I')
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
            if tearingdive==1:
                print('Tearing dive I')
                print('')
            if fastlearner==1:
                print('Fast learner I')
                print('')
            if stealing==1:
                print('Stealing I')
                print('')
            if moneyrain==1:
                print('Money rain I')
                print('')
            if business==1:
                print('Smart business I')
                print('')
            if weaken==1:
                print('Weaken I')
                print('')
            if weaken==2:
                print('Weaken II')
                print('')
            if weaken==3:
                print('Weaken III')
                print('')
            if stunning==1:
                print('Stunning I')
                print('')
            if sabotage==1:
                print('Sabotage I')
                print('')
            if fireaura==1:
                print('Fire aura I')
                print('')
            if tearing==1:
                print('Tearing I')
                print('')
            if tearing==2:
                print('Tearing II')
                print('')
            if tearing==3:
                print('Tearing III')
                print('')
            if downfall==1:
                print('Downfall I')
                print('')
            if downfall==2:
                print('Downfall II')
                print('')
            if downfall==3:
                print('Downfall III')
                print('')
            if finish==1:
                print('Finish I')
                print('')
            if perfecthealth==1:
                print('Perfect health I')
                print('')
            if perfecthealth==2:
                print('Perfect health II')
                print('')
            if perfecthealth==3:
                print('Perfect health III')
                print('')
            if skillpoint>0:
                print('Skill points:',skillpoint,'')
            print('')
            print('Enemies killed:',enemieskilled)
            print('Character value:',value)
            print('Score:',score)
            print('')

def weapon_equip():
                global equippedweapon
                global woodendaggeramount
                global woodenswordamount
                global catswordamount
                global copperswordamount
                global loot1
                global loot2
                global loot3
                global block1w
                global block2w
                global block3w
                global sharp1
                global sharp2
                global sharp3
                global curse1
                global curse2
                global curse3
                global looting1catsword
                global looting1coppersword
                global looting1woodensword
                global looting1woodendagger
                global looting2catsword
                global looting2coppersword
                global looting2woodensword
                global looting2woodendagger
                global looting3catsword
                global looting3coppersword
                global looting3woodensword
                global looting3woodendagger
                global blocking1catsword
                global blocking1coppersword
                global blocking1woodensword
                global blocking1woodendagger
                global blocking2catsword
                global blocking2coppersword
                global blocking2woodensword
                global blocking2woodendagger
                global blocking3catsword
                global blocking3coppersword
                global blocking3woodensword
                global blocking3woodendagger
                global curse1catsword
                global curse1coppersword
                global curse1woodensword
                global curse1woodendagger
                global curse2catsword
                global curse2coppersword
                global curse2woodensword
                global curse2woodendagger
                global curse3catsword
                global curse3coppersword
                global curse3woodensword
                global curse3woodendagger
                global sharpness1catsword
                global sharpness1coppersword
                global sharpness1woodensword
                global sharpness1woodendagger
                global sharpness2catsword
                global sharpness2coppersword
                global sharpness2woodensword
                global sharpness2woodendagger
                global sharpness3catsword
                global sharpness3coppersword
                global sharpness3woodensword
                global sharpness3woodendagger
                global isenchanted
                isenchanted='No'
                if equippedweapon=='Wooden dagger':
                    if sharp1==1:
                        sharpness1woodendagger=sharpness1woodendagger+1
                        isenchanted='Yes'
                    if sharp2==1:
                        sharpness2woodendagger=sharpness2woodendagger+1
                        isenchanted='Yes'
                    if sharp3==1:
                        sharpness3woodendagger=sharpness3woodendagger+1
                        isenchanted='Yes'
                    if block1w==1:
                        blocking1woodendagger=blocking1woodendagger+1
                        isenchanted='Yes'
                    if block2w==1:
                        blocking2woodendagger=blocking2woodendagger+1
                        isenchanted='Yes'
                    if block3w==1:
                        blocking3woodendagger=blocking3woodendagger+1
                        isenchanted='Yes'
                    if loot1==1:
                        looting1woodendagger=looting1woodendagger+1
                        isenchanted='Yes'
                    if loot2==1:
                        looting2woodendagger=looting2woodendagger+1
                        isenchanted='Yes'
                    if loot3==1:
                        looting3woodendagger=looting3woodendagger+1
                        isenchanted='Yes'
                    if curse1==1:
                        curse1woodendagger=curse1woodendagger+1
                        isenchanted='Yes'
                    if curse2==1:
                        curse2woodendagger=curse2woodendagger+1
                        isenchanted='Yes'
                    if curse3==1:
                        curse3woodendagger=curse3woodendagger+1
                        isenchanted='Yes'
                    if isenchanted=='No':
                        woodendaggeramount=woodendaggeramount+1
                    printR('Wooden dagger unequipped')
                    print("")
                if equippedweapon=='Wooden sword':
                    if sharp1==1:
                        sharpness1woodensword=sharpness1woodensword+1
                        isenchanted='Yes'
                    if sharp2==1:
                        sharpness2woodensword=sharpness2woodensword+1
                        isenchanted='Yes'
                    if sharp3==1:
                        sharpness3woodensword=sharpness3woodensword+1
                        isenchanted='Yes'
                    if block1w==1:
                        blocking1woodensword=blocking1woodensword+1
                        isenchanted='Yes'
                    if block2w==1:
                        blocking2woodensword=blocking2woodensword+1
                        isenchanted='Yes'
                    if block3w==1:
                        blocking3woodensword=blocking3woodensword+1
                        isenchanted='Yes'
                    if loot1==1:
                        looting1woodensword=looting1woodensword+1
                        isenchanted='Yes'
                    if loot2==1:
                        looting2woodensword=looting2woodensword+1
                        isenchanted='Yes'
                    if loot3==1:
                        looting3woodensword=looting3woodensword+1
                        isenchanted='Yes'
                    if curse1==1:
                        curse1woodensword=curse1woodensword+1
                        isenchanted='Yes'
                    if curse2==1:
                        curse2woodensword=curse2woodensword+1
                        isenchanted='Yes'
                    if curse3==1:
                        curse3woodensword=curse3woodensword+1
                        isenchanted='Yes'
                    if isenchanted=='No':
                        woodenswordamount=woodenswordamount+1
                    printR('Wooden sword unequipped')
                    print('')
                if equippedweapon=='Copper sword':
                    if sharp1==1:
                        sharpness1coppersword=sharpness1coppersword+1
                        isenchanted='Yes'
                    if sharp2==1:
                        sharpness2coppersword=sharpness2coppersword+1
                        isenchanted='Yes'
                    if sharp3==1:
                        sharpness3coppersword=sharpness3coppersword+1
                        isenchanted='Yes'
                    if block1w==1:
                        blocking1coppersword=blocking1coppersword+1
                        isenchanted='Yes'
                    if block2w==1:
                        blocking2coppersword=blocking2coppersword+1
                        isenchanted='Yes'
                    if block3w==1:
                        blocking3coppersword=blocking3coppersword+1
                        isenchanted='Yes'
                    if loot1==1:
                        looting1coppersword=looting1coppersword+1
                        isenchanted='Yes'
                    if loot2==1:
                        looting2coppersword=looting2coppersword+1
                        isenchanted='Yes'
                    if loot3==1:
                        looting3coppersword=looting3coppersword+1
                        isenchanted='Yes'
                    if curse1==1:
                        curse1coppersword=curse1coppersword+1
                        isenchanted='Yes'
                    if curse2==1:
                        curse2coppersword=curse2coppersword+1
                        isenchanted='Yes'
                    if curse3==1:
                        curse3coppersword=curse3coppersword+1
                        isenchanted='Yes'
                    if isenchanted=='No':
                        copperswordamount=copperswordamount+1
                    printR('Copper sword unequipped')
                    print('')
                if equippedweapon=='Maxwell sword':
                    if sharp1==1:
                        sharpness1catsword=sharpness1catsword+1
                        isenchanted='Yes'
                    if sharp2==1:
                        sharpness2catsword=sharpness2catsword+1
                        isenchanted='Yes'
                    if sharp3==1:
                        sharpness3catsword=sharpness3catsword+1
                        isenchanted='Yes'
                    if block1w==1:
                        blocking1catsword=blocking1catsword+1
                        isenchanted='Yes'
                    if block2w==1:
                        blocking2catsword=blocking2catsword+1
                        isenchanted='Yes'
                    if block3w==1:
                        blocking3catsword=blocking3catsword+1
                        isenchanted='Yes'
                    if loot1==1:
                        looting1catsword=looting1catsword+1
                        isenchanted='Yes'
                    if loot2==1:
                        looting2catsword=looting2catsword+1
                        isenchanted='Yes'
                    if loot3==1:
                        looting3catsword=looting3catsword+1
                        isenchanted='Yes'
                    if curse1==1:
                        curse1catsword=curse1catsword+1
                        isenchanted='Yes'
                    if curse2==1:
                        curse2catsword=curse2catsword+1
                        isenchanted='Yes'
                    if curse3==1:
                        curse3catsword=curse3catsword+1
                        isenchanted='Yes'
                    if isenchanted=='No':
                        catswordamount=catswordamount+1
                    printR('Maxwell sword unequipped')
                    print('')
                else:
                    print('')
                enchantcheckweapon()

def armor_equip():
                global equippedarmor
                global leatherarmoramount
                global catarmoramount
                global copperarmoramount
                global block1a
                global block2a
                global block3a
                global res1
                global res2
                global res3
                global curse1a
                global curse2a
                global curse3a
                global blocking1catarmor
                global blocking1leatherarmor
                global blocking1copperarmor
                global blocking2copperarmor
                global blocking2catarmor
                global blocking2leatherarmor
                global blocking3copperarmor
                global blocking3catarmor
                global blocking3leatherarmor
                global resistance1catarmor
                global resistance1leatherarmor
                global resistance1copperarmor
                global resistance2catarmor
                global resistance2leatherarmor
                global resistance2copperarmor
                global resistance3catarmor
                global resistance3leatherarmor
                global resistance3copperarmor
                global curse1leatherarmor
                global curse1copperarmor
                global curse1catarmor
                global curse2leatherarmor
                global curse2copperarmor
                global curse2catarmor
                global curse3leatherarmor
                global curse3copperarmor
                global curse3catarmor
                global isenchanted
                isenchanted='No'
                if equippedarmor=='Leather armor':
                    if block1a==1:
                        blocking1leatherarmor=blocking1leatherarmor+1
                        isenchanted='Yes'
                    if block2a==1:
                        blocking2leatherarmor=blocking2leatherarmor+1    
                        isenchanted='Yes'
                    if block3a==1:
                        blocking3leatherarmor=blocking3leatherarmor+1
                        isenchanted='Yes'
                    if curse1a==1:
                        curse1leatherarmor=curse1leatherarmor+1
                        isenchanted='Yes'
                    if curse2a==1:
                        curse2leatherarmor=curse2leatherarmor+1
                        isenchanted='Yes'
                    if curse3a==1:
                        curse3leatherarmor=curse3leatherarmor+1
                        isenchanted='Yes'
                    if res1==1:
                        resistance1leatherarmor=resistance1leatherarmor+1
                        isenchanted='Yes'
                    if res2==1:
                        resistance2leatherarmor=resistance2leatherarmor+1
                        isenchanted='Yes'
                    if res3==1:
                        resistance3leatherarmor=resistance3leatherarmor+1
                        isenchanted='Yes'
                    if isenchanted=='No':
                        leatherarmoramount=leatherarmoramount+1
                    printR('Leather armor unequipped')
                    print("")
                if equippedarmor=='Copper armor':
                    if block1a==1:
                        blocking1copperarmor=blocking1copperarmor+1
                        isenchanted='Yes'
                    if block2a==1:
                        blocking2copperarmor=blocking2copperarmor+1   
                        isenchanted='Yes' 
                    if block3a==1:
                        blocking3copperarmor=blocking3copperarmor+1
                        isenchanted='Yes'
                    if curse1a==1:
                        curse1copperarmor=curse1copperarmor+1
                        isenchanted='Yes'
                    if curse2a==1:
                        curse2copperarmor=curse2copperarmor+1
                        isenchanted='Yes'
                    if curse3a==1:
                        curse3copperarmor=curse3copperarmor+1
                        isenchanted='Yes'
                    if res1==1:
                        resistance1copperarmor=resistance1copperarmor+1
                        isenchanted='Yes'
                    if res2==1:
                        resistance2copperarmor=resistance2copperarmor+1
                        isenchanted='Yes'
                    if res3==1:
                        resistance3copperarmor=resistance3copperarmor+1
                        isenchanted='Yes'
                    if isenchanted=='No':
                        copperarmoramount=copperarmoramount+1
                    printR('Copper armor unequipped')
                    print('')
                if equippedarmor=='Maxwell armor':
                    if block1a==1:
                        blocking1catarmor=blocking1catarmor+1
                        isenchanted='Yes'
                    if block2a==1:
                        blocking2catarmor=blocking2catarmor+1    
                        isenchanted='Yes'
                    if block3a==1:
                        blocking3catarmor=blocking3catarmor+1
                        isenchanted='Yes'
                    if curse1a==1:
                        curse1catarmor=curse1catarmor+1
                        isenchanted='Yes'
                    if curse2a==1:
                        curse2catarmor=curse2catarmor+1
                        isenchanted='Yes'
                    if curse3a==1:
                        curse3catarmor=curse3catarmor+1
                        isenchanted='Yes'
                    if res1==1:
                        resistance1catarmor=resistance1catarmor+1
                        isenchanted='Yes'
                    if res2==1:
                        resistance2catarmor=resistance2catarmor+1
                        isenchanted='Yes'
                    if res3==1:
                        resistance3catarmor=resistance3catarmor+1
                        isenchanted='Yes'
                    if isenchanted=='No':
                        catarmoramount=catarmoramount+1
                    printR('Maxwell armor unequipped')
                    print('')
                else:
                    print('')
                enchantcheckarmor()

def maxhp_modifier():
                global type
                global maxhp
                global perfecthealth
                if type=='Swordsman':
                    maxhp=maxhp*0.85
                if type=='Trader' or type=='Wizard':
                    maxhp=maxhp*0.7
                if type=='Warrior':
                    maxhp=maxhp*1.25
                if perfecthealth==1:
                    maxhp=maxhp*1.1
                if perfecthealth==2:
                    maxhp=maxhp*1.2
                if perfecthealth==3:
                    maxhp=maxhp*1.3

def power_modifier():
                global type
                global power
                if type=='Healer':
                    power=power*0.8

def buy(price,item,itemid):
            global treasury
            global x
            global doing4
            global progress
            if treasury>price:
                price=price+0.01
                print('')
                printG('Purchase succesfull')
                print('+ 1',itemid,'(',item+1,')')
                print('-',price,'gold (',treasury-price,')')
                treasury=treasury-price
                x=item
                x=x+1
                print('')
                if doing4=='Yes':
                    progress=progress+1
            else:
                print('')
                printR('Purchase insuccesfull')
                print('Not enough gold for purchase')
                print('')

def sell(price,item,itemid):
            global treasury
            global x
            global doing3
            global progress
            if item>0:
                print('')
                printG('Sell succesfull')
                print('- 1',itemid,'(',item-1,')')
                print('+',price,'gold (',treasury+price,')')
                treasury=treasury+price
                x=item
                x=x-1
                print('')
                if doing3=='Yes':
                    progress=progress+1
            else:
                print('')
                printR('Sell insuccesfull')
                print('You do not have a',itemid,'')
                print('')

def enemyencounter(enemyname,emaxhp,ehp,lowxp,a,b,c,d):
    global enemylvl
    global enemymaxhp
    global enemyhp
    global battle
    global xp
    global enemyname2
    print('')
    enemymaxhp=emaxhp
    if xp<lowxp:
        enemylvl=random.randint(a,b)
    else:
        enemylvl=random.randint(c,d)
    enemymaxhp=((enemylvl/10)*enemymaxhp)+enemymaxhp
    enemyhp=enemymaxhp
    enemyname2=enemyname
    print('LVL',enemylvl,enemyname,'encounter:')
    print('Enemy HP:',enemyhp,'')
    battle=input('1=Run, 2=Fight')

def skilllearn(learnedlevel,skillname,learnedlevelname,skillpointcost):
    global skillpoint

    global l

    global focus
    global vampire
    global advancedlooting
    global healing

    global laststand
    global learning
    global shield
    global tearingdive

    global stealing
    global moneyrain
    global fastlearner

    global stunning
    global weaken
    global sabotage

    global tearing
    global downfall
    global finish
    global finishchance

    global doing10
    global progress

    if skillpoint>skillpointcost-1:
        print('')
        print('',skillname,learnedlevelname,'skill learned')
        print('')
        l=learnedlevel
        skillpoint=skillpoint-skillpointcost
        if doing10=='Yes':
            progress=progress+1
    else:
        print('')
        print('Not enough skill points :c')
        print('')

def enchantxp():
                global enchantmentscroll
                global type
                global xp
                global xpgain
                if enchantmentscroll>0:
                    print('Enchantment scroll used')
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

def enchantcheckweapon():
    global sharp1
    global sharp2
    global sharp3
    global curse1
    global curse2
    global curse3
    global loot1
    global loot2
    global loot3
    global block1w
    global block2w
    global block3w
    if sharp1==1:
        sharp1=0
    if sharp2==1:
        sharp2=0
    if sharp3==1:
        sharp3=0
    if curse1==1:
        curse1=0
    if curse2==1:
        curse2=0
    if curse3==1:
        curse3=0
    if loot1==1:
        loot1=0
    if loot2==1:
        loot2=0
    if loot3==1:
        loot3=0
    if block1w==1:
        block1w=0
    if block2w==1:
        block2w=0
    if block3w==1:
        block3w=0

def enchantcheckarmor():
    global block1a
    global block2a
    global block3a
    global curse1a
    global curse2a
    global curse3a
    global res1
    global res2
    global res3
    if block1a==1:
        block1a=0
    if block2a==1:
        block2a=0
    if block3a==1:
        block3a=0
    if curse1a==1:
        curse1a=0
    if curse2a==1:
        curse2a=0
    if curse3a==1:
        curse3a=0
    if res1==1:
        res1=0
    if res2==1:
        res2=0
    if res3==1:
        res3=0

def leatherarmorequip():
                global maxhp
                global equippedarmor
                global leatherarmoramount
                global armorresistance
                printG('Leather armor equipped')
                maxhp=20
                armor_equip()
                equippedarmor='Leather armor'
                armorresistance=1
                maxhp_modifier()

def woodendaggerequip():
                global power
                global equippedweapon
                global woodendaggeramount
                printG('Wooden dagger equipped')
                power=1.3
                weapon_equip()
                equippedweapon='Wooden dagger'
                power_modifier()

def catarmorequip():
                global maxhp
                global equippedarmor
                global leatherarmoramount
                global armorresistance
                printG('Maxwell armor equipped')
                maxhp=35
                armorresistance=3
                armor_equip()
                equippedarmor='Maxwell armor'
                maxhp_modifier()

def copperarmorequip():
                global maxhp
                global equippedarmor
                global leatherarmoramount
                global armorresistance
                printG('Copper armor equipped')
                maxhp=25
                armorresistance=2
                armor_equip()
                equippedarmor='Copper armor'
                maxhp_modifier()

def woodenswordequip():
                global power
                global equippedweapon
                global woodenswordamount
                printG('Wooden sword equipped')
                power=1.5
                weapon_equip()
                equippedweapon='Wooden sword'
                power_modifier()

def copperswordequip():
                global power
                global equippedweapon
                global woodendaggeramount
                printG('Copper sword equipped')
                power=1.7
                weapon_equip()
                equippedweapon='Copper sword'
                power_modifier()

def catswordequip():
                global power
                global equippedweapon
                global woodendaggeramount
                printG('Maxwell sword equipped')
                power=2
                weapon_equip()
                equippedweapon='Maxwell sword'
                power_modifier()

def deathmessage():
                            global score
                            global value
                            global enemieskilled
                            global name
                            global enemyname2
                            enemieskilled=enemieskilled-1
                            printR('You do not have a revive potion, the game is over :c')
                            print('')
                            print(name,'was slained by',enemyname2)
                            print('')
                            if score>3499:
                                print('Score:',score,'-', end='')
                                printY('Legendary!!!')
                            if score>2499 and score<3500:
                                print('Score:',score,'-', end='')
                                printP('Epic!!')
                            if score>1499 and score<2500:
                                print('Score:',score,'-', end='')
                                printB('Good!')
                            else:
                                print('Score:',score,'-', end='')
                                print(' Bad')
                            if value>249:
                                print('Value:',value,'-', end='')
                                printY('Legendary!!!')
                            if value>174 and value<250:
                                print('Value:',value,'-', end='')
                                printP('Epic!!')
                            if value>99 and value<175:
                                print('Value:',value,'-', end='')
                                printB('Good!')
                            else:
                                print('Value:',value,'-', end='')
                                print(' Bad')
                            print('Enemies killed:',enemieskilled)
                            print('')

def questreward(rewardtype,questquality,rewardamount,reward):
    global rewardtype1
    global rewardtype2
    global rewardtype3
    global questquality1
    global questquality2
    global questquality3
    global rewardamount1
    global rewardamount2
    global rewardamount3
    global reward1
    global reward2
    global reward3
    global rewt
    global quality
    global rewa
    global rew
    if questquality=='Low':
        rewt=random.randint(1,9)
        if rewt==1:
            rewt='Health potion'
            rewa=random.randint(1,3)
            if rewa==1:
                rew='1 × Health potion'
            if rewa==2:
                rew='2 × Health potion'
            if rewa==3:
                rew='3 × Health potion'
        if rewt==2:
            rewt='Strength potion'
            rewa=random.randint(1,2)
            if rewa==1:
                rew='1 × Strength potion'
            if rewa==2:
                rew='2 × Strength potion'
        if rewt==3:
            rewt='Resistance potion'
            rewa=random.randint(1,2)
            if rewa==1:
                rewa='1 × Resistance potion'
            if rewa==2:
                rewa='2 × Resistance potion'
        if rewt==4:
            rewt='Stamina potion'
            rewa=random.randint(1,2)
            if rewa==1:
                rew='1 × Stamina potion'
            if rewa==2:
                rew='2 × Stamina potion'
        if rewt==5:
            rewt='Leather armor'
            rewa=1
            if rewa==1:
                rew='1 × Leather armor'
        if rewt==6:
            rewt='Wooden dagger'
            rewa=1
            if rewa==1:
                rew='1 × Wooden dagger'
        if rewt==7:
            rewt='Wooden sword'
            rewa=1
            if rewa==1:
                rew='1 × Wooden sword'
        if rewt==8:
            rewt='Score'
            rewa=random.randint(1,2)
            if rewa==1:
                rew='250 × Score'
                rewa=250
            if rewa==2:
                rew='500 × Score'
                rewa=500
        if rewt==9:
            rewt='Gold'
            rewa=random.randint(3,10)
            if rewa==3:
                rew='3 × Gold'
            if rewa==4:
                rew='4 × Gold'
            if rewa==5:
                rew='5 × Gold'
            if rewa==6:
                rew='6 × Gold'
            if rewa==7:
                rew='7 × Gold'
            if rewa==8:
                rew='8 × Gold'
            if rewa==9:
                rew='9 × Gold'
            if rewa==10:
                rew='10 × Gold'
    if questquality=='High':
        rewt=random.randint(1,9)
        if rewt==1:
            rewt='Health potion'
            rewa=random.randint(4,6)
            if rewa==4:
                rew='4 × Health potion'
            if rewa==5:
                rew='5 × Health potion'
            if rewa==6:
                rew='6 × Health potion'
        if rewt==2:
            rewt='Strength potion'
            rewa=random.randint(3,4)
            if rewa==3:
                rew='3 × Strength potion'
            if rewa==4:
                rew='4 × Strength potion'
        if rewt==3:
            rewt='Resistance potion'
            rewa=random.randint(3,4)
            if rewa==3:
                rew='3 × Resistance potion'
            if rewa==4:
                rew='4 × Resistance potion'
        if rewt==4:
            rewt='Stamina potion'
            rewa=random.randint(3,4)
            if rewa==3:
                rew='3 × Stamina potion'
            if rewa==4:
                rew='4 × Stamina potion'
        if rewt==5:
            rewt='Copper armor'
            rewa=1
            if rewa==1:
                rew='1 × Copper armor'
        if rewt==6:
            rewt='Copper sword'
            rewa=1
            if rewa==1:
                rew='1 × Copper sword'
        if rewt==7:
            rewt='Enchantment scroll'
            rewa=1
            if rewa==1:
                rew='1 × Enchantment scroll'
        if rewt==8:
            rewt='Score'
            rewa=random.randint(1,2)
            if rewa==1:
                rew='750 × Score'
                rewa=750
            if rewa==2:
                rew='1000 × Score'
                rewa=1000
        if rewt==9:
            rewt='Gold'
            rewa=random.randint(10,20)
            if rewa==10:
                rew='10 × Gold'
            if rewa==11:
                rew='11 × Gold'
            if rewa==12:
                rew='12 × Gold'
            if rewa==13:
                rew='13 × Gold'
            if rewa==14:
                rew='14 × Gold'
            if rewa==15:
                rew='15 × Gold'
            if rewa==16:
                rew='16 × Gold'
            if rewa==17:
                rew='17 × Gold'
            if rewa==18:
                rew='18 × Gold'
            if rewa==19:
                rew='19 × Gold'
            if rewa==20:
                rew='20 × Gold'

def quest(quest,number,questtype,lvlofenchant):
    global progress
    global number1
    global number2
    global number3
    global questtype1
    global questtype2
    global questtype3
    global inprogress1
    global inprogress2
    global inprogress3
    global quest1
    global quest2
    global quest3
    global rewardamount1
    global rewardamount2
    global rewardamount3
    global rewardtype1
    global rewardtype2
    global rewardtype3
    global questquality1
    global questquality2
    global questquality3
    global reward1
    global reward2
    global reward3
    global rewt
    global quality
    global rewa
    global rew
    global num
    global qt
    global lvlofenchant1
    global lvlofenchant2
    global lvlofenchant3
    if quest==1:
        num=random.randint(3,10)
        if num>5:
            quality='High'
        else:
            quality='Low'
    if quest==2:
        num=1
        quality='Low'
    if quest==3:
        num=random.randint(1,3)
        quality='Low'
    if quest==4:
        num=random.randint(1,5)
        quality='Low'
    if quest==5:
        num=random.randint(3,10)
        quality='Low'
    if quest==6:
        num=random.randint(1,3)
        qt=random.randint(1,4)
        if qt==1:
            quality='Low'
            qt='Wolf'
        if qt==2:
            quality='Low'
            qt='Bear'
        if qt==3:
            quality='High'
            qt='Bandit'
        if qt==4:
            quality='High'
            qt='Slime'
    if quest==7:
            num=random.randint(1,3)
            if num==1:
                num=50
                quality='Low'
            if num==2:
                num=100
                quality='High'
            if num==3:
                num=150
                quality='High'
    if quest==8:
            num=random.randint(1,3)
            if num==1:
                num=1000
                quality='Low'
            if num==2:
                num=1500
                quality='High'
            if num==3:
                num=2000
                quality='High'
    if quest==9:
            num=random.randint(1,2)
            if num==1:
                num=1
                lvlofenchant=2
                quality='High'
            if num==2:
                num=1
                lvlofenchant=3
                quality='High'
    if quest==10:
            num=random.randint(1,3)
            if num==1:
                quality='Low'
            if num==2:
                quality='Low'
            if num==3:
                quality='High'
    if quest==11:
        num=1
        qt=random.randint(1,5)
        if qt==1:
            quality='Low'
            qt='Leather armor'
        if qt==2:
            quality='Low'
            qt='Wooden dagger'
        if qt==3:
            quality='High'
            qt='Copper armor'
        if qt==4:
            quality='High'
            qt='Copper sword'
        if qt==5:
            quality='Low'
            qt='Wooden sword'
    if quest==12:
        num=random.randint(5,15)
        if num>9:
            quality='High'
        else:
            quality='Low'
    if quest==13:
        num=random.randint(5,15)
        quality='Low'

def questprint(quest,inprogress,reward,questnumber,number,questtype,lvlofenchant):
    global quest1
    global quest2
    global quest3
    global inprogress1
    global inprogress2
    global inprogress3
    global reward1
    global reward2
    global reward3
    global number1
    global number2
    global number3
    global questtype1
    global questtype2
    global questtype3
    global lvlofenchant1
    global lvlofenchant2
    global lvlofenchant3
    print('')
    print('(',questnumber,') Quest')
    if quest==1:
        print('Kill',number,'× enemies')
    if quest==2:
        print('Enchant an equipment')
    if quest==3:
        print('Sell',number,'× items')
    if quest==4:
       print('Buy',number,'× items')
    if quest==5:
       print('Gamble',number,'× times')
    if quest==6:
       print('Kill',number,'×',questtype)
    if quest==7:
       print('Reach',number,'value')
    if quest==8:
       print('Reach',number,'score')
    if quest==9:
       print('Get a level',lvlofenchant,'enchantment or higher')
    if quest==10:
       print('Use skillpoints',number,'× times')
    if quest==11:
       print('Get a',questtype)
    if quest==12:
       print('Deal',number,'× critical hits')
    if quest==13:
       print('Block',number,'× times')
    print('Reward:',reward)
    if inprogress=='Yes':
        print('Progress:',progress,'/',number)
    print('')

def questselect(quest):
    global quest1
    global quest2
    global quest3
    global doing1
    global doing2
    global doing3
    global doing4
    global doing5
    global doing6
    global doing7
    global doing8
    global doing9
    global doing10
    global doing11
    global doing12
    global doing13
    if quest==1:
        doing1='Yes'
    if quest==3:
        doing3='Yes'
    if quest==4:
        doing4='Yes'
    if quest==5:
        doing5='Yes'
    if quest==6:
        doing6='Yes'
    if quest==7:
        doing7='Yes'
    if quest==8:
        doing8='Yes'
    if quest==9:
        doing9='Yes'
    if quest==2:
        doing2='Yes'
    if quest==10:
        doing10='Yes'
    if quest==11:
        doing11='Yes'
    if quest==12:
        doing12='Yes'
    if quest==13:
        doing13='Yes'

def questcompletion(reward,rewardamount,rewardtype,inprogress,questquality,lvlofenchant):
    global quest1
    global quest2
    global quest3
    global doing1
    global doing2
    global doing3
    global doing4
    global doing5
    global doing6
    global doing7
    global doing8
    global doing9
    global doing10
    global doing11
    global doing12
    global doing13
    global inprogress1
    global inprogress2
    global inprogress3
    global reward1
    global reward2
    global reward3
    global number1
    global number2
    global number3
    global questtype1
    global questtype2
    global questtype3
    global leatherarmoramount
    global copperarmoramount
    global staminapotionamount
    global strengthpotionamount
    global resistancepotionamount
    global healthpotionamount
    global revivepotionamount
    global woodendaggeramount
    global woodenswordamount
    global copperswordamount
    global enchantmentscroll
    global score
    global value
    global progress
    global treasury
    global rewardamount1
    global rewardamount2
    global rewardamount3
    global questquality1
    global questquality2
    global questquality3
    global reward1
    global reward2
    global reward3
    global rewardtype1
    global rewardtype2
    global rewardtype3
    global inprogress1
    global inprogress2
    global inprogress3
    global lvlofenchant1
    global lvlofenchant2
    global lvlofenchant3
    print('')
    printG('Quest completed')
    time.sleep(2)
    print('Reward:', end='')
    printY(reward)
    print('')
    if questquality=='Low':
                if rewardtype=='Health potion':
                    healthpotionamount=healthpotionamount+rewardamount
                if rewardtype=='Strength potion':
                    strengthpotionamount=strengthpotionamount+rewardamount
                if rewardtype=='Resistance potion':
                    resistancepotionamount=resistancepotionamount+rewardamount
                if rewardtype=='Stamina potion':
                    staminapotionamount=staminapotionamount+rewardamount
                if rewardtype=='Leather armor':
                    leatherarmoramount=leatherarmoramount+rewardamount
                if rewardtype=='Wooden dagger':
                    woodendaggeramount=woodendaggeramount+rewardamount
                if rewardtype=='Wooden sword':
                    woodenswordamount=woodenswordamount+rewardamount
                if rewardtype=='Score':
                    score=score+rewardamount
                if rewardtype=='Gold':
                    treasury=treasury+rewardamount
    if questquality=='High':
                if rewardtype=='Health potion':
                    healthpotionamount=healthpotionamount+rewardamount
                if rewardtype=='Strength potion':
                    strengthpotionamount=strengthpotionamount+rewardamount
                if rewardtype=='Resistance potion':
                    resistancepotionamount=resistancepotionamount+rewardamount
                if rewardtype=='Stamina potion':
                    staminapotionamount=staminapotionamount+rewardamount
                if rewardtype=='Copper armor':
                    copperarmoramount=copperarmoramount+rewardamount
                if rewardtype=='Copper sword':
                    copperswordamount=copperswordamount+rewardamount
                if rewardtype=='Enchantment':
                    enchantmentscroll=enchantmentscroll+rewardamount
                if rewardtype=='Score':
                    score=score+rewardamount
                if rewardtype=='Gold':
                    treasury=treasury+rewardamount
    lvlofenchant=5
    doing1='No'
    doing2='No'
    doing3='No'
    doing4='No'
    doing5='No'
    doing6='No'
    doing7='No'
    doing8='No'
    doing9='No'
    doing10='No'
    doing11='No'
    doing12='No'
    doing13='No'
    if inprogress1=='Yes':
        quest(quest1,number1,questtype1,lvlofenchant1)
        number1=num
        questtype1=qt
        questquality1=quality
        questreward(rewardtype1,questquality1,rewardamount1,reward1)
        rewardtype1=rewt
        rewardamount1=rewa
        reward1=rew
    if inprogress2=='Yes':
        quest(quest2,number2,questtype2,lvlofenchant2)
        number2=num
        questtype2=qt
        questquality2=quality
        questreward(rewardtype2,questquality2,rewardamount2,reward2)
        rewardtype2=rewt
        rewardamount2=rewa
        reward2=rew
    if inprogress3=='Yes':
        quest(quest3,number3,questtype3,lvlofenchant3)
        number3=num
        questtype3=qt
        questquality3=quality
        questreward(rewardtype3,questquality3,rewardamount3,reward3)
        rewardtype3=rewt
        rewardamount3=rewa
        reward3=rew
    inprogress1=='No'
    inprogress2=='No'
    inprogress3=='No'
    progress=0
    while True:
        if quest1==quest2 or quest1==quest3:
            quest1=random.randint(1,13)
            continue
        else:
            break
    time.sleep(3)

#-----------------------Print-----------------------#

def printR(skk): print("\033[91m {}\033[00m" .format(skk))
def printG(skk): print("\033[92m {}\033[00m" .format(skk))
def printB(skk): print("\033[96m {}\033[00m" .format(skk))
def printY(skk): print("\033[93m {}\033[00m" .format(skk))
def printP(skk): print("\033[95m {}\033[00m" .format(skk))

def printBLACK(skk): print("\033[98m {}\033[00m" .format(skk))
def printGRAY(skk): print("\033[97m {}\033[00m" .format(skk))

printY('The beginning, always press enter to continue.\n')
time.sleep(1)
#-----------------------Stats-----------------------#

xp=0
treasury=0
maxhp=15
hp=15
power=1
hploss=0
strength=hp*power
armorresistance=0

equippedweapon=''
equippedarmor=''

skillpoint=3

enemieskilled=0
value=0
valuegain=0
score=0

name=0

#-----------------------Potions-----------------------#

revivepotionamount=0
healthpotionamount=0
resistancepotionamount=0
strengthpotionamount=0
staminapotionamount=0

#-----------------------Armors-----------------------#

leatherarmoramount=0
copperarmoramount=0
catarmoramount=0

#-----------------------Weapons-----------------------#

woodendaggeramount=0
woodenswordamount=0
catswordamount=0
copperswordamount=0

#-----------------------Enchants-----------------------#

weaponenchant=''
armorenchant=''

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
curse1a=0
curse2a=0
curse3a=0
res1=0
res2=0
res3=0

sharpness1woodendagger=0
sharpness2woodendagger=0
sharpness3woodendagger=0
looting1woodendagger=0
looting2woodendagger=0
looting3woodendagger=0
curse1woodendagger=0
curse2woodendagger=0
curse3woodendagger=0
blocking1woodendagger=0
blocking2woodendagger=0
blocking3woodendagger=0

sharpness1woodensword=0
sharpness2woodensword=0
sharpness3woodensword=0
looting1woodensword=0
looting2woodensword=0
looting3woodensword=0
curse1woodensword=0
curse2woodensword=0
curse3woodensword=0
blocking1woodensword=0
blocking2woodensword=0
blocking3woodensword=0

sharpness1coppersword=0
sharpness2coppersword=0
sharpness3coppersword=0
looting1coppersword=0
looting2coppersword=0
looting3coppersword=0
curse1coppersword=0
curse2coppersword=0
curse3coppersword=0
blocking1coppersword=0
blocking2coppersword=0
blocking3coppersword=0

sharpness1catsword=0
sharpness2catsword=0
sharpness3catsword=0
looting1catsword=0
looting2catsword=0
looting3catsword=0
curse1catsword=0
curse2catsword=0
curse3catsword=0
blocking1catsword=0
blocking2catsword=0
blocking3catsword=0

resistance1leatherarmor=0
resistance2leatherarmor=0
resistance3leatherarmor=0
blocking1leatherarmor=0
blocking2leatherarmor=0
blocking3leatherarmor=0
curse1leatherarmor=0
curse2leatherarmor=0
curse3leatherarmor=0

resistance1copperarmor=0
resistance2copperarmor=0
resistance3copperarmor=0
blocking1copperarmor=0
blocking2copperarmor=0
blocking3copperarmor=0
curse1copperarmor=0
curse2copperarmor=0
curse3copperarmor=0

resistance1catarmor=0
resistance2catarmor=0
resistance3catarmor=0
blocking1catarmor=0
blocking2catarmor=0
blocking3catarmor=0
curse1catarmor=0
curse2catarmor=0
curse3catarmor=0

enchantmentscroll=0
magneticstone=0

#-----------------------Special-----------------------#

point=300

x=0

stamina=100
block=100
blocktype='High'
staminatype='High'
blockchance=100
movement='1'
staminaloss=0
staminaplus=0
blockloss=0
blockplus=0

enemystamina=100
enemyblock=100
enemyblockchance=100
enemymovement=1
enemystaminaloss=0
enemystaminaplus=0
enemyblockloss=0
enemyblockplus=0

strengthuse=0
resistanceuse=0

enemylvl=0
a=0
b=0

l=0

isenchanted=''

weaponvarmor=0

enemyname2=0

enchantlevel=0

potions=0

#-----------------------Quests-----------------------#

questz1=''
questz2=''
questz3=''

quest1=0
quest2=0
quest3=0

quest1=random.randint(1,13)
quest2=random.randint(1,13)
quest3=random.randint(1,13)

while True:
    if quest1==quest2 or quest1==quest3:
        quest1=random.randint(1,13)
    if quest2==quest1 or quest2==quest3:
        quest2=random.randint(1,13)
    if quest3==quest2 or quest3==quest1:
        quest3=random.randint(1,13)
    if quest1==quest2 or quest1==quest3 or quest2==quest3:
        continue
    else:
        break

progress=0
startedquestnumber=0
number1=0
number2=0
number3=0
num=0
questtype1=0
questtype2=0
questtype3=0
qt=0
reward1=''
reward2=''
reward3=''
rew=''
rewardtype1=''
rewardtype2=''
rewardtype3=''
rewt=''
inprogress1='No'
inprogress2='No'
inprogress3='No'
rewardamount1=0
rewardamount2=0
rewardamount3=0
rewa=0
questquality1=''
questquality2=''
questquality3=''
quality=''
lvlofenchant1=5
lvlofenchant2=5
lvlofenchant3=5

quest(quest1,number1,questtype1,lvlofenchant1)
number1=num
questtype1=qt
questquality1=quality
questreward(rewardtype1,questquality1,rewardamount1,reward1)
rewardtype1=rewt
rewardamount1=rewa
reward1=rew

quest(quest2,number2,questtype2,lvlofenchant2)
number2=num
questtype2=qt
questquality2=quality
questreward(rewardtype2,questquality2,rewardamount2,reward2)
rewardtype2=rewt
rewardamount2=rewa
reward2=rew

quest(quest3,number3,questtype3,lvlofenchant3)
number3=num
questtype3=qt
questquality3=quality
questreward(rewardtype3,questquality3,rewardamount3,reward3)
rewardtype3=rewt
rewardamount3=rewa
reward3=rew

questchoice=''

doing1=0
doing2=0
doing3=0
doing4=0
doing5=0
doing6=0
doing7=0
doing8=0
doing9=0
doing10=0
doing11=0
doing12=0
doing13=0

#-----------------------Skills-----------------------#

focus=0
vampire=0
advancedlooting=0
healing=0
turncount=0

laststand=0
learning=0
shield=0
tearingdive=0
tearingdiveskill=0

stealing=0
moneyrain=0
fastlearner=0
critcount=0
business=0

stunning=0
stun=0
weaken=0
sabotage=0
fireaura=0
fireauracrit=0

tearing=0
downfall=0
finish=0
finishchance=0
perfecthealth=0

#-----------------------Name-----------------------#

while True:
    print('')
    printB('Type the name of your character!')
    name=input('')
    if name=='':
        print('')
        printR('Please choose something different')
        continue
    else:
        break

#-----------------------Classes-----------------------#

while True:
    printB('\nChoose a class:')
    print(' 1=Healer: +5 Health potion; -20% power \n 2=Swordsman: +Wooden sword; -15% maxHP \n 3=Trader: +10 gold; -30% maxHP \n 4=Wizard:  +Wooden dagger; enchanting only costs 15 XP; -20% maxHP \n 5=Warrior: +Copper sword; +leather armor; +25% maxHP; -50% gold gain')
    type=input('')
    print('')
    if type=='1':
        healthpotionamount=5
        power=power*0.8
        type='Healer'
        printG('Class selected: Healer')
        break
    if type=='2':
        equippedweapon='Wooden sword'
        maxhp=maxhp*0.85
        hp=maxhp
        type='Swordsman'
        printG('Class selected: Swordsman')
        break
    if type=='3':
        treasury=10
        maxhp=maxhp*0.7
        hp=maxhp
        type='Trader'
        printG('Class selected: Trader')
        break
    if type=='4':
        maxhp=maxhp*0.8
        hp=maxhp
        type='Wizard'
        equippedweapon='Wooden dagger'
        printG('Class selected: Wizard')
        break
    if type=='5':
        maxhp=maxhp*1.25
        hp=maxhp
        equippedarmor='Leather armor'
        equippedweapon='Copper sword'
        type='Warrior'
        printG('Class selected: Warrior')
        break
    else:
        printG('I said choose a class')
        continue

time.sleep(1)

#-----------------------Game-----------------------#

while True:

    if inprogress1=='Yes':
        if doing7=='Yes':
            if value==number1 or value>number1:
                progress=1
    if inprogress2=='Yes':
        if doing7=='Yes':
            if value==number2 or value>number2:
                progress=1
    if inprogress3=='Yes':
        if doing7=='Yes':
            if value==number3 or value>number3:
                progress=1

    if inprogress1=='Yes':
        if doing8=='Yes':
            if score==number1 or score>number1:
                progress=1
    if inprogress2=='Yes':
        if doing8=='Yes':
            if score==number2 or score>number2:
                progress=1
    if inprogress3=='Yes':
        if doing8=='Yes':
            if score==number3 or score>number3:
                progress=1

    value=15

    weaponenchant=''
    armorenchant=''

    if res1==1:
        armorenchant='Resistance I'
    if res2==1:
        armorenchant='Resistance II'
    if res3==1:
        armorenchant='Resistance III'
    if block1a==1:
        armorenchant='Blocking I'
    if block2a==1:
        armorenchant='Blocking II'
    if block3a==1:
        armorenchant='Blocking III'
    if curse1a==1:
        armorenchant='Curse I'
    if curse2a==1:
        armorenchant='Curse II'
    if curse3a==1:
        armorenchant='Curse III'
    if sharp1==1:
        weaponenchant='Sharpness I'
    if sharp2==1:
        weaponenchant='Sharpness II'
    if sharp3==1:
        weaponenchant='Sharpness III'
    if loot1==1:
        weaponenchant='Looting I'
    if loot2==1:
        weaponenchant='Looting II'
    if loot3==1:
        weaponenchant='Looting III'
    if curse1==1:
        weaponenchant='Curse I'
    if curse2==1:
        weaponenchant='Curse II'
    if curse3==1:
        weaponenchant='Curse III'
    if block1w==1:
        weaponenchant='Blocking I'
    if block2w==1:
        weaponenchant='Blocking II'
    if block3w==1:
        weaponenchant='Blocking III'

    if stamina<101 and stamina>79: #--Stamina--#
        staminatype='High'
    if stamina<80 and stamina>39:
        staminatype='Medium'
    if stamina<40:
        staminatype='Low'
    if block<101 and block>79: #--Block--#
        blocktype='High'
    if block<80 and block>39:
        blocktype='Medium'
    if block<40:
        blocktype='Low'

    maxhp=round(maxhp,3)
    if point<21:
        print('')
        if fastlearner==1:
            skillpoint=skillpoint+2
            print('+ 2 Skill point (',skillpoint,')')
            valuegain=valuegain+10
        else:
            skillpoint=skillpoint+1
            print('+ Skill point (',skillpoint,')')
            valuegain=valuegain+5
        print('')
        point=100
    else:
        skillpoint=skillpoint

    power=1
    if equippedweapon=='Wooden dagger':
        power=1.3
        value=value+5
    if equippedweapon=='Wooden sword':
        power=1.5
        value=value+7
    if equippedweapon=='Copper sword':
        power=1.7
        value=value+9
    if equippedweapon=='Maxwell sword':
        power=2
        value=value+11
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

    if equippedarmor=='Leather armor':
        value=value+6
    if equippedarmor=='Copper armor':
        value=value+8
    if equippedarmor=='Maxwell armor':
        value=value+10

    if loot<200:
        value=value+(healthpotionamount*3)
        value=value+(revivepotionamount*10)
        value=value+(resistancepotionamount*6)
        value=value+(strengthpotionamount*6)
        value=value+(staminapotionamount*3)
        value=value+(leatherarmoramount*6)
        value=value+(copperswordamount*8)
        value=value+(catarmoramount*10)
        value=value+(woodendaggeramount*5)
        value=value+(woodenswordamount*7)
        value=value+(copperswordamount*9)
        value=value+(catswordamount*11)
        value=value+(magneticstone*2)
        value=value+(enchantmentscroll*15)
        value=value+(xp*0.5)
        value=value+treasury
        value=value+valuegain

    if doing7=='Yes':
        progress=value
    if doing8=='Yes':
        progress=score

    if inprogress1=='Yes':
        if progress==number1 or progress>number1:
            printG('Quest completed!')
            print('')
    if inprogress2=='Yes':
        if progress==number2 or progress>number2:
            printG('Quest completed!')
            print('')
    if inprogress3=='Yes':
        if progress==number3 or progress>number3:
            printG('Quest completed!')
            print('')


    printB('\nOptions:')
    print(' 1 - Adventure \n 2 - Profile \n 3 - Inventory \n 4 - Shop \n 5 - Help \n 6 - Item list \n 7 - Gamble \n 8 - Enchanting \n 9 - Skills \n 10 - Quests \n')
    choice=input('')

    if choice=='1':
        enemystamina=100
        enemyblock=100
        critcount=0
        turncount=0
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
                print('That is correct, the scientist gives you a enchantment scroll, with which it is free to enchant an item')
                print('')
                enchantmentscroll=enchantmentscroll+1
            else:
                print('You are bad at maths bruh')
                print('')

        if xp<50 or xp==50:
            if 0<chance and chance<50:
                enemyencounter('Wolf',3,3,25,1,5,5,10)
                if battle=='1':
                    hploss=random.randint(0,1)
                    xpgain=random.randint(1,5)
                    run_modifiers()
                    xp=xp+xpgain
                    hp=hp-hploss
                    if hp<0 or hp==0:
                        print('')
                        printR('You died')
                        if laststand==1:
                            if laststandskill=='In use':
                                laststand=laststand
                            else:
                                hp=maxhp*0.2
                                print('Last stand skill in use, HP:',round(hp,3),'')
                                laststandskill='In use'
                                continue
                        if revivepotionamount>0:
                            revivepotionamount=revivepotionamount-1
                            print('Revive potion used (',revivepotionamount,'remaining)')
                            hp=maxhp
                            continue
                        else:
                            deathmessage()
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',round(hploss,3),'HP (',round(hp,3),'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    enemieskilled=enemieskilled+1
                    if doing1=='Yes':
                        progress=progress+1
                    if inprogress1=='Yes':
                        if doing6=='Yes' and questtype1=='Wolf':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing6=='Yes' and questtype2=='Wolf':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing6=='Yes' and questtype3=='Wolf':
                            progress=progress+1
                    score=score+100
                    while True:
                        if enemyhp<0 or enemyhp==0:
                            printG('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        fight()
                        if hp<0 or hp==0:
                            print('')
                            printR('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',round(hp,3),'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                deathmessage()
                                break
                        if enemyhp<0 or enemyhp==0:
                            printG('Fight finished, you won')
                            print('')
                            break
                        else:
                            time.sleep(2)
                            continue
                    if hp<0 or hp==0:
                        break
                    else:
                        xpgain=random.randint(1,8)
                        goldgain=random.randint(0,5)
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        wolf_loot()
                        time.sleep(3)
                        continue
                else:
                    continue
            if 50<chance:
                enemyencounter('Bear',5,5,25,1,5,5,10)  
                if battle=='1':
                    hploss=random.randint(0,2)
                    xpgain=random.randint(1,7)
                    run_modifiers()
                    xp=xp+xpgain
                    hp=hp-hploss
                    if hp<0 or hp==0:
                        print('')
                        printR('You died')
                        if laststand==1:
                            if laststandskill=='In use':
                                laststand=laststand
                            else:
                                hp=maxhp*0.2
                                print('Last stand skill in use, HP:',round(hp,3),'')
                                laststandskill='In use'
                                continue
                        if revivepotionamount>0:
                            revivepotionamount=revivepotionamount-1
                            print('Revive potion used (',revivepotionamount,'remaining)')
                            hp=maxhp
                            continue
                        else:
                            deathmessage()
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',round(hploss,3),'HP (',round(hp,3),'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    enemieskilled=enemieskilled+1
                    if doing1=='Yes':
                        progress=progress+1
                    if inprogress1=='Yes':
                        if doing6=='Yes' and questtype1=='Bear':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing6=='Yes' and questtype2=='Bear':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing6=='Yes' and questtype3=='Bear':
                            progress=progress+1
                    score=score+150
                    while True:
                        if enemyhp<0 or enemyhp==0:
                            printG('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        fight()
                        if hp<0 or hp==0:
                            print('')
                            printR('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',round(hp,3),'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                deathmessage()
                                break
                        if enemyhp<0 or enemyhp==0:
                            printG('Fight finished, you won')
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        bear_loot()
                        continue
                else:
                    continue

            if chance==0:
                gold_box()
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
                if prize==2:
                    revivepotionamount=revivepotionamount+1
                    print('Item box:')
                    print('+ 1 Revive potion (',revivepotionamount,')')
                if prize==3:
                    leatherarmoramount=leatherarmoramount+1
                    print('Item box:')
                    print('+ 1 Leather armor (',leatherarmoramount,')')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Leather armor':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Leather armor':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Leather armor':
                            progress=progress+1
                if prize==4:
                    woodendaggeramount=woodendaggeramount+1
                    print('Item box:')
                    print('+ 1 Wooden dagger (',woodendaggeramount,')')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Wooden dagger':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Wooden dagger':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Wooden dagger':
                            progress=progress+1
                if prize==5:
                    resistancepotionamount=resistancepotionamount+1
                    print('Item box:')
                    print('+ 1 Resistance potion (',resistancepotionamount,')')
                if prize==6:
                    strengthpotionamount=strengthpotionamount+1
                    print('Item box:')
                    print('+ 1 Strength potion (',strengthpotionamount,')')
                print('')
                time.sleep(3)
                continue

            else:
                continue
        
        if xp>50 and xp<101:

            if chance==0:
                gold_box()
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
                if prize==2:
                    revivepotionamount=revivepotionamount+1
                    print('Item box:')
                    print('+ 1 Revive potion (',revivepotionamount,')')
                if prize==3:
                    leatherarmoramount=leatherarmoramount+1
                    print('Item box:')
                    print('+ 1 Leather armor (',leatherarmoramount,')')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Leather armor':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Leather armor':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Leather armor':
                            progress=progress+1
                if prize==4:
                    woodendaggeramount=woodendaggeramount+1
                    print('Item box:')
                    print('+ 1 Wooden dagger (',woodendaggeramount,')')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Wooden dagger':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Wooden dagger':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Wooden dagger':
                            progress=progress+1
                if prize==5:
                    copperarmoramount=copperarmoramount+1
                    print('Item box:')
                    print('+ 1 Copper armor (',copperarmoramount,')')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Copper armor':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Copper armor':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Copper armor':
                            progress=progress+1
                if prize==6:
                    copperswordamount=copperswordamount+1
                    print('Item box:')
                    print('+ 1 Copper sword (',copperswordamount,')')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Copper sword':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Copper sword':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Copper sword':
                            progress=progress+1
                if prize==7:
                    revivepotionamount=revivepotionamount+1
                    print('Item box:')
                    print('+ 1 Revive potion (',revivepotionamount,')')
                if prize==8:
                    resistancepotionamount=resistancepotionamount+1
                    print('Item box:')
                    print('+ 1 Resistance potion (',resistancepotionamount,')')
                if prize==9:
                    strengthpotionamount=strengthpotionamount+1
                    print('Item box:')
                    print('+ 1 Strength potion (',strengthpotionamount,')')
                print('')
                continue
            if 5<chance and chance<50:
                enemyencounter('Bandit',7,7,75,1,5,5,10)
                if battle=='1':
                    hploss=random.randint(0,3)
                    xpgain=random.randint(1,7)
                    run_modifiers()
                    xp=xp+xpgain
                    hp=hp-hploss
                    if hp<0 or hp==0:
                        print('')
                        print('You died')
                        if laststand==1:
                            if laststandskill=='In use':
                                laststand=laststand
                            else:
                                hp=maxhp*0.2
                                print('Last stand skill in use, HP:',round(hp,3),'')
                                laststandskill='In use'
                                continue
                        if revivepotionamount>0:
                            revivepotionamount=revivepotionamount-1
                            print('Revive potion used (',revivepotionamount,'remaining)')
                            hp=maxhp
                            continue
                        else:
                            deathmessage()
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',round(hploss,3),'HP (',round(hp,3),'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    enemieskilled=enemieskilled+1
                    if doing1=='Yes':
                        progress=progress+1
                    if inprogress1=='Yes':
                        if doing6=='Yes' and questtype1=='Bandit':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing6=='Yes' and questtype2=='Bandit':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing6=='Yes' and questtype3=='Bandit':
                            progress=progress+1
                    score=score+400
                    while True:
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,5)
                        fight()
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',round(hp,3),'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                deathmessage()
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        rare_loot()
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
                        if választás=='1':
                            print('')
                            catswordamount=catswordamount+1
                            print('+ Maxwell sword ')
                            print('')
                            continue
                        if választás=='2':
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
                        if választás=='1':
                            print('')
                            catswordamount=catswordamount+1
                            print('+ Maxwell sword ')
                            print('')
                            continue
                        if választás=='2':
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
                enemyencounter('Wolf',3,3,75,10,15,15,20)  
                if battle=='1':
                    hploss=random.randint(0,1)
                    xpgain=random.randint(1,5)
                    run_modifiers()
                    xp=xp+xpgain
                    hp=hp-hploss
                    if hp<0 or hp==0:
                        print('')
                        print('You died')
                        if laststand==1:
                            if laststandskill=='In use':
                                laststand=laststand
                            else:
                                hp=maxhp*0.2
                                print('Last stand skill in use, HP:',round(hp,3),'')
                                laststandskill='In use'
                                continue
                        if revivepotionamount>0:
                            revivepotionamount=revivepotionamount-1
                            print('Revive potion used (',revivepotionamount,'remaining)')
                            hp=maxhp
                            continue
                        else:
                            deathmessage()
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',round(hploss,3),'HP (',round(hp,3),'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    enemieskilled=enemieskilled+1
                    if doing1=='Yes':
                        progress=progress+1
                    if inprogress1=='Yes':
                        if doing6=='Yes' and questtype1=='Wolf':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing6=='Yes' and questtype2=='Wolf':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing6=='Yes' and questtype3=='Wolf':
                            progress=progress+1
                    score=score+200
                    while True:
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        fight()
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',round(hp,3),'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                deathmessage()
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        wolf_loot()
                        continue
                else:
                    continue
            if 90<chance and chance<100:
                enemyencounter('Bear',5,5,75,10,15,15,20)  
                if battle=='1':
                    hploss=random.randint(0,2)
                    xpgain=random.randint(1,7)
                    run_modifiers()
                    xp=xp+xpgain
                    hp=hp-hploss
                    if hp<0 or hp==0:
                        print('')
                        print('You died')
                        if laststand==1:
                            if laststandskill=='In use':
                                laststand=laststand
                            else:
                                hp=maxhp*0.2
                                print('Last stand skill in use, HP:',round(hp,3),'')
                                laststandskill='In use'
                                continue
                        if revivepotionamount>0:
                            revivepotionamount=revivepotionamount-1
                            print('Revive potion used (',revivepotionamount,'remaining)')
                            hp=maxhp
                            continue
                        else:
                            deathmessage()
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',round(hploss,3),'HP (',round(hp,3),'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    enemieskilled=enemieskilled+1
                    if doing1=='Yes':
                        progress=progress+1
                    if inprogress1=='Yes':
                        if doing6=='Yes' and questtype1=='Bear':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing6=='Yes' and questtype2=='Bear':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing6=='Yes' and questtype3=='Bear':
                            progress=progress+1
                    score=score+300
                    while True:
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,2)
                        fight()
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',round(hp,3),'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                deathmessage()
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        bear_loot()
                        continue
                else:
                    continue
            else:
                enemyencounter('Slime',10,10,75,1,5,5,10)
                if battle=='1':
                    hploss=random.randint(0,4)
                    xpgain=random.randint(1,8)
                    run_modifiers()
                    xp=xp+xpgain
                    hp=hp-hploss
                    if hp<0 or hp==0:
                        print('')
                        print('You died')
                        if laststand==1:
                            if laststandskill=='In use':
                                laststand=laststand
                            else:
                                hp=maxhp*0.2
                                print('Last stand skill in use, HP:',round(hp,3),'')
                                laststandskill='In use'
                                continue
                        if revivepotionamount>0:
                            revivepotionamount=revivepotionamount-1
                            print('Revive potion used (',revivepotionamount,'remaining)')
                            hp=maxhp
                            continue
                        else:
                            deathmessage()
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',round(hploss,3),'HP (',round(hp,3),'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
                    enemieskilled=enemieskilled+1
                    if doing1=='Yes':
                        progress=progress+1
                    if inprogress1=='Yes':
                        if doing6=='Yes' and questtype1=='Slime':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing6=='Yes' and questtype2=='Slime':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing6=='Yes' and questtype3=='Slime':
                            progress=progress+1
                    score=score+500
                    while True:
                        if enemyhp<0 or enemyhp==0:
                            print('Fight finished, you won')
                            print('')
                            break
                        hploss=random.randint(0,6)
                        fight()
                        if hp<0 or hp==0:
                            print('')
                            print('You died')
                            if laststand==1:
                                if laststandskill=='In use':
                                    laststand=laststand
                                else:
                                    hp=maxhp*0.2
                                    print('Last stand skill in use, HP:',round(hp,3),'')
                                    laststandskill='In use'
                                    continue
                            if revivepotionamount>0:
                                revivepotionamount=revivepotionamount-1
                                print('Revive potion used (',revivepotionamount,'remaining)')
                                hp=maxhp
                                continue
                            else:
                                deathmessage()
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        rare_loot()
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
                            hploss=random.randint(5,15)
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
                                        printR('You do not have a revive potion, the game is over :c')
                                        print('')
                                        print(name,'slained by Muftosz')
                                        print('')
                                        if score>6999:
                                            print('Score:',score,'-', end='')
                                            printY('Legendary!!!')
                                        if score>4999 and score<7000:
                                            print('Score:',score,'-', end='')
                                            printP('Epic!!')
                                        if score>1999 and score<5000:
                                            print('Score:',score,'-', end='')
                                            printB('Good!')
                                        else:
                                            print('Score:',score,'-', end='')
                                            print('Bad')
                                        if value>149:
                                            print('Value:',value,'-', end='')
                                            printY('Legendary!!!')
                                        if score>99 and score<150:
                                            print('Value:',value,'-', end='')
                                            printP('Epic!!')
                                        if score>50 and score<100:
                                            print('Value:',value,'-', end='')
                                            printB('Good!')
                                        else:
                                            print('Value:',value,'-', end='')
                                            print('Bad')
                                        print('Enemies killed:',enemieskilled)
                                        print('')
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
                            hploss=random.randint(5,15)
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
                                        printR('You do not have a revive potion, the game is over :c')
                                        print('')
                                        print(name,'slained by Muftosz')
                                        print('')
                                        if score>6999:
                                            print('Score:',score,'-', end='')
                                            printY('Legendary!!!')
                                        if score>4999 and score<7000:
                                            print('Score:',score,'-', end='')
                                            printP('Epic!!')
                                        if score>1999 and score<5000:
                                            print('Score:',score,'-', end='')
                                            printB('Good!')
                                        else:
                                            print('Score:',score,'-', end='')
                                            print('Bad')
                                        if value>149:
                                            print('Value:',value,'-', end='')
                                            printY('Legendary!!!')
                                        if score>99 and score<150:
                                            print('Value:',value,'-', end='')
                                            printP('Epic!!')
                                        if score>50 and score<100:
                                            print('Value:',value,'-', end='')
                                            printB('Good!')
                                        else:
                                            print('Value:',value,'-', end='')
                                            print('Bad')
                                        print('Enemies killed:',enemieskilled)
                                        print('')
                                        break
                            else:
                                print('')
                                continue
                if hp<0 or hp==0:
                    break 
                print('You defeated MUFTOSZ, you spent some of your time to do this so shame on you')
                print('')
                if score>3499:
                    print('Score:',score,'-', end='')
                    printY('Legendary!!!')
                if score>2499 and score<3500:
                    print('Score:',score,'-', end='')
                    printP('Epic!!')
                if score>1499 and score<2500:
                    print('Score:',score,'-', end='')
                    printB('Good!')
                else:
                    print('Score:',score,'-', end='')
                    print(' Bad')
                if value>249:
                    print('Value:',value,'-', end='')
                    printY('Legendary!!!')
                if value>174 and value<250:
                    print('Value:',value,'-', end='')
                    printP('Epic!!')
                if value>99 and value<175:
                    print('Value:',value,'-', end='')
                    printB('Good!')
                else:
                    print('Value:',value,'-', end='')
                    print(' Bad')
                print('Enemies killed:',enemieskilled)
                print('')
                break               
            else:
                continue
        
        else:
            continue

    if choice=='2':
        if xp<50:
            print('')
            print('  ',name,'  ')
            print('LVL 1 (',xp,'xp )')
            profile()
        if 50<xp and xp<150:
            print('')
            print('  ',name,'  ')
            print('LVL 2 (',xp,'xp )')
            profile()
        time.sleep(5)
        continue

    if choice=='3':
        print('')
        printB('Potions:')
        print('')
        if healthpotionamount>0:
            print('(1)',healthpotionamount,'× Health potion')
        if revivepotionamount>0:
            print('(2)',revivepotionamount,'× Revive potion')
        if resistancepotionamount>0:
            print('(10)',resistancepotionamount,'× Resistance potion')
        if strengthpotionamount>0:
            print('(11)',strengthpotionamount,'× Strength potion')
        if staminapotionamount>0:
            print('(12)',staminapotionamount,'× Stamina potion')
        else:
            treasury=treasury
        print('')
        printB('Armors:')
        print('')
        if leatherarmoramount>0:
            print('(3)',leatherarmoramount,'× Leather armor')
        if resistance1leatherarmor>0:
            print('(3a1)',resistance1leatherarmor,'× Leather armor - Resistance I')
        if resistance2leatherarmor>0:
            print('(3a2)',resistance2leatherarmor,'× Leather armor - Resistance II')
        if resistance3leatherarmor>0:
            print('(3a3)',resistance3leatherarmor,'× Leather armor - Resistance III')
        if blocking1leatherarmor>0:
            print('(3b1)',blocking1leatherarmor,'× Leather armor - Blocking I')
        if blocking2leatherarmor>0:
            print('(3b2)',blocking2leatherarmor,'× Leather armor - Blocking II')
        if blocking3leatherarmor>0:
            print('(3b3)',blocking3leatherarmor,'× Leather armor - Blocking III')
        if curse1leatherarmor>0:
            print('(3c1)',curse1leatherarmor,'× Leather armor - Curse I')
        if curse2leatherarmor>0:
            print('(3c2)',curse2leatherarmor,'× Leather armor - Curse II')
        if curse3leatherarmor>0:
            print('(3c3)',curse3leatherarmor,'× Leather armor - Curse III')

        if copperarmoramount>0:
            print('(6)',copperarmoramount,'× Copper armor')
        if resistance1copperarmor>0:
            print('(6a1)',resistance1copperarmor,'× Copper armor - Resistance I')
        if resistance2copperarmor>0:
            print('(6a2)',resistance2copperarmor,'× Copper armor - Resistance II')
        if resistance3copperarmor>0:
            print('(6a3)',resistance3copperarmor,'× Copper armor - Resistance III')
        if blocking1copperarmor>0:
            print('(6b1)',blocking1copperarmor,'× Copper armor - Blocking I')
        if blocking2copperarmor>0:
            print('(6b2)',blocking2copperarmor,'× Copper armor - Blocking II')
        if blocking3copperarmor>0:
            print('(6b3)',blocking3copperarmor,'× Copper armor - Blocking III')
        if curse1copperarmor>0:
            print('(6c1)',curse1copperarmor,'× Copper armor - Curse I')
        if curse2copperarmor>0:
            print('(6c2)',curse2copperarmor,'× Copper armor - Curse II')
        if curse3copperarmor>0:
            print('(6c3)',curse3copperarmor,'× Copper armor - Curse III')

        if catarmoramount>0:
            print('(5)',catarmoramount,'× Maxwell armor')
        if resistance1catarmor>0:
            print('(5a1)',resistance1catarmor,'× Maxwell armor - Resistance I')
        if resistance2catarmor>0:
            print('(5a2)',resistance2catarmor,'× Maxwell armor - Resistance II')
        if resistance3catarmor>0:
            print('(5a3)',resistance3catarmor,'× Maxwell armor - Resistance III')
        if blocking1catarmor>0:
            print('(5b1)',blocking1catarmor,'× Maxwell armor - Blocking I')
        if blocking2catarmor>0:
            print('(5b2)',blocking2catarmor,'× Maxwell armor - Blocking II')
        if blocking3catarmor>0:
            print('(5b3)',blocking3catarmor,'× Maxwell armor - Blocking III')
        if curse1catarmor>0:
            print('(5c1)',curse1catarmor,'× Maxwell armor - Curse I')
        if curse2catarmor>0:
            print('(5c2)',curse2catarmor,'× Maxwell armor - Curse II')
        if curse3catarmor>0:
            print('(5c3)',curse3catarmor,'× Maxwell armor - Curse III')

        else:
            treasury=treasury
        print('')
        printB('Weapons:')
        print('')
        if woodendaggeramount>0:
            print('(4)',woodendaggeramount,'× Wooden dagger')
        if sharpness1woodendagger>0:
            print('(4a1)',sharpness1woodendagger,'× Wooden dagger - Sharpness I')
        if sharpness2woodendagger>0:
            print('(4a2)',sharpness2woodendagger,'× Wooden dagger - Sharpness II')
        if sharpness3woodendagger>0:
            print('(4a3)',sharpness3woodendagger,'× Wooden dagger - Sharpness III')
        if looting1woodendagger>0:
            print('(4b1)',looting1woodendagger,'× Wooden dagger - Looting I')
        if looting2woodendagger>0:
            print('(4b2)',looting2woodendagger,'× Wooden dagger - Looting II')
        if looting3woodendagger>0:
            print('(4b3)',looting3woodendagger,'× Wooden dagger - Looting III')
        if curse1woodendagger>0:
            print('(4c1)',curse1woodendagger,'× Wooden dagger - Curse I')
        if curse2woodendagger>0:
            print('(4c2)',curse2woodendagger,'× Wooden dagger - Curse II')
        if curse3woodendagger>0:
            print('(4c3)',curse3woodendagger,'× Wooden dagger - Curse III')
        if blocking1woodendagger>0:
            print('(4d1)',blocking1woodendagger,'× Wooden dagger - Blocking I')
        if blocking2woodendagger>0:
            print('(4d2)',blocking2woodendagger,'× Wooden dagger - Blocking II')
        if blocking3woodendagger>0:
            print('(4d3)',blocking3woodendagger,'× Wooden dagger - Blocking III')

        if woodenswordamount>0:
            print('(7)',woodenswordamount,'× Wooden sword')
        if sharpness1woodensword>0:
            print('(7a1)',sharpness1woodensword,'× Wooden sword - Sharpness I')
        if sharpness2woodensword>0:
            print('(7a2)',sharpness2woodensword,'× Wooden sword - Sharpness II')
        if sharpness3woodensword>0:
            print('(7a3)',sharpness3woodensword,'× Wooden sword - Sharpness III')
        if looting1woodensword>0:
            print('(7b1)',looting1woodensword,'× Wooden sword - Looting I')
        if looting2woodensword>0:
            print('(7b2)',looting2woodensword,'× Wooden sword - Looting II')
        if looting3woodensword>0:
            print('(7b3)',looting3woodensword,'× Wooden sword - Looting III')
        if curse1woodensword>0:
            print('(7c1)',curse1woodensword,'× Wooden sword - Curse I')
        if curse2woodensword>0:
            print('(7c2)',curse2woodensword,'× Wooden sword - Curse II')
        if curse3woodensword>0:
            print('(7c3)',curse3woodensword,'× Wooden sword - Curse III')
        if blocking1woodensword>0:
            print('(7d1)',blocking1woodensword,'× Wooden sword - Blocking I')
        if blocking2woodensword>0:
            print('(7d2)',blocking2woodensword,'× Wooden sword - Blocking II')
        if blocking3woodensword>0:
            print('(7d3)',blocking3woodensword,'× Wooden sword - Blocking III')

        if copperswordamount>0:
            print('(8)',copperswordamount,'× Copper sword')
        if sharpness1coppersword>0:
            print('(8a1)',sharpness1coppersword,'× Copper sword - Sharpness I')
        if sharpness2coppersword>0:
            print('(8a2)',sharpness2coppersword,'× Copper sword - Sharpness II')
        if sharpness3coppersword>0:
            print('(8a3)',sharpness3coppersword,'× Copper sword - Sharpness III')
        if looting1coppersword>0:
            print('(8b1)',looting1coppersword,'× Copper sword - Looting I')
        if looting2coppersword>0:
            print('(8b2)',looting2coppersword,'× Copper sword - Looting II')
        if looting3coppersword>0:
            print('(8b3)',looting3coppersword,'× Copper sword - Looting III')
        if curse1coppersword>0:
            print('(8c1)',curse1coppersword,'× Copper sword - Curse I')
        if curse2coppersword>0:
            print('(8c2)',curse2coppersword,'× Copper sword - Curse II')
        if curse3coppersword>0:
            print('(8c3)',curse3coppersword,'× Copper sword - Curse III')
        if blocking1coppersword>0:
            print('(8d1)',blocking1coppersword,'× Copper sword - Blocking I')
        if blocking2coppersword>0:
            print('(8d2)',blocking2coppersword,'× Copper sword - Blocking II')
        if blocking3coppersword>0:
            print('(8d3)',blocking3coppersword,'× Copper sword - Blocking III')
        
        if catswordamount>0:
            print('(9)',catswordamount,'× Maxwell sword')
        if sharpness1catsword>0:
            print('(9a1)',sharpness1catsword,'× Maxwell sword - Sharpness I')
        if sharpness2catsword>0:
            print('(9a2)',sharpness2catsword,'× Maxwell sword - Sharpness II')
        if sharpness3catsword>0:
            print('(9a3)',sharpness3catsword,'× Maxwell sword - Sharpness III')
        if looting1catsword>0:
            print('(9b1)',looting1catsword,'× Maxwell sword - Looting I')
        if looting2catsword>0:
            print('(9b2)',looting2catsword,'× Maxwell sword - Looting II')
        if looting3catsword>0:
            print('(9b3)',looting3catsword,'× Maxwell sword - Looting III')
        if curse1catsword>0:
            print('(9c1)',curse1catsword,'× Maxwell sword - Curse I')
        if curse2catsword>0:
            print('(9c2)',curse2catsword,'× Maxwell sword - Curse II')
        if curse3catsword>0:
            print('(9c3)',curse3catsword,'× Maxwell sword - Curse III')
        if blocking1catsword>0:
            print('(9d1)',blocking1catsword,'× Maxwell sword - Blocking I')
        if blocking2catsword>0:
            print('(9d2)',blocking2catsword,'× Maxwell sword - Blocking II')
        if blocking3catsword>0:
            print('(9d3)',blocking3catsword,'× Maxwell sword - Blocking III')

        else:
            treasury=treasury
        print('')
        printB('Other:')
        print('')
        if enchantmentscroll>0:
            print(enchantmentscroll,'× Enchantment scroll')
        if magneticstone>0:
            print('(13)',magneticstone,'× Magnetic stone')
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

        if use=='2':
            print('')
            if revivepotionamount>0:
                printR('You can only use a revive potion when you die during an adventure')

        if use=='3':
            print('')
            if leatherarmoramount>0:
                printG('Leather armor equipped')
                maxhp=20
                armor_equip()
                equippedarmor='Leather armor'
                leatherarmoramount=leatherarmoramount-1
                armorresistance=1
                maxhp_modifier()
        if use=='3a1':
            print('')
            if resistance1leatherarmor>0:
                leatherarmorequip()
                maxhp=maxhp*1.15
                res1=1
                resistance1leatherarmor=resistance1leatherarmor-1
        if use=='3a2':
            print('')
            if resistance2leatherarmor>0:
                leatherarmorequip()
                maxhp=maxhp*1.3
                res2=1
                resistance2leatherarmor=resistance2leatherarmor-1
        if use=='3a3':
            print('')
            if resistance3leatherarmor>0:
                leatherarmorequip()
                maxhp=maxhp*1.5
                res3=1
                resistance3leatherarmor=resistance3leatherarmor-1
        if use=='3b1':
            print('')
            if blocking1leatherarmor>0:
                leatherarmorequip()
                block1a=1
                blocking1leatherarmor=blocking1leatherarmor-1
        if use=='3b2':
            print('')
            if blocking3leatherarmor>0:
                leatherarmorequip()
                block2a=1
                blocking2leatherarmor=blocking2leatherarmor-1
        if use=='3b3':
            print('')
            if blocking3leatherarmor>0:
                leatherarmorequip()
                block3a=1
                blocking3leatherarmor=blocking3leatherarmor-1
        if use=='3c1':
            print('')
            if curse1leatherarmor>0:
                leatherarmorequip()
                maxhp=maxhp*0.85
                curse1a=1
                curse1leatherarmor=curse1leatherarmor-1
        if use=='3c2':
            print('')
            if curse2leatherarmor>0:
                leatherarmorequip()
                maxhp=maxhp*0.7
                curse2a=1
                curse2leatherarmor=curse2leatherarmor-1
        if use=='3c3':
            print('')
            if curse3leatherarmor>0:
                leatherarmorequip()
                maxhp=maxhp*0.5
                curse3a=1
                curse1leatherarmor=curse1leatherarmor-1

        if use=='4':
            print('')
            if woodendaggeramount>0:
                printG('Wooden dagger equipped')
                power=1.3
                weapon_equip()
                equippedweapon='Wooden dagger'
                woodendaggeramount=woodendaggeramount-1
                power_modifier()
        if use=='4a1':
            print('')
            if sharpness1woodendagger>0:
                woodendaggerequip()
                sharp1=1
                sharpness1woodendagger=sharpness1woodendagger-1
        if use=='4a2':
            print('')
            if sharpness2woodendagger>0:
                woodendaggerequip()
                sharp2=1
                sharpness2woodendagger=sharpness2woodendagger-1
        if use=='4a3':
            print('')
            if sharpness3woodendagger>0:
                woodendaggerequip()
                sharp3=1
                sharpness3woodendagger=sharpness3woodendagger-1
        if use=='4b1':
            print('')
            if looting1woodendagger>0:
                woodendaggerequip()
                loot1=1
                looting1woodendagger=looting1woodendagger-1
        if use=='4b2':
            print('')
            if looting2woodendagger>0:
                woodendaggerequip()
                loot2=1
                looting2woodendagger=looting2woodendagger-1
        if use=='4b3':
            print('')
            if looting2woodendagger>0:
                woodendaggerequip()
                loot3=1
                looting3woodendagger=looting3woodendagger-1
        if use=='4c1':
            print('')
            if curse1woodendagger>0:
                woodendaggerequip()
                curse1=1
                curse1woodendagger=curse1woodendagger-1
        if use=='4c2':
            print('')
            if curse2woodendagger>0:
                woodendaggerequip()
                curse2=1
                curse2woodendagger=curse2woodendagger-1
        if use=='4c3':
            print('')
            if curse3woodendagger>0:
                woodendaggerequip()
                curse3=1
                curse3woodendagger=curse3woodendagger-1
        if use=='4d1':
            print('')
            if blocking1woodendagger>0:
                woodendaggerequip()
                block1w=1
                blocking1woodendagger=blocking1woodendagger-1
        if use=='4d2':
            print('')
            if blocking2woodendagger>0:
                woodendaggerequip()
                block2w=1
                blocking2woodendagger=blocking2woodendagger-1
        if use=='4d3':
            print('')
            if blocking3woodendagger>0:
                woodendaggerequip()
                block3w=1
                blocking3woodendagger=blocking3woodendagger-1

        if use=='5':
            print('')
            if catarmoramount>0:
                printG('Maxwell armor equipped')
                maxhp=35
                armorresistance=3
                armor_equip
                equippedarmor='Maxwell armor'
                catarmoramount=catarmoramount-1
                maxhp_modifier()
        if use=='5a1':
            print('')
            if resistance1catarmor>0:
                catarmorequip()
                maxhp=maxhp*1.15
                res1=1
                resistance1catarmor=resistance1catarmor-1
        if use=='5a2':
            print('')
            if resistance2catarmor>0:
                catarmorequip()
                maxhp=maxhp*1.3
                res2=1
                resistance2catarmor=resistance2catarmor-1
        if use=='5a3':
            print('')
            if resistance3catarmor>0:
                catarmorequip()
                maxhp=maxhp*1.5
                res3=1
                resistance3catarmor=resistance3catarmor-1
        if use=='5b1':
            print('')
            if blocking1catarmor>0:
                catarmorequip()
                block1a=1
                blocking1catarmor=blocking1catarmor-1
        if use=='5b2':
            print('')
            if blocking3catarmor>0:
                catarmorequip()
                block2a=1
                blocking2catarmor=blocking2catarmor-1
        if use=='5b3':
            print('')
            if blocking3catarmor>0:
                catarmorequip()
                block3a=1
                blocking3catarmor=blocking3catarmor-1
        if use=='5c1':
            print('')
            if curse1catarmor>0:
                catarmorequip()
                maxhp=maxhp*0.85
                curse1a=1
                curse1catarmor=curse1catarmor-1
        if use=='5c2':
            print('')
            if curse2catarmor>0:
                catarmorequip()
                maxhp=maxhp*0.7
                curse2a=1
                curse2catarmor=curse2catarmor-1
        if use=='5c3':
            print('')
            if curse3catarmor>0:
                catarmorequip()
                maxhp=maxhp*0.5
                curse3a=1
                curse3catarmor=curse3catarmor-1

        if use=='6':
            print('')
            if copperarmoramount>0:
                printG('Copper armor equipped')
                maxhp=25
                armorresistance=2
                armor_equip()
                equippedarmor='Copper armor'
                copperarmoramount=copperarmoramount-1
                maxhp_modifier()
        if use=='6a1':
            print('')
            if resistance1copperarmor>0:
                copperarmorequip()
                maxhp=maxhp*1.15
                res1=1
                resistance1copperarmor=resistance1copperarmor-1
        if use=='6a2':
            print('')
            if resistance2copperarmor>0:
                copperarmorequip()
                maxhp=maxhp*1.3
                res2=1
                resistance2copperarmor=resistance2copperarmor-1
        if use=='6a3':
            print('')
            if resistance3copperarmor>0:
                copperarmorequip()
                maxhp=maxhp*1.5
                res3=1
                resistance3copperarmor=resistance3copperarmor-1
        if use=='6b1':
            print('')
            if blocking1copperarmor>0:
                copperarmorequip()
                block1a=1
                blocking1copperarmor=blocking1copperarmor-1
        if use=='6b2':
            print('')
            if blocking2copperarmor>0:
                copperarmorequip()
                block2a=1
                blocking2copperarmor=blocking2copperarmor-1
        if use=='6b3':
            print('')
            if blocking3copperarmor>0:
                copperarmorequip()
                block3a=1
                blocking3copperarmor=blocking3copperarmor-1
        if use=='6c1':
            print('')
            if curse1copperarmor>0:
                copperarmorequip()
                maxhp=maxhp*0.85
                curse1a=1
                curse1copperarmor=curse1copperarmor-1
        if use=='6c2':
            print('')
            if curse2copperarmor>0:
                copperarmorequip()
                maxhp=maxhp*0.7
                curse2a=1
                curse2copperarmor=curse2copperarmor-1
        if use=='6c3':
            print('')
            if curse3copperarmor>0:
                copperarmorequip()
                maxhp=maxhp*0.5
                curse3a=1
                curse3copperarmor=curse3copperarmor-1

        if use=='7':
            print('')
            if woodenswordamount>0:
                printG('Wooden sword equipped')
                power=1.5
                weapon_equip()
                equippedweapon='Wooden sword'
                woodenswordamount=woodenswordamount-1
                power_modifier()
        if use=='7a1':
            print('')
            if sharpness1woodensword>0:
                woodenswordequip()
                sharp1=1
                sharpness1woodensword=sharpness1woodensword-1
        if use=='7a2':
            print('')
            if sharpness2woodensword>0:
                woodenswordequip()
                sharp2=1
                sharpness2woodensword=sharpness2woodensword-1
        if use=='7a3':
            print('')
            if sharpness3woodensword>0:
                woodenswordequip()
                sharp3=1
                sharpness3woodensword=sharpness3woodensword-1
        if use=='7b1':
            print('')
            if looting1woodensword>0:
                woodenswordequip()
                loot1=1
                looting1woodensword=looting1woodensword-1
        if use=='7b2':
            print('')
            if looting2woodensword>0:
                woodenswordequip()
                loot2=1
                looting2woodensword=looting2woodensword-1
        if use=='7b3':
            print('')
            if looting2woodensword>0:
                woodenswordequip()
                loot3=1
                looting3woodensword=looting3woodensword-1
        if use=='7c1':
            print('')
            if curse1woodensword>0:
                woodenswordequip()
                curse1=1
                curse1woodensword=curse1woodensword-1
        if use=='7c2':
            print('')
            if curse2woodensword>0:
                woodenswordequip()
                curse2=1
                curse2woodensword=curse2woodensword-1
        if use=='7c3':
            print('')
            if curse3woodensword>0:
                woodenswordequip()
                curse3=1
                curse3woodensword=curse3woodensword-1
        if use=='7d1':
            print('')
            if blocking1woodensword>0:
                woodenswordequip()
                block1w=1
                blocking1woodensword=blocking1woodensword-1
        if use=='7d2':
            print('')
            if blocking2woodensword>0:
                woodenswordequip()
                block2w=1
                blocking2woodensword=blocking2woodensword-1
        if use=='7d3':
            print('')
            if blocking3woodensword>0:
                woodenswordequip()
                block3w=1
                blocking3woodensword=blocking3woodensword-1

        if use=='8':
            print('')
            if copperswordamount>0:
                printG('Copper sword equipped')
                power=1.7
                weapon_equip()
                equippedweapon='Copper sword'
                copperswordamount=copperswordamount-1
                power_modifier()
        if use=='8a1':
            print('')
            if sharpness1coppersword>0:
                copperswordequip()
                sharp1=1
                sharpness1coppersword=sharpness1coppersword-1
        if use=='8a2':
            print('')
            if sharpness2coppersword>0:
                copperswordequip()
                sharp2=1
                sharpness2coppersword=sharpness2coppersword-1
        if use=='8a3':
            print('')
            if sharpness3coppersword>0:
                copperswordequip()
                sharp3=1
                sharpness3coppersword=sharpness3coppersword-1
        if use=='8b1':
            print('')
            if looting1coppersword>0:
                copperswordequip()
                loot1=1
                looting1coppersword=looting1coppersword-1
        if use=='8b2':
            print('')
            if looting2coppersword>0:
                copperswordequip()
                loot2=1
                looting2coppersword=looting2coppersword-1
        if use=='8b3':
            print('')
            if looting3coppersword>0:
                copperswordequip()
                loot3=1
                looting3coppersword=looting3coppersword-1
        if use=='8c1':
            print('')
            if curse1coppersword>0:
                copperswordequip()
                curse1=1
                curse1coppersword=curse1coppersword-1
        if use=='8c2':
            print('')
            if curse2coppersword>0:
                copperswordequip()
                curse2=1
                curse2coppersword=curse2coppersword-1
        if use=='8c3':
            print('')
            if curse3coppersword>0:
                copperswordequip()
                curse3=1
                curse3coppersword=curse3coppersword-1
        if use=='8d1':
            print('')
            if blocking1coppersword>0:
                copperswordequip()
                block1w=1
                blocking1coppersword=blocking1coppersword-1
        if use=='8d2':
            print('')
            if blocking2coppersword>0:
                copperswordequip()
                block2w=1
                blocking2coppersword=blocking2coppersword-1
        if use=='8d3':
            print('')
            if blocking3coppersword>0:
                woodenswordequip()
                block3w=1
                blocking3coppersword=blocking3coppersword-1

        if use=='9':
            print('')
            if catswordamount>0:
                printG('Maxwell sword equipped')
                power=2
                weapon_equip
                equippedweapon='Maxwell sword'
                catswordamount=catswordamount-1
                power_modifier()
        if use=='9a1':
            print('')
            if sharpness1catsword>0:
                catswordequip()
                sharp1=1
                sharpness1catsword=sharpness1catsword-1
        if use=='9a2':
            print('')
            if sharpness2catsword>0:
                catswordequip()
                sharp2=1
                sharpness2catsword=sharpness2catsword-1
        if use=='9a3':
            print('')
            if sharpness3catsword>0:
                catswordequip()
                sharp3=1
                sharpness3catsword=sharpness3catsword-1
        if use=='9b1':
            print('')
            if looting1catsword>0:
                catswordequip()
                loot1=1
                looting1catsword=looting1catsword-1
        if use=='9b2':
            print('')
            if looting2catsword>0:
                catswordequip()
                loot2=1
                looting2catsword=looting2catsword-1
        if use=='9b3':
            print('')
            if looting2catsword>0:
                catswordequip()
                loot3=1
                looting3catsword=looting3catsword-1
        if use=='9c1':
            print('')
            if curse1catsword>0:
                catswordequip()
                curse1=1
                curse1catsword=curse1catsword
        if use=='9c2':
            print('')
            if curse2catsword>0:
                catswordequip()
                curse2=1
                curse2catsword=curse2catsword
        if use=='9c3':
            print('')
            if curse3catsword>0:
                catswordequip()
                curse3=1
                curse3catsword=curse3catsword
        if use=='9d1':
            print('')
            if blocking1catsword>0:
                catswordequip()
                block1w=1
                blocking1catsword=blocking1catsword
        if use=='9d2':
            print('')
            if blocking2catsword>0:
                catswordequip()
                block2w=1
                blocking2catsword=blocking2catsword
        if use=='9d3':
            print('')
            if blocking3catsword>0:
                catswordequip()
                block3w=1
                blocking3catsword=blocking3catsword

        if use=='10':
            print('')
            if resistancepotionamount>0:
                printG('Resistance potion activated for 3 adventures')
                resistancepotionamount=resistancepotionamount-1
                resistanceuse=4

        if use=='11':
            print('')
            if strengthpotionamount>0:
                strengthpotionamount=strengthpotionamount-1
                printG('Strength potion activated for 3 adventures')
                strengthuse=4

        if use=='12':
            print('')
            if staminapotionamount>0:
                staminapotionamount=staminapotionamount-1
                printG('Stamina and block replenished')
                stamina=100
                block=100
        
        if use=='13':
            print('')
            print('From which one do you want to remove the enchant? 1 = Equipped weapon, 2 = Equipped armor')
            weaponvarmor=input()
            isenchanted='No'
            if weaponvarmor=='1':
                if equippedweapon=='Wooden dagger' or equippedweapon=='Wooden sword' or equippedweapon=='Copper sword' or equippedweapon=='Maxwell sword':
                    if sharp1==1:
                        isenchanted='Yes'
                    if sharp2==1:
                        isenchanted='Yes'
                    if sharp3==1:
                        isenchanted='Yes'
                    if block1w==1:
                        isenchanted='Yes'
                    if block2w==1:
                        isenchanted='Yes'
                    if block3w==1:
                        isenchanted='Yes'
                    if loot1==1:
                        isenchanted='Yes'
                    if loot2==1:
                        isenchanted='Yes'
                    if loot3==1:
                        isenchanted='Yes'
                    if curse1==1:
                        isenchanted='Yes'
                    if curse2==1:
                        isenchanted='Yes'
                    if curse3==1:
                        isenchanted='Yes'
                    if isenchanted=='Yes':
                        enchantcheckweapon()
                        printG('Enchant succesfully removed!')
                        magneticstone=magneticstone-1
                    else:
                        printR('Your weapon is not enchanted!')
                else:
                    printR('You need to equip your weapon to remove the enchant!')
            if weaponvarmor=='2':
                if equippedarmor=='Leather armor' or equippedarmor=='Copper armor' or equippedarmor=='Maxwell armor':
                    if block1a==1:
                        blocking1leatherarmor=blocking1leatherarmor+1
                        isenchanted='Yes'
                    if block2a==1:
                        blocking2leatherarmor=blocking2leatherarmor+1    
                        isenchanted='Yes'
                    if block3a==1:
                        blocking3leatherarmor=blocking3leatherarmor+1
                        isenchanted='Yes'
                    if curse1a==1:
                        curse1leatherarmor=curse1leatherarmor+1
                        isenchanted='Yes'
                    if curse2a==1:
                        curse2leatherarmor=curse2leatherarmor+1
                        isenchanted='Yes'
                    if curse3a==1:
                        curse3leatherarmor=curse3leatherarmor+1
                        isenchanted='Yes'
                    if res1==1:
                        resistance1leatherarmor=resistance1leatherarmor+1
                        isenchanted='Yes'
                    if res2==1:
                        resistance2leatherarmor=resistance2leatherarmor+1
                        isenchanted='Yes'
                    if res3==1:
                        resistance3leatherarmor=resistance3leatherarmor+1
                        isenchanted='Yes'
                    if isenchanted=='Yes':
                        enchantcheckarmor()
                        printG('Enchant succesfully removed!')
                        magneticstone=magneticstone-1
                    else:
                        printR('Your armor is not enchanted!')

                else:
                    printR('You need to equip your armor to remove the enchant!')
            else:
                print('')
                continue             

        print('')
        time.sleep(3)
        continue
    
    if choice=='4':
        print('')
        printB('Potions:')
        print('')
        print('(1) Health potion = 3 gold (2 gold for sell)')
        print('(2) Revive potion = 10 gold (7 gold for sell)')
        print('(10) Resistance potion = 6 gold (4 gold for sell)')
        print('(11) Strength potion = 6 gold (4 gold for sell)')
        print('(12) Stamina potion = 3 gold (2 gold for sell)')        
        print('')
        printB('Armors:')
        print('')
        print('(3) Leather armor (15 HP) = 6 gold (4 gold for sell)')
        print('(9) Copper armor (20 HP) = 8 gold (Only for sell)')
        printB('Weapons:')
        print('')
        print('(4) Wooden dagger (1.3 Power) = 5 gold (3 gold for sell)')
        print('(5) Wooden sword (1.5 Power) = 7 gold (5 gold for sell)')
        print('(8) Copper sword (1.7 Power) = 9 gold (Only for sell)')
        print('')
        printB('Lootboxes:')
        print('')
        print('(6) Common lootbox = 5 gold')
        print('(7) Rare lootbox = 12 gold')
        print('')
        print('Other:')
        print('')
        print('(13) Magnetic stone = 2 gold (1 gold for sell)')
        print('')
        print('Treasury:',treasury,'')
        print('')
        purchase=input('')
        if purchase=='1':
            buy(2.99,healthpotionamount,'Health potion')
            healthpotionamount=x
            
        if purchase=='sell 1':
            if business==1:
                sell(3,healthpotionamount,'Health potion')
            else:
                sell(2,healthpotionamount,'Health potion')
            healthpotionamount=x

        if purchase=='2':
            buy(9.99,revivepotionamount,'Revive potion')
            revivepotionamount=x

        if purchase=='sell 2':
            if business==1:
                sell(10,revivepotionamount,'Revive potion')
            else:
                sell(7,revivepotionamount,'Revive potion')
            revivepotionamount=x

        if purchase=='3':
            if treasury>5.99:
                if inprogress1=='Yes':
                    if doing11=='Yes' and questtype1=='Leather armor':
                        progress=progress+1
                if inprogress2=='Yes':
                    if doing11=='Yes' and questtype2=='Leather armor':
                        progress=progress+1
                if inprogress3=='Yes':
                    if doing11=='Yes' and questtype3=='Leather armor':
                        progress=progress+1
            buy(5.99,leatherarmoramount,'Leather armor')
            leatherarmoramount=x

        if purchase=='sell 3':
            if business==1:
                sell(5,leatherarmoramount,'Leather armor')
            else:
                sell(4,leatherarmoramount,'Leather armor')
            leatherarmoramount=x

        if purchase=='4':
            if treasury>4.99:
                if inprogress1=='Yes':
                    if doing11=='Yes' and questtype1=='Wooden dagger':
                        progress=progress+1
                if inprogress2=='Yes':
                    if doing11=='Yes' and questtype2=='Wooden dagger':
                        progress=progress+1
                if inprogress3=='Yes':
                    if doing11=='Yes' and questtype3=='Wooden dagger':
                        progress=progress+1
            buy(4.99,woodendaggeramount,'Wooden dagger')
            woodendaggeramount=x

        if purchase=='sell 4':
            if business==1:
                sell(5,woodendaggeramount,'Wooden dagger')
            else:
                sell(3,woodendaggeramount,'Wooden dagger')
            woodendaggeramount=x

        if purchase=='5':
            if treasury>6.99:
                if inprogress1=='Yes':
                    if doing11=='Yes' and questtype1=='Wooden sword':
                        progress=progress+1
                if inprogress2=='Yes':
                    if doing11=='Yes' and questtype2=='Wooden sword':
                        progress=progress+1
                if inprogress3=='Yes':
                    if doing11=='Yes' and questtype3=='Wooden sword':
                        progress=progress+1
            buy(6.99,woodenswordamount,'Wooden sword')
            woodenswordamount=x

        if purchase=='sell 5':
            if business==1:
                sell(7,woodenswordamount,'Wooden sword')
            else:
                sell(5,woodenswordamount,'Wooden sword')
            woodenswordamount=x

        if purchase=='6':
            if treasury>5.99:
                print('')
                print('Purchase succesfull')
                print('- 5 gold (',treasury-5,')')
                treasury=treasury-5
                item=random.randint(1,7)
                if item==1:
                    woodendaggeramount=woodendaggeramount+1
                    print('+ Wooden dagger (',woodendaggeramount,') ')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Wooden dagger':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Wooden dagger':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Wooden dagger':
                            progress=progress+1
                if item==2:
                    woodenswordamount=woodenswordamount+1
                    print('+ Wooden sword (',woodenswordamount,') ')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Wooden sword':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Wooden sword':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Wooden sword':
                            progress=progress+1
                if item==3:
                    leatherarmoramount=leatherarmoramount+1
                    print('+ Leather armor (',leatherarmoramount,') ')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Leather armor':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Leather armor':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Leather armor':
                            progress=progress+1
                if item==4:
                    healthpotionamount=healthpotionamount+1
                    print('+ Health potion (',healthpotionamount,') ')
                if item==5:
                    resistancepotionamount=resistancepotionamount+1
                    print('+ Resistance potion (',resistancepotionamount,') ')
                if item==6:
                    strengthpotionamount=strengthpotionamount+1
                    print('+ Strength potion (',strengthpotionamount,') ')
                if item==7:
                    staminapotionamount=staminapotionamount+1
                    print('+ Stamina potion (',staminapotionamount,') ')
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
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
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Copper armor':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Copper armor':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Copper armor':
                            progress=progress+1
                if item==2:
                    copperswordamount=copperswordamount+1
                    print('+ Copper sword (',copperswordamount,') ')
                    if inprogress1=='Yes':
                        if doing11=='Yes' and questtype1=='Copper armor':
                            progress=progress+1
                    if inprogress2=='Yes':
                        if doing11=='Yes' and questtype2=='Copper armor':
                            progress=progress+1
                    if inprogress3=='Yes':
                        if doing11=='Yes' and questtype3=='Copper armor':
                            progress=progress+1
                if item==3:
                    revivepotionamount=revivepotionamount+1
                    print('+ Revive potion (',revivepotionamount,') ')
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
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
            sell(9,copperswordamount,'Copper sword')
            copperswordamount=x

        if purchase=='sell 9':
            sell(8,copperarmoramount,'Copper armor')
            copperarmoramount=x

        if purchase=='10':
            buy(5.99,resistancepotionamount,'Resistance potion')
            resistancepotionamount=x
            
        if purchase=='sell 10':
            if business==1:
                sell(6,resistancepotionamount,'Resistance potion') 
            else:
                sell(4,resistancepotionamount,'Resistance potion')
            resistancepotionamount=x

        if purchase=='11':
            buy(5.99,strengthpotionamount,'Strength potion')
            strengthpotionamount=x
            
        if purchase=='sell 11':
            if business==1:
                sell(6,strengthpotionamount,'Strength potion')
            else:
                sell(4,strengthpotionamount,'Strength potion')
            strengthpotionamount=x

        if purchase=='12':
            buy(2.99,staminapotionamount,'Stamina potion')
            staminapotionamount=x
            
        if purchase=='sell 12':
            if business==1:
                sell(3,staminapotionamount,'Stamina potion')
            else:
                sell(2,staminapotionamount,'Stamina potion')
            staminapotionamount=x

        if purchase=='13':
            buy(1.99,magneticstone,'Magnetic stone')
            magneticstone=x

        if purchase=='sell 13':
            if business==1:
                sell(2,magneticstone,'Magnetic stone')
            else:
                sell(1,magneticstone,'Magnetic stone')
            magneticstone=x

        time.sleep(3)
        continue
    
    if choice=='5':
        print('')
        printB('Adventure:')
        print('')
        print('In adventure, you can fight and get xp and gold but it comes with a price: HPloss')
        print('The more xp you have, the harder the fights get')
        print('Here you can decide to run or fight: if you run, then you get some XP and lose some HP, if you fight, you will deal damage to the enemy according to your weapon, you will also lose HP, if your HP gets below 0 or is 0, then you die and if the enemys HP is down then you win, in fights you get more XP than running and also get gold. \nStamina and block also determines how you fight: If your stamina is high, then you have increased critical hit chance. If it is medium, you do not get any boosts, but if it gets to low, then your attacks damage half the amount. Same applies to block: If it is high, then you have an increased chance to block hits. If it is medium, then everything is normal and if it is low then you will lose 1.5X more HP during enemy attacks.\nDuring fights you are given the choice to attack or defend, if you attack, you lose stamina but gain block and you will damage 1.5X more, but lose 1.5X more HP. If you defend you get block and lose stamina, your enemy deals half the amount of damage but your attacks deal half the amount of damage. At the start of a fight i recommend blocking since your enemy always starts with high stamina and block so they can block your attacks easily.')
        print('')
        printB('Items:')
        print('')
        print('On your journey you can get different types of items. You can open the item lis menu (6) to see their attributes.')
        print('')
        printB('Shop:')
        print('')
        print('In the shop, enter the number of the item to buy it, if you want to sell something, just put sell before it like sell 1 ')
        print('')
        printB('Profile & Inventory:')
        print('')
        print('In the inventory you can view your items and in the profile you can check your stats')
        print('In the inventory, write the number of the item to use it or equip it')
        print('When you equip something, you cannot sell it anymore, so equip them wisely! (You can unequip them by equipping another stuff)')
        print('')
        printB('Gamble:')
        print('')
        print('Here you can bet an amount of gold and maybe lose the half it or win +50% DO NOT WRITE A LETTER HERE, JUST NUMBERS OR ELSE THE GAME WILL BREAK')
        print('')
        printB('Enchanting:')
        print('')
        print('Here you can get enchantments to your weapons or to your armors. You can only enchant when your XP is above 30 and enchanting costs 30 XP. You can only have one enchant on an item at the same time. Enchanted items cannot be sold, you need to remove the enchant with a magnetic stone if you want to sell it.')
        print('')
        printB('Classes - Skills:')
        print('')
        print('There are five classes in the game: Healer, Swordsman, Trader, Wizard and Warrior. Each class has its own advantages and disadvantages. Each class also has unique skills which you can learn in the skills menu (9) with skill points')
        print('')
        printB('Quests:')
        print('')
        print('When you open the quests menu then 3 quests will appear. You can only choose one and when you already started one then you must finish it to start another one. Quests will give you additional rewards throughout your gameplay. To accept a quest just simply write the number of the quest.')
        print('')
        printB('Gameplay:')
        print('')
        print('The goal of the game is to reach 100 xp and to survive, there are many rare events to help your journey')
        print('The game is made up of two section, one is before reaching 50 xp and the other is after 50 xp, this section is harder')
        print('')
        continue

    if choice=='6':
        print('')
        printG('Potions:')
        print('')
        print('Health potion - Common (+30% HP) - Source: Adventure loot, Common lootbox, Shop, Quests')
        printB('Revive potion - Rare! (Allows to continue the game with full HP after dying) - Source: Adventure loot, Rare lootbox, Shop')
        print('Resistance potion - Common (-50% HP loss for 3 adventures) - Source: Adventure loot, Common lootbox, Shop, Quests')
        print('Strength potion - Common (+50% Strength for 3 adventures) - Source: Adventure loot, Common lootbox, Shop, Quests')
        print('Stamina potion - Common (Replenishes stamina and block) - Source: Adventure loot, Common lootbox, Shop, Quests')
        print('')
        printG('Armors:')
        print('')
        print('Leather armor - Common (20 HP - 1 Armor Resistance) - Source: Adventure loot, Common lootbox, Shop, Quests')
        printB('Copper armor - Rare! (25 HP - 2 Armor Resistance) - Source: Adventure loot, Rare lootbox, Quests')
        printP('Maxwell armor - Epic!! (35 HP - 3 Armor Resistance) - Source: Maxwell event')
        print('')
        printG('Weapons:')
        print('')
        print('Wooden dagger - Common (1.3 Power) - Source: Adventure loot, Common lootbox, Shop, Quests')
        print('Wooden sword - Common (1.5 Power) - Source: Adventure loot, Common lootbox, Shop, Quests')
        printB('Copper sword - Rare! (1.7 Power) - Source: Adventure loot, Rare lootbox, Quests')
        printP('Maxwell sword - Epic!! (2 Power) - Source: Maxwell event')
        print('')
        printG('Other:')
        print('')
        printB('Enchantment scroll - Rare! (Used to enchant without XP loss) - Source: Strange Scientist event, Quests')
        print('Magnetic stone -  Common (Used to remove an enchant from an item) - Source: Shop')

    if choice=='7':
        odd=random.randint(1,2)
        print("")
        print('50-50%, double or half')
        bet= float(input('Make a bet: '))
        if bet>treasury:
            print('')
            print('Eyo you do not even have that many gold')
            print('')
            time.sleep(2)
            continue
        if bet<treasury or bet==treasury:
            if bet==0:
                print('')
                print('Nah bro, why zero')
                print('')
                time.sleep(2)
                continue
            if doing5=='Yes':
                progress=progress+1
            if odd==1:
                print('')
                print('Win - +50%')
                goldgain=0.5*bet
                treasury=goldgain+treasury
                print('+',goldgain,'gold (',treasury,')')
                print('')
                time.sleep(2)
                continue
            else:
                print('')
                print('Lose - -50%')
                goldgain=0.5*bet
                treasury=treasury-goldgain
                print('-',goldgain,'gold (',treasury,')')
                print('')
                time.sleep(2)
                continue
        else:
            time.sleep(2)
            continue

    if choice=='8':
        if xp>29:
            print('')
            entype=input('What would you like to enchant? 1=Equipped weapon, 2=Equipped armor')
            enchant=random.randint(1,100)
            if entype=='1':
                if equippedweapon=='Wooden dagger' or equippedweapon=='Wooden sword' or equippedweapon=='Copper sword' or equippedweapon=='Maxwell sword':
                    enchantxp()
                    if enchant>0 and enchant<16:
                        weaponenchant='Sharpness I'
                        printG('Your weapon got enchanted with: Sharpness I\n+15% Power')
                        print('')
                        power=power*1.15
                        enchantcheckweapon()
                        sharp1=1
                        enchantlevel=1
                    if enchant>15 and enchant<23:
                        weaponenchant='Sharpness II'
                        printB('Your weapon got enchanted with: Sharpness II\n+30% Power')
                        print('')
                        power=power*1.3
                        enchantcheckweapon()
                        sharp2=1
                        enchantlevel=2
                    if enchant>22 and enchant<26:
                        weaponenchant='Sharpness III'
                        printP('Your weapon got enchanted with: Sharpness III\n+50% Power')
                        print('')
                        power=power*1.5
                        enchantcheckweapon()
                        sharp3=1
                        enchantlevel=3
                    if enchant>25 and enchant<41:
                        weaponenchant='Curse I'
                        printR('Your weapon got enchanted with: Curse I\n-15% Power')
                        print('')
                        power=power*0.85
                        enchantcheckweapon()
                        curse1=1
                        enchantlevel=1
                    if enchant>40 and enchant<48:
                        weaponenchant='Curse II'
                        printR('Your weapon got enchanted with: Curse II\n-30% Power')
                        print('')
                        power=power*0.7
                        enchantcheckweapon()
                        curse2=1
                        enchantlevel=2
                    if enchant>47 and enchant<51:
                        weaponenchant='Curse III'
                        printR('Your weapon got enchanted with: Curse III\n-50% Power')
                        print('')
                        power=power*0.5
                        enchantcheckweapon()
                        curse3=1
                        enchantlevel=3
                    if enchant>50 and enchant<66:
                        weaponenchant='Looting I'
                        printG('Your weapon got enchanted with: Looting I\n+25% Goldgain')
                        print('')
                        enchantcheckweapon()
                        loot1=1
                        enchantlevel=1
                    if enchant>65 and enchant<73:
                        weaponenchant='Looting II'
                        printB('Your weapon got enchanted with: Looting II\n+50% Goldgain')
                        print('')
                        enchantcheckweapon()
                        loot2=1
                        enchantlevel=2
                    if enchant>72 and enchant<76:
                        weaponenchant='Looting III'
                        printP('Your weapon got enchanted with: Looting III\n+75% Goldgain')
                        print('')
                        enchantcheckweapon()
                        loot3=1
                        enchantlevel=3
                    if enchant>75 and enchant<91:
                        weaponenchant='Blocking I'
                        printG('Your weapon got enchanted with: Blocking I\n-15% HPloss')
                        print('')
                        enchantcheckweapon()
                        block1w=1
                        enchantlevel=1
                    if enchant>90 and enchant<98:
                        weaponenchant='Blocking II'
                        printB('Your weapon got enchanted with: Blocking II\n-30% HPloss')
                        print('')
                        enchantcheckweapon()
                        block2w=1
                        enchantlevel=2
                    if enchant>97:
                        weaponenchant='Blocking III'
                        printP('Your weapon got enchanted with: Blocking III\n-50% HPloss')
                        print('')
                        enchantcheckweapon()
                        block3w=1
                        enchantlevel=3
                    if doing2=='Yes':
                        progress=progress+1
                    if doing9=='Yes':
                        if inprogress1=='Yes':
                            if enchantlevel==lvlofenchant1 or enchantlevel>lvlofenchant1:
                                progress=progress+1
                        if inprogress2=='Yes':
                            if enchantlevel==lvlofenchant2 or enchantlevel>lvlofenchant2:
                                progress=progress+1
                        if inprogress3=='Yes':
                            if enchantlevel==lvlofenchant3 or enchantlevel>lvlofenchant3:
                                progress=progress+1
                    time.sleep(2)
                    continue
                else:
                    print('')
                    print('You need to equip the weapon to enchant it!')
                    print('')
                    time.sleep(2)
                    continue
            if entype=='2':
                if equippedarmor=='Leather armor' or equippedarmor=='Copper armor' or equippedarmor=='Maxwell armor':
                    enchantxp()
                    if enchant>0 and enchant<16:
                        armorenchant='Resistance I'
                        printG('Your armor got enchanted with: Resistance I\n+15% MaxHP')
                        print('')
                        enchantcheckarmor()
                        maxhp=maxhp*1.15
                        res=1
                        enchantlevel=1
                    if enchant>15 and enchant<23:
                        armorenchant='Resistance II'
                        printB('Your armor got enchanted with: Resistance II\n+30% MaxHP')
                        print('')
                        enchantcheckarmor()
                        maxhp=maxhp*1.3
                        res2=1
                        enchantlevel=2
                    if enchant>22 and enchant<26:
                        armorenchant='Resistance III'
                        printP('Your armor got enchanted with: Resistance III\n+50% MaxHP')
                        print('')
                        enchantcheckarmor()
                        maxhp=maxhp*1.5
                        res3=1
                        enchantlevel=3
                    if enchant>25 and enchant<41:
                        armorenchant='Curse I'
                        printR('Your armor got enchanted with: Curse I\n-15% MaxHP')
                        print('')
                        enchantcheckarmor()
                        maxhp=maxhp*0.85
                        curse1=1
                        enchantlevel=1
                    if enchant>40 and enchant<48:
                        armorenchant='Curse II'
                        printR('Your armor got enchanted with: Curse II\n-30% MaxHP')
                        print('')
                        enchantcheckarmor()
                        maxhp=maxhp*0.7
                        curse2a=1
                        enchantlevel=2
                    if enchant>47 and enchant<51:
                        armorenchant='Curse III'
                        printR('Your armor got enchanted with: Curse III\n-50% MaxHP')
                        print('')
                        enchantcheckarmor()
                        maxhpx=maxhp*0.5
                        curse3=1
                        enchantlevel=3
                    if enchant>75 and enchant<91:
                        armorenchant='Blocking III'
                        printP('Your armor got enchanted with: Blocking III\n-50% HPloss')
                        print('')
                        enchantcheckarmor()
                        block3a=1
                        enchantlevel=3
                    if enchant>90 and enchant<98:
                        armorenchant='Blocking II'
                        printB('Your armor got enchanted with: Blocking II\n-30% HPloss')
                        print('')
                        enchantcheckarmor()
                        block2a=1
                        enchantlevel=2
                    if enchant>97:
                        armorenchant='Blocking I'
                        printG('Your armor got enchanted with: Blocking I\n-15% HPloss')
                        print('')
                        enchantcheckarmor()
                        block1a=1
                        enchantlevel=1
                    if doing2=='Yes':
                        progress=progress+1
                    if doing9=='Yes':
                        if inprogress1=='Yes':
                            if enchantlevel==number1 or enchantlevel>number1:
                                progress=progress+1
                        if inprogress2=='Yes':
                            if enchantlevel==number2 or enchantlevel>number2:
                                progress=progress+1
                        if inprogress3=='Yes':
                            if enchantlevel==number3 or enchantlevel>number3:
                                progress=progress+1
                    time.sleep(2)
                    continue
                else:
                    print('')
                    print('You need to equip the armor to enchant it!')
                    print('')
                    time.sleep(2)
                    continue
            else:
                continue

        else:
            print('')
            printR('You did not reach 30XP :c')
            time.sleep(2)
            continue

    if choice=='9':
        print('')
        print('Skill points:',skillpoint,'')
        print('')
        if type=='Healer':
            print('Passive skills:')
            if vampire==0:
                print('1 = Vampire I: 15% chance to damage 30% of your enemys max HP and heal by that amount - 3 skill points required')
            if vampire==1:
                print('1 = Vampire II: 30% chance to damage 30% of your enemys max HP and heal by that amount - 3 skill points required')
            if vampire==2:
                print('1 = Vampire III: 50% chance to damage 30% of your enemys max HP and heal by that amount - 3 skill points required')
            if focus==0:
                print('2 = Focus I: Decrease enemy critical hit chance by 5% - 1 skill point required')
            if focus==1:
                print('2 = Focus II: Decrease enemy critical hit chance by 10% - 1 skill point required')
            if focus==2:
                print('2 = Focus III: Decrease enemy critical hit chance by 15% - 1 skill point required')
            if advancedlooting==0:
                print('3 = Advanced looting: Extra health potion in adventures if you get one - 1 skill point required')
            print('Active skills:')
            if healing==0:
                print('4 = Healing: You can heal by 20% of your max HP every 4 turns - 5 skill points required')
            skillchoice=input('')
            if skillchoice=='1':
                if vampire==0:
                    skilllearn(1,'Vampire','I',3)
                    vampire=l
                    continue
                if vampire==1:
                    skilllearn(2,'Vampire','II',3)
                    vampire=l
                    continue
                if vampire==2:
                    skilllearn(3,'Vampire','III',3)
                    vampire=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='2':
                if focus==0:
                    skilllearn(1,'Focus','I',1)
                    focus=l
                    continue
                if focus==1:
                    skilllearn(2,'Focus','II',1)
                    focus=l
                    continue
                if focus==2:
                    skilllearn(3,'Focus','III',1)
                    focus=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='3':
                if advancedlooting==0:
                    skilllearn(1,'Advanced looting','I',1)
                    advancedlooting=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='4':
                if healing==0:
                    skilllearn(1,'Healing','I',5)
                    healing=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            else:
                continue
        if type=='Swordsman':
            print('Passive skills:')
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
            print('Active skills:')
            if tearingdive==0:
                print('4 = Tearing dive: Every 4 turn you can make an attack which penetrates block and becomes critical - 5 skill points required')
            skillchoice=input('')
            if skillchoice=='1':
                if learning==0:
                    skilllearn(1,'Improved learning','I',2)
                    learning=l
                    continue
                if learning==1:
                    skilllearn(2,'Improved learning','II',2)
                    learning=l
                    continue
                if learning==2:
                    skilllearn(3,'Improved learning','III',2)
                    learning=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='2':
                if shield==0:
                    skilllearn(1,'Shield','I',1)
                    shield=l
                    continue
                if shield==1:
                    skilllearn(2,'Shield','II',1)
                    shield=l
                    continue
                if shield==2:
                    skilllearn(3,'Shield','III',1)
                    shield=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='3':
                if laststand==0:
                    skilllearn(1,'Last stand','I',3)
                    laststand=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='4':
                if tearingdive==0:
                    skilllearn(1,'Tearing dive','I',5)
                    tearingdive=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            else:
                continue
        if type=='Trader':
            if fastlearner==0:
                print('1 = Fast learner: 50% to gain two skill points, when you gain one - 2 skill points required')
            if stealing==0:
                print('2 = Stealing: Critical hits get you 3 gold - 3 skill points required')
            if moneyrain==0:
                print('3 = Money rain: 50% chance to double gained gold - 4 skill points required')
            if business==0:
                print('4 = Smart business: You can sell items for the purchase price - 2 skill points required')
            skillchoice=input('')
            if skillchoice=='1':
                if fastlearner==0:
                    skilllearn(1,'Fast learner','I',2)
                    fastlearner=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='2':
                if stealing==0:
                    skilllearn(1,'Stealing','I',3)
                    stealing=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='3':
                if moneyrain==0:
                    skilllearn(1,'Money rain','I',4)
                    moneyrain=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='4':
                if business==0:
                    skilllearn(1,'Smart business','I',2)
                    business=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            else:
                continue
        if type=='Wizard':
            if weaken==0:
                print('1 = Weaken I: Decrease enemy damage by 7% - 1 skill point required')
            if weaken==1:
                print('1 = Weaken II: Decrease enemy damage by 14% - 1 skill point required')
            if weaken==2:
                print('1 = Weaken III: Decrease enemy damage by 20% - 1 skill point required')
            if stunning==0:
                print('2 = Stunning: Critical hits stun the enemy for 3 turns - 5 skill points required')
            if sabotage==0:
                print('3 = Sabotage: Enemy cannot do critical hits - 3 skill points required')
            if fireaura==0:
                print(' 4 = Fire aura: Critical hits trigger a fire aura which does damage for 3 turns - 3 skill points required')
            skillchoice=input('')
            if skillchoice=='1':
                if weaken==0:
                    skilllearn(1,'Weaken','I',1)
                    weaken=l
                    continue
                if weaken==1:
                    skilllearn(2,'Weaken','II',1)
                    weaken=l
                    continue
                if weaken==2:
                    skilllearn(3,'Weaken','III',1)
                    weaken=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='2':
                if stunning==0:
                    skilllearn(1,'Stunning','I',3)
                    stunning=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='3':
                if sabotage==0:
                    skilllearn(1,'Sabotage','I',3)
                    sabotage=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='4':
                if fireaura==0:
                    skilllearn(1,'Fire aura','I',3)
                    fireaura=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            else:
                print('')
                continue
        if type=='Warrior':
            if tearing==0:
                print('1 = Tearing I: +5% critical hit chance - 1 skill point required')
            if tearing==1:
                print('1 = Tearing II: +10% critical hit chance - 1 skill point required')
            if tearing==2:
                print('1 = Tearing III: +15% critical hit chance - 1 skill point required')
            if downfall==0:
                print('2 = Downfall I: +15% critical hit damage - 1 skill point required')
            if downfall==1:
                print('2 = Downfall II: +30% critical hit damage - 1 skill point required')
            if downfall==2:
                print('2 = Downfall III: +50% critical hit damage - 1 skill point required')
            if finish==0:
                print('3 = Finish: 10% chance to damage +500% of original damage - 3 skill points required')
            if perfecthealth==0:
                print('4 = Perfect health I: +10% max HP - 1 skill point required')
            if perfecthealth==1:
                print('4 = Perfect health II: +20% max HP - 1 skill point required')
            if perfecthealth==3:
                print('4 = Perfect health III: +30% max HP - 1 skill point required')
            skillchoice=input('')
            if skillchoice=='1':
                if tearing==0:
                    skilllearn(1,'Tearing','I',1)
                    tearing=l
                    continue
                if tearing==1:
                    skilllearn(2,'Tearing','II',1)
                    tearing=l
                    continue
                if tearing==2:
                    skilllearn(3,'Tearing','III',1)
                    tearing=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='2':
                if downfall==0:
                    skilllearn(1,'Downfall','I',1)
                    downfall=l
                    continue
                if downfall==1:
                    skilllearn(2,'Downfall','II',1)
                    downfall=l
                    continue
                if downfall==2:
                    skilllearn(3,'Downfall','III',1)
                    downfall=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='3':
                if finish==0:
                    skilllearn(1,'Finish','I',3)
                    finish=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue
            if skillchoice=='4':
                if perfecthealth==0:
                    skilllearn(1,'Perfect health','I',1)
                    perfecthealth=l
                    continue
                if perfecthealth==1:
                    skilllearn(2,'Perfect health','II',1)
                    perfecthealth=l
                    continue
                if perfecthealth==2:
                    skilllearn(3,'Perfect health','III',1)
                    perfecthealth=l
                    continue
                else:
                    print('')
                    print('This skill is already on max level')
                    print('')
                    continue           
            else:
                print('')
                continue
        continue

    if choice=='10':
        if inprogress1=='Yes' and progress==number1 or progress>number1:
            questcompletion(reward1,rewardamount1,rewardtype1,inprogress1,questquality1,lvlofenchant1)
            inprogress1='No'
        if inprogress2=='Yes' and progress==number2 or progress>number2:
            questcompletion(reward2,rewardamount2,rewardtype2,inprogress2,questquality2,lvlofenchant2)
            inprogress2='No'
        if inprogress3=='Yes' and progress==number3 or progress>number3:
            questcompletion(reward3,rewardamount3,rewardtype3,inprogress3,questquality3,lvlofenchant3)
            inprogress3='No'
        print('')
        questprint(quest1,inprogress1,reward1,1,number1,questtype1,lvlofenchant1)
        questprint(quest2,inprogress2,reward2,2,number2,questtype2,lvlofenchant2)
        questprint(quest3,inprogress3,reward3,3,number3,questtype3,lvlofenchant3)
        if inprogress1=='Yes' or inprogress2=='Yes' or inprogress3=='Yes':
            printB('You are already doing a quest')
        else:
            questchoice=input('')
            if questchoice=='1':
                printG('Quest 1 selected')
                inprogress1='Yes'
                questselect(quest1)
            if questchoice=='2':
                printG('Quest 2 selected')
                inprogress2='Yes'
                questselect(quest2)
            if questchoice=='3':
                printG('Quest 3 selected')
                inprogress3='Yes'
                questselect(quest3)
        print('')
        time.sleep(3)
        continue

    if choice=='cheat':
        treasury=10000
        xp=101
        skillpoint=1000
        continue

    if choice == 'stop':
        break

    else:
        print('There is no such command as [',choice,']')
        continue
        
        
                    