import random

entityList = [0]


class entity():

    def __init__(self, UID, Sex, rootM, rootF, geneA : list, geneB : list):
        self.UID = UID #index on entityList

        self.Sex = Sex #0:M, 1:F
        self.rootM = rootM #index num
        self.rootF = rootF #index num

        #dominant : Large Letter

        self.geneA = geneA #ex AA, aa 
        self.geneB = geneB #ex BB, Bb

        self.isDead = False

    def __str__(self) -> str:
        print(" UID : {}\n SEX : {}\n MOTHER : {}\n FATHER : {}\n GENE.A : {}\n GENE.B : {}\n".format(self.UID, self.Sex, self.rootM, self.rootF, self.geneA, self.geneB))


    #extract random gene >> hardi-weinberg 
    def extractGeneSingle(self):
        return random.choice(self.geneA), random.choice(self.geneB)


    def goDead(self):
        self.isDead = True



def initAdamNEve():
    adamGeneA, adamGeneB = str(input("set ADAM(Male)  >> geneA geneB >>")).split()
    eveGeneA, eveGeneB = str(input("set ADAM(Male)  >> geneA geneB >>")).split()

    list(adamGeneA)
    list(adamGeneB)
    list(eveGeneA)
    list(eveGeneB)


    globals()['entity_1'] = entity(1, 0, 0, 0, adamGeneA, adamGeneB)
    entityList.append(globals()['entitiy_1'])

    globals()['entity_2'] = entity(2, 1, 0, 0, eveGeneA, eveGeneB)
    entityList.append(globals()['entitiy_2'])


def matingCouple(male : entity, female : entity, sex : int):
    if(male.Sex != 0 and female.Sex != 1):
        return
    else:
        indexNum = len(entityList)
        maleA = male.extractGeneSingle[0]
        maleB = male.extractGeneSingle[1]

        femaleA = female.extractGeneSingle[0]
        femaleB = female.extractGeneSingle[1]

        resA = maleA + femaleA
        resB = maleB + femaleB
        
        globals()['entitiy_1'.format(indexNum)] = entity(indexNum, sex, male.UID, female.UID, resA, resB)

        entityList.append(globals()['entitiy_{}'.format(indexNum)])
        

