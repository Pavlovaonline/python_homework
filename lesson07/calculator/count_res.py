import re
import output_log

def read_expression():
    text = output_log.read_log().split(":")
    sp_text = text[4]
    sp_text = sp_text.replace("result", "")
    sp_text = sp_text.replace(" ", "")
    return str(sp_text)

def get_result():
    res = eval(read_expression())
    return res



# def read_expression():
#     text = output_log.read_log().split(":")
#     sp_text = text[4]
#     sp_text = sp_text.replace("result", "")
#     sp_text = sp_text.replace(" ", "")
#     return sp_text
# def count_float(expression):
#     while "." in expression:
#         for i in range (len(expression)):
#             if expression[i] == ".":
#                 res = expression[i].join(expression[i+1])
#                 expression[i] = res
#                 expression[i-1] = " "
#                 expression[i+1] = " "
#     while expression.count(" ") > 0:
#             expression.remove(" ")
#     return str(expression)
# def count_res(expression):
#     while "+" in expression or "-" in expression or "*" in expression or "/" in expression:
#         for i in range (len(expression)):
#             if expression[i] == "*":
#                 res = float(expression[i-1])*float(expression[i+1])
#                 expression[i-1] = " "
#                 expression[i] = " "
#                 expression[i+1] = res
#             elif expression[i] == "/":
#                 res = round((float(float(expression[i-1])/float(expression[i+1]))), 2)
#                 expression[i-1] = " "
#                 expression[i] = " "
#                 expression[i+1] = res
#         while expression.count(" ") > 0:
#             expression.remove(" ")
#         for i in range (len(expression)):
#             if expression[i] == "+":
#                 res = float(expression[i-1])+float(expression[i+1])
#                 expression[i-1] = " "
#                 expression[i] = " "
#                 expression[i+1] = res
#             elif expression[i] == "-":
#                 res = float(expression[i-1])-float(expression[i+1])
#                 expression[i-1] = " "
#                 expression[i] = " "
#                 expression[i+1] = res
#         while expression.count(" ") > 0:
#             expression.remove(" ")
#     return str(expression)
# count_res(read_expression())