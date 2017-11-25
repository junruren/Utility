import sys
from collections import defaultdict
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
	char_string = "[80 Chars] (-X): "
	tab_string = "[Indentations] (-X): tabs found at "
	for source_filename in source_filenames:
		source_file = open(source_filename, "r")
		line_count = 1
		lines_have_tabs = defaultdict(set)
		lines_over_80 = defaultdict(set)
		for line in source_file:
			if "\t" in line:
				lines_have_tabs[source_filename].add(line_count)
			if len(line) > 80:
				lines_over_80[source_filename].add(line_count)
			line_count += 1
		source_file.close()
	# print results
	for (filename, lines) in lines_have_tabs.items():
		tab_string += filename[2:] + ":"
		line_str = ""
		for (idx, line) in enumerate(list(lines)):
			line_str += str(line)
			if idx < len(lines) - 1:
				line_str += ", "
		tab_string += line_str + "; "
	for (filename, lines) in lines_over_80.items():
		char_string += filename[2:] + ":"
		line_str = ""
		for (idx, line) in enumerate(list(lines)):
			line_str += str(line)
			if idx < len(lines) - 1:
				line_str += ", "
		char_string += line_str + "; "
	if len(lines_over_80):
		print(char_string)
	if len(lines_have_tabs):
		print(tab_string)


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
