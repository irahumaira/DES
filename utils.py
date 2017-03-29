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
