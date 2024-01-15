# l = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27456), ('Jack Kallis', 25534), ('Virat Kohli', 24736)]
# l.sort(key = lambda x: x[1])
# print(sortedList)
# l = [1,2,3,4,5,6,7,8,9,10]
# sq = list(map(lambda x: x**2, l))
# print(sq)
# tpstr = tuple(map(lambda x: str(x), l))
# print(tpstr)
# import functools
# l = [i for i in range(1,26)]
# l1 = functools.reduce(lambda x, y: x*y, l)
# print(l1)
# l = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
# l1 = list(filter(lambda x : x % 2 == 0 and x % 3 == 0, l))
# print(l1)
# l = ['python', 'php', 'aba', 'radar', 'level']
# palindrome = list(filter(lambda x: x if x[::-1] == x else False, l))
# print(palindrome)