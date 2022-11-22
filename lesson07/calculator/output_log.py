def read_log ():
    with open("C:/GB/Python/homework/lesson07/calculator/logs.txt", "r") as file:
        log = str(file.readline())
        return log
# print(read_log ())