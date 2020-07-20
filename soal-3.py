
data_list = [5,3,2,8,1,4]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
odds = []
evens = []
for i in new_list:
    if i % 2 == 0:
      (evens.append(i))
    else:
        odds.append(i)

print(odds+evens)