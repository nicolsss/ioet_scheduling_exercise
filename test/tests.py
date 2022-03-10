import unittest
import schedule_functions as utils


class TestAreTimesOverlap(unittest.TestCase):
    def test_are_times_overlap(self):
        """
        are_times_overlap determines if two employees' time frame match
        """
        time_e1 = (1000, 1200)
        time_e2 = (1000, 1200)
        time_e3 = (800, 1000)

        result_true = utils.are_times_overlap(time_e1, time_e2)
        result_false = utils.are_times_overlap(time_e1, time_e3)

        assert result_true is True
        assert result_false is False


class TestGetTotalOverlap(unittest.TestCase):
    def test_get_total_overlap(self):
        """
        get_total_overlap return the total of time frames two employees match
        """
        schedule_e1 = {
            'MO': (0, 230),
            'TH': (1300, 1400),
            'SU': (1115, 1300)}
        schedule_e2 = {
            'MO': (215, 400),
            'TH': (1200, 1400),
            'SU': (1250, 1300)}
        schedule_e3 = {
            'MO': (1200, 1600),
            'TH': (1000, 1100),
            'SU': (1600, 1700)}

        result_e1_e2 = utils.get_total_overlap(schedule_e1, schedule_e2)
        result_e2_e3 = utils.get_total_overlap(schedule_e2, schedule_e3)
        assert result_e1_e2 == 3
        assert result_e2_e3 == 0


class TestGetTotalOverlapEmployees(unittest.TestCase):
    def test_get_total_overlap_employees(self):
        """
        get_total_overlap_employees get the total of an employee's time frame match with each other employees
        """
        name_e1 = 'SEBAS'
        name_e2 = 'DULCE'
        name_e3 = 'DOME'
        schedules = {
            'SEBAS': {
                'MO': (0, 230),
                'TH': (1300, 1400),
                'SU': (1115, 1650)
            },
            'DAYA': {
                'MO': (215, 400),
                'TH': (1200, 1400),
                'SU': (1250, 1300)
            },
            'DULCE': {
                'MO': (1200, 1600),
                'TH': (1000, 1100),
                'SU': (1600, 1700)
            },
            'DOME': {
                'TU': (1200, 1600),
                'WE': (1000, 1100)
            }
        }

        result_sebas = utils.get_total_overlap_employees(name_e1, schedules)
        result_dulce = utils.get_total_overlap_employees(name_e2, schedules)
        result_dome = utils.get_total_overlap_employees(name_e3, schedules)

        assert result_sebas == {'SEBAS-DAYA': 3, 'SEBAS-DULCE': 1}
        assert result_dulce == {'DULCE-SEBAS': 1}
        assert result_dome == {}


class TestPaseTimeToInt(unittest.TestCase):
    def test_parse_time_to_int(self):
        """
        parse_time_to_int transform a string time in format HH:MM to integer
        """
        time_1 = '10:15'
        time_2 = '00:00'
        time_3 = '02:00'
        
        result_time_1 = utils.parse_time_to_int(time_1)
        result_time_2 = utils.parse_time_to_int(time_2)
        result_time_3 = utils.parse_time_to_int(time_3)
        
        assert result_time_1 == 1015
        assert result_time_2 == 0
        assert result_time_3 == 200


class TestFormatScheduleDay(unittest.TestCase):
    def test_format_schedule_day(self):
        """
        format_schedule_day return a time frame creating a tuple with start and end times
        """
        day_mo = '10:15-12:00'
        day_su = '00:00-02:30'

        result_mo = utils.format_schedule_day(day_mo)
        result_su = utils.format_schedule_day(day_su)

        assert result_mo == (1015, 1200)
        assert result_su == (0, 230)


class TestStructSchedule(unittest.TestCase):
    def test_struct_schedule(self):
        """
        struct_schedule create a dictionary struct include day of week keys and a tuple of time frame
        """
        times_e1 = 'MO10:15-12:00,TU10:00-12:00,SU20:00-21:00'
        times_e2 = 'MO00:00-02:30,TH13:00-14:00,SU11:15-16:50'

        result_time_e1 = utils.struct_schedule(times_e1)
        result_time_e2 = utils.struct_schedule(times_e2)

        assert result_time_e1 == {'MO': (1015, 1200), 'TU': (1000, 1200), 'SU': (2000, 2100)}
        assert result_time_e2 == {'MO': (0, 230), 'TH': (1300, 1400), 'SU': (1115, 1650)}


if __name__ == '__main__':
    unittest.main()
