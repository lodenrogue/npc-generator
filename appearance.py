import random
from file_utils import FileUtils

APPEARANCE_FILE = 'appearance.txt'

class Appearance:

	def __init__(self):
		file_utils = FileUtils()
		features = file_utils.read_file(APPEARANCE_FILE)
		self.feature = random.choice(features)
