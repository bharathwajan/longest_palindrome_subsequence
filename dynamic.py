def fib(num):  # example of divide and conquer
    memory = [None]*num
    memory[0] = memory[1] = 1
    print(memory)
    for value in range(2, num):
        # print(value)
        memory[value] = memory[value-1]+memory[value-2]
    return memory[-1]


res = fib(8)
# print(temp)
print(f"the fibo value of 8th index is ", res)
