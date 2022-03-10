from functions.schedule_functions import *
from functions.message_functions import *

exit_program = False
while not exit_program:
    print_menu()
    option = input("Enter an option: ")
    if option == '1':
        try:
            file_name = input("Schedule file name: ")
            employees_schedule = dict()
            with open('./data/' + file_name, 'r') as schedule_file:
                for line in schedule_file:
                    employee_name, times = line.split('=')
                    employees_schedule[employee_name] = struct_schedule(times)
                    total_overlap_employees = get_total_overlap_employees(employee_name, employees_schedule)
                    [print_total_overlap(employee_team) for employee_team in total_overlap_employees.items()]
        except FileNotFoundError:
            print_msg("File not found", 'error')
    elif option == '2':
        exit_program = True
    else:
        print_msg('Invalid option', 'warning')
