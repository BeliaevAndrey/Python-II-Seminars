BIN_CONST = 2
OCT_CONST = 8
HEX_CONST = 16


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
        out_str = str(num % HEX_CONST) + out_str
        num //= HEX_CONST
    return '0x' + out_str


number = int(input('Your integer: '))
print(get_bin(number), bin(number))
print(get_oct(number), oct(number))
print(get_hex(number), hex(number))
