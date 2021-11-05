from concept import Concept
from motivation import Motivation
from appearance import Appearance


def run():
	concept = Concept()
	motivations = [Motivation() for _ in range(3)]
	appearance = Appearance()

	print(f'Appearance: {appearance.feature}\n')

	print(f'Concept: {concept.modifier}, {concept.noun}\n')

	for motivation in motivations:
		print(f'Motivation: {motivation.verb}, {motivation.noun}')

if __name__ == '__main__':
	run()