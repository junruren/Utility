import sys

from os import walk, path

def main():
	source_filenames = []
	if len(sys.argv) <= 1:
		for (dirpath, dirnames, filenames) in walk("."):
			for filename in filenames:
				filepath = path.join(dirpath, filename)
				if filepath is not path.relpath(__file__):
					source_filenames.append(filepath)
	else:
		source_filenames.extend(sys.argv[1:])
	for source_filename in source_filenames:
		source_file = open(source_filename, "r")
		line_count = 1
		for line in source_file:
			if "\t" in line:
				print(source_filename + ":" + str(line_count) + " tab found!")
			if len(line) > 80:
				print(source_filename + ":" + str(line_count) + " exceeds 80 chars")
			line_count += 1

if __name__ == "__main__":
	main()
