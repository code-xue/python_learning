#r:以只读方式打开文件，文件的指针会放在文件的开头
#w:以只读方式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头
#a:以追加模式打开文件，如果文件不存在则创建，文件指针在文件开头，如果文件存在，则在文件末尾追加内容，文件指针在原文件末尾
#b:以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，如rb,wb
#+:以读写方式打开文件，不能单独使用，需要与其他模式一起使用，如a+

file=open("test1.txt","r")
print(file.readlines())
file.close()

file1=open("test2.txt","w")
file1.write("python")
file1.close()

file2=open("test2.txt","a")
file2.write("python")
file2.close()

src_file=open("123.jpg","rb")
copy_file=open("copy.jpg","wb")
copy_file.write(src_file.read())
src_file.close()
copy_file.close()
