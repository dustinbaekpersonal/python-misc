# k = 3
# nums = [1,2,3,4,5,6,7]
# empt = [0] * k
# res = nums
# res = empt + res
# res[0:k] = res[-k:]

# for _ in range(k):
#     res.pop()
# nums = res

# print(nums)

k = 10

asdf = [1,2,3,4,5,]
zeros = [0] * k
zeros.extend(asdf)
print(zeros[:-k])
