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
newEvens= sorted(evens, reverse=True)
print(odds[0],odds[1],newEvens[0],newEvens[1],odds[2],newEvens[2])