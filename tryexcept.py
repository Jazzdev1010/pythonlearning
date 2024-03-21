x=10
y=0
print()
try:
    print(x/y)
except ZeroDivisionError as e:
    print('Not allowed to devide bt zero')
else:
    print('Something went wrong')
finally:
    print('It will run in any situation')