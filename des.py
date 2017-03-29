import tables
import utils


def permute(binary, table):
    permuted = ''
    length = len(table)
    for i in range(length):
        permuted += binary[table[i] - 1]
    return permuted


def sbox(binary):
    b = ''
    for i in range(0, len(binary), 6):
        x = int(binary[i] + binary[i + 5], 2)
        y = int(binary[i + 1:i + 5], 2)
        # utils.debug('x',  x)
        # utils.debug('y', y)
        # utils.debug('SBOX', utils.int_to_binary(tables.SBOX[i/6][x][y]))
        b += utils.int_to_binary(tables.SBOX[i / 6][x][y])
    return b


def start():

    # plain text
    with open('input.txt', 'rb') as f:
        plain = f.read()
    plain_splitted = utils.string_to_array(plain, 8)
    plain_binary_splitted = []
    for plain in plain_splitted:
        plain_binary_splitted.append(utils.string_to_binary(plain))
    print ''
    utils.debug('plain text', [plain])
    utils.debug('splitted', plain_splitted)
    utils.debug('plain binary', plain_binary_splitted)

    # key
    key = '12345678'
    key_binary = utils.string_to_binary(key)
    print ''
    utils.debug('key', key)
    utils.debug('key binary', key_binary, 8)

    # generate L, R
    lr0 = permute(plain_binary_splitted[0], tables.IP)
    l = [lr0[:len(tables.IP) / 2]]
    r = [lr0[len(tables.IP) / 2:]]
    print ''
    utils.debug('L0', l[0], 8)
    utils.debug('R0', r[0], 8)

    # generate C, D
    cd0 = permute(key_binary, tables.PC1)
    c = [cd0[:len(tables.PC1) / 2]]
    d = [cd0[len(tables.PC1) / 2:]]
    print ''
    utils.debug('CD0', cd0, 7)
    for i in range(16):
        c.append(utils.left_shift(c[i], tables.LEFT_SHIFT[i]))
        d.append(utils.left_shift(d[i], tables.LEFT_SHIFT[i]))
        utils.debug('CD' + str(i + 1), c[i + 1] + d[i + 1], 7)

    # generate K
    print ''
    k = ['']
    for i in range(16):
        k.append(permute(c[i + 1] + d[i + 1], tables.PC2))
        utils.debug('K' + str(i + 1), k[i + 1], 6)

    # ---
    er = []
    a = ['']
    b = ['']
    pb = ['']
    for i in range(16):
        er.append(permute(r[i], tables.EXPANSION))
        a.append(utils.xor(er[i], k[i + 1]))
        b.append(sbox(a[i + 1]))
        pb.append(permute(b[i + 1], tables.PBOX))
        r.append(utils.xor(l[i], pb[i + 1]))
        l.append(r[i])
        print ''
        utils.debug('ER' + str(i), er[i], 6)
        utils.debug('A' + str(i + 1), a[i], 6)
        utils.debug('B' + str(i + 1), b[i], 4)
        utils.debug('PB' + str(i + 1), pb[i], 8)
        utils.debug('R' + str(i + 1), r[i + 1], 8)
        utils.debug('L' + str(i + 1), l[i + 1], 8)

    # cipher
    cipher_binary = permute(r[16] + l[16], tables.IP_INV)
    cipher_binary_splitted = utils.string_to_array(cipher_binary, 8)
    cipher = ''
    for i in range(len(cipher_binary_splitted)):
        cipher += utils.binary_to_hex(cipher_binary_splitted[i])
    print ''
    utils.debug('cipher binary', cipher_binary, 8)
    utils.debug('cipher', cipher)

    with open('output.txt', 'wb') as f:
        f.write(cipher)


start()
