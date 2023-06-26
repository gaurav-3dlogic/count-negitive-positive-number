a = [10, -21, 4, -45, 66, -93, 1]
 
 
pos_num,neg_num = 0 , 0 

for i in a:
    if i >= 0:
        pos_num += 1 
    else:
        neg_num += 1
        
        
print("Positive number is",pos_num)
print("Negitive number is",neg_num)
