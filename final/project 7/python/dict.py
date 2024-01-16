d = {'Anushka':90, 'Jayraj':78, 'Sunil':80, 'Sampada':85}
print(d)
l = d.keys()
print(l)
b = d.values()
print(b)
del d['Jayraj']
d['vaishnavi'] = 75
print(d)
marks = d['Sunil']
print(marks)
if('harman' in d):
	print("yes")
else:
	print("no")
print(len(d))	   
for i in d:
	print(i,d[i])
	