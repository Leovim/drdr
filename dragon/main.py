# _*_coding:utf8_*_
import level, map, monster

woods = map.WoodsMap()
hero = level.Level()

while True:
    if woods.monster_in_room[0].be_attacked(hero.attacking()):
        print woods.monster_in_room[0]
        print hero.health
        break

    if hero.be_attacked(woods.monster_in_room[0].attacking()):
        print woods.monster_in_room[0]
        print woods.monster_in_room[0].health
        break

