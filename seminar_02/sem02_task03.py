BIN_CONST = 2
OCT_CONST = 8
HEX_CONST = 16
HEX_ALPHA = '0123456789abcdef'


def conv(num: int, base: int):
    if base not in [BIN_CONST, OCT_CONST, HEX_CONST]:
        print('Unsupported')
        raise SystemExit
    out = ""
    if base == HEX_CONST:
        while num:
            out = HEX_ALPHA[num % base] + out
            num //= base
        return '0x' + out
    else:
        while num:
            out = str(num % base) + out
            num //= base
        if base == OCT_CONST:
            return '0o' + out
        else:
            return '0b' + out


def get_bin(num):
    out_str = ""
    while num > 0:
        out_str = str(num % BIN_CONST) + out_str
        num //= BIN_CONST
    return '0b' + out_str


def get_oct(num):
    out_str = ""
    while num > 0:
        out_str = str(num % OCT_CONST) + out_str
        num //= OCT_CONST
    return '0o' + out_str


def get_hex(num):
    out_str = ""
    while num > 0:
        out_str = HEX_ALPHA[num % HEX_CONST] + out_str
        num //= HEX_CONST
    return '0x' + out_str


number = int(input('Your integer: '))
print(get_bin(number), bin(number))
print(get_oct(number), oct(number))
print(get_hex(number), hex(number))
print(conv(number, HEX_CONST), hex(number))
print(conv(number, BIN_CONST), bin(number))
print(conv(number, OCT_CONST), oct(number))
print(conv(number, 30), oct(number))
