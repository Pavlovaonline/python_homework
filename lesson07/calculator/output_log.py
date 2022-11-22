def read_log ():
    with open("C:/GB/Python/homework/lesson07/exercise/logs.txt", "r") as file:
        log = str(file.readline())
        return log