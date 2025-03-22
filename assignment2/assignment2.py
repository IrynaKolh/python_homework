import csv
import os
import custom_module
from datetime import datetime

"""
Task 2: Read a CSV File
1. Create a function called read_employees that has no arguments, and do the following within it.
    - Declare an empty dict. You'll add the key/value pairs to that. Declare also an empty list to store the rows.
    - You next read a csv file. Use a try block and a with statement, so that your code is robust and so that the file gets closed.
    - Read ../csv/employees.csv using csv.reader(). (This csv file is used in a later lesson to populate a database.)
    - As you loop through the rows, store the first row in the dict using the key "fields". These are the column headers.
    - Add all the other rows (not the first) to your rows list.
    - Add the list of rows (this is a list of lists) to the dict, using the key "rows".
    - The function should return the dict.
    - Add a line below the function that calls read_employees and stores the returned value in a global variable 
      called employees. Then print out this value, to verify that the function works.
    - In this case, it's not clear what to do if you get an exception. You might get an exception because the 
      filename is bad, or because the file couldn't be parsed as a CSV file. 
      For now, just use the same approach as described above: catch the exception, print out the information, 
      and exit the program. One likely exception in this case is an error in the syntax of your code.

2. Run the test to see if you have this much right.
"""

def read_employees():
    employees_data = {"fields": [], "rows": []}
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            employees_data["fields"] = next(reader)
            
            employees_data["rows"] = []    # employees_data["rows"] = [row for row in reader] 
            for row in reader:
                employees_data["rows"].append(row)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        exit(1)
    
    return employees_data

employees = read_employees()

"""
Task 3: Find the Column Index
1. Create a function called column_index. The input is a string. The function looks in employees["fields"] 
    (an array of column headers) to find the index of the column header requested. 
    There won't be much to this function, because you just use the index() method of the list class, like so:
        employees["fields"].index("first_name")

2. The index() method returns the index of the matching value from the list.
    - The column_index function should return this index.
    - Run the test again to see if the test passes.
    - Call the column_index function in your program, passing the parameter "employee_id".  
        Store the column you get back in a variable called employee_id_column.  
        This global value is used for subsequent steps.
"""

def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"Column '{column_name}' not found.")
        exit(1)

employee_id_column = column_index("employee_id")

"""
Task 4: Find the Employee First Name
1. Create a function called first_name. It takes one argument, the row number.  
    The function should retrieve the value of first_name from a row as stored in the employees dict.
2. You should first call your column_index function to find out what column index you want.
3. Then you go to the requested row as stored in the employees dict, and get the value at that index in the row.
4. Return the value.
5. Try the test again.
"""

def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

"""
Task 5: Find the Employee: a Function in a Function
1. Create a function called employee_find.  This is passed one argument, an integer.  
    Just call it employee_id in your function declaration. We want it to return the rows with the matching employee_id.  
    There should only be one, but sometimes a CSV file has bad data.
2. We could do this with a loop.  But we are going to use the filter() function.  
    Inside the employee_find function (yes, you do declare functions inside functions sometimes), 
    create the following employee_match function:
        def employee_match(row):
        return int(row[employee_id_column]) == employee_id
3. This function is referencing the employee_id value that is passed to the employee_find function.  
    It can access that value because the employee_match function is inside the employee_find function.  
    Note that we need to do type conversion here, because the CSV reader just returns strings as the values in the roows.  
    This inner function returns True if there is a match.  We are using the employee_id_column global value you set in Task 3.
        - Now, still within the employee_find function, call the filter() function. 
        This is another one of those Python free standing functions. (It is not a method of the list class.) 
        You call filter() as follows:
            matches=list(filter(employee_match, employees["rows"]))
4. The filter() function needs to know how to filter, and the employee_match function provides that information.  
    The filter() function calls employee_match once per row, saying, Do we want this one?  
    When the filter function completes, we need to do type conversion to convert the result to a list.
        - The employee_find function then returns the matches.
        - Run the test and see if you got it right.
"""

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    try:
        matches = list(filter(employee_match, employees["rows"]))
        return matches
    except Exception as e:
        print(f"'{employee_id}' not found.")
        exit(1)

"""
Task 6: Find the Employee with a Lambda
1. The employee_match function is a silly one-liner.  Lambdas allow us to give the logic inline.
    - Create a function employee_find_2. This function does exactly what employee_find does -- but it uses a lambda.
        def employee_find_2(employee_id):
        matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
        return matches
2. Note that there is no return statement in the lambda.  There is the parameter passed to the lambda (a row), 
    followed by a colon, followed by the expression that gives the result.
    - Run the test to make sure things still work.
"""

def employee_find_2(employee_id):
    try:
        matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
        return matches
    except Exception as e:
        print(f"'{employee_id}' not found.")
        exit(1)
    
"""
Task 7: Sort the Rows by last_name Using a Lambda
We want to call the sort() method on the rows.  However, we need to tell it which column to use for the sort.
    1. Create a function sort_by_last_name.  It takes no parameters.  You sort the rows you have stored in the dict.
    2. Within the function, you call employees["rows"].sort().  This sorts the list of rows in place. 
        But, you need pass to the list.sort() method a keyword argument called key 
        (so you pass a parameter with key= when you call it).  You set that keyword parameter equal to a lambda.  
        The lambda is passed the row, and the expression after the colon gives the value from the row to be used in the sort.  
        You might want to use your column_index function for last_name 
        so you know which value from the row should be given in the lambda expression.  
        Remember that the sort() method sorts the list in place and does not return the sorted list.
    3. The sort_by_last_name function returns the sorted list of rows.
    4. Run the test until this works.
    5. Call the function in your program, and then print out the employees dict, to see it in sorted form.
"""

def sort_by_last_name():
    try:
        last_name_column = column_index("last_name")
        employees["rows"].sort(key=lambda row: row[last_name_column])
        return employees["rows"]
    except Exception as e:
        print("Not sorted")
        exit(1)
   
"""
Task 8: Create a dict for an Employee
1. Create a function called employee_dict.  It is passed a row from the employees dict (not a row number).  It returns a dict.
    - The keys in the dict are the column headers from employees["fields"].
    - The values in the dict are the corresponding values from the row.
    - Do not include the employee_id in the dict. You skip that field for now.
2. Return the resulting dict for the employee.
3. Add a line to your program that calls this function and prints the result.  
    Use a row from the rows stored in the employees dict to pass to the function for this test.
4. Get the test working.
If you want to try something extra, look up the zip() function, which can be used to simplify the code for this problem.
"""

def employee_dict(row):
    if len(row) != len(employees["fields"]):
        raise ValueError("Row length doesn't match the number of fields.")
    try:
        return {field: value for field, value in zip(employees["fields"], row) if field != "employee_id"}
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

"""
Task 9: A dict of dicts, for All Employees
1. Create a function called all_employees_dict.
    - The keys in the dict are the employee_id values from the rows in the employees dict.
    - For each key, the value is the employee dict created for that row. (Use the employee_dict function you created in task 8.)
2. The function should return the resulting dict of dicts.
3. Add a line to your program that calls this function and prints the result.
4. Get the test working.
"""

def all_employees_dict():
    if not employees.get("fields") or not employees.get("rows"):
        raise ValueError("Invalid or empty data.")

    employee_id_col = column_index("employee_id")

    return {
        str(row[employee_id_col]): employee_dict(row)
        for row in employees["rows"]
        if len(row) == len(employees["fields"])
    }

"""
Task 10: Use the os Module
Sometimes the behavior of a program is to be modified without changing the program itself.  
One way is to use environment variables.  Environment variables are also used to store secrets needed by the program, 
such as passwords.  Environment variables are accessed via the os.getenv() function.  
Of course, there are many other functions in the os package.
1. Within the terminal, enter the command export THISVALUE=ABC.
2. Add a line to assignment2.py to import the os module.
3. Create a function get_this_value().  This function takes no parameters and returns the value of 
    the environment variable THISVALUE.
4. Get the test working.  (Note that each time you want this test to pass, you have to have the 
    THISVALUE environment variable set in your terminal session.)
"""

def get_this_value():
    return os.getenv('THISVALUE')
print(get_this_value()) 

"""
Task 11: Creating Your Own Module
1. In the same folder, create a file called custom_module.py, with the following contents:
        secret = "shazam!"

        def set_secret(new_secret):
        global secret
        secret = new_secret
2. Add the line import custom_module to assignment2.py.
3. Create a function called set_that_secret.  It should accept one parameter, which is the new secret to be set.  
    It should call custom_module.set_secret(), passing the parameter, so as to set the secret in custom_module.
4. Add a line to your program to call set_that_secret, passing the new string of your choice.
5. In another line, print out custom_module.secret.  Verify that it has the value you expect.
6. Run the test until the next part passes.
"""

def set_that_secret(secret):
    custom_module.set_secret(secret)
    

"""
Task 12: Read minutes1.csv and minutes2.csv
The "story" behind the following list of tasks is as follows.  A club meets, and for each meeting, there is a chairperson.  
    The club keeps several notebooks that record who whas the chairperson on a given date. 
    Some of the information is in one notebook, some in the other.  The club now wants to combine this information, 
    to get the list of chairpersons sorted by date.  But the information in the csv files contains duplicates 
    and is in no particular order.  (Yeah, the story is lame, but it is similar to other data analysis tasks.)
1. Create a function called read_minutes.  It takes no parameters.  It creates two dicts, minutes1 and minutes2, 
    by reading ../csv/minutes1.csv and ../csv/minutes2.csv.  Each dict has fields and rows, just as the employees dict had.  
    However! As you create the list of rows for both minutes1 and minutes2, convert each row to a tuple.  
    The function should return both minutes1 and minutes2.  Note You can return several values from a Python function, 
    as follows: return v1, v2.  Don't worry about duplicates yet.  They will be dealt with in later tasks.  
    Think about the DRY (Don't repeat Yourself principal).  You may want to create a helper function to avoid duplicating code.
2. Call the function within your assignment2.py script.  Store the values from the values it returns in the global variables 
    minutes1 and minutes2. Note When a function returns several values, you get them as follows: v1, v2 = function(). 
    Print out those dicts, so that you can see what's stored.
3. Run the test until this part passes.
"""

def read_minutes():
    try:
        minutes_data = {}
        with open('../csv/minutes1.csv', 'r') as file1:
            reader = csv.reader(file1)
            first_row = True
            rows = []
            for row in reader:
                if first_row:
                    first_row = False
                    minutes_data["minutes1"] = {"fields": row}
                else:
                    rows.append(tuple(row))
            minutes_data["minutes1"]["rows"] = rows
        with open('../csv/minutes2.csv', 'r') as file2:
            reader = csv.reader(file2)
            first_row = True
            rows = []
            for row in reader:
                if first_row:
                    first_row = False
                    minutes_data["minutes2"] = {"fields": row}
                else:
                    rows.append(tuple(row))
            minutes_data["minutes2"]["rows"] = rows
        return minutes_data["minutes1"], minutes_data["minutes2"]
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

minutes1, minutes2 = read_minutes()

"""
Task 13: Create minutes_set
1. Create a function called create_minutes_set.  It takes no parameters. It creates two sets from the rows 
    of minutes1 and minutes2 dicts.  (This is just type conversion.  However, to make it work, each row has to be hashable!  
    Sets only support hashable elements.  Lists aren't hashable, so that is why you stored the rows as tuples in Task 10.)  
    Combine the members of both sets into one single set.  (This operation is called a union.)  
    The function returns the resulting set.
2. Call the function within your assignment2.py script.  Store the value returned in the global variable minutes_set.
3. Run the test until the next part passes.
"""

def create_minutes_set():
    try:
        minutes_set_1 = set(minutes1["rows"]) 
        minutes_set_2 = set(minutes2["rows"])      
        result_set = minutes_set_1.union(minutes_set_2)
        return result_set
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

minutes_set = create_minutes_set()

"""
Task 14: Convert to datetime
1. Add a statement, from datetime import datetime, to your program.  The datetime module has some nice capabilities 
    for converting strings to dates.  You can look them up: strptime() and strftime().
2. Create a function called create_minutes_list.  It takes no parameters, and does the following:
    - Create a list from the minutes_set. This is just type conversion.
    - Use the map() function to convert each element of the list. At present, each element is a list of strings, 
        where the first element of that list is the name of the recorder and the second element is the date when they recorded.
    - The map() should covert each of these into a tuple. The first element of the tuple is the name (unchanged). 
        The second element of the tuple is the date string converted to a datetime object.
    - You convert the date strings into datetime objects using datetime.strptime(string, "%B %d, %Y").
    - So, you could use the following lambda: lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y"))
    - The function should return the resulting list.
3. Call the function from within your program.  Store the return value in the minutes_list global.  
    Print it out, so you can see what it looks like.
4. Run the test until the next part passes.
"""

def create_minutes_list():
    try:
        minutes_list = list(minutes_set)
        minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
        return minutes_list
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

minutes_list = create_minutes_list()

"""
Task 15: Write Out Sorted List
1. Create a function called write_sorted_list.  It takes no parameters.  It should do the following:
    - Sort minutes_list in ascending order of datetime.
    - Call map again to convert the list. In this case, for each tuple, you create a new tuple. 
        The first element of the tuple is the name (unchanged). The second element of the tuple is the datetime converted back to 
        a string, using datetime.strftime(date, "%B %d, %Y")
    - Open a file called ./minutes.csv. Use a csv.writer to write out the resulting sorted data. 
        The first row you write should be the value of fields the from minutes1 dict. 
        The subsequent rows should be the elements from minutes_list.
    - The function should return the converted list.
2. Call this function from within your program.  Then check that the file is created, and that it contains appropriate content.
3. Run the test again until the next test has passed.
"""

def write_sorted_list():
    try:
        sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
        sorted_minutes = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_minutes))
        
        with open('./minutes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1['fields'])
            for row in sorted_minutes:
                writer.writerow(row)        
        return sorted_minutes
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

sorted_minutes_list = write_sorted_list()
