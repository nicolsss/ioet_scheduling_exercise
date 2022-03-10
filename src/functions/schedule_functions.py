def are_times_overlap(time_e1, time_e2):
    """
    Check if two employees' time frame match
    :param time_e1: tuple
        Time frame of an employee
    :param time_e2: tuple
        Time frame of another employee
    :return: bool
        True if time frame of the two employee match
    """
    start_e1, end_e1 = time_e1
    start_e2, end_e2 = time_e2
    return start_e1 <= start_e2 < end_e1 or start_e2 <= start_e1 < end_e2


def get_total_overlap(schedule_e1, schedule_e2):
    """
    Calculate the total of time frames two employees match
    :param schedule_e1: dict
        Schedule of an employee
    :param schedule_e2:
        Schedule of another employee
    :return: int
        Total value of the matching schedules
    """
    total = 0
    for day in schedule_e1.keys():
        if day in schedule_e2:
            time_e1 = schedule_e1[day]
            time_e2 = schedule_e2[day]
            if are_times_overlap(time_e1, time_e2):
                total += 1
    return total


def get_total_overlap_employees(name_e1, schedules):
    """
    Get the total of an employee's time frame match with each other employees,
    if two employees have 0 matches the total is not added to the dictionary
    :param name_e1: str
        Name of an employee
    :param schedules: dict
        Schedules of all employees
    :return: dict
        Dictionary with the total values of employees' time frame matching
    """
    overlap_employees = dict()
    for name_e2 in schedules.keys():
        if name_e1 != name_e2:
            schedule_e1 = schedules[name_e1]
            schedule_e2 = schedules[name_e2]
            total_overlap = get_total_overlap(schedule_e1, schedule_e2)
            if total_overlap != 0:
                overlap_employees[name_e1 + '-' + name_e2] = total_overlap
    return overlap_employees


def parse_time_to_int(time):
    """
    Parse time string(HH:MM) to integer(HHMM)
    :param time: str
        Time string with HH:MM format
    :return: int
        Integer value of time string
    """
    return int(time.strip().replace(':', ''))


def format_schedule_day(schedule_day):
    """
    Format schedule day to time frame tuple
    :param schedule_day: str
        Time frame string
    :return: tuple
        Time frame tuple with start and end
    """
    start, end = schedule_day.split('-')
    start = parse_time_to_int(start)
    end = parse_time_to_int(end)
    return start, end


def struct_schedule(times):
    """
    Create a dictionary with schedules by day of week
    :param times:str
        Weekly schedule with time frames separated by commas
    :return: dict
        Schedule by day of week
    """
    schedule = dict()
    for time in times.split(','):
        day = time[:2]
        schedule[day] = format_schedule_day(time[2:])
    return schedule


def print_total_overlap(team):
    """
    Prints the employees' name ant the total time frame match
    :param team:tuple
        Has the employees' name and total time frames match
    :return:
    """
    print(team[0]+':'+str(team[1]))