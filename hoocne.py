import math 
import numpy as np 

import ham_thuat_toan as fl 
print("Chương trình tính giá trị của đa thức.")
# gia tri cua he so da thúc
a = np.array([ -120 , 274 , - 225 , 85 , -15 , 1 ] , dtype = float )
# gia tri x can tinh 
x = 2.5

b = fl.tinh_gia_tri(a , x ) 
print(b)

