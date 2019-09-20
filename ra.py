#
data = []   #empty list
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1    #equal to count = count + 1
		if count % 1000 == 0:  # % = 餘數,每1000次才印一次
			print(len(data)) #print 1000000
print(len(data))  #print data length

print(data[0])    #首段
print('-----------------')
print('\n')
print(data[999999])    #第二段
print('-----------------')