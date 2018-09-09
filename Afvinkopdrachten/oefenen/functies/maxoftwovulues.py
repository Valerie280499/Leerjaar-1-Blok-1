def main():
    max_num = max_number()
    print(max_num)

def max_number():
    number_1 = int(input('number 1:'))
    number_2 = int(input('number 2:'))

    if number_1 > number_2:
        return number_1
    elif number_2 > number_1:
        return number_2
    else:
        print('de getallen zijn evengroot')
    

main()
