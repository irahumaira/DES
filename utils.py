def split_string(text, length):
    texts = []
    for i in range(0, len(text), length):
        texts.append(text[i:i + length])
    return texts

def string_to_binary(text):
    binary = ''
    for c in text:
        binary+=(format(ord(c), 'b').zfill(8))
    return binary

def int_to_binary(num):
    return format(num, 'b').zfill(4)

def left_shift(binary, num):
    # print '--' + binary
    # print '--' + binary[:num]
    # print '--' + binary[num:]
    return binary[num:] + binary[:num]

def split_text(binary, length):
    bin = ''
    for i in range(0, len(binary), length):
        bin += binary[i:i+length] + ' '
    return bin

def debug(tag, content, length=None):
    content = str(content)
    if length is None:
        print tag + ' : ' + content
    else:
        print tag + ' : ' + split_text(content, length)

def xor(binary1, binary2):
    result = ''
    length = len(binary1)
    for i in range(length):
        if binary1[i] == binary2[i]:
            result += '0'
        else:
            result += '1'
    return result

def binary_to_int(binary):
    return int(binary,2)

def binary_to_hex(binary):
    return hex(int(binary,2))[2:]
