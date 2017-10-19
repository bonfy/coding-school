# coding: utf-8

# [<class '__main__.T_1'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
# do this by A
# [<class '__main__.T_2'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.A'>, <class 'object'>]
# do this by D

# 先深度优先，如果有实现 method 就返回了， 如果是两个继承自同一个父类， 那这个父类之前会遍历它所有的子类 再去查找它


class A:

    def dothis(self):
        print('do this by A')


class B(A):
    pass


class C:

    def dothis(self):
        print('do this by C')


class D(A):

    def dothis(self):
        print('do this by D')


class T_1(B, C):

    pass


class T_2(B, D):

    pass


if __name__ == '__main__':
    t1 = T_1()
    print(T_1.mro())
    t1.dothis()

    t2 = T_2()
    print(T_2.mro())
    t2.dothis()
