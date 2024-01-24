from collections import OrderedDict

dict = {}
line = 'which is better python 2 or python 3'
line = line.split()
for word in line:
    data = dict.get(word)
    if data is None:
        dict.update({word : 1})
    else:
        data += 1
        dict.update({word: data})

dict = OrderedDict(sorted(dict.items()))
for key, data in dict.items():
    print(f'{(key, data)}')