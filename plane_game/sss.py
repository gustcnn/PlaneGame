#--*--coding:utf-8
#Author:cnn
import random

pos_0 = (0, 0, 120, 124)
#round(x,2)控制小数点位数
random_x=round(random.uniform(0,480),2)
list_pos=list(pos_0)
list_pos[1]=random_x
random_tuple=tuple(list_pos)
print(random_tuple)
print(type(random_tuple))