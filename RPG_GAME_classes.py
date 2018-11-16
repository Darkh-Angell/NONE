import os
classes = ['Warrior', 'Assasian', 'Mage', 'Hunter']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

'''
Warrior
'''
war_skills = ['Earthen Bond', 'Chaosus']
war_ult_skill = ['Tremor']
#Passive ability == God's Weapon - Increasing strength of the weapon

def warrior_help():
    clear_screen()
    print('{}Warrior{}'.format('-'*5, '-'*5))
    print('Skills:\n'
    '-Earthen Bond: Increases the damage output and shield of the character.\n'
        '-Damage increase: 5%\n'
        '-Shield increase: 10%\n'
    '-Chaosus: An ancient move where the character uses all his might and slashes the target in 10 Vital spots.\n'
        '-Damage: 55 x 10')
    print('\nUltimate Skill:\n'
    '-Tremor: The character and smashes the end of his weapon onto the ground causing a great tremor.\n'
        '-Damage: 960')
    print('\nPassive ability: God\'s Weapon - The character\'s weapon strength increases bit by bit in 10 secs from 50 to 250')

'''
Assasian
'''

ass_skills = ['Dark Nebula', 'Death mark']
ass_ult_skill = ['Darkhest Night']
#Passive ability == Blood brothers - Gains life steal after 1st kill : life steal == 10% of the enemy's total hitpoints

def assasian_help():
    clear_screen()
    print('Skills:\n'
    '-Dark Nebula: The character slashes rapidly causing a rift to open, the rift causes a massive quantum damage to the target.\n'
        '-Damage: 600\n'
    '-Death mark: Whilst increasing the character\'s own shield amount and lowering his attack, he leaves a death mark on his target.\n'
    'The mark increases in strength for 3 secs and then explodes. This returns the character\'s stats to normal.\n'
        '-Damage: 500-550\n'
        '-Shield amount increase: 5%\n'
        '-Damage decrease: 5%')
    print('\nUltimate Skill:\n'
    '-Darkhest Night: Causes a rain of daggers and venom on top of the target. This also venomizes the target.\n'
        '-Damage: 960\n'
        '-Damage due to venom: 10 per second (lasts for 10 secs)')
    print('\nPassive ability: Blood Brothers - After their first kill, the character gains 10% lifesteal')
    

'''
Mage
'''

mage_skills = ['Solar wind', 'Gyro sphere']
mage_ult_skills = ['Tetradrone']
#passive ability == Essence of the Gods - if the health of character decreases below 50%, the character will start healing 20 hp per second, lasting 20 seconds.

def mage_help():
    clear_screen()
    print('Skills:\n'
    '-Solar wind: The character blows a fiery wind at the target, causing damage to the target and healing to themself for 6 seconds\n'
        '-Damage/sec: 100\n'
        '-Healing/sec: 60\n'
    
    '-Gyro sphere: Releases an orb of magic on top of the target, causing elemental damage to the target for 4 seconds\n'
        '-Elemental Damage = 150')
    print('\nUltimate Skill:\n'
    '-Tetradrone: Hurls psychic objects at the target from all directions\n'
        '-Damage: 960')
    print('\nPassive ability: Essence of the Gods - if the health of character decreases below 50%,\n'
    'the character will start healing 40 hp per second, lasting 20 seconds.')

'''
Hunter
'''

hunt_skills = ['Hunt-Power','Storm shaft']
hunt_ult_skills = ['Frenzy shot']
#passive ability == Dragon sidekick - a young dragon sidekick who is mentally linked with the hunter

def hunt_help():
  print('Skills:\n'
  '-Hunt-Power: The character tells the dragon to shoot a ball of elemental energy\n'
               'which is then shot by the character causing an explosion which leaves the enemies seriously damaged.\n'
        '-Damage: 600\n'
  '-Storm Shaft: The character shoots arrows imbued with storm energy\n'
        '-Damage: 650')
  print('\nUltimate Skills:\n'
  '-Frenzy shot: The character shoots an arrow that causes plants to sprout on the target,\n'
                'which suffocates it, after 3 seconds it explodes dealing damage to enemies near it.\n'
        '-Damage per sec: 300 per sec for 3 secs')
  print('\nPassive ability: Dragon Sidekick: A young dragon who is mentally linked to the hunter.')
        
