print('The beginning, always press enter to continue.')
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
                        if sabotage==1:
                            enemycrit=100  
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
                        print('1=Defend, 2=Attack')
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
                                print('SHIELD ACTIVE')
                            else:
                                hploss=hploss
                        if shield==2:
                            if protection<11:
                                hploss=0
                                print('')
                                print('SHIELD ACTIVE')
                            else:
                                hploss=hploss
                        if shield==3:
                            if protection<16:
                                hploss=0
                                print('')
                                print('SHIELD ACTIVE')
                            else:
                                hploss=hploss
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
                                print('ENEMY STUNNED')
                                stun=3
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
                            print('HIT BLOCKED')
                            print('')
                            hploss=0
                        else:
                            hploss=hploss
                        if enemyblockchance==1 or enemyhploss==0:
                            print('')
                            print('ENEMY BLOCKED HIT')
                            print('')
                            enemyhploss=0
                        else:
                            enemyhploss=enemyhploss
                        hp=hp-hploss
                        enemyhp=enemyhp-enemyhploss
                        print('')
                        if crit<21 and enemyhploss>0:
                            print('Enemy HP: -',round(enemyhploss,2),' Critical hit! (',round(enemyhp,2),'/',enemymaxhp,')')
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
                        if 0<loot and loot<20:
                            woodendaggeramount=woodendaggeramount+1
                            print('+ Wooden dagger (',woodendaggeramount,')')
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
                        if 0<loot and loot<20:
                            leatherarmoramount=leatherarmoramount+1
                            print('+ Leather armor (',leatherarmoramount,')')
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
                            if prize==4:
                                woodendaggeramount=woodendaggeramount+1
                                print('+ 1 Wooden dagger (',woodendaggeramount,')')
                            if prize==5:
                                copperarmoramount=copperarmoramount+1
                                print('+ 1 Copper armor (',copperarmoramount,')')
                            if prize==6:
                                copperswordamount=copperswordamount+1
                                print('+ 1 Copper sword (',copperswordamount,')')
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
                print('Gold box:')
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
            print('Class:',type,'')
            print('Treasury:',treasury,'')
            print('HP:',round(hp,2),'/',maxhp, equippedarmor,'')
            print('Strength:',round(power,2), equippedweapon,'')
            print('Stamina:',staminatype,'')
            print('Block:',blocktype,'')
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
            if fastlearner==1:
                print('Fast learner I')
                print('')
            if stealing==1:
                print('Stealing I')
                print('')
            if moneyrain==1:
                print('Money rain I')
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
            if skillpoint>0:
                print('Skill points:',skillpoint,'')
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

def armor_equip():
                global equippedarmor
                global leatherarmoramount
                global catarmoramount
                global copperarmoramount
                global block1a
                global block2a
                global block3a
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

def maxhp_modifier():
                global type
                global maxhp
                if type=='Swordsman':
                    maxhp=maxhp*0.85
                if type=='Trader' or type=='Wizard':
                    maxhp=maxhp*0.7
                if type=='Warrior':
                    maxhp=maxhp*1.25

def power_modifier():
                global type
                global power
                if type=='Healer':
                    power=power*0.8

def buy(price,item,itemid):
            global treasury
            global x
            if treasury>price:
                price=price+0.01
                print('')
                print('Purchase succesfull')
                print('+ 1',itemid,'(',item+1,')')
                print('-',price,'gold (',treasury-price,')')
                treasury=treasury-price
                x=item
                x=x+1
                print('')
            else:
                print('')
                print('Purchase insuccesfull')
                print('Not enough gold for purchase')
                print('')

def sell(price,item,itemid):
            global treasury
            global x
            if item>0:
                print('')
                print('Sell succesfull')
                print('- 1',itemid,'(',item-1,')')
                print('+',price,'gold (',treasury+price,')')
                treasury=treasury+price
                x=item
                x=x-1
                print('')
            else:
                print('')
                print('Sell insuccesfull')
                print('You do not have a',itemid,'')
                print('')

def enemyencounter(enemyname,emaxhp,ehp,lowxp,a,b,c,d):
    global enemylvl
    global enemymaxhp
    global enemyhp
    global battle
    global xp
    print('')
    enemymaxhp=emaxhp
    if xp<lowxp:
        enemylvl=random.randint(a,b)
    else:
        enemylvl=random.randint(c,d)
    enemymaxhp=((enemylvl/10)*enemymaxhp)+enemymaxhp
    enemyhp=enemymaxhp
    print('LVL',enemylvl,enemyname,'encounter:')
    print('Enemy HP:',enemyhp,'')
    battle=input('1=Run, 2=Fight')

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

skillpoint=0

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

#-----------------------Skills-----------------------#

focus=0
vampire=0
advancedlooting=0

laststand=0
learning=0
shield=0

stealing=0
moneyrain=0
fastlearner=0
critcount=0

stunning=0
stun=0
weaken=0
sabotage=0

tearing=0
downfall=0
finish=0
finishchance=0

#-----------------------Classes-----------------------#

while True:
    type=input('Choose a class: \n 1=Healer: +5 Health potion; -20% power \n 2=Swordsman: +Wooden sword; -15% maxHP \n 3=Trader: +10 gold; -30% maxHP \n 4=Wizard:  +Wooden dagger; enchanting only costs 15 XP; -20% maxHP \n 5=Warrior: +Copper sword; +leather armor; +25% maxHP; -50% gold gain')
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
        hp=maxhp
        type='Swordsman'
        print('Class selected: Swordsman')
        break
    if type=='3':
        treasury=10
        maxhp=maxhp*0.7
        hp=maxhp
        type='Trader'
        print('Class selected: Trader')
        break
    if type=='4':
        maxhp=maxhp*0.8
        hp=maxhp
        type='Wizard'
        equippedweapon='Wooden dagger'
        print('Class selected: Wizard')
        break
    if type=='5':
        maxhp=maxhp*1.25
        hp=maxhp
        equippedarmor='Leather armor'
        equippedweapon='Copper sword'
        type='Warrior'
        print('Class selected: Warrior')
        break
    else:
        print('I said choose a class')
        continue

#-----------------------Game-----------------------#

while True:

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
        else:
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

    print('Options:\n 1 - Adventure \n 2 - Profile \n 3 - Inventory \n 4 - Shop \n 5 - Help \n 6 - Item list \n 7 - Gamble \n 8 - Enchanting \n 9 - Skills \n')
    choice=input('')

    if choice=='1':
        enemystamina=100
        enemyblock=100
        critcount=0
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
                enemyencounter('Wolf',3,3,25,1,10,10,20)
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
                            print('You do not have a revive potion, the game is over :c')
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        wolf_loot()
                        continue
                else:
                    continue
            if 50<chance:
                enemyencounter('Bear',5,5,25,1,10,10,25)  
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
                            print('You do not have a revive potion, the game is over :c')
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
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
                if prize==4:
                    woodendaggeramount=woodendaggeramount+1
                    print('Item box:')
                    print('+ 1 Leather armor (',leatherarmoramount,')')
                if prize==5:
                    resistancepotionamount=resistancepotionamount+1
                    print('Item box:')
                    print('+ 1 Resistance potion (',resistancepotionamount,')')
                if prize==6:
                    strengthpotionamount=strengthpotionamount+1
                    print('Item box:')
                    print('+ 1 Strength potion (',strengthpotionamount,')')
                print('')
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
                if prize==4:
                    woodendaggeramount=woodendaggeramount+1
                    print('Item box:')
                    print('+ 1 Wooden dagger (',woodendaggeramount,')')
                if prize==5:
                    copperarmoramount=copperarmoramount+1
                    print('Item box:')
                    print('+ 1 Copper armor (',copperarmoramount,')')
                if prize==6:
                    copperswordamount=copperswordamount+1
                    print('Item box:')
                    print('+ 1 Copper sword (',copperswordamount,')')
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
                enemyencounter('Bandit',7,7,75,1,10,10,20)
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
                            print('You do not have a revive potion, the game is over :c')
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
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
                enemyencounter('Wolf',3,3,75,10,20,20,30)  
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
                            print('You do not have a revive potion, the game is over :c')
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        wolf_loot()
                        continue
                else:
                    continue
            if 90<chance and chance<100:
                enemyencounter('Bear',5,5,75,10,20,20,30)  
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
                            print('You do not have a revive potion, the game is over :c')
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
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
                        win()
                        xp=xp+xpgain
                        treasury=treasury+goldgain
                        advplus(xp, xpgain, treasury, goldgain, hploss, hp, maxhp)
                        bear_loot()
                        continue
                else:
                    continue
            else:
                enemyencounter('Slime',10,10,75,1,10,10,20)
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
                            print('You do not have a revive potion, the game is over :c')
                            break
                    print('+',xpgain,'xp (',xp,')')
                    print('-',hploss,'HP (',hp,'/',maxhp,')')
                    print('')
                    continue
                if battle=='2':
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
            profile()
            continue
        if 50<xp or xp<100:
            print('')
            print('LVL 2 (',xp,'xp )')
            profile()
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
        if staminapotionamount>0:
            print('(12) Stamina potion:',staminapotionamount,'')
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
                maxhp=20
                armor_equip()
                equippedarmor='Leather armor'
                leatherarmoramount=leatherarmoramount-1
                armorresistance=1
                maxhp_modifier()
                continue
            else:
                print('You do not have a leather armor :c')
                continue
        if use=='4':
            print('')
            if woodendaggeramount>0:
                print('Wooden dagger equipped')
                power=1.3
                weapon_equip()
                equippedweapon='Wooden dagger'
                woodendaggeramount=woodendaggeramount-1
                power_modifier()
                continue
            else:
                print('You do not have a woodendagger :c')
                continue
        if use=='5':
            print('')
            if catarmoramount>0:
                print('Maxwell armor equipped')
                maxhp=35
                armorresistance=3
                armor_equip
                equippedarmor='Maxwell armor'
                catarmoramount=catarmoramount-1
                maxhp_modifier()
                continue
            else:
                print('You do not have a Maxwell armor :c')
                continue
        if use=='6':
            print('')
            if copperarmoramount>0:
                print('Copper armor equipped')
                maxhp=25
                armorresistance=2
                armor_equip()
                equippedarmor='Copper armor'
                copperarmoramount=copperarmoramount-1
                maxhp_modifier()
                continue
            else:
                print('You do not have a copper armor :c')
                continue
        if use=='7':
            print('')
            if woodenswordamount>0:
                print('Wooden sword equipped')
                power=1.5
                weapon_equip()
                equippedweapon='Wooden sword'
                woodenswordamount=woodenswordamount-1
                power_modifier()
                continue
            else:
                print('You do not have a wooden sword :c')
                continue
        if use=='8':
            print('')
            if copperswordamount>0:
                print('Copper sword equipped')
                power=1.7
                weapon_equip()
                equippedweapon='Copper sword'
                copperswordamount=copperswordamount-1
                power_modifier()
                continue
            else:
                print('You do not have a copper sword :c')
                continue
        if use=='9':
            print('')
            if catswordamount>0:
                print('Maxwell sword equipped')
                power=2
                weapon_equip
                equippedweapon='Maxwell sword'
                catswordamount=catswordamount-1
                power_modifier()
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
        if use=='12':
            print('')
            if staminapotionamount>0:
                staminapotionamount=staminapotionamount-1
                print('Stamina and block replenished')
                stamina=100
                block=100
                continue
            else:
                print('You do not have a stamina potion :c')
                used=0
                continue
        continue
    
    if choice=='4':
        print('')
        print('Potions:')
        print('')
        print('(1) Health potion = 3 gold (2 gold for sell)')
        print('(2) Revive potion = 10 gold (7 gold for sell)')
        print('(10) Resistance potion = 6 gold (4 gold for sell)')
        print('(11) Strength potion = 6 gold (4 gold for sell)')
        print('(12) Stamina potion = 3 gold (2 gold for sell)')        
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
        print('')
        print('Treasury:',treasury,'')
        print('')
        purchase=input('')
        if purchase=='1':
            buy(2.99,healthpotionamount,'Health potion')
            healthpotionamount=x
            
        if purchase=='sell 1':
            sell(2,healthpotionamount,'health potion')
            healthpotionamount=x

        if purchase=='2':
            buy(9.99,revivepotionamount,'Revive potion')
            revivepotionamount=x

        if purchase=='sell 2':
            sell(7,revivepotionamount,'revive potion')
            revivepotionamount=x

        if purchase=='3':
            buy(5.99,leatherarmoramount,'Leather armor')
            leatherarmoramount=x

        if purchase=='sell 3':
            sell(4,leatherarmoramount,'leather armor')
            leatherarmoramount=x

        if purchase=='4':
            buy(4.99,woodendaggeramount,'Wooden dagger')
            woodendaggeramount=x

        if purchase=='sell 4':
            sell(3,woodendaggeramount,'wooden dagger')
            woodendaggeramount=x

        if purchase=='5':
            buy(6.99,woodenswordamount,'Wooden sword')
            woodenswordamount=x

        if purchase=='sell 5':
            sell(5,woodenswordamount,'wooden sword')
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
                if item==2:
                    woodenswordamount=woodenswordamount+1
                    print('+ Wooden sword (',woodenswordamount,') ')
                if item==3:
                    leatherarmoramount=leatherarmoramount+1
                    print('+ Leather armor (',leatherarmoramount,') ')
                if item==4:
                    healthpotionamount=healthpotionamount+1
                    print('+ Leather armor (',healthpotionamount,') ')
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
                if item==2:
                    copperswordamount=copperswordamount+1
                    print('+ Copper sword (',copperswordamount,') ')
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
            sell(9,copperswordamount,'copper sword')
            copperswordamount=x

        if purchase=='sell 9':
            sell(8,copperarmoramount,'copper armor')
            copperarmoramount=x

        if purchase=='10':
            buy(5.99,resistancepotionamount,'Resistance potion')
            resistancepotionamount=x
            
        if purchase=='sell 10':
            sell(4,resistancepotionamount,'resistance potion')
            resistancepotionamount=x

        if purchase=='11':
            buy(5.99,strengthpotionamount,'Strength potion')
            strengthpotionamount=x
            
        if purchase=='sell 11':
            sell(4,strengthpotionamount,'strength potion')
            strengthpotionamount=x

        if purchase=='12':
            buy(2.99,staminapotionamount,'Stamina potion')
            staminapotionamount=x
            
        if purchase=='sell 12':
            sell(2,staminapotionamount,'stamina potion')
            staminapotionamount=x

        continue
    
    if choice=='5':
        print('')
        print('Adventure:')
        print('')
        print('In adventure, you can fight and get xp and gold but it comes with a price: HPloss')
        print('The more xp you have, the harder the fights get')
        print('Here you can decide to run or fight: if you run, then you get some XP and lose some HP, if you fight, you will deal damage to the enemy according to your weapon, you will also lose HP, if your HP gets below 0 or is 0, then you die and if the enemys HP is down then you win, in fights you get more XP than running and also get gold. \nStamina and block also determines how you fight: If your stamina is high, then you have increased critical hit chance. If it is medium, you do not get any boosts, but if it gets to low, then your attacks damage half the amount. Same applies to block: If it is high, then you have an increased chance to block hits. If it is medium, then everything is normal and if it is low then you will lose 1.5X more HP during enemy attacks.\nDuring fights you are given the choice to attack or defend, if you attack, you lose stamina but gain block and you will damage 1.5X more, but lose 1.5X more HP. If you defend you get block and lose stamina, your enemy deals half the amount of damage but your attacks deal half the amount of damage. At the start of a fight i recommend blocking since your enemy always starts with high stamina and block so they can block your attacks easily.')
        print('')
        print('Items:')
        print('')
        print('On your journey you can get different types of items. You can open the item lis menu (6) to see their attributes.')
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
        print('')
        print('Here you can get enchantments to your weapons or to your armors. Unequipping an enchanted armor will result in losing the enchantment, enchanting costs 30xp, use it wisely!')
        print('')
        print('Classes - Skills:')
        print('')
        print('There are five classes in the game: Healer, Swordsman, Trader, Wizard and Warrior. Each class has its own advantages and disadvantages. Each class also has unique skills which you can learn in the skills menu (9) with skill points')
        print('')
        print('Gameplay:')
        print('')
        print('The goal of the game is to reach 100 xp and to survive, there are many rare events to help your journey')
        print('The game is made up of two section, one is before reaching 50 xp and the other is after 50 xp, this section is harder')
        print('')
        continue

    if choice=='6':
        print('')
        print('Potions:')
        print('')
        print('Health potion - Common (+30% HP) - Source: Adventure loot, Common lootbox, Shop')
        print('Revive potion - Rare! (Allows to continue the game with full HP after dying) - Source: Adventure loot, Rare lootbox, Shop')
        print('Resistance potion - Common (-50% HP loss for 3 adventures) - Source: Adventure loot, Common lootbox, Shop')
        print('Strength potion - Common (+50% Strength for 3 adventures) - Source: Adventure loot, Common lootbox, Shop')
        print('Stamina potion - Common (Replenishes stamina and block) - Source: Adventure loot, Common lootbox, Shop')
        print('')
        print('Armors:')
        print('')
        print('Leather armor - Common (20 HP - 1 Armor Resistance) - Source: Adventure loot, Common lootbox, Shop')
        print('Copper armor - Rare! (25 HP - 2 Armor Resistance) - Source: Adventure loot, Rare lootbox')
        print('Maxwell armor - Epic!! (35 HP - 3 Armor Resistance) - Source: Maxwell event')
        print('')
        print('Weapons:')
        print('')
        print('Wooden dagger - Common (1.3 Power) - Source: Adventure loot, Common lootbox, Shop')
        print('Wooden sword - Common (1.5 Power) - Source: Adventure loot, Common lootbox, Shop')
        print('Copper sword - Rare! (1.7 Power) - Source: Adventure loot, Rare lootbox')
        print('Maxwell sword - Epic!! (2 Power) - Source: Maxwell event')
        print('')
        print('Other:')
        print('')
        print('Enchantment scroll - Rare! (Used to enchant without XP loss) - Source: Strange Scientist event')

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
                    continue
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
        print('')
        print('Skill points:',skillpoint,'')
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
                        print('Last stand skill learned')
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
        if type=='Trader':
            if fastlearner==0:
                print('1 = Fast learner: 50% to gain two skill points, when you gain one - 2 skill points required')
            if stealing==0:
                print('2 = Stealing: Critical hits get you 3 gold - 3 skill points required')
            if moneyrain==0:
                print('3 = Money rain: 50% chance to double gained gold - 4 skill points required')
            skillchoice=input('')
            if skillchoice=='1':
                if fastlearner==0:
                    if skillpoint>1:
                        print('')
                        print('Fast learner skill learned')
                        print('')
                        fastlearner=1
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
                if stealing==0:
                    if skillpoint>2:
                        print('')
                        print('Stealing skill learned')
                        print('')
                        stealing=1
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
            if skillchoice=='3':
                if moneyrain==0:
                    if skillpoint>3:
                        print('')
                        print('Money rain skill learned')
                        print('')
                        moneyrain=1
                        skillpoint=skillpoint-4
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
        if type=='Wizard':
            if weaken==0:
                print('1 = Weaken I: Decrease enemy damage by 7% - 1 skill point required')
            if weaken==1:
                print('1 = Weaken II: Decrease enemy damage by 14% - 1 skill point required')
            if weaken==2:
                print('1 = Weaken III: Decrease enemy damage by 20% - 1 skill point required')
            if stunning==0:
                print('2 = Stunning: Critical hits stun the enemy for 3 turns - 3 skill points required')
            if sabotage==0:
                print('3 = Sabotage: Enemy cannot do critical hits - 3 skill points required')
            skillchoice=input('')
            if skillchoice=='1':
                if weaken==0:
                    if skillpoint>0:
                        print('')
                        print('Weaken I skill learned')
                        print('')
                        weaken=1
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if weaken==1:
                    if skillpoint>0:
                        print('')
                        print('Weaken II skill learned')
                        print('')
                        weaken=2
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if weaken==2:
                    if skillpoint>0:
                        print('')
                        print('Weaken III skill learned')
                        print('')
                        weaken=3
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
            if skillchoice=='2':
                if stunning==0:
                    if skillpoint>2:
                        print('')
                        print('Stunning skill learned')
                        print('')
                        stunning=1
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
            if skillchoice=='3':
                if sabotage==0:
                    if skillpoint>2:
                        print('')
                        print('Sabotage skill learned')
                        print('')
                        sabotage=1
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
            skillchoice=input('')
            if skillchoice=='1':
                if tearing==0:
                    if skillpoint>0:
                        print('')
                        print('Tearing I skill learned')
                        print('')
                        tearing=1
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if tearing==1:
                    if skillpoint>0:
                        print('')
                        print('Tearing II skill learned')
                        print('')
                        tearing=2
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if tearing==2:
                    if skillpoint>0:
                        print('')
                        print('Tearing III skill learned')
                        print('')
                        tearing=3
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
            if skillchoice=='2':
                if downfall==0:
                    if skillpoint>0:
                        print('')
                        print('Downfall I I skill learned')
                        print('')
                        downfall=1
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if downfall==1:
                    if skillpoint>0:
                        print('')
                        print('Downfall II skill learned')
                        print('')
                        downfall=2
                        skillpoint=skillpoint-1
                        continue
                    else:
                        print('')
                        print('Not enough skill points :c')
                        print('')
                        continue
                if downfall==2:
                    if skillpoint>0:
                        print('')
                        print('Downfall III skill learned')
                        print('')
                        downfall=3
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
                if finish==0:
                    if skillpoint>2:
                        print('')
                        print('Finish skill learned')
                        print('')
                        finish=1
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
                print('')
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
        
        
                    