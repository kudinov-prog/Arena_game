from random import randint


def main():

    NAMES = ["Джон Сноу", "Дейнерис Таргариен", "Тирион Ланнистер", "Лорд Бейлиш", "Арья Старк", 
            "Бриенна Тарт", "Григор Клиган", "Вонючка", "Санса Старк", "Джейме Ланнистер",
            "Король Ночи", "Бран Старк", "Ходор", "Красная женщина", "Серсея Ланнистер",
            "Мергери", "Варис", "Сем Тарли", "Яра", "Кхал Дрого"]

    CLASSES = ["Paladin", "Warrior"]

    heroes = []

    things = []


    class Thing:

        def __init__(self, name, protection, attack, life_amount):
            self.name = name
            self.protection = protection
            self.attack = attack
            self.life_amount = life_amount


    class Person:
        
        def __init__(self, name, hp_amount, base_attack, base_protection):
            self.name = name
            self.hp_amount = hp_amount
            self.base_attack = base_attack
            self.base_protection = base_protection
            self.attack_damage = base_attack
            self.final_protection = base_protection

        def setThings(self, things):
            for thing in things:
                self.attack_damage += thing.attack
                self.final_protection += thing.protection
                self.final_protection = round(self.final_protection, 2)
                self.hp_amount += thing.life_amount

        def attacks(self, defender):
            print(f'{self.name} атакует {defender.name}')
            defender.defends(self)
        
        def defends(self, attacker):
            self.hp_amount -= (attacker.attack_damage - attacker.attack_damage*self.final_protection)
            self.hp_amount = round(self.hp_amount, 2)
            if self.hp_amount > 0:
                print(f'{self.name} выживает под натиском оппонента!')
            elif self.hp_amount < 0:
                print(f'{self.name} проигрывает и покидает арену!')


    class Paladin(Person):
        def __init__(self, name, hp_amount, base_attack, base_protection):
            super().__init__(name, hp_amount, base_attack, base_protection)
            self.hp_amount = hp_amount*2
            self.base_protection = round(base_protection*2, 2)
            self.final_protection = round(base_protection*2, 2)


    class Warrior(Person):
        def __init__(self, name, hp_amount, base_attack, base_protection):
            super().__init__(name, hp_amount, base_attack, base_protection)
            self.base_attack = base_attack*2
            self.attack_damage = base_attack*2


    def create_things():
        for new_thing in range(0, 30):
            thing = Thing(name=f'Item_{new_thing}', protection=round(0.01*randint(0, 10), 2),
                        attack=randint(5, 30), life_amount=randint(1, 20))
            things.append(thing)
        things.sort(key=lambda x: x.protection)   

        print('\n< Создан комплект рандомных вещей для участников битвы! >\n')  

    def create_heroes_and_equip():
        len_names = len(NAMES)-1
        for new_hero in range(0, 10):
            hero_class = CLASSES[randint(0, 1)]
            if hero_class == "Paladin":
                hero = Paladin(name=NAMES[randint(0, len_names)],
                               hp_amount=100,
                               base_attack=randint(0, 70),
                               base_protection=round(0.01*randint(0, 40), 2))
            else:
                hero = Warrior(name=NAMES[randint(0, len_names)],
                               hp_amount=100,
                               base_attack=randint(0, 70),
                               base_protection=round(0.01*randint(0, 40), 2))
            hero_things = []
            for item in range(1, randint(1, 4)):
                thing = things[randint(1, 24)]
                hero_things.append(thing)
            hero.setThings(hero_things)
            heroes.append(hero)

        print(f'< Создано {len(heroes)} участников битвы! >\n')

    def fight():

        print('<<<<< Да начнется великое сражение за королевский трон! >>>>>')

        round_num = 0
        while len(heroes) > 1:
            round_num += 1

            print(f'\n-----Начинается {round_num} раунд!-----\n')

            fighter_1 = heroes[randint(0, len(heroes)-1)]
            fighter_2 = heroes[randint(0, len(heroes)-1)]
            while fighter_2 == fighter_1:
                fighter_2 = heroes[randint(0, len(heroes)-1)]

            print(f'В схватке сойдутся {fighter_1.name} и {fighter_2.name}!')

            while fighter_2.hp_amount >= 0 and fighter_1.hp_amount >= 0:
                fighter_1.attacks(fighter_2)
                if fighter_2.hp_amount <= 0:
                    break
                fighter_2.attacks(fighter_1)
            if fighter_1.hp_amount <= 0:
                heroes.remove(fighter_1)
            elif fighter_2.hp_amount <= 0:
                heroes.remove(fighter_2)
        winner_fight = heroes[0].name

        print('\n>>>>> Битва закончена <<<<<')
        print(f'\n>>>>> Победитель великой битвы {winner_fight} <<<<<\n')
          
    create_things()
    create_heroes_and_equip()
    fight()

if __name__ == "__main__":
    main()
