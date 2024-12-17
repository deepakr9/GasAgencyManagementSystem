emp_id = [100, 101, 102, 103]
name = ['harsha', 'dhanush', 'ajay', 'lohith']
res = zip(emp_id, name)
print(res)



#multiple list
emp_id = [100, 101, 102, 103]
name = ['harsha', 'dhanush', 'ajay', 'lohith']
mob = [1111, 2222, 3333, 4444]
add = ['blg', 'mum', 'clk', 'mlg']
info = list(zip( name, mob, add))
res = dict(zip(emp_id, info))
print(res)