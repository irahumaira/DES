import tables
import utils


def do_ip(binary):
    ip_x = ''
    length = len(tables.IP)
    for i in range(length):
        ip_x += binary[tables.IP[i] - 1]
    l0 = ip_x[:length / 2]
    r0 = ip_x[length / 2:]

    utils.debug('IP(x)', ip_x, 8)
    utils.debug('L0', l0, 8)
    utils.debug('R0', r0, 8)
    return l0, r0


def do_pc1(binary):
    cd_k = ''
    length = len(tables.PC1)
    for i in range(length):
        cd_k += binary[tables.PC1[i] - 1]
    c0 = cd_k[:length / 2]
    d0 = cd_k[length / 2:]

    utils.debug('IP(x)', cd_k, 7)
    utils.debug('L0', c0, 7)
    utils.debug('R0', d0, 7)
    return c0, d0


def do_pc2(binary):
    k = ''
    length = len(tables.PC2)
    for i in range(length):
        k += binary[tables.PC2[i] - 1]
    return k


def start():
    # plain text
    with open('input.txt', 'rb') as f:
        plain = f.read().splitlines()[0]
    utils.debug('plain text', plain)

    # split text
    plains = utils.split_string(plain, 8)
    plains = utils.split_string('COMPUTER', 8)
    utils.debug('splitted', plains)

    # to binary
    plains_binary = []
    for plain in plains:
        plains_binary.append(utils.string_to_binary(plain))
    utils.debug('plain binary', plains_binary)

    # key
    key = '12345678'
    key_binary = utils.string_to_binary(key)
    key_binary = '0001001100110100010101110111100110011011101111001101111111110001'
    utils.debug('key', key)
    utils.debug('key binary', key_binary, 8)

    # generate
    l0, r0 = do_ip(plains_binary[0])
    c0, d0 = do_pc1(key_binary)
    l = [l0]
    r = [r0]
    c = [c0]
    d = [d0]

    # shift
    for i in range(len(tables.LEFT_SHIFT)):
        c.append(utils.left_shift(c[i], tables.LEFT_SHIFT[i]))
        d.append(utils.left_shift(d[i], tables.LEFT_SHIFT[i]))
        # utils.debug('C' + str(i + 1), c[i + 1], 7)
        # utils.debug('D' + str(i + 1), d[i + 1], 7)
        utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)
    c.remove(c0)
    d.remove(d0)

    # pc2
    k = []
    for i in range(len(tables.LEFT_SHIFT)):
        k.append(do_pc2(c[i] + d[i]))
        utils.debug('K' + str(i), k[i], 6)


start()
