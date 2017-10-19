from assignments import MaxSizeList

a = MaxSizeList(1)
b = MaxSizeList(3)

a.push('hey')
a.push('hi')
a.push('let')
a.push('go')

b.push('hey')
b.push('hi')
b.push('let')
b.push('go')

print(a.get_list())  # ['go']
print(b.get_list())  # ['hi', 'let', 'go']
