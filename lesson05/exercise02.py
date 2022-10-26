with open("C:/GB/Python/homework/lesson05/originaltext.txt", "r") as file: 
    original_text = file.read()

with open("C:/GB/Python/homework/lesson05/RLE_code.txt", "r") as file: 
     decode_text = str(file.read())

def rle_encode (text):
    code = ""
    symbol = ""
    count = 1
    for char in text:
        if char != symbol:
            if symbol:
                code += str(count) + str(symbol) 
            count = 1
            symbol = char
        else:
            count += 1
    else: 
        code += str(count) + str(symbol)
    with open("C:/GB/Python/homework/lesson05/RLE_code.txt", "w") as file: 
        file.write(code)
    return code

def rle_decode (text):
    code = ""
    count = ""
    for char in text:
        if char.isdigit():
            count += char
        else: 
            code += char * int(count)
            count = ""
    return code

print(rle_encode(original_text))
print(rle_decode(decode_text))