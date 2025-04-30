"""
Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
1. Create a DataFrame from a dictionary:
    Use a dictionary containing the following data:
        Name: ['Alice', 'Bob', 'Charlie']
        Age: [25, 30, 35]
        City: ['New York', 'Los Angeles', 'Chicago']
    Convert the dictionary into a DataFrame using Pandas.
    Print the DataFrame to verify its creation.
    save the DataFrame in a variable called task1_data_frame and run the tests.
2. Add a new column:
    Make a copy of the dataFrame you created named task1_with_salary (use the copy() method)
    Add a column called Salary with values [70000, 80000, 90000].
    Print the new DataFrame and run the tests.
3. Modify an existing column:
    Make a copy of task1_with_salary in a variable named task1_older
    Increment the Age column by 1 for each entry.
    Print the modified DataFrame to verify the changes and run the tests.
4. Save the DataFrame as a CSV file:
    Save the task1_older DataFrame to a file named employees.csv using to_csv(), do not include an index in the csv file.
    Look at the contents of the CSV file to see how it's formatted.
    Run the tests.
"""

import pandas as pd

my_dict = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"],
}

task1_data_frame = pd.DataFrame(my_dict)    # Create a DataFrame from a dictionary
print(task1_data_frame)

task1_with_salary=task1_data_frame.copy()     # Make a copy
task1_with_salary["Salary"] = [70000, 80000, 90000]     # Add a column called Salary
print(task1_with_salary)

task1_older = task1_with_salary.copy()
task1_older["Age"] += 1         # Increment the Age column by 1 for each entry
print(task1_older)

task1_older.to_csv("employees.csv", index=False)


"""
Task 2: Loading Data from CSV and JSON
1. Read data from a CSV file:
    Load the CSV file from Task 1 into a new DataFrame saved to a variable task2_employees.
    Print it and run the tests to verify the contents.
2. Read data from a JSON file:
    Create a JSON file (additional_employees.json). The file adds two new employees. Eve, who is 28, lives in Miami, and has a salary of 60000, 
        and Frank, who is 40, lives in Seattle, and has a salary of 95000.
    Load this JSON file into a new DataFrame and assign it to the variable json_employees.
    Print the DataFrame to verify it loaded correctly and run the tests.
3. Combine DataFrames:
    Combine the data from the JSON file into the DataFrame Loaded from the CSV file and save it in the variable more_employees.
    Print the combined Dataframe and run the tests.
"""

task2_employees = pd.read_csv("employees.csv")  # Load data from CSV file
print(task2_employees)

json_employees=pd.read_json("additional_employees.json")  # Load additional
print(json_employees)

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)   # Combine DataFrames
print(more_employees)

"""
Task 3: Data Inspection - Using Head, Tail, and Info Methods
1. Use the head() method:
    Assign the first three rows of the more_employees DataFrame to the variable first_three
    Print the variable and run the tests.
2. Use the tail() method:
    Assign the last two rows of the more_employees DataFrame to the variable last_two
    Print the variable and run the tests.
3. Get the shape of a DataFrame
    Assign the shape of the more_employees DataFrame to the variable employee_shape
    Print the variable and run the tests
4. Use the info() method:
    Print a concise summary of the DataFrame using the info() method to understand the data types and non-null counts.
"""

first_three = more_employees.head(3)  # first three rows
print(first_three)

last_two = more_employees.tail(2)   # last two rows
print(last_two)

employee_shape = more_employees.shape   # Get the shape of a DataFrame
print(employee_shape)

print(more_employees.info())

"""
Task 4: Data Cleaning
1. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data.
    Print it and run the tests.
    Create a copy of the dirty data in the varialble clean_data (use the copy() method). You will use data cleaning methods to update clean_data.
2. Remove any duplicate rows from the DataFrame
    Print it and run the tests.
3. Convert Age to numeric and handle missing values
    Print it and run the tests.
4. Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN
    print it and run the tests.
5. Fill missing numeric values (use fillna).  Fill Age which the mean and Salary with the median
    Print it and run the tests
6. Convert Hire Date to datetime
    Print it and run the tests
7. Strip extra whitespace and standardize Name and Department as uppercase
    Print it and run the tests
"""

dirty_data = pd.read_csv("dirty_data.csv")  #Create a DataFrame from dirty_data.csv
print(dirty_data)

clean_data = dirty_data.copy()   #Create a copy
clean_data = clean_data.drop_duplicates()    #Remove duplicates

clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")  #Convert Age to numeric
mean_age = clean_data['Age'].mean()   #handle missing values and fill Age which the mean
clean_data['Age'] = clean_data['Age'].fillna(mean_age)

clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA) #Convert Salary to numeric and replace known placeholders with NaN
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")  

median_salary = clean_data['Salary'].median()  #handle missing values and fill Salary which the median
clean_data['Salary'] = clean_data['Salary'].fillna(median_salary)

clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce")  #Convert Hire Date to datetime

clean_data["Name"] = clean_data["Name"].str.strip() #Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

print(clean_data)
