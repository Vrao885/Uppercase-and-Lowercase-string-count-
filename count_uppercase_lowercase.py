def calculate_uppercase_and_lowercase(string):
    uppercase_count= 0 
    lowercase_count = 0
    for i in string: 
        if i.isupper()== True:
            uppercase_count+=1
            
            
        elif i.islower() ==True:
            lowercase_count +=1
    return uppercase_count, lowercase_count      
string1= input("enter a string : ")

result=calculate_uppercase_and_lowercase(string1)
print ("The number of upper case letters is:", result[0])   #printing the first element
print ("The number of lower case letters is:", result[1])    # printing second element










