from datetime import datetime
import user_interface

big_dictionary = {}
id = len(big_dictionary)
date_input = f"{datetime.now().day}.{datetime.now().month}.{datetime.now().year}"
time_input = f"{datetime.now().hour}.{datetime.now().minute}.{datetime.now().second}"
text = user_interface.Entry.get()
res =  user_interface.print_result()

def save_log ():
    dictionary_log = {"id": id, "date": date_input, "time": time_input, "text": text, "result": res}
    big_dictionary.update(dictionary_log)
    
    str_dict_log = str(f"{big_dictionary},\n")
    with open("C:/GB/Python/homework/lesson07/exercise/logs.txt", "a") as file:
        file.write(str_dict_log)

def read_log ():
    with open("C:/GB/Python/homework/lesson07/exercise/logs.txt", "r") as file:
        return file.readlines()

if user_interface.Entry.get() != None: save_log()
        