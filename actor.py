import random
from colorama import Fore, Back, Style


class Creature:
	def __init__(self, name, level, strength):
		self.name = name
		self.level = level
		self.strength = strength

	def __repr__(self):
		return "{}: {}".format(self.name, self.level, self.strength)

	def defensive_roll(self):
		roll = random.randint(1, 12)
		return roll * self.level


#
class Wizard(Creature):
	def attack(self, creature):

		while True:
			my_roll = self.level * random.randint(1, 12)
			creature_roll = creature.defensive_roll()
			print("Your roll: {}".format(my_roll))
			print("{} roll: {}".format(creature.name, creature_roll))
			if my_roll >= creature_roll:
				# print("You have defeated {}!!!".format(creature.name))
				creature.strength -= 2
				print("You Attack!!!!")
				print("{}'s strength is now {}".format(creature.name, creature.strength))

				if creature.strength <= 0:
					print("You've defeated {}".format(creature.name))
					return True

			else:
				self.strength -= 2
				print(Fore.RED + "{} Attack!!!!".format(creature.name))
				print(Style.RESET_ALL + "Your strength is now {}".format(self.strength))
				if self.strength <= 0:
					print("You've been defeated!!!!!")
					return False


class Dragon(Creature):
	def __init__(self, name, level, strength, scaliness, breaths_fire):
		super().__init__(name, level, strength)
		self.scaliness = scaliness
		self.breathes_fire = breaths_fire

	def defensive_roll(self):
		roll = super().defensive_roll()
		value = roll * self.scaliness
		if self.breathes_fire:
			value = value * 2

		return value
