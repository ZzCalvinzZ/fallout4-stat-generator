from tabulate import tabulate
import random

class FalloutCharacter(object):

	def __init__(self):
		self.stats = [
			{'name': 'strength', 'count': 1 },
			{'name': 'perception', 'count': 1 },
			{'name': 'endurance', 'count': 1 },
			{'name': 'charisma', 'count': 1 },
			{'name': 'intelligence', 'count': 1 },
			{'name': 'agility', 'count': 1 },
			{'name': 'luck', 'count': 1 },
		]

		self.distribution_count = 21
		self.generate()

	def generate(self):
		for point in range(self.distribution_count):
			stat = random.randint(0, 6)
			self.stats[stat]['count'] += 1

	def display(self):
		format = []
		headers = []
		for stat in self.stats:
			format.append(stat['count'])
			headers.append(stat['name'])

		print tabulate([format], headers=headers)

character = FalloutCharacter().display()

