'''
 Write a program that prints a right triangle of numbers, where each row has one more number 
 than the previous, starting with 1. (e.g. 1, 2 3, 4 5 6)
'''
for num in range(1,7):
    for i in range(1, num):
        print(i, sep=" ", end=" ")
    print("\n")
