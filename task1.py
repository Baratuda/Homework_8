import random as ra

# Метод который позволяет производить input() для переменной и массива и принимает на как параметр значение 
# "message" и "arrayIndex" - нужен для определения что данный метод будет заполнять.
# Если  "arrayIndex" = True то будет произведен  
def data_entry_method(message="", arrayIndex=False):
    if arrayIndex:
        print(message)
        return [int(i) for i in input().split(' ')]  
    else:
        return input(message)

def multiplier(number_1, number_2, result=0):
    if number_2 == 1: return result
    else: 
        if result == 0: result=number_1*number_1
        else: result*=number_1
        return multiplier(number_1,number_2-1, result)
    
def main():
    first_number = int(data_entry_method("Please input number: "))
    second_number = int(data_entry_method("Please input multiplier: "))
    print(multiplier(first_number,second_number))

main()    