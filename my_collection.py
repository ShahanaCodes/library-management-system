from collections import namedtuple
#define a namedtuple type
point = namedtuple(typename="point", field_names=["x","y"])
#create an object

p = point(10, 20)
print(p.x)
print(p[1])

from collections import deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
print(dq)

dq.pop()
dq.popleft()
print(dq)

from collections import Counter
data = ["apple", "bananan", "apple", "orange", "banana", "apple"]
count = Counter(data)
print(count)
print(count.most_common(2))


from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

od.move_to_end('a')
print(od)

'''from collections import defaultdict
dd = dafaultdict(int)
dd['a'] += 1
print(dd)

#with default list
dd_list = defaultdict(list)
dd_list['fruits'].append('apple')
print(dd_list)'''

from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

cm = ChainMap(dict1, dict2)
print(cm['a'])
print(cm['b'])
print(cm['c'])