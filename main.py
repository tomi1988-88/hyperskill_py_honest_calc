msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msg_lst = [msg_10, msg_11, msg_12]

memory = 0.0


def is_one_digit(v):
    if v in range(-9, 11):
        return True
    else:
        return False


def check(x, oper, y):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_6

    if (x == 1 or y == 1) and oper == "*":
        msg += msg_7

    if (x == 0 or y == 0) and oper in "*+-":
        msg += msg_8

    if msg != "":
        msg = msg_9 + msg
        print(msg)


while True:
    print(msg_0)

    calc = input()

    try:
        x, oper, y = calc.split(" ")

        if x == "M" and y == "M":
            x, y = memory, memory
        elif x == "M":
            x, y = memory, float(y)
        elif y == "M":
            x, y = float(x), memory
        else:
            x, y = float(x), float(y)

    except ValueError:
        print(msg_1)
        continue

    if not (len(oper) == 1 and oper in "+-*/"):
        print(msg_2)
        continue

    check(x, oper, y)

    res = 0.0

    if oper == "+":
        res = x + y
    elif oper == "-":
        res = x - y
    elif oper == "*":
        res = x * y
    elif oper == "/" and y != 0:
        res = x / y
    else:
        print(msg_3)
        continue

    print(res)

    while True:
        answer = input(msg_4)

        if answer == "y":
            one_digit = False
            
            if is_one_digit(res):
                one_digit = True
                msg_index = 0

                while True:
                    answer = input(msg_lst[msg_index])
                    if answer == "y" and msg_index < 2:
                        msg_index += 1
                    elif answer == "y" and not(msg_index < 2):
                        one_digit = False
                        break
                    elif answer == "n":
                        break
                    else:
                        continue

            if not one_digit:
                memory = res
                break
            if answer == "n":
                break

        elif answer == "n":
            break
        else:
            continue

    while True:
        answer = input(msg_5)

        if answer == "y":
            break
        elif answer == "n":
            break
        else:
            continue

    if answer == "n":
        break
