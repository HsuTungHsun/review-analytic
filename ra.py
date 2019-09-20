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

#filter
new = []
for d in data: #d is string , data = 1million piece of data list
	if len(d) < 100:  #len(d) = length of d < 100
		new.append(d)
		#print('There are :', len(new), 'piece of data string length below 100')
		#↑if this situation then print in for loop
print('There are :', len(new), 'piece of data string length below 100')
#↑ print after for loop end
print(new[0])

#filter word
good = []
for d in data:   #把每一筆留言叫出來
	if 'good' in d:  #if string 'good' in reviews then
	#if "True/False" then
		good.append(d) #make 'good' into good list
print('There are: ', len(good), 'piece of reviews contain good')
print(good[0])   #print first list contain 'good'

#list comprehension清單快寫法
#This code is equal to filter word 'good'
#↓ output=[(number-1) for number in reference if number % 2 ==0]
good1 = [d for d in data if 'good' in d]
#        ↑This d equal to good.append(d) 
print(good1[0])   #print first list contain 'good'

#filter bad from all word
bad = ['bad' in d     for d in data]
#       b     ool      1million datta
print(bad)