# 打开文件，选择模式
file1 = open("1.txt", "wb");
# 获取属性
print(file1.name);

print(file1.mode);

# 写入文件
file1.write("hello write file!");

# 关闭文件
file1.close();
