import tables
import utils


def do_ip(binary):
    lr0 = ''
    length = len(tables.IP)
    for i in range(length):
        lr0 += binary[tables.IP[i] - 1]
    l0 = lr0[:length / 2]
    r0 = lr0[length / 2:]

    utils.debug('LR0', lr0, 8)
    utils.debug('L0', l0, 8)
    utils.debug('R0', r0, 8)
    return l0, r0


def do_ip_inv(binary):
    ip = ''
    length = len(tables.IP_INV)
    for i in range(length):
        ip += binary[tables.IP_INV[i] - 1]
    return ip


def do_pc1(binary):
    cd_k = ''
    length = len(tables.PC1)
    for i in range(length):
        cd_k += binary[tables.PC1[i] - 1]
    c0 = cd_k[:length / 2]
    d0 = cd_k[length / 2:]

    utils.debug('CD0', cd_k, 7)
    utils.debug('C0', c0, 7)
    utils.debug('D0', d0, 7)
    return c0, d0


def do_pc2(binary):
    k = ''
    length = len(tables.PC2)
    for i in range(length):
        k += binary[tables.PC2[i] - 1]
    return k


def expands(binary):
    e = ''
    length = len(tables.EXPANSION)
    for i in range(length):
        e += binary[tables.EXPANSION[i] - 1]
    return e


def sbox(binary):
    b = ''
    for i in range(0, len(binary), 6):
        x = int(binary[i] + binary[i + 5], 2)
        y = int(binary[i + 1:i + 5], 2)
        # utils.debug('x',  x)
        # utils.debug('y', y)
        # utils.debug('S', utils.int_to_binary(tables.S[i/6][x][y]))
        b += utils.int_to_binary(tables.S[i / 6][x][y])
    return b


def pbox(binary):
    pb = ''
    length = len(tables.P)
    for i in range(length):
        pb += binary[tables.P[i] - 1]
    return pb


def start():
    # plain text
    with open('input.txt', 'rb') as f:
        plain = f.read()
    utils.debug('plain text', [plain])

    # split text
    plain_splitted = utils.split_string(plain, 8)
    #plain_splitted = utils.split_string('COMPUTER', 8)
    utils.debug('splitted', plain_splitted)

    # to binary
    plain_binary_splitted = []
    for plain in plain_splitted:
        plain_binary_splitted.append(utils.string_to_binary(plain))
    utils.debug('plain binary', plain_binary_splitted)

    # key
    key = '12345678'
    key_binary = utils.string_to_binary(key)
    #key_binary = '0001001100110100010101110111100110011011101111001101111111110001'
    print ''
    utils.debug('key', key)
    utils.debug('key binary', key_binary, 8)

    # generate L(0), R(0), C(0), D(0)
    print ''
    l0, r0 = do_ip(plain_binary_splitted[0])
    c0, d0 = do_pc1(key_binary)
    l = [l0]
    r = [r0]
    c = [c0]
    d = [d0]

    # generate c, d
    print ''
    for i in range(16):
        c.append(utils.left_shift(c[i], tables.LEFT_SHIFT[i]))
        d.append(utils.left_shift(d[i], tables.LEFT_SHIFT[i]))
        utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)

    # generate k
    print ''
    k = ['']
    for i in range(16):
        k.append(do_pc2(c[i + 1] + d[i + 1]))
        utils.debug('K' + str(i + 1), k[i + 1], 6)

    # ---
    er = []
    a = ['']
    b = ['']
    pb = ['']
    for i in range(16):
        er.append(expands(r[i]))
        a.append(utils.xor(er[i], k[i + 1]))
        b.append(sbox(a[i + 1]))
        pb.append(pbox(b[i + 1]))
        r.append(utils.xor(l[i], pb[i + 1]))
        l.append(r[i])
        print ""
        utils.debug('ER' + str(i), er[i], 6)
        utils.debug('A' + str(i + 1), a[i], 6)
        utils.debug('B' + str(i + 1), b[i], 4)
        utils.debug('PB' + str(i + 1), pb[i], 8)
        utils.debug('R' + str(i + 1), r[i + 1], 8)
        utils.debug('L' + str(i + 1), l[i + 1], 8)

    # cipher
    rl16 = r[16] + l[16]
    cipher_binary = do_ip_inv(rl16)
    cipher_binary_splitted = utils.split_string(cipher_binary, 8)
    chiper = ''
    for i in range(len(cipher_binary_splitted)):
        chiper += utils.binary_to_hex(cipher_binary_splitted[i])
    print ''
    utils.debug('RL16', rl16, 8)
    utils.debug('cipher binary', cipher_binary, 8)
    utils.debug('chiper', chiper)


start()
