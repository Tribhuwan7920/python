name = "tribhuwan sharma"

# len function
print(len(name))

# endswith function 
print(name.endswith("sharma"))

# count function 
print(name.count("a"))
print(name.count("tr"))

# capatalize function 
print(name.capitalize())

# find function 
# a = input("enter string : ")
# print(name.find(a) , name[name.find(a)])

# replace function 
print(name.replace("sharma","singh"))
print(name)

# question 1 
# name = input("enter your name : ")
print("good afternoon "+name)

# question 2
statement = "i am a amazing person"
print(statement.replace("i am","tribhuwan sharma is"))

# question 3
st = "this    is   a   string   with  double  spaces"
print(st.find("  "))

# question 4 
for i in range(st.count("  ")):
    st = st.replace("  "," ")
print(st)

# question 4
letter = "dear\n\t tribhuwan sharma, please keep silence"
print(letter)