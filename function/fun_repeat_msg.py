def repeat_msg(msg, repeat=3):
    for i in range(repeat):
        print(msg,end=', ')

repeat_msg('Hello')                    # Hello, Hello, Hello,
print()
repeat_msg('Yahho', repeat=5)          # Yahho, Yahho, Yahho, Yahho, Yahho,