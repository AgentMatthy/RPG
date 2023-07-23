vampire=0
skillpoint=3
def skilllearn(skill,learnedlevel,skillname,learnedlevelname,skillpointcost):
    global skillpoint
    global skill

    if skillpoint>skillpointcost-1:
        print('')
        print('',skillname,learnedlevelname,'skill learned')
        print('')
        skill=learnedlevel
        skillpoint=skillpoint-skillpointcost
    else:
        print('')
        print('Not enough skill points :c')
        print('')

skilllearn(vampire,1,'Vampire','I',3)
print(vampire)