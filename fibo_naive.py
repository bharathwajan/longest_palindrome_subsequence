#fibbonaci naive approach 
def fib(num):  # example of divide and conquer
    print(num)
    if num <= 2:
        # print("inside if and the value is", num)
        return 1
    else:
        return fib(num-1)+fib(num-2)
res = fib(7)
print("result", res)
