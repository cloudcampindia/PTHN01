# fp = open('sample.txt', mode='r', encoding="utf-8") # (0 - 2**8)
# print(dir(fp))

# methods_on_fp = ['buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'reconfigure', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'write_through', 'writelines']
# print(len(methods_on_fp))

# data = fp.read() # "Not recommend" to use when the file size is larger and its contents are also larger enough
# print(type(data))

# data = fp.readlines()
# print(type(data))

# data = fp.readline() # default: reads the first line that is present in the file
# data = fp.readline(5) # It extracts the no: of character specified by the user

# while True:
#     try:
#         data = fp.readline().strip()
#         print(data)
#     except:
#         print("reached the end of the file")
#         break
# fp.close()

# fp = open('sample.txt', mode='r', encoding="utf-8")
# data = fp.read(5)
# print(data)

# data_1 = fp.readline(5)
# print(data_1)
# fp.close()

# fp = open('sample_1.txt', mode='r', encoding="utf-8")
# print(fp.tell())
# data = fp.read(2)
# print(data)

# fp.seek(15, 0)
# print(fp.tell())
# data = fp.read()
# print(data)

# print(fp.tell())
# fp.close()

# fp = open('sample copy.txt', mode='w', encoding="utf-8")
# s = "Welcome to Python API training offered at cloud camp\n"
# fp.write(s)
# fp.close()

# fp = open('sample_3.txt', mode='a', encoding="utf-8")
# s = "Welcome to Python API training offered at cloud camp"
# fp.write(s)
# fp.close()

# fp = open('sample.txt', mode='r', encoding="utf-8")

# for x in fp:
#     print(x)
#     break
# fp.close()

# fp = open("sample_4.txt", "w")
# s = "Welcome to Python API training offered at cloud camp"
# fp.write(s)
# print(fp.tell())
# fp.seek(0) # fp.seek(0, 0)
# data = fp.read() # Error
# print(data)
# fp.close()

# try:
#     fp = open("sample_4.txt", "w+")
#     s = "Welcome to Python API training offered at cloud camp"
#     fp.write(s)
#     print(fp.tell())

#     fp.seek(0) # fp.seek(0, 0)
#     data = fp.read()
#     print(data)
#     fp.close()
# except FileNotFoundError as e:
#     print(e)

# fp = open("sample_4.txt", "a")
# s = "\nWelcome to Python API training offered at cloud camp"
# fp.write(s)
# print(fp.tell())
# fp.seek(0) # fp.seek(0, 0)
# data = fp.read() # Error
# print(data)
# fp.close()

# try:
#     fp = open("sample_4.txt", "a+")
#     s = "\nWelcome to Python API training offered at cloud camp"
#     fp.write(s)
#     print(fp.tell())

#     fp.seek(0) # fp.seek(0, 0)
#     data = fp.read()
#     print(data)
#     fp.close()
# except FileNotFoundError as e:
#     print(e)


with open("sample_1.txt") as f:
    data = f.read()
print(len(data))


# fp = open('sample.txt', mode='r', encoding="utf-8")
# data = fp.read(5)
# print(data)
# fp.close()