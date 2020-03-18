#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
print("猜拳遊戲！ 1 = 剪刀/ 2 = 石頭/ 3 = 布/ 4 = 不玩了")
name =['哈','剪刀','石頭','布']
i = 0
while (True):   
    i=i+1
    num = random.randint(1,3)
    guess = int(input("請輸入你猜的數字："))
    if guess > 3 or guess < 1:
        if guess == 4:
            break
        else: 
            print("請輸入1~3!")
            continue
    elif guess == num:
        print("你出的是:%s" %name[guess]+"\n" + "我出的是:%s" %name[num])
        print("平手！\n")
    elif (guess-num)==-1 or (guess-num)==2 :
        print("你出的是:%s" %name[guess]+"\n" + "我出的是:%s" %name[num])
        print("你輸了~\n")    
    else:
        print("你出的是:%s" %name[guess]+"\n" + "我出的是:%s" %name[num])
        print("你贏了~\n")
        
print("你總共猜了%d" %(i-1) + "次",end = '')
print(",古德掰...")


# In[ ]:




