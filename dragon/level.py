# _*_coding:utf8_*_

class Level(object):
    '''docstring for Level'''
    def __init__(self):
        self.exp_needed = [10, 30, 60, 100, 150, 220, 310, 420, 570]
        self.exp = 0
        self.level = 1
        self.health = 25
        self.attack = 10
        self.defense = 5
        self.skill = [1, 0, 0, 0]

    def attacking(self):
        return self.attack

    def be_attacked(self, attack_number):
        self.health = self.health - (attack_number - self.defense)
        if self.health <= 0:
            return self.dead()

    def dead(self):
        self.gameover()
        return True

    def gameover(self):
        print "*" * 14
        print "胜败乃兵家常事"
        print "请大侠重头来过"
        print "*" * 14

