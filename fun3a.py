def get_initials(name):
    initial = name[0:1]
    return initial

first_name=input('Enter your first name:')
first_name_initial= get_initials(first_name)
middle_name=input('Enter your middle name:')
middle_name_initial= get_initials(middle_name)
last_name=input('Enter your last name:')
last_name_initial= get_initials(last_name)
print('Your initials are:' +first_name_initial+middle_name_initial+last_name_initial)