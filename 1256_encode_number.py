class Solution:
	def encode(self, num):
		
		s = 0
		cnt = 1
		while True:
			s += 2**cnt

			if s > num:
				n = num - s + 2**cnt -1
				break
			cnt += 1

		result = str(bin(n).replace("0b", ""))
		
		if len(result) < cnt:
			for i in range(cnt-len(result)):
				result = '0'+result
				
		return result

s = Solution()
print(s.encode(23))
