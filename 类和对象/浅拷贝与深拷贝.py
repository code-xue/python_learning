#浅拷贝：python中拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝
#源对象与拷贝对象会引用同一个子对象

class Cpu:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1=Cpu()
disk1=Disk()
computer1=Computer(cpu1,disk1)

import copy
computer2=copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer2.cpu,computer2.disk)
#浅拷贝computer1与computer2的地址不同，但是其子对象的地址不变，都是同一个

#深拷贝：可以使用copy的deepcopy函数，递归拷贝对象中包含的子对象，
#源对象和拷贝对象所有的子对象也不相同

computer3 = copy.deepcopy(computer1)
print(computer3,computer3.cpu,computer3.disk)
#深拷贝computer1与computer3的地址不同，其子对象的地址也不同
