#
data = []   #empty list
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1    #equal to count = count + 1
		if count % 1000 == 0:  # % = 餘數,每1000次才印一次
			print(len(data)) #print 1000000
print('There is total', len(data), 'piece of data')  #print data length

#計算平均長度

sum_len = 0  #加總長度的int
for d in data:   # d is string
	sum_len = sum_len + len(d)    #equal sum_len = sum_len + len(d)
	#print(sum_len)

print('Avg Reviews length is: ', sum_len/len(data))
