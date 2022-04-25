#with语句：上下文管理器
#with可以自动管理上下文资源，不论什么原因跳出with块，都能确保文件正确的关闭，达到释放资源的目的

#使用with语句实现123.jpg文件的复制：
with open("123.jpg","rb") as src_file:
    with open("copy2.jpg","wb") as copy_file:
        copy_file.write(src_file.read())