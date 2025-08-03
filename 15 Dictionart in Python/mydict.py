d = {'name':'coder','age':25}

#empty dict
# d = {}

#Accesing dictionary values
print(d['name'])#access value by key
print(d.get('age'))#safer way#return none if no element found
print(d.get('city','Bangalore'))

#Add or update items
d['city'] = 'Bangalore' #add the item
d['name'] = 'Bob'#update
d2 = {'designation':'Software Developer', 'skill':'python'}
d.update(d2)
print(d)

#Remove items form dictionary
d.pop('age')#removees item
d.popitem()#remove last item
del d['name'] #delete specific key
d.clear() #remove all items
print(d)


#.keys(),.values(),.items()
d2 = {'designation':'Software Developer', 'skill':'python'}
print(d2.keys())
print(d2.values())
print(d2.items())

#To fetch oky keys and values
for key,value in d2.items():
    print(key,value)

#Nested dictionary (JSON)
person = {
    'name':'bob',
    'address':{'city':'Mysore','pin':57001}
}
#acces only his city
print(person['address']['city'])

#len(),sorted

#Merged
d1 = {'Domain':'Python'}
d2 = {'Topic':'Dictionary'}
merged = d1 | d2
print(merged)