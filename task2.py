def data_entry_method(message="", arrayIndex=False):
    if arrayIndex:
        print(message)
        return [int(i) for i in input().split(' ')]  
    else:
        return input(message)

def multiplier(number_1, number_2):
    if number_2 == 0: return number_1
    else: 
        return multiplier(number_1+1,number_2-1)
    
def main():
    first_number = int(data_entry_method("Please input first number: "))
    second_number = int(data_entry_method("Please input second number: "))
    print(multiplier(first_number,second_number))

main()  