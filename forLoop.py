# loops is a tool in python which is used to do repetedly work

# there are 2 type of loop in python
# 1. for loop
# 2. while loopg

# looping a string
name = "tribhuwan sharma"

for i in range(len(name)):
    print(name[i])

for i in name:
    print(i, end=",")
print()


# iterating a list 
friends= ['ankit','abhishek','pyush kumar','sahil','jonny bhaiya'] 
for i in friends:
    for j in i:
        print(i,j) 

for i in range(len(friends)):
    print(friends[i])


# # range function 
# it is a built in function which is generally use in a for loop it has three argument 

# range(start,stop,step-size)

# start => included
# end => excluded

# range(10) =>  it runs from 0 to 9
# range(2,34) => it runs from 2 to 33
# range(2,34,5) => it runs from 2 to 33 with the step size of 5


for i in range(1,2000):
    print(i)