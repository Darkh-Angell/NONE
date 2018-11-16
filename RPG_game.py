import os, random, datetime, time
import RPG_GAME_classes as rg
import RPG_messages as rm
from RPG_inventory import *

'''
Need to create instances and methods for character passive abilities
'''
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')  #Clear screen code that clears the screen as long as the computer is a modern one

def welcome_mess():  #This is the Welcome Message of the game
    print('-'*24)     
    print('Axel: The golden edition')
    print('-'*24)

welcome_mess()

#-------- Game HElP section '''----------#

def game_help():          #sends user the Help choices
    clear_screen()
    game_help_choice  = int(input('Help choices:\n'       #ASKS USER TO CHOSE WHAT HE WANTS HELP IN
                                '1 - Classes\n'
                                '2 - Rules\n'
                                '3 - Quit\n'
                                '>>> '))
    while game_help_choice == 1:          
        clear_screen()
        Class_choice = int(input('1 - Warrior\n'        #TO REVEAL THE SKILLS OF THE CLASSES
                                '2 - Assassin\n'
                                '3 - Mage\n'
                                '4 - Hunter\n'
                                '5 - Quit\n'
                                '>>> '))
        if Class_choice == 1:
            rg.warrior_help()
            input()
        elif Class_choice == 2:
            rg.assassin_help()
            input()
        elif Class_choice == 3:
            rg.mage_help()
            input()
        elif Class_choice == 4:
            rg.hunt_help()
            input()
        elif Class_choice == 5:
            break

pass

class Character:            #MAIN CLASS THAT OTHER CHARACTER CLASSES INHERIT FROM, IN SHORT 'THE PARENT CLASS'
    #Hp = None               #SETS THE HITPOINTS OF THE CHARACTER TO 'NONE'
    #Shield = None
    def __init__(self,Hp='', Shield='', Spd='',MeleeDamage='',**kwargs):       #THIS CODE RUNS WHENEVER THE CHARACTER CLASS IS CALLED
        self.Hp = Hp
        self.Shield = Shield
        self.Spd = Spd
        self.MeleeDamage = MeleeDamage
        for key, value in kwargs.items(): #SETS ANY KEY AND VALUES GIVEN IN AS A VARIABLE
            setattr(self, key, value)
    
    def dead_or_alive(self):        #THIS CODE RETURNS WHETHER THE CHARACTER IS DEAD OR NOT
        if self.Hp <= 0:
            print ('Character is dead')
        elif self.Hp <= 1000:
            print('Character is in the verge of dying')
        elif self.Hp > 0:
            print('Character is still alive')
        return ('Character Health: {}\n'
                'Character Shield {}'.format(self.Hp, self.Shield))
    
    def DamageDealt(self, damage):
        self.damage = damage
    
    def ReadStats(self, choice=''):
        value = 0
        if choice == 'Hp':
            value = self.Hp
        elif choice == 'Spd':
            value = self.Spd
        elif choice == 'Shield':
            value = self.Shield
        elif choice == 'MeleeDamage':
            value = self.MeleeDamage

        return value

class Warrior(Character):        #WARRIOR CLASS, INHERITS FROM PARENT CLASS           
    skill1 = 'Earthen Bond'
    skill2 = 'Chaosus'
    ultSkill = 'Tremor'
    Earthern_Bond = False    #SETS ONE OF HIS TURN-TIME SKILLS ACTIVITY TO FALSE
    Chaosus_cd = False
    Tremor_cd = False
    def __init__(self, Hp=4000, Shield=1000, Spd=300, MeleeDamage=7500):
        super().__init__(Hp=Hp, Shield=Shield, Spd=Spd, MeleeDamage=MeleeDamage)
    def ReadStats(self, choice = ''):
        value = 0
        if choice == 'Hp':
            value = self.Hp
        elif choice == 'Spd':
            value = self.Spd
        elif choice == 'Shield':
            value = self.Shield
        elif choice == 'MeleeDamage':
            value = self.MeleeDamage

        return value

    def DamageDone(self, damage):       #RETURNS THE HP AND THE SHIELD AMOUNT OF THE WARRIOR CHARACTER
        super().DamageDealt(damage)     #AFTER DAMAGE IS DONE TO HIM/HER
        if self.Shield > 0:
            self.Shield -= int(self.damage * 0.75)
        elif self.Shield < 0:
            self.Shield = 0
        else:
            self.Hp -= self.damage
        
        return ('Hp: {}\n'
                'Shield: {}'.format(self.Hp, self.Shield))
    
    def MeleeDealt(self):        #MEELE DAMAGE
        damage = self.MeleeDamage
        return damage
    
    def skills(self, SkillMove, turn=''):       #SKILL USAGE
        self.SkillMove = SkillMove
        self.turn = turn
        damage = 0      #SETS DAMAGE TO 0
        
        if self.SkillMove == 'Melee Damage':
          damage = self.MeleeDealt()        #NEED TO DO THE SAME THING WITH OTHER CLASSES
          print('You attack the enemy with your weapon')
        if self.SkillMove == self.skill1:
            if self.Earthern_Bond == False:
                self.MeleeDamage = int(self.MeleeDamage*1.05)
                self.Shield = int(self.Shield*1.1)
                self.Earthern_Bond = True
                global turn_time 
                turn_time = self.turn + 4
                print(rm.warrior_messages(self.skill1))
            elif self.Earthern_Bond == True:
                print ('Cooldown Turns Left: {}'.format(turn_time - self.turn))
        if self.SkillMove == self.skill2:
            if self.Chaosus_cd == False:
                damage = 550
                self.Chaosus_cd = True
                global turn_time_2
                turn_time_2 = self.turn +2
                print(rm.warrior_messages(self.skill2))
            elif self.Chaosus_cd == True:
                print('Cooldown Turns Left: {}'.format(turn_time_2 - self.turn))
        if self.SkillMove == self.ultSkill:
            if self.Tremor_cd == False:
                damage = 960
                self.Tremor_cd = True
                global turn_time_ult
                turn_time_ult = self.turn + 8
                print(rm.warrior_messages(self.ultSkill))
            elif self.Tremor_cd == True:
                print('Cooldown Turns Left: {}'.format(turn_time_ult - self.turn))

        while self.Earthern_Bond == True:
            if self.turn == turn_time:     #TURN TIME STAT SKILLS ENDING
                self.MeleeDamage = int(self.MeleeDamage/1.05)
                self.Shield = int(self.Shield/1.05)
                self.Earthern_Bond = False
            break
        while self.Chaosus_cd == True:
            if self.turn == turn_time_2:
                self.Chaosus_cd = False
            break
        while self.Tremor_cd == True:
            if self.turn == turn_time_ult:
                self.Tremor_cd = False
            break
        return damage


    
    def statDisp(self):         #DISPLAYS STATS
        return ('Hitpoints: {}\n'
                'Shield: {}\n'
                'Speed: {}\n'.format(self.Hp, self.Shield, self.Spd))


class Assassin(Character): # SAME AS THE WARRIOR CLASS BUT FOR THE ASSASsINS
    skill1 = 'Dark Nebula'
    skill2 = 'Death mark'
    ultSkill = 'Darkhest Night'
    Dark_Nebula = False
    Death_mark = False
    D_Night = False
    def __init__(self, Hp=4800, Shield=200, Spd=700, MeleeDamage=75):
        super().__init__(Hp=Hp, Shield=Shield, Spd=Spd, MeleeDamage=MeleeDamage)
    
    def ReadStats(self, choice = ''):
        value = 0
        if choice == 'Hp':
            value = self.Hp
        elif choice == 'Spd':
            value = self.Spd
        elif choice == 'Shield':
            value = self.Shield
        elif choice == 'MeleeDamage':
            value = self.MeleeDamage

        return value
    
    def DamageDone(self, damage):
        super().DamageDealt(damage)
        if self.Shield > 0:
            self.Shield -= int(self.damage * 0.75)
        elif self.Shield < 0:
            self.Shield = 0
        else:
            self.Hp -= self.damage
        
        return ('Hp: {}\n'
                'Shield: {}'.format(self.Hp, self.Shield))
    
    def MeleeDealt(self):
        damage = self.MeleeDamage
        return damage
    
    def skills(self, SkillMove, turn=''):
        self.SkillMove = SkillMove
        self.turn = turn                
        damage = 0
        if self.SkillMove == 'Melee Damage':
          damage = self.MeleeDealt()        #NEED TO DO THE SAME THING WITH OTHER CLASSES
          print('You attack the enemy with your weapon')
        if self.SkillMove == self.skill1:
            if self.Dark_Nebula == False:
                damage = 600
                global turn_1
                turn_1 = self.turn +2
                print(rm.assassin_messages(self.skill1))
            elif self.Dark_Nebula == True:
                print('Cooldown turns left: {}'.format(turn_1 - self.turn))
            
        if self.SkillMove == self.skill2:
            if self.Death_mark == False:
                self.Shield = int(self.Shield*1.05)
                self.MeleeDamage = int(self.MeleeDamage*0.95)
                self.Death_mark =True
                global turn_time
                turn_time = self.turn + 4
                print(rm.assassin_messages(self.skill2))
            elif self.Death_mark == True:
                print('Cooldown Turns Left {}'.format(turn_time - self.turn))     
        if self.SkillMove == self.ultSkill:
            if self.D_Night == False:
                damage = 960
                self.D_Night = True
                print ('Enemy Poisoned')
                global turn_time_ult
                turn_time_ult = self.turn + 8
                print(rm.assassin_messages(self.ultSkill))
            if self.D_Night == True:
                print('Cooldown Turns Left: {}'.format(turn_time_ult - self.turn))
        
        if self.Dark_Nebula == True:
            if turn_1 == self.turn:
                self.Dark_Nebula = False
        if self.Death_mark == True:
            if self.turn == turn_time:
                damage += random.randint(500, 550)
                self.Shield = int(self.Shield/1.05)
                self.MeleeDamage = int(self.MeleeDamage/0.95)
                self.Death_mark = False
        if self.D_Night == True:
            if self.turn < turn_time_ult:
                damage += 15
            elif self.turn == turn_time_ult:
                self.D_Night = False
                print('Enemy cured of poisoning')
        return damage

    def statDisp(self):
        return ('Hitpoints: {}\n'
                'Shield: {}\n'
                'Speed: {}\n'.format(self.Hp, self.Shield, self.Spd))

class Mage(Character): # SAME AS THE WARRIOR CLASS BUT FOR THE MAGES
    skill1 = 'Solar wind'
    skill2 = 'Gyro sphere'
    ultSkill = 'Tetradrone'
    solar_wind = False
    gyro_sphere = False
    Tetra_cd = False
    def __init__(self, Hp=3000, Shield=2000, Spd=500, MeleeDamage=65):
        super().__init__(Hp=Hp, Shield=Shield, Spd=Spd, MeleeDamage=MeleeDamage)

    def ReadStats(self, choice = ''):
        value = 0
        if choice == 'Hp':
            value = self.Hp
        elif choice == 'Spd':
            value = self.Spd
        elif choice == 'Shield':
            value = self.Shield
        elif choice == 'MeleeDamage':
            value = self.MeleeDamage

        return value

    def DamageDone(self, damage):
        super().DamageDealt(damage)
        if self.Shield > 0:
            self.Shield -= int(self.damage * 0.75)
        elif self.Shield < 0:
            self.Shield = 0
        else:
            self.Hp -= self.damage
        
        return ('Hp: {}\n'
                'Shield: {}'.format(self.Hp, self.Shield))

    def MeleeDealt(self):
        damage = self.MeleeDamage
        return damage
    
    def skills(self, SkillMove, turn=''):
        self.SkillMove = SkillMove
        self.turn = turn                
        damage = 0
        
        if self.SkillMove == 'Melee Damage':
          damage = self.MeleeDealt()        #NEED TO DO THE SAME THING WITH OTHER CLASSES
          print('You attack the enemy with your weapon')
        if self.SkillMove == self.skill1:
            if self.solar_wind == False:
                self.solar_wind = True
                global turn_time_sw
                turn_time_sw = self.turn + 7
                print(rm.mage_messages(self.skill1))
            elif self.solar_wind == True:
                print('Cooldown Turns Left: {}'.format(turn_time_sw-self.turn))
        
        if self.SkillMove == self.skill2:
            if self.gyro_sphere == False:
                self.gyro_sphere = True
                global turn_time_gs
                turn_time_gs = self.turn + 5
                print(mage_messages(self.skill2))
            elif self.gyro_sphere == True:
                print('Cooldown Turns Left: {}'.format(turn_time_gs - self.turn))

        if self.SkillMove == self.ultSkill:
            if self.Tetra_cd == False:
                damage = 960
                self.Tetra_cd = True
                global turn_time_ult
                turn_time_ult = self.turn + 8
                print(mage_messages(self.ultSkill))
            elif self.Tetra_cd == True:
                print('Cooldown Turns Left: {}'.format(turn_time_ult - self.turn))
        
        if self.solar_wind == True:
            if self.turn < turn_time_sw:
                damage += 100
                while self.Hp != 3000 and self.Hp < 3000:
                    self.Hp += 60
                else:
                    pass
            elif self.turn == turn_time_sw:
                self.solar_wind = False

        if self.gyro_sphere == True:
            if self.turn < turn_time_gs:
                damage += 150
            elif self.turn == turn_time_gs:
                self.gyro_sphere = False 
        
        if self.Tetra_cd == True:
            if self.turn == turn_time_ult:
                self.Tetra_cd = False
        return damage

    def statDisp(self):
        return ('Hitpoints: {}\n'
                'Shield: {}\n'
                'Speed: {}\n'.format(self.Hp, self.Shield, self.Spd))

class Hunter(Character):    # SAME AS THE WARRIOR CLASS BUT FOR THE HUNTERS
    skill1 = 'Hunt-Power'
    skill2 = 'Storm shaft'
    ultSkill = 'Frenzy shot'
    Hunt_power = False
    S_Shaft = False
    Frenzy_shot = False
    def __init__(self, Hp=4200, Shield=400, Spd=600, MeleeDamage=75):
        super().__init__(Hp=Hp, Shield=Shield, Spd=Spd, MeleeDamage=MeleeDamage)
    def ReadStats(self, choice = ''):
        value = 0
        if choice == 'Hp':
            value = self.Hp
        elif choice == 'Spd':
            value = self.Spd
        elif choice == 'Shield':
            value = self.Shield
        elif choice == 'MeleeDamage':
            value = self.MeleeDamage

        return value
    def DamageDone(self, damage):
        super().DamageDealt(damage)
        if self.Shield > 0:
            self.Shield -= int(self.damage * 0.75)
        elif self.Shield < 0:
            self.Shield = 0
        else:
            self.Hp -= self.damage
        
        return ('Hp: {}\n'
                'Shield: {}'.format(self.Hp, self.Shield))

    def MeleeDealt(self):
        damage = self.MeleeDamage
        return damage
    
    def skills(self, SkillMove, turn=''):
        self.SkillMove = SkillMove
        self.turn = turn                
        damage = 0
        if self.SkillMove == 'Melee Damage':
          damage = self.MeleeDealt()        #NEED TO DO THE SAME THING WITH OTHER CLASSES
          print('You attack the enemy with your weapon')
        if self.SkillMove == self.skill1:
            if self.Hunt_power == False:
                damage = 600
                self.Hunt_power = True
                global turn_hp
                turn_hp = self.turn + 3
                print(rm.hunter_messages(self.skill1))
            elif self.Hunt_power == True:
                print('Cooldown Turns Left: {}'.format(turn_hp - self.turn))
        if self.SkillMove == self.skill2:
            if self.S_Shaft == False:
                damage = 650
                self.S_Shaft = True
                global turn_ss
                turn_ss = self.turn + 3
                print(rm.hunter_messages(self.skill2))
            elif self.S_Shaft == True:
                print('Cooldown Turns Left: {}'.format(turn_ss - self.turn))
        if self.SkillMove == self.ultSkill:
            if self.Frenzy_shot == False:
                self.Frenzy_shot = True
                global turn_time_ult
                turn_time_ult = self.turn + 4
                print(rm.hunter_messages(self.ultSkill))
            elif self.Frenzy_shot == True:
                print('Cooldown Turns Left: {}'.format(turn_time_ult - self.turn))
        
        if self.Hunt_power == True:
            if turn_hp == self.turn:
                self.Hunt_power = False
        
        if self.S_Shaft == True:
            if turn_ss == self.turn:
                self.S_Shaft = False
        if self.Frenzy_shot == True:
            if self.turn < turn_time_ult:
                damage += 300
            elif self.turn == turn_time_ult:
                self.Frenzy_shot = False

        return damage

    def statDisp(self):
        return ('Hitpoints: {}\n'
                'Shield: {}\n'
                'Speed: {}\n'.format(self.Hp, self.Shield, self.Spd))

class enemyN(Character): #NORMAL ENEMY CLASS
    monsterName = 'Enemy'
    def __init__(self, Hp=10000, Shield=0, Spd=250, MeleeDamage=100):
        super().__init__(Hp=Hp, Shield=Shield, Spd=Spd, MeleeDamage=MeleeDamage)
    def ReadStats(self, choice = ''):
        value = 0
        if choice == 'Hp':
            value = self.Hp
        elif choice == 'Spd':
            value = self.Spd
        elif choice == 'Shield':
            value = self.Shield
        elif choice == 'MeleeDamage':
            value = self.MeleeDamage

        return value
    def DamageDone(self, damage):
        super().DamageDealt(damage)
        if self.Shield > 0:
            self.Shield -= int(self.damage * 0.75)
        elif self.Shield < 0:
            self.Shield = 0
        else:
            self.Hp -= self.damage
        
        return ('Hp: {}\n'
                'Shield: {}'.format(self.Hp, self.Shield))
    

    def statDisp(self):
        return ('Hitpoints: {}\n'
                'Shield: {}\n'
                'Speed: {}\n'.format(self.Hp, self.Shield, self.Spd))

class enemyM(enemyN, Character):  #MEGA ENEMY CLASS
    monsterName = 'Enemy Major'
    def __init__(self, Hp=15000, Shield=3000, Spd=550, MeleeDamage=200):
        super().__init__(Hp=Hp, Shield=Shield, Spd=Spd, MeleeDamage=MeleeDamage)
    def ReadStats(self, choice = ''):
        value = 0
        if choice == 'Hp':
            value = self.Hp
        elif choice == 'Spd':
            value = self.Spd
        elif choice == 'Shield':
            value = self.Shield
        elif choice == 'MeleeDamage':
            value = self.MeleeDamage

        return value
    def DamageDone(self, damage):
        super().DamageDone(damage)
        if self.Shield > 0:
            self.Shield -= int(self.damage*0.75)
        elif self.Shield < 0:
            self.Shield = 0
        else:
            self.Hp -= self.damage
        
        return ('Hp: {}\n'
                'Shield: {}'.format(self.Hp, self.Shield))
    
    def statDisp(self):
        return ('Hitpoints: {}\n'
                'Shield: {}\n'
                'Speed: {}\n'.format(self.Hp, self.Shield, self.Spd))    


def ClassChoice():      #CLASS CHOICE
    choice = int(input('Choose the class you want to play as: \n'
            '1 - Warrior\n'
            '2 - Assassin\n'
            '3 - Mage\n'
            '4 - Hunter\n'
            '>>> '))
    if choice == 1:
      return Warrior()
    elif choice == 2:
      return Assassin()
    elif choice == 3:
      return Mage()   
    elif choice == 4:
      return Hunter()
                   
def CheckMove(MoveToCheck): #NEEDED TO CHECK THE VALIDITY OF THE MOVE THE CHARACTER USES
    MoveCheck = True
    if not (MoveToCheck in ['1','2','3','4']):
        MoveCheck = False
    else:
        MoveCheck = True
    return MoveCheck
        
class Game:           #THE REAL GAME CLASS
    monster = None
    
    def __init__(self, NewGame='', TrainingGame=''):
        self.playerClass = ClassChoice()
        self.PlayerName = input('What is your name?\n'
                                '>>> ')
        self.NewGame = NewGame
        self.TrainingGame = TrainingGame
        self.monsterN = enemyN()
        self.monsterM = enemyM()
        
        
    
    def lvl(self):
        start = int(input('Choose level:\n'
                      '1 - Easy\n'
                      '2 - Hard\n'
                      '>>> '))
        if start == 1:
            self.monster = self.monsterN
        elif start == 2:
            self.monster = self.monsterM

    def UserMove(self, turn):
        ChooseMove = input('1 - MeleeAttack\n'
                          '2 - {}\n'
                          '3 - {}\n'
                          '4 - {}\n'
                          '>>> '.format(self.playerClass.skill1, self.playerClass.skill2, self.playerClass.ultSkill))
        Checked = CheckMove(ChooseMove)
        while Checked == False:
            print('Wrong Move! Try Again')
            ChooseMove = input('1 - MeleeAttack\n'
                          '2 - {}\n'
                          '3 - {}\n'
                          '4 - {}\n'
                          '>>> '.format(self.playerClass.skill1, self.playerClass.skill2, self.playerClass.ultSkill))
            Checked = CheckMove(ChooseMove)
        while True:
            if ChooseMove == '2':
              ChooseMove = self.playerClass.skill1
            elif ChooseMove == '3':
              ChooseMove = self.playerClass.skill2
            elif ChooseMove == '4':
              ChooseMove = self.playerClass.ultSkill
            elif ChooseMove == '1':
              ChooseMove = 'Melee Damage'
            UserDamage = self.playerClass.skills(ChooseMove, turn=turn)
            while type(UserDamage) == str:
              print(UserDamage)
              ChooseMove = input('1 - MeleeAttack\n'
                          '2 - {}\n'
                          '3 - {}\n'
                          '4 - {}\n'
                          '>>> '.format(self.playerClass.skill1, self.playerClass.skill2, self.playerClass.ultSkill))
              Checked = CheckMove(ChooseMove)
              while True:
                  if ChooseMove == '2':
                    ChooseMove = self.playerClass.skill1
                  elif ChooseMove == '3':
                    ChooseMove = self.playerClass.skill2
                  elif ChooseMove == '4':
                    ChooseMove = self.playerClass.ultSkill
                  elif ChooseMove == '1':
                    ChooseMove = 'Melee Damage'
                  UserDamage = self.playerClass.skills(ChooseMove, turn=turn)
                  break    
            break     
        else:
          pass
        self.monster.DamageDone(UserDamage)

    def MonsterMove(self):
        MonsterDamage = self.monster.ReadStats(choice='MeleeDamage')
        self.playerClass.DamageDone(MonsterDamage)
        print(rm.E_messages(self.monster.monsterName))
    def Play(self):
        while True:
            self.lvl()
            turn = None
            MoveFirst = None
            if self.TrainingGame == True:
                turn = 0
                if self.playerClass.ReadStats(choice='Spd') > self.monster.ReadStats(choice='Spd'):
                    MoveFirst = True
                else:
                    MoveFirst = False
            else:
                turn = None
            if turn == 0:
                clear_screen()
                print('{}        VS      {}\n'
                      'Hp:{}     ¦     Hp:{}\n'
                      'Shield:{} ¦ Shield:{}'.format(self.PlayerName, self.monster.monsterName, self.playerClass.ReadStats(choice='Hp'), self.monster.ReadStats(choice='Hp'), self.playerClass.ReadStats(choice='Shield'), self.monster.ReadStats(choice='Shield')))
                        
                if MoveFirst == True:
                    self.UserMove(turn)
                    turn += 1
                elif MoveFirst == False:
                    self.MonsterMove()
                    print('Move ENDED for monster')
                    turn += 1
            while turn !=0:
                #clear_screen()
                print('{}        ¦        {}\n'
                      'Hp:{}     ¦     Hp:{}\n'
                      'Shield:{} ¦ Shield:{}'.format(self.PlayerName, self.monster.monsterName, self.playerClass.ReadStats(choice='Hp'), self.monster.ReadStats(choice='Hp'), self.playerClass.ReadStats(choice='Shield'), self.monster.ReadStats(choice='Shield')))
                while MoveFirst == True:
                    self.MonsterMove()
                    self.UserMove(turn)
                    break
                while MoveFirst == False:
                    self.UserMove(turn)
                    self.MonsterMove()
                    break
                if self.playerClass.ReadStats(choice='Hp') <= 0 or self.monster.ReadStats(choice='Hp') <= 0:
                    if self.playerClass.ReadStats(choice='Hp') <= 0:
                        winner = 'Enemy'
                    elif self.monster.ReadStats(choice='Hp') <= 0:
                        winner = self.PlayerName
                    
                    return ('{} has won the game'.format(winner))
                else:
                    turn += 1
        


while True:
    menu_choice = int(input('1 - Start New Game\n'
                          '2 - Start Training Game\n'
                          '3 - Help\n'
                          '4 - Quit\n'
                          '>>> '))
    if menu_choice == 1:
        Game(NewGame=False, TrainingGame=False)
    elif menu_choice == 2:
        keiron = Game(NewGame=False, TrainingGame=True)
        print(keiron.Play())
    elif menu_choice == 3:
        game_help()
    else:
        pass
    pass   
exit()