
import os
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
    student_query=[]
    while True:
        id=""
        name=""
        if os.path.exists(filename):
            mode=input("按id查找请输入1，按名字查找请输入2:")
            if mode=="1":
                id=input("请输入要查找的id:")
            elif mode=="2":
                name=input("请输入要查找的名字:")
            else:
                print("输入错误，请重新输入")
                search()
            with open(filename,"r",encoding="utf-8") as rfile:
                student_info=rfile.readlines()
            for item in student_info:
                d=dict(eval(item))
                if id!="":
                    if d["id"]==id:
                        student_query.append(d)
                elif name!="":
                    if d["name"]==name:
                        student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer=input("是否继续查找:y/n")
            if answer=="y" or answer=="Y":
                search()
            else:
                break
        else:
            print("找不到学生信息")
            return
def show_student(lst):
    if len(lst)==0:
        print("没有查询到学生信息")
        return
    format_title="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    print(format_title.format("id","名字","c语言成绩","python成绩","java成绩","总成绩"))
    format_data="{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}"
    for item in lst:
        print(format_data.format(item["id"],
                                 item["name"],
                                 item["c"],
                                 item["python"],
                                 item["java"],
                                 int(item["c"])+int(item["python"])+int(item["java"])))
def delete():
    while True:
        student_id=input("请输入要删除的学生id：")
        if student_id!= '':
            if os.path.exists(filename):
                with open(filename,"r",encoding="utf-8") as file:
                    student_old=file.readlines()
            else:
                student_old=[]
            flag=False    #标记是否成功删除
            if student_old:
                with open(filename,"w",encoding="utf-8") as wfile:
                    d={}
                    for item in student_old:
                        d=dict(eval(item))
                        if(d["id"]!=student_id):
                            wfile.write(str(d)+"\n")
                        else:
                            flag=True
                    if flag:
                        print("id为%s的学生信息已删除" % student_id)
                    else:
                        print("找不到id为%s的学生信息" % student_id)
            else:
                print("找不到学生信息")
                break
            show()
        else:
            print("请输入信息")
            break
        answer=input("是否继续删除:y/n:")
        if answer=='y' or answer=='Y':
            continue
        else:
            break
def modify():
    show()
    while True:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as rfile:
                student_old = rfile.readlines()
        else:
            print("找不到学生信息")
            break
        student_id=input("请输入要修改的学生id：")
        with open(filename,"w",encoding="utf-8") as wfile:
            if student_id!='':
                d={}
                flag=False

                for item in student_old:
                    d=dict(eval(item))
                    if(d["id"]==student_id):
                        while True:
                            print("请输入修改后的信息")
                            try:
                                d["name"]=input("请输入名字：")
                                d["c"]=input("请输入c语言成绩：")
                                d["python"]=input("请输入python成绩")
                                d["java"]=input("请输入java成绩")
                            except:
                                print("输入有误，请重新输入")
                            else:
                                break
                        wfile.write(str(d)+"\n")
                        print("修改成功")
                        flag=True
                    else:
                        wfile.write(str(d) + "\n")
                if not flag:
                    print("找不到id为%s的学生" % student_id)
            else:
                print("请输入信息")
        show()
        answer=input("是否继续修改学生信息:y/n")
        if answer=='y' or answer=='Y':
            continue
        else:
            break
def sort():
    pass
def total():
    if os.path.exists(filename):
        with open(filename,"r",encoding="utf-8") as rfile:
            student_info=rfile.readlines()
        if student_info:
            print("一共有%d名学生" % len(student_info))
        else:
            print("没有学生信息")
    else:
        print("还没有录入学生信息")
def show():
    if os.path.exists(filename):
        student_lst=[]
        with open(filename,"r",encoding="utf-8") as rfile:
            student=rfile.readlines()
        if student:
            for item in student:
                student_lst.append(dict(eval(item)))
            show_student(student_lst)
        else:
            print("无学生信息")
    else:
        print("还没有录入学生信息")

if __name__ == "__main__":
    main()