# _*_coding:utf8_*_

class Monster(object):
    ''' 怪物父类 '''
    def __init__(self, health, attack, defense, exp):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.exp = exp

    def attacking(self):
        return self.attack

    def be_attacked(self, attack_number):
        self.health = self.health - (attack_number - self.defense)
        if self.health <= 0:
            return self.dead()

    def dead(self):
        print "*" * 8
        print "  胜利"
        print "*" * 8
        return True

class Slime(Monster):
    ''' 古森基本怪物之一：史莱姆 '''
    def __init__(self):
        Monster.__init__(self, 22, 8, 6, 5)
        
class Goblin(Monster):
    ''' 古森基本怪物之一：哥布林 '''
    def __init__(self):
        Monster.__init__(self, 20, 11, 5, 5)
       
class Zombie(Monster):
    ''' 古森基本怪物之一：僵尸 '''
    def __init__(self):
        Monster.__init__(self, 24, 12, 4, 6)
        
class Buck(Monster):
    ''' 古森基本怪物之一：雄鹿 '''
    def __init__(self):
        Monster.__init__(self, 25, 8, 4, 6)
        
class Rogue(Monster):
    ''' 古森基本怪物之一：流氓 '''
    def __init__(self):
        Monster.__init__(self, 18, 13, 4, 5)
        
