class UserError(Exception):
    pass

class ValueTooSmallError(UserError):
    pass

class ValueTooLargeError(UserError):
    pass


number = 100

while True:
    try:
        i_int = int(input("Enter a number: "))
        if i_int < number:
            raise ValueTooSmallError
        elif i_int > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print('Число меньше загаданного, попробуйте ещё раз!')
    except ValueTooLargeError:
        print('Число больше загаданного, попробуйте ещё раз!')

print('Вы угадали!')