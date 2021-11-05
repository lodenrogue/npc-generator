class FileUtils:

	def read_file(self, filename):
		with open(filename, 'r') as f:
			return [line.replace('\n', '') for line in f.readlines()]
		