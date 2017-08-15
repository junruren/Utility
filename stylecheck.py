import sys

from os import walk

def main():
	source_files = []
	if len(sys.argv) <= 1:
		for (dirpath, dirnames, filenames) in walk("."):
			source_files.extend(filenames)
	else:
		source_files.extend(sys.argv[1:])
	
	print(source_files)

if __name__ == "__main__":
	main()
