# make simple calculator with terminal
# 1. add
# 2. sub
# 3. mul
# 4. div

# 1. add
def add(a, b):
    return a + b

# 2. sub
def sub(a, b):
    return a - b

# 3. mul
def mul(a, b):
    return a * b

# 4. div
def div(a, b):
    return a / b

# 5. run calculator
def run_calculator():
    print("1. add")
    print("2. sub")
    print("3. mul")
    print("4. div")
    print("5. quit")
    while True:
        menu = int(input("select menu: "))
        if menu == 5:
            break
        a = int(input("input a: "))
        b = int(input("input b: "))
        if menu == 1:
            print(add(a, b))
        elif menu == 2:
            print(sub(a, b))
        elif menu == 3:
            print(mul(a, b))
        elif menu == 4:
            print(div(a, b))
        else:
            print("wrong menu")

# 6. main
if __name__ == "__main__":
    run_calculator()

# 7. test
# python calculator.py
# 1. add
# 2. sub   
# 3. mul
# 4. div
# 5. quit
# select menu: 1
# input a: 10
# input b: 20
# 30
# select menu: 2
# input a: 10
# input b: 20
# -10
# select menu: 3
# input a: 10
# input b: 20
# 200
# select menu: 4
# input a: 10
# input b: 20
# 0.5
# select menu: 5
# >>>

# 8. test
# python calculator.py
