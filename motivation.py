import random
from file_utils import FileUtils

MOTIVATION_VERB_FILE = 'motivation_verb.txt'
MOTIVATION_NOUN_FILE = 'motivation_noun.txt'

class Motivation:

	def __init__(self):
		file_utils = FileUtils()
		motivation_verbs = file_utils.read_file(MOTIVATION_VERB_FILE)
		motivation_nouns = file_utils.read_file(MOTIVATION_NOUN_FILE)

		self.verb = random.choice(motivation_verbs)
		self.noun = random.choice(motivation_nouns)
