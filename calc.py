import sys

#decide the type of user input
def decide_input_type(user_input):
    user_input = list(user_input)
    input_type = False  

    #if there is a single number input, means no "(" 
    if "(" not in user_input:
        input_type = "single_number"
    elif user_input.count("(") == 1:
        input_type = "single_method"
    else:
        input_type = "nested"

    return input_type


#deal with single function, add or multiply, can extend to more 
def single_function(user_input):
    user_input = list(user_input)
    if user_input[1] == "a":
        method = "add"
        result = 0
    elif user_input[1] == "m":
        method = "mul"
        result = 1

    length = len(user_input)
    number_str =""

    if method == "add":
        #from the number after "add "
        for index in range(5,length-1):
            if user_input[index] != " ":
                number_str += user_input[index]
            else:
                add_number = int(number_str)
                result += add_number
                number_str = ""
        add_number = int(number_str)
        result += add_number

    elif method == "mul":
        result = 1
        #from the number after "multiply ""
        for index in range(10,length-1):
            if user_input[index] != " ":
                number_str += user_input[index]
            else:
                multi_number = int(number_str)
                result *= multi_number
                number_str = ""
        multi_number = int(number_str)
        result *= multi_number
 
    return result 

#find the index of innnest "(" and return it
def find_inner_index(user_input):
    number_of_multi = user_input.count("(multiply") 
    number_of_add = user_input.count("(add")
    number_of_functions = number_of_add+number_of_multi
    index = 0
    inner_index = -1
    for element in user_input:
        inner_index += 1
        if element == "(multiply" or element == "(add":
            index+=1
            #if it matches the number of function, means it is the most inside function
            if index == number_of_functions:
                break 
    return inner_index 



def solve_function(user_input):
    user_input = user_input.split(" ")
   
    inner_index = find_inner_index(user_input)
    single_string = ""

    #get the inner string
    for i in range(inner_index,len(user_input)):
        element = user_input[i]
        if ")" not in (element):
            single_string += element
            single_string += " " 
        else:
            element = element.replace(")","")
            element = element + ")"
            single_string += element
            outter_index = i 
            break
    
    #clear the inner function find 
    user_input[inner_index:outter_index+1] = []
    
    result = single_function(single_string)
    #replace the inner function with its calculation result
    user_input.insert(inner_index,result)
    
    #get the new string as user input
    new_string = ''
    for e in user_input:
        new_string = new_string +str(e) + " "  
    if ")" not in new_string:
        new_string = new_string[:-1]
        new_string = new_string+")"
            
        
    return new_string
        


def main():
    user_input = sys.argv[1]

    output = -1

    #get the input type
    input_type = decide_input_type(user_input)


    if input_type == "single_number":
        output = user_input
    elif input_type == "single_method":
        output = single_function(user_input)          
    else:
        #repeatly calculated the inner function until we have single function
        while (user_input.count("add")+user_input.count("multiply"))>1:
            user_input = solve_function(user_input)
        
        #if the second to last char is " ",get rid of it 
        if user_input[-2] == " ":
            length = len(user_input)
            index = length-2
            user_input = user_input[:index] + user_input[index + 1:]

        #get the result of single function 
        output = single_function(user_input)
      
    #print the output to user
    print(output)

            
main()