# string is a datatype of python (primary datatype)

# there are three waye to make a string  in python
# 1. single quoted string (' ')
# 2. double quoted string (" ")
# 3. triple quoted string (''' ''')

# single quoted string 
name_1 = 'tribhuwan sharma '
print(name_1)
print(type(name_1))

# double quoted string 
name_2 = "saim babu "
print(name_2)
print(type(name_2))

# triple quoted string
name_3 = '''it is used for 
multiline string'''
print(name_3)
print(type(name_3))

# string slicing 

# string_variable_name[start: end : step_size]
name = "tribhuwan sharma"
print(name[0])
for i in range(len(name)):
    print(name[i])
print(name[1:5])
print(name[2:])
print(name[:5])
print(name[:5:])
print(name[::3])
# negative indicing 
print( "negative indicing : ",name[-6])
for i in range(len(name)):
    # print(i)
    print(name[(len(name)-(i+1))])



# string concatination
first_name = "tribhhuwan"
last_name = "sharma"
print(first_name + " " + last_name)