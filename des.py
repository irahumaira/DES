import constants
import utils


def do_ip(binary):
    ip_x = ''
    length = len(constants.IP)
    for i in range(length):
        ip_x += binary[constants.IP[i] - 1]
    print 'IP(x) : ' + ip_x
    print 'L0 : ' + ip_x[:length / 2]
    print 'R0 : ' + ip_x[length / 2:]


def do_pc1(binary):
    cd_k = ''
    length = len(constants.PC1)
    for i in range(length):
        cd_k += binary[constants.PC1[i] - 1]
    print 'CD(k) : ' + cd_k
    print 'C0 : ' + cd_k[:length / 2]
    print 'D0 : ' + cd_k[length / 2:]


def start():
    # plain text
    with open('input.txt', 'rb') as f:
        plain = f.read().splitlines()[0]
    print 'plain text : ' + plain

    # split text
    plains = utils.split_string(plain, 8)
    plains = utils.split_string('COMPUTER', 8)
    print 'splitted : '
    print plains

    # to binary
    plains_binary = []
    for plain in plains:
        plains_binary.append(utils.string_to_binary(plain))
    print 'plain binary : '
    print plains_binary

    # key
    key = '12345678'
    key_binary = utils.string_to_binary(key)
    key_binary = '0001001100110100010101110111100110011011101111001101111111110001'
    print 'key : ' + key
    print 'key binary : ' + key_binary

    do_ip(plains_binary[0])
    do_pc1(key_binary)


start()
