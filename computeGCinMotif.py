import sys


def make_divid(file1):
"""
对motif进行分类 
"""
	types = {}
	with open (file1. "r") as file:
		for line in file:
			array = line.strip().split(",")
			listname = str(len(array[3])) + "base"
			types[listname]  = []
"""确定motif的类型（碱基长度），每个motif一个列表"""

	with open (file1, "r") as file:
		for line in file:
			array = line.strip().split(",")
			listname = str(len(array[3])) + "base"
			types[listname].append(array[3])
"""向每个motif中填入长度相符的数据"""

	return types

def compute(types):
	for base in types.keys():
		total = ''.join(types[base])
		print(base, float(total.count("G")+total.count("C"))/len(total)*100)

def main():
	file1 = sys.argv[1]
	types = make_divid(file1)
	compute(types)

if __name__ = "__main__"
	main()

