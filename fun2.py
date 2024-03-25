from datetime import datetime
# Function to orint current date & time
def print_time(task_name):
    print(task_name)
    print(datetime.now())

fn='Suchi'
print('Hi!'+fn)
print_time('Printed first name')

for x in range(0,10):
    print(x)
print_time('Printed a for loop')