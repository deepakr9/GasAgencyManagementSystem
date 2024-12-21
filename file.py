
# # with open("file.txt", 'a') as f:
# #   for i in range(5):
# #     res = input()
# #     f.write(res+'\n')


# # f.close()

# # Read methods

# with open('file.txt', 'r') as f:
#     res = f.read()
#     with open('file4.txt', 'a') as f1:
#         f1.write(res)
#     f1.close()
# f.close()

# with open('file4.txt', 'r') as f3:
#     result = f3.read()
#     print(result)
# f3.close()

with open('image.jpg', 'rb') as f1:
    res = f1.read(95000)
    with open('car.jpg', 'wb') as f2:
        f2.write(res)
        f2.close()
    f1.close()