import random

class Pokemon:

    def __init__(self, name, level, types, strengths, weeknesses, hp, sp_atk, sp_def, phy_atk, phy_def, speed, evasiveness, precision, attacks, strong, week, sp_state):

        self.name = name
        self.level = level
        self.types = types
        self.strengths = strengths
        self.weeknesses = weeknesses
        self.hp = hp
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.phy_atk = phy_atk
        self.phy_def = phy_def
        self.speed = speed
        self.evasiveness = evasiveness
        self.precision = precision
        self.attack = attacks
        self.strong = strong
        self.week = week
        self.sp_state = sp_state

    def generate_damage(self, index):

        ## check if attacker can hit the target
        hitting_ratio = random.randrange(0, 1)
        if hitting_ratio < ((1 - self.attacks[index]["precision"]) / self.precision):
            return 0, self.generate_msg('fail', 0)
        ## As pokemon is attacking .. 1 PP has to be taken
        self.attacks[index]["PP"] -= 1
        ## Check if attack is critical
        critical_attack = random.randrange(0, 1)
        if critical_attack > 0.9:
            attack_power = self.attacks[index]["attack_power"] * 1.5
        else:
            attack_power = self.attacks[index]["attack_power"]

        ## check wether attacker is strong or week for that kind of attacks
        if self.attacks[index]["attack_type"] == self.strong:
            return random.randrange(attack_power, attack_power * 1.2)
        elif self.attacks["attack_type"] == self.week:
            return random.randrange(attack_power * 0.8, attack_power)
        else:
            return attack_power

    def take_damage(self, damage, attack_type):
        
        ## check if Pokemon can evade attack
        evasiveness_ratio = random.randrange(0,1)
        if evasiveness_ratio > (1 - self.evasiveness):
            return self.generate_msg('evade')
        ## check attack_type to know if it's strong or week against Pokemon type
        if (attack_type == 'normal' or attack_type == 'fight') & self.type == 'ghost':
            return self.generate_msg('no_damage')
        elif attack_type in self.weeknesses:
            ## take damage x2
            self.hp -= damage * 2
            return self.generate_msg('take_x2_damage')
        elif attack_type in self.strengths:
            ## take damage x1/2
            self.hp -= damage / 2
            if self.hp <= 0:
                return self.generate_msg('dead')
            else:
                return self.generate_msg('take_1/2_damage')
        else:
            ## take damage
            return self.generate_msg('take_damage')
        
    
    def generate_msg(self, action):

        if action == "attack":
            return 'Attacked!'
        elif action == "fail":
            return 'Attack Failed!'
        elif action == "evade":
            return 'Attack Evaded!'
        elif action == "no_damage":
            return 'Attack is Useless!'
        elif action == "take_x2_damage":
            return 'Attack is Strong!'
        elif action == "take_1/2_damage":
            return 'Attack is not to strong!'
        elif action == "take_damage":
            return 'Normal Attack!'
        elif action == "dead":
            return 'Your Pokemon died!'