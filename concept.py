import random
from file_utils import FileUtils

NPC_MODIFIER_FILE = 'npc_modifier.txt'
NPC_NOUN_FILE = 'npc_noun.txt'

class Concept:

	def __init__(self):
		file_utils = FileUtils()
		npc_modifiers = file_utils.read_file(NPC_MODIFIER_FILE)
		npc_nouns = file_utils.read_file(NPC_NOUN_FILE)

		self.modifier = random.choice(npc_modifiers)
		self.noun = random.choice(npc_nouns)
