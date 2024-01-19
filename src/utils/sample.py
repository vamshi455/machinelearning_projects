## Reverse of a string
# str_name = 'vamshi'

# l = len(str_name) #Len of string
# i = 0   #initialize
# s = ''  #to hold final string

# while i < l:
#     s = s + str_name[l-1]
#     l = l-1
       
# print(s)


## list comprehensions

# lst = [1,2,3,4,5,6]
# lst_new = list(map(lambda x: x+1, lst))  # list comprehsions
# print(lst_new)

##smallest value and largest value 
# lst = [1,2,3,4,5,6]
# print(min(lst))
# print(max(lst))

##least value from dictionary
dict_new = { 
                'x' : -2,
                'y' : -1
           }

v = dict_new['x'] #-1

for key in dict_new:
    if v >= dict_new[key]: 
        v = dict_new[key]

print(v)




