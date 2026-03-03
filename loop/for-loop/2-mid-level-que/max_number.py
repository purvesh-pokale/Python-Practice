#. Find the maximum number from a given list. 
lst=[20,63,16,38,46,27,49]
max_num =lst[0]           #assum it is max number because we need somthing to compare with other number

for i in lst:
    if(i>max_num):
        max_num=i
print("max number-",max_num)

'''
o/p
max number- 63
'''

'''
Dry run
| Iteration | i  | max_num Before | Condition (i > max_num) | max_num After |
| --------- | -- | -------------- | ----------------------- | ------------- |
| 1         | 20 | 20             | False                   | 20            |
| 2         | 63 | 20             | True                    | 63            |
| 3         | 16 | 63             | False                   | 63            |
| 4         | 38 | 63             | False                   | 63            |
| 5         | 46 | 63             | False                   | 63            |
| 6         | 27 | 63             | False                   | 63            |
| 7         | 49 | 63             | False                   | 63            |

'''