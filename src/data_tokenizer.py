import sys
import re

from pythainlp.tokenize import word_tokenize

def load_corpus(file_directory):
	corpus = []

	f = open(file_directory, 'r')
	data = f.read().splitlines()
	f.close()

	for line in data[1:]:
		comment = ''.join(x for x in line.split(':')[2:])
		corpus.append(comment)

	return corpus

def clean(doc):
	while True:
		new_doc = re.sub('[^" "\u0E00-\u0E7F]+', '', doc)
		if doc == new_doc:
			break
		else:
			doc = new_doc
	doc = doc.strip()
	return doc

def main():
	file_name = sys.argv[1]
	if not file_name:
		return

	corpus = load_corpus('../data/' + file_name)
	print('Total documents', len(corpus))

	with open('../data/tokenized/newmm/tokenized_' + file_name, 'w') as f:
		tokenized_corpus = []
		for doc in corpus:
			cleaned_doc = clean(doc)
			print(cleaned_doc)
			tokenized_doc = word_tokenize(cleaned_doc, engine='newmm')
			tokenized_doc = [word for word in tokenized_doc if word.strip() != '']
			tokenized_corpus.append(tokenized_doc)
		f.write(str(tokenized_corpus))

if __name__ == "__main__":
  main()
