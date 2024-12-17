
# with open("file.txt", 'a') as f:
#   for i in range(5):
#     res = input()
#     f.write(res+'\n')


# f.close()

# Read methods

with open('file.txt', 'r') as f:
    res = f.readlines()
    print(res)
f.close()