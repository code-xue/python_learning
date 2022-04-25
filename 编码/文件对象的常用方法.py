#read([size]):从文件中读取size个字节或字符的内容返回，省略则默认读取到文件末尾
file=open("test1.txt","r")
print(file.read(1))
file.close()

#readline:读取一行内容
#readlines:把每一行都作为独立的字符串对象，以列表的形式返回

#write(str):将字符串str内容写入文件
file1=open("test2.txt","w")
file1.write("hello")
file1.close()
#writelines(s_list):将字符串列表写入文本文件，不添加换行符
lst=["hello","world"]
file2=open("test2.txt","w")
file2.writelines(lst)
file2.close()

#seek(offset[,whence]):把文件指针移动到新的位置，offset表示相对于whence的位置
#offset为正往结束方向移动，为负往开始方向移动
#whence不同的值表示不同的含义：
#0:从文件头开始计算（默认）
#1:从当前位置开始计算
#2:从文件尾开始计算
file3=open("test1.txt","r")
file3.seek(2)
print(file3.read())
file3.close()

#tell:返回文件指针的当前位置

#flush:把缓冲区的内容写入文件，但不关闭文件

#close:把缓冲区的内容写入文件，同时关闭文件，释放文件对象相关资源