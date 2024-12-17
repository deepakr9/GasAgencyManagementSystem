import copy

student = {
    'name': "Deepak",
    'age': 22
}
s0 = student     #shallow copy
s1 = student.copy() #deep copy
s2 = copy.deepcopy(student) #deep copy in nested list or dict
print(student)
s1.pop('name')
s1['add'] = 'magadi road'
print(student)
print(s1)
print(s2)