# _*_coding:utf8_*_
import monster
from random import randint

class SceneMap(object):
    ''' 场景地图类'''
    def __init__(self, room_number):
        self.room_number = room_number 
        self.monster_in_room = []
        self.monster_gen()

    def monster_gen(self):
        ''' 随机生成各房间对应的怪物 '''
        self.monster_in_room = self.gen(5, self.room_number)

    def gen(self, n, m):
        ''' 用抽签法从n个中抽出m个 '''
        res = []
        i = 0
        while i < m:
            r = randint(0, n - 1)
            if r not in res:
                res.append(r)
                i += 1

        return res

class WoodsMap(SceneMap):
    '''古森，第一级场景，会出现史莱姆，哥布林，僵尸，雄鹿，流氓等'''
    def __init__(self):
        SceneMap.__init__(self, 3)
        self.monster_init()

    def monster_init(self):
        for index, monster in enumerate(self.monster_in_room):
            self.monster_in_room[index] = self.monster_list(monster)

    def monster_list(self, index):
        return {
            0: monster.Slime(),
            1: monster.Goblin(),
            2: monster.Zombie(),
            3: monster.Buck(),
            4: monster.Rogue(),
        }[index]

