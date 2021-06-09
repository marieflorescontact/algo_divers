#Etape 1 : parsing

def create_list_of_elements(elements):
    return elements.split(" ")
array_of_elements = create_list_of_elements("4 + 6.5 * 8")


#Etape 2 : qualification des elements 

def qualify_type_of_elements(array_of_strings):

    for i in range(len(array_of_strings)):
        if(array_of_strings[i].isdigit()):
            array_of_strings[i] = int(array_of_strings[i])
        elif("." in array_of_strings[i]):
             array_of_strings[i] =float(array_of_strings[i])
        print(type(array_of_strings[i]))

    return(array_of_strings)

print(qualify_type_of_elements(array_of_elements))


#Etape 3 : Opérations de base

def add(first_number, second_number):
    return first_number + second_number

print(add(5, 0))

def minus(first_number, second_number):
    return first_number - second_number

print(minus(3, 9))

def multiply(first_number, second_number):
    return first_number * second_number

print(multiply(2, 0))

def true_divide(first_number, second_number):
    return first_number / second_number

print(true_divide(1, 2))


# Étapes 4 - Calcul de l'expression (approche)

mathematical_expression = create_list_of_elements("98 - 6 * 8 * 1.5 + 4 - 1 / 5")
print(qualify_type_of_elements(mathematical_expression))

def calculate_expression(expression_with_all_mathematical_operators):
    expression_after_prioritaty_operators_calculus = []
    i = 0

    while i < len(expression_with_all_mathematical_operators):
        if (expression_with_all_mathematical_operators[i] != "*" and 
            expression_with_all_mathematical_operators[i] != "/"):
            expression_after_prioritaty_operators_calculus.append(expression_with_all_mathematical_operators[i]) 
        elif (expression_with_all_mathematical_operators[i] == "*"):
            expression_after_prioritaty_operators_calculus.append(multiply(expression_after_prioritaty_operators_calculus[-1], 
            expression_with_all_mathematical_operators[i+1]))
            del expression_after_prioritaty_operators_calculus[-2]
            i+=1
        elif (expression_with_all_mathematical_operators[i] == "/"):
            expression_after_prioritaty_operators_calculus.append(true_divide(expression_after_prioritaty_operators_calculus[-1], 
            expression_with_all_mathematical_operators[i+1]))
            del expression_after_prioritaty_operators_calculus[-2]
            i+=1
        i+=1
    i=0

    result = expression_after_prioritaty_operators_calculus[0]

    while i < len(expression_after_prioritaty_operators_calculus): 
        if (expression_after_prioritaty_operators_calculus[i] == "-"):
            result = minus(result,expression_after_prioritaty_operators_calculus[i+1])
        elif (expression_after_prioritaty_operators_calculus[i] == "+"):
            result = add(result,expression_after_prioritaty_operators_calculus[i+1])
        print(result)
        print(i)
        print(expression_after_prioritaty_operators_calculus)
        print("-")
        i+=1
    print(result)
    return result

calculate_expression(mathematical_expression) 