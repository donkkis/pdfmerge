import argparse
from pypdf import PdfMerger


def merge(args):
	pdfs = list(args)
	merger = PdfMerger()

	for pdf in pdfs:
    		merger.append(pdf)

	merger.write("result.pdf")
	merger.close()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('args', nargs='*')
	args = parser.parse_args()
	merge(args.args)
