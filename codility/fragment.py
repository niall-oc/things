import os

def split_solutions(text, delimiter="# https:"):
	"""
	Step through solutions.py scratch file and save all solutions to separate python files.
	"""
	start = text.find(delimiter)
	end = text.find(delimiter, start+1)
	while end > 0:
		code = text[start:end]
		url = code[0:code.find('\n')]
		filename = url.split('/')[-2]
		with open("{0}.py".format(filename), "w") as out_f:
			out_f.write(code)

		start = end
		end = text.find(delimiter, end+1)

if __name__ == '__main__':
	with open('solutions.py') as f:
		split_solutions(f.read(), delimiter="# https:")
