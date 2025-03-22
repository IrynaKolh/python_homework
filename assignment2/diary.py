import traceback
from datetime import datetime


def main():
    try:
        with open('diary.txt', 'a') as file:
            print("What happened today?")
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')

            while True:
                user_input = input()
                if user_input.lower() == "done for now":
                    file.write("done for now\n")
                    break
                else:
                    print("What else? ")
                file.write(user_input + '\n')

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")


def main2():
    try:
        with open('diary.txt', 'a') as file:
            print("What happened today?")
            user_input = ""
            data = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n'

            while user_input.lower() != "done for now":
                user_input = input() 
                if user_input.lower() != "done for now": 
                    data += user_input + '\n'  
                    print("What else?") 

            file.write(data + "done for now\n" + '\n') 

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

main()
