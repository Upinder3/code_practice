class Solution:
	def generateSentences(self, synonyms, text):
		import collections
		import itertools
		uf = {}
		
		def union(x, y):
			uf[find(y)] = find(x)
			
		def find(x):
			uf.setdefault(x, x)
			if uf[x]!=x:
				uf[x] = find(uf[x])
			return uf[x]
		
		for a,b in synonyms:
			union(a, b)
			
		d = collections.defaultdict(set)
		for a, b in synonyms:
			root = find(a)
			d[root] |= set([a, b])
		txt = text.split()
		res = []
		
		for t in txt:
			if t not in uf:
				res.append([t])
			else:
				r = find(t)
				res.append(list(d[r]))
		print(res)
		fin_res = [" ".join(sentence) for sentence in itertools.product(*res)]
		return sorted(fin_res)

synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"

s = Solution()
import pprint

pprint.pprint(s.generateSentences(synonyms, text))
