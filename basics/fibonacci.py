#Time Complexity: O(2N)
#Auxiliary Space: O(N)

# def fibonacci(n):
#     if n <= 0:
#         return "Invalid input"
    
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    

# print(fibonacci(10))




# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1
 
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

 
print(fibonacci(9))