import sys

def get_gene(line):
	gene = []
	for i in line.strip().split(",")[13].strip().split("/"):
		gene.append(i)
	return gene


def get_annotation(file2):
	annnotaion = {}
	with open (file2, "r") as file:
		for line in file:
			array = line.strip().split("\t")
			annotaion[array[2]] = array[3]
	return annotation

def annotation(gene, annotaion):
	result = []
	for gen in gene:
		if gene in annotation.keys():
			result.append(annotation[gene])
		else:
			result.append(gen)
	return ','.join(result)

def main():
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	annotation = get_annotation(file2)
	with open (file1, "r") as file:
		for line in file:
			gene = get_gene(line.strip())
			result = annotation(gene, annotation)
			print(line.strip().split()[8:10],",", line.strip().split()[11], ",",line.strip().split()[2],",", result)
if __name__ == "__main__":

	main()

