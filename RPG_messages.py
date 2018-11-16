import random


def warrior_messages(Move):
    while True:
        if Move == 'Earthen Bond':
            return ('You channeled the powers of the earth increasing your shield and damage output!')
            
        elif Move == 'Chaosus':
            return('You used all your might to strike your oponent dealing massive damage!')
            
        elif Move == 'Tremor':
            return('You strike the earth causing a great tremor!')
def assassin_messages(Move):
    while True:
        if Move == 'Dark Nebula':
            return('Dark energy flows through you as you open a rift.\n'
                       ' The rift deals damage!')
            
        elif Move == 'Death mark':
            return('You call upon your Dark Energy, your shield increases whilst your damage decreases.\n'
                        'You mark your enemy for death!')
            
        elif Move == 'Darkhest Night':
            return('A rain of black daggers descend from the air, dripping with toxic poison!')
def mage_messages(Move):
    while True:
        if Move == 'Solar wind':
            return('You summon a tailwind towards the target, burning him and healing yourself in the process!')
            
        elif Move == 'Gyro sphere':
            return('Magical energy crackles as you release an orb of pure energy on top of your target!')
            
        elif Move == 'Tetradrone':
            return('You pull your surroundings towards your opponent, surrounding them with massive psychic objects!')
def hunter_messages(Move):
    while True:
        if Move == 'Hunt-Power':
            return('Your dragon obeys as it releases a flaming bolt of elemental energy at your opponent, you follow up with a shot of your own!')
            
        elif Move == 'Storm shaft':
            return('You pull an arrow from your quiver and release it at lighting fast speed, imbued with energy, it deals Elemental Damage to your opponent!')
            
        elif Move == 'Frenzy shot':
            return('You enchant your arrow with life, it sinks into its target, sprouting plants all over your enemy, they begin to suffocate and then Explode!')




def E_messages(level):
    while True:
        if level == 'Enemy Major':
            EM_say = random.choice(['The Enemy stomps the ground and rushes forward causing major damage!','The enemy throws his hooks at you causing blood damage!'])
            return(EM_say)

        elif level == 'Enemy':
            E_say = random.choice(['The enemy shoots dark matter at you!','The enemy rushes forward with great momentum, damaging you!'])
            return(E_say)