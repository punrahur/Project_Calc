from calc import do_addition,do_subtraction


def print_info():
    print('calculator app:')
    print("""
        \nSelect the function:
          1.Add
          2.Subtract
    """)

    user_input = input('select the function')

    a = int(input('val of a'))
    b = int(input('val of b'))

    if user_input == '1':
        result = do_addition(a,b)
    elif user_input == '2':
        result = do_subtraction(a,b)

    print('Result: ',result)

if __name__=="__main__":
    print_info()

