'''
Task 1: Hello
    Write a hello function that takes no arguments and returns Hello!.  
    Now, what matters here is what the function returns.  
    You can print() whatever you want for debugging purposes, 
    but the tests ignore that, and only check the return value.
'''

def hello():
    return "Hello!"

'''
Task 2: Greet with a Formatted String
    Write a greet function.  It takes one argument, a name, and returns Hello, Name!.  
    Use a formatted string.  Note that you have to return exactly the right string or 
    the test fails -- but PyTest tells you what didn't match.
'''

def greet(name):
    return f"Hello, {name}!"

'''
Task 3: Calculator
    * Write a calc function. It takes three arguments. 
        The default value for the third argument is "multiply". 
        The first two arguments are values that are to be combined 
        using the operation requested by the third argument, 
        a string that is one of the following add, subtract, multiply, divide, 
        modulo, int_divide (for integer division) and power. 
        The function returns the result.
    * Error handling: When the function is called, it could ask you to divide by 0. 
        That will throw an exception: Which one? You can find out by triggering the exception 
        in your program or in the Python Interactive Shell. 
        Wrap the code within the calc function in a try block, 
        and put in an except statement for this exception. 
        If the exception occurs, return the string "You can't divide by 0!".
    * More error handling: When the function is called, the parameters that are passed 
        might not work for the operation. For example, you can't multiply two strings. 
        Find out which exception occurs, catch it, and return the string 
        "You can't multiply those values!".
    * Here's a tip. You have to do different things for add, multiply, divide and so on.
        So you can do a conditional cascade, if/elif/elif/else. 
        That's perfectly valid. But you might want to use the match-case Python statement 
        instead. Look it up! It just improves code appearance.
    Again, as you complete each function, you run the test 
    to see whether everything is correct.
'''

def calc(a, b, operation="multiply"):
    if isinstance(a, (int, float)):
        if (operation == "add"):
            return a + b
        elif (operation == "subtract"):
            return a - b
        elif (operation == "multiply"):
            return a * b
        elif (operation == "divide"):
            try:
                return a / b
            except ZeroDivisionError: 
                return "You can't divide by 0!"
        elif (operation == "modulo"):
            return a % b    
    else:
        return "You can't multiply those values!"

'''
Task 4: Data Type Conversion
    * Create a function called data_type_conversion. It takes two parameters, 
        the value and the name of the data type requested, one of float, str, or int. 
        Return the converted value.
    * Error handling: The function might be called with a bad parameter. 
        For example, the caller might try to convert the string "nonsense" to a float. 
        Catch the error that occurs in this case. If this error occurs, return the string 
        You can't convert {value} into a {type}., 
        except you use the value and data type that are passed as parameters -- so again 
        you use a formatted string.
'''    

def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return f"Invalid data type: {data_type}."
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."

'''
Task 5: Grading System, Using *args
    * Create a grade function. It should collect an arbitrary number of parameters, 
        compute the average, and return the grade. based on the following scale:
        A: 90 and above
        B: 80-89
        C: 70-79
        D: 60-69
        F: Below 60
    * When you use *args you get access to a variable named args in your function, 
        which is a tuple, an ordered collection of values like a list. 
        You'll learn more about tuples and lists in the next lesson. 
        There are some helpful functions you can use at this point: sum(args), len(args), 
        and so on. One of the curiosities of Python is that these are not methods of any class.
        They are just standalone functions.
    * Handle the error that occurs if the parameters are nonsense. 
        Return the string "Invalid data was provided." in this case. 
        (Typically, you don't handle every possible exception in your error handling, 
        except if the values in the parameters comes from the end user.)
'''    

def grade(*args):
    try:
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."
    
'''
Task 6: Use a For Loop with a Range
    * Create a function called repeat. It takes two parameters, a string and a count, 
        and returns a new string that is the old one repeated count times.
    * You can get the test to pass by just returning string * count. 
        That would produce the correct return value. 
        But, for this task, do it using a for loop and a range.
'''

def repeat(string, count):
    # return string * count
    result = ""
    for _ in range(count):
        result += string
    return result

'''
Task 7: Student Scores, Using **kwargs
    * Create a function called student_scores. It takes one positional parameter 
        and an arbitrary number of keyword parameters. The positional parameter is either
        "best" or "mean". If it is "best", the name of the student with the higest score 
        is returned. If it is "mean", the average score is returned.
    * As you are using **kwargs, your function can access a variable named kwargs, 
        which is a dict. The next lesson explains about dicts. 
        What you need to know now is the following:
            A dict is a collection of key value pairs.
            You can iterate through the dict as follows:
                for key, value in kwargs.items():
            You can also get kwargs.keys() and kwargs.values().
    * The arbitrary list of keyword arguments uses the names of students as the keywords and their test score as the value for each.
'''

def student_scores(position, **kwargs):
    if not kwargs:
        return None
    
    if position == "best":
        return max(kwargs, key=kwargs.get)
    elif position == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return None
    
'''
Task 8: Titleize, with String and List Operations
    * Create a function called titleize. It accepts one parameter, a string. 
        The function returns a new string, where the parameter string is capitalized as 
        if it were a book title.
        * The rules for title capitalization are: 
        (1) The first word is always capitalized.
        (2) The last word is always capitalized. 
        (3) All the other words are capitalized, except little words. 
        For the purposes of this task, the little words are 
        "a", "on", "an", "the", "of", "and", "is", and "in".
    * The following string methods may be helpful: split(), join(), and capitalize(). Look 'em up.
    * The split() method returns a list. You might store this in the words variable. 
        words[-1] gives the last element in the list.
    * The in comparison operator: You have seen in used in loops. 
        But it can also be used for comparisons, for example to check to see if a substring occurs in a string, or a value occurs in a list.
    * A new trick: As you loop through the words in the words list, 
        it is helpful to have the index of the word for each iteration. 
        You can access that index using the enumerate() function:
            for i, word in enumerate(words):
'''

def titleize(string):
    short_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = string.lower().split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in short_words:
            words[i] = word.capitalize()

    return " ".join(words)

'''
Task 9: Hangman, with more String Operations
    * Create a function hangman. It takes two parameters, both strings, the secret and the guess.
    * The secret is some word that the caller doesn't know. So the caller guesses 
        various letters, which are the ones in the guess string.
    * A string is returned. Each letter in the returned string corresponds to a letter 
        in the secret, except any letters that are not in the guess string are replaced 
        with an underscore. The others are returned in place. 
        Not everyone has played this kid's game, but it's common in the US.
    * Example: Suppose the secret is "alphabet" and the guess is "ab". 
        The returned string would be "a___ab__".
    * Note that Python strings are immutable. That means that the following code would give an error:
            secret = "alphabet"
            secret[1] = "_"
    * On the other hand, you can concatenate strings with the + operator.
'''

def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

'''
Task 10: Pig Latin, Another String Manipulation Exercise
    * Pig Latin is a kid's trick language. Each word is modified according to the following rules. 
        (1) If the string starts with a vowel (aeiou), "ay" is tacked onto the end. 
        (2) If the string starts with one or several consonants, they are moved to the end and "ay" is tacked on after them. 
        (3) "qu" is a special case, as both of them get moved to the end of the word, as if they were one consonant letter.
    * Create a function called pig_latin. It takes an English string or sentence and 
        converts it to Pig Latin, returning the result. We will assume that there is no punctuation and 
        that everything is lower case.
'''

def pig_latin(sentense):
    vowels= "aeiou"
    words = sentense.split()
    pl_words = []

    for word in words:
        if word[0] in vowels:
            pl_words.append(word + "ay")
        elif "qu" in word:
            qu_index = word.index("qu") + 2
            pl_words.append(word[qu_index:] + word[:qu_index] + "ay")
        else:       
            for i, letter in enumerate(word):
                if letter in vowels:
                    pl_words.append(word[i:] + word[:i] + "ay")
                    break

    return " ".join(pl_words)  