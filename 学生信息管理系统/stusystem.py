filename="student.txt"
def main():
    while True:
        menu()
        choice = int(input("请选择"))
        if choice in range(0,8):
            if choice==0:
                answer = input("确定要退出系统吗?y/n")
                if answer=='y' or answer=='Y':
                    print("谢谢您的使用")
                    break
                else:
                    continue
            elif choice==1:
                insert()
            elif choice==2:
                search()
            elif choice==3:
                delete()
            elif choice==4:
                modify()
            elif choice==5:
                sort()
            elif choice==6:
                total()
            elif choice==7:
                show()

def menu():
    print("==============================学生信息管理系统================================")
    print("----------------------------------功能菜单-----------------------------------")
    print("\t\t\t\t\t\t1.录入学生信息")
    print("\t\t\t\t\t\t2.查找学生信息")
    print("\t\t\t\t\t\t3.删除学生信息")
    print("\t\t\t\t\t\t4.修改学生信息")
    print("\t\t\t\t\t\t5.排序")
    print("\t\t\t\t\t\t6.统计学生总人数")
    print("\t\t\t\t\t\t7.显示所有学生信息")
    print("\t\t\t\t\t\t0.退出系统")
    print("---------------------------------------------------------------------------")


def insert():
    student_list=[]
    while True:
        id=input("请输入学生id")
        if not id:
            break
        name=input("请输入学生名字")
        if not name:
            break
        try:
            c=int(input("请输入c语言成绩"))
            python=int(input("请输入python成绩"))
            java=int(input("请输入java成绩"))
        except:
            print("输入格式有误，成绩必须是整数")
            continue
        #将学生信息以字典方式存储
        stu={"id":id,"name":name,"c":c,"python":python,"java":java}
        #将学生信息保存在列表中
        student_list.append(stu)
        answer=input("是否继续缇添加?y/n")
        if answer=='y' or answer=='Y':
            continue
        else:
            break

    #调用save函数保存信息到本地文件中
    save(student_list)
    print("学生信息录入完毕")
def save(lst):
    try:
        stu_file=open(filename,"a",encoding="utf-8")
    except:
        stu_file=open(filename,"w",encoding="utf-8")
    for item in lst:
        stu_file.write(str(item)+'\n')
    stu_file.close()

def search():
    pass
def delete():
    pass
def modify():
    pass
def sort():
    pass
def total():
    pass
def show():
    pass

if __name__ == "__main__":
    main()