# _*_coding:utf8_*_
from random import randint
class Test(object):
    '''docstring for Test'''
    def __init__(self, string):
        self.string = string

    def method(self):
        print "What are you?"    


class TestChild(Test):
    def printer(self):
        print self.string
        self.string = "test"
        print self.string

# t = TestChild("teeeeeest")
# t.printer()

class Monster(object):
    ''' 怪物父类 '''
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack(self):
        return self.attack

    def be_attacked(self, attack_number):
        self.health = self.health - (attack_number - defense)
        if self.health <= 0:
            self.dead()

        return False

    def dead():
        return True

class Slime(Monster):
    ''' 古森基本怪物之一：史莱姆 '''
    def __init__(self):
        Monster.__init__(self, 20, 10, 6)

#slime = Slime()
#print slime.health
#print slime.attack
#print slime.defense

def monster_list(index):
    return {
        0: Slime(),
        1: Slime(),
        2: Slime(),
        3: Slime(),
        4: Slime(),
    }[index]

def gen(n, m):
    res = []
    i = 0
    while i < m:
        r = randint(0, n - 1)
        if r not in res:
            res.append(r)
            i += 1

    return res
