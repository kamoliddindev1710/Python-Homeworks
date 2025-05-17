#task 1
import numpy as np
lst=[12.23, 13.32, 100, 36.32]

arr=np.array(lst)

print(arr)
#task 2
import numpy as np

arr=np.arange(2,11).reshape(3,3)

print(arr.ndim)

#task 3
import numpy as np

arr=np.zeros(10)
arr[6]=11
print(arr)

#task 4

import numpy as np

arr=np.arange(12,38)

print(arr)
#task 5
import numpy as np

arr=np.array([[1,2,3],[4,5,6]])

nwarr=arr.astype(float)

print(nwarr.dtype)

#task 6
import numpy as np

def celcius_to_farangeit(nw_lst:list):
    new_arr=np.array(nw_lst)
    return (new_arr*9/5) +32


def farangeit_to_celcius(nw_lst:list):
    new_arr=np.array(nw_lst)
    return (new_arr-32) *9/5

path=input("Choose the path \n [1] Celcius to Fahrenheit \n [2] Fahrenheit to Celcius ")

if path=='1':
    clst=[]
    temp=input("Enter the celcius degress with comma ")

    clst=temp.split(',')
    try:
        clst=[float(x) for x in clst]
    except Exception as ex:
        print("Enter the only numbers ")
    
    cresult=celcius_to_farangeit(clst)
    print(f'The result in fahranheit :{cresult}')
elif path=='2':
    flst=[]
    temp=input("Enter the fahranheit degress with comma ")

    flst=temp.split(',')
    try:
        lst=[float(x) for x in flst]
    except Exception as ex:
        print("Enter the only numbers ")
    
    fresult=farangeit_to_celcius(flst)
    print(f'The result in celcius :{fresult}')
else:
    print("Enter only 1 or 2")

#task 7
import numpy as np

arr=np.array([10,20,30])
new_arr=np.array([40,50,60,70,80,90])
try:
    adding_arr=np.append(arr,new_arr)
except Exception as ex:
    print(ex)
print(adding_arr)

#task 8
import numpy as np
try:
   top=int(input("Enter the high number of random numbers"))
except Exception as Exception:
 print(ex) 

random_array=np.random.randint(0,top,size=(1,10))

print(random_array)

rmean=np.mean(random_array)

rmedian=np.median(random_array)

rvar=np.var(random_array)

print(f' Mean:{rmean}\n Median:{rmedian}\n Variation:{rvar}')

#task 9
import numpy as np

random_array=np.random.random(size=(10,10))

arr_max=np.max(random_array)
print(random_array)

arr_min=np.min(random_array)

print(f' Max:{arr_max}\n Min:{arr_min}')

#task 10
import numpy as np
try:
    top=int(input("Enter the high number of random numbers"))
except Exception as ex:
    print(ex)
    
random_array=np.random.randint(0,100,size=(3,3,3))

print(random_array)

