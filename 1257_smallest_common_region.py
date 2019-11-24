class Solution:
	def findSmallestRegion(self, regions, region1, region2):
		source = [ r[0] for r in regions]
		d = {}

		for r in regions:
			node = r[0]
			d[node] = []
			for sub_r in r[1:]:
				if sub_r in source:
					source.remove(sub_r)
				d[node].append(sub_r)

		queue = []

		for sub_r in d[source[0]]:
			queue.append((sub_r, [source[0],sub_r]))

		region1_path = []
		region2_path = []

		while queue:
			region, path = queue.pop()

			if region == region1:
				region1_path = path.copy()

			if region == region2:
				region2_path = path.copy()

			if region1_path != [] and region2_path != []:
				break

			if region in d.keys():
				for r in d[region]:
					p = path.copy()
					p.append(r)
					queue.append((r, p))

		print(region1_path)
		print(region2_path)
		l_path = region1_path if len(region1_path) >= len(region2_path) else region2_path
		s_path = region1_path if len(region1_path) < len(region2_path) else region2_path

		for r1 in reversed(l_path):
			for r2 in reversed(s_path):
				if r1 == r2:
					return r1	

regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]]
region1 = "Quebec",
region2 = "New York"

s = Solution()
print(s.findSmallestRegion(regions, region1, region2))
