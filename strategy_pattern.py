

def brute_force(nums, x): # n^2
	results = []
	for n in nums: # n
		if x - n in nums: # n
			results.append((x, x - n))
	return results


def optimised(nums, x): # total nlogn
	results = []
	nums.sort() # nlogn

	i = 0
	j = len(nums) - 1

	while i < j: # n
		pair_sum = nums[i] + nums[j] 
		
		if pair_sum == x:
			results.append(nums[i], nums[j])
			i += 1
			j -= 1

		elif pair_sum > x:
			j -= 1

		else:
			i += 1

	return results



class PairSumToX:
	def __init__(self, strategy=optimised)
		self._strategy = strategy

	def run(self, nums, x):
		return self._strategy(nums, x)