class Battle:
    
    def __init__(self, tohit, towound, tosave, rend, attacks):
        self.tohit = tohit
        self.towound = towound
        self.tosave = tosave
        self.rend = rend
        self.attacks = attacks
    
    def gettohit(self):
        return self.tohit
    
    def gettowound(self):
        return self.towound
    
    def gettosave(self):
        return self.tosave
    
    def getrend(self):
        return self.rend
    
    def getattacks(self):
        return self.attacks
    
    
attacks = int(input('Enter the number of attacks: ')) 
tohit = int(input('Enter the roll needed to hit: ')) 
towound = int(input('Enter the roll needed to wound: '))  
tosave = int(input('Enter the roll needed to save: '))
rend = int(input('Enter rending value of attack: '))

unit = Battle(tohit, towound, tosave, rend, attacks)

hit = 0
wound = 0
woundthrough = 0
for i in range(0,100000):
    if(r.randrange(1,7) >= unit.gettohit()):
        hit = hit + 1
        if(r.randrange(1,7) >= unit.gettowound()):
            wound = wound + 1
            if(r.randrange(1,7) < (unit.gettosave() + unit.getrend())):
                woundthrough = woundthrough + 1
            
print("\nChance to hit: {:.2f}".format((hit / 100000) * 100 ), '%')
print("Chance to wound: {:.2f}".format((wound / 100000) * 100), '%')
print("Chance wound goes through: {:.2f}".format((woundthrough/100000) * 100), '%\n')

print('Likely # of hits: ', (unit.getattacks() * hit) / 100000)
print('Likely # of  wound: ', (unit.getattacks() * wound) / 100000)
print('Likely # of wound that go through: ', (unit.getattacks() * woundthrough)/100000)
