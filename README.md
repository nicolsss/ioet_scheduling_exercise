# Scheduling Exercise
## Problem
The company ACME offers their employees the flexibility to work the hours they want. But due to some external 
circumstances they need to know what employees have been at the office within the same time frame.  
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in 
the office.

### Input
The name of an employee and the schedule they worked, indicating the time and hour. For example:
~~~
RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00  
ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00  
ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
~~~
### Output
~~~
ASTRID-RENE: 2  
ASTRID-ANDRES: 3  
RENE-ANDRES: 2
~~~
## Solution
### Assumptions
About the data, this program expects the file has:
* Each line has information for only one employee.
* Each employee appears only once in the file.
* One day of the week, has only one time frame (the same person cannot have several time slots on the same day of the week).

### Data Structures:
The solution uses dictionaries to store information about employees, schedules by day of week and the result. 
It also uses tuples to store time frames.

### Algorithm
The algorithm start reading the provided file, when it reads a line the principal dictionary (which has 
the data of employees) is updated, after(while still reading) the algorithm compares the current employee 
data with the other employees' data in such a way that no needs to iterate the main dictionary at the end with 
all employees.  
The algorithm strategy focuses on separating tasks into small functions that do a single task, which will 
help test better. The tasks that the algorithm does are:
* [Creating the dictionary structure where store day of week information](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/functions/schedule_functions.py?plain=1#L83)
* [Creating tuples to store time frames](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/functions/schedule_functions.py?plain=1#L69)
* [Parsing time string to integer](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/functions/schedule_functions.py?plain=1#L58)
* [Creating dictionary where store the pairs of employees and the total coincided](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/functions/schedule_functions.py?plain=1#L36)
* [Calculating the total matches in two schedules](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/functions/schedule_functions.py?plain=1#L16)
* [Determining if two time frames match](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/functions/schedule_functions.py?plain=1#L1)

#### Algorithmic complexity
The algorithm avoids iterating twice the dictionary with all the names `(n)`, and only iterates those that have been 
added before the current employee, additionally for each employee the days of the week `(m)` must be iterated, 
whose maximum value could be 7.
The number of iterations are similar to Gauss Sum, so the algorithmic complexity is `O(n(n+1)/2 * m)`  
![Gauss Sum](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/assets/gauss_sum.png)  
![Employee Matrix](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/assets/employees_matrix_ex.png)
## Project Structure
The principal code is in [src](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/) folder in 
the `main.py`, this file use some functions which are in 
[functions](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/functions/) folder,
that folder has two files `schedule_functions.py` which has the "business logic" and `message_functions.py` which 
helps the `main.py` print messages. Also in [src](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/)
is the [data](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/data/) folder where are the files
to be processed.
There is also the [test](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/test/)  folder where `test.py` 
has all the unit test for the `shcedule_functinos.py`

## How to run project locally
The project solution need to have installed [Python(3.7.6)](https://www.python.org/downloads/release/python-376/)
### 1. Clone 
Clone the project using:
~~~
git clone https://github.com/nicolsss/ioet_scheduling_exercise.git
~~~
### 2. Upload File  
Upload files to be processed in [data](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/src/data/) folder.
When the project starts, it will ask for the name of the file to process.
### 3. Run Project
Windows:
~~~
python src/main.py
~~~
Mac/Linux
~~~
python3 src/main.py
~~~
## How to run test
The test were created using unittest. All tests are located in 
[test.py](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/test/)   
__1. Move to test folder__
~~~
cd test
~~~
__2. Run tests__  
Windows:
~~~
python -m unittest -v
~~~
Mac/Linux:
~~~
python3 -m unittest -v
~~~
### Tests results
![Passed tests](https://github.com/nicolsss/ioet_scheduling_exercise/blob/master/assets/tests_passed.png)