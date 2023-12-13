def frequency_analytic(s):
	dic = {}
	for chr in s:
		if chr in dic:
			dic[chr] += 1
		else:
			dic[chr] = 1
	dic = dict(sorted(dic.items()))
	dic_keys = dic.keys()
	dic_values = dic.values()
	dic_keys = list(dic_keys)
	dic_values = list(dic_values)
	for i in range(len(dic)):
		print(dic_keys[i], ":", dic_values[i])

if __name__ == "__main__":
	msg = input("input your message:")
	frequency_analytic(msg)

