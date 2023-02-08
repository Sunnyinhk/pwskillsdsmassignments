#!/usr/bin/env python
# coding: utf-8

# # Q1. Create a function which will take a list as an argument and return the product of all the numbers
# after creating a flat list.
# 
# Use the below-given list as an argument for your function.
# 
# 
# list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
# 22, 61, 34)}, [56, 'data science'], 'Machine Learning']
# 
# 
# Note: you must extract numeric keys and values of the dictionary also.

# In[14]:


list1 = [1,2,3,4, [44,55,66, True], False, (34,56,78,89,34), {1,2,3,3,2,1}, {1:34, "key2": [55, 67, 78, 89], 4: (45,
22, 61, 34)}, [56, 'data science'], 'Machine Learning']
def num_prod(a):
    n=[]
    for i in a:
        if type(i)==int:
            n.append(i)
        elif type(i) == list:
            for j in i:
                if type(j)==int:
                    n.append(j)
        elif type(i) == tuple:
            for k in i:
                if type(k)==int:
                    n.append(k)
        elif type(i) ==set:
            for l in i:
                if type(l)==int:
                    n.append(l)
        elif type(i)== dict:
            x = list(i.values())
            
            for b in x:
                if type(b)==int:
                    n.append(b)
                elif type(b) == list:
                    for o in b:
                        if type(o)==int:
                            n.append(o)
                elif type(b) == tuple:
                    for p in b:
                        if type(p)==int:
                            n.append(p)
    return n

l1 = num_prod(list1)


# In[18]:


l2 =num_prod(list1)
from functools import reduce
reduce(lambda x,y: x*y, l2)


# Q2. Write a python program for encrypting a message sent to you by your friend. The logic of encryption
# should be such that, for a the output should be z. For b, the output should be y. For c, the output should
# be x respectively. Also, the whitespace should be replaced with a dollar sign. Keep the punctuation
# marks unchanged.
# 
# 
# Input Sentence: I want to become a Data Scientist.
# 
# 
# Encrypt the above input sentence using the program you just created.
# 
# 
# Note: Convert the given input sentence into lowercase before encrypting. The final output should be
# lowercase.

# In[150]:


input_text="I want to become a Data Scientist"
key = 25
ledger = "abcdefghijklmnopqrstuvwxyz"
output_text =""
input_text=input_text.lower()
for char in input_text:       
    if char==" ":
        output_text=output_text + "$"
    else:
        inputIndex = ledger.find(char)
        outputIndex = inputIndex + key
        if outputIndex >=len(ledger):
            outputIndex = outputIndex-len(ledger)
        elif outputIndex < 0:
            outputIndex = outputIndex + len(ledger)
        output_text = output_text + ledger[outputIndex]
      
print(output_text)

   


# In[ ]:




