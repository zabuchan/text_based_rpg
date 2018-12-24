import random
from colorama import Fore, Back, Style

from actor import Creature, Wizard, Dragon


def main():
	print_header()
	game_loop()


def print_header():
	print('------------------------------------------------')
	print('                  TEXT BASED RPG')
	print('------------------------------------------------')
	print()


def game_loop():
	creatures = [
		Creature('Bat', 3, 4),
		Dragon('Black Dragon', 50, 10, scaliness=2, breaths_fire=False),
		Dragon('Fire Dragon', 40, 15, scaliness=2, breaths_fire=True),
		Creature('Lizard man', 15, 10),
		Wizard('Evil Wizard', 50, 10)
	]
	# print(creatures)

	hero = Wizard('Gandolf', 50, 30)
	# print(hero)

	while True:
		active_creature = random.choice(creatures)
		print("")
		print("Your strength is {}".format(hero.strength))
		print(Fore.YELLOW + "{} has appeared from a dark forest!!!".format(active_creature.name))
		print(Style.RESET_ALL)
		cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')

		if cmd == 'a':
			result = hero.attack(active_creature)
			if result:
				creatures.remove(active_creature)
				if len(creatures) == 0:
					print()
					print(Fore.MAGENTA + "You have defeated all the creatures!!!!!!!!!")
					print(Style.RESET_ALL)
					break
			else:
				break

		elif cmd == 'r':
			print('The wizard has become unsure of his power and flees!')
		elif cmd == 'l':
			for creature in creatures:
				print(" * {} Level:{}".format(creature.name, creature.level))

		else:
			print("exit...")
			break


if __name__ == '__main__':
	main()
