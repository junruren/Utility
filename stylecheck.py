import sys

from os import walk, path

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

ignore_dirs = [".git"]
source_extensions = [".java", "README"]

def main():
	source_filenames = make_source_filenames()
	for source_filename in source_filenames:
		source_file = open(source_filename, "r")
		line_count = 1
		lines_have_tabs = []
		lines_over_80 = []
		for line in source_file:
			if "\t" in line:
				lines_have_tabs.append(line_count)
			if len(line) > 80:
				lines_over_80.append(line_count)
			line_count += 1
		if len(lines_over_80) > 0:
			print(
					source_filename 
					+ bcolors.FAIL
					+ " exceeds 80 chars"
					+ bcolors.ENDC
					+ " at line " 
					+ str(lines_over_80)
				)
		if len(lines_have_tabs) > 0:
			print(
					source_filename 
					+ bcolors.FAIL 
					+ " has tabs"
					+ bcolors.ENDC
					+ " at line " 
					+ str(lines_have_tabs) 
				)

def make_source_filenames():
	source_filenames = []
	my_path = "./" + path.relpath(__file__)
	if len(sys.argv) <= 1:
		for (dirpath, dirnames, filenames) in walk("."):
			if is_ignored(dirpath):
				continue
			else:
				for filename in filenames:
					if not is_valid_extension(filename):
						continue
					filepath = path.join(dirpath, filename)
					if filepath != my_path:
						source_filenames.append(filepath)
	else:
		source_filenames.extend(sys.argv[1:])
	return source_filenames

def is_valid_extension(filename):
	for source_extension in source_extensions:
		if filename.endswith(source_extension):
			return True
	return False

def is_ignored(dirpath):
	for ignore_dir in ignore_dirs:
		if ignore_dir in dirpath:
			return True
	return False

if __name__ == "__main__":
	main()