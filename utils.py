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
