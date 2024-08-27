import hashlib
import base64
import os
import sys
import re
from configobj import ConfigObj


def genpass(seed, has, char, plen):

    # Apply hash function

    if has == ('sha384'):
        h = hashlib.sha384(seed)
    elif has == ('sha512'):
        h = hashlib.sha512(seed)
    elif has == ('sha3_384'):
        h = hashlib.sha3_384(seed)
    elif has == ('sha3_512'):
        h = hashlib.sha3_512(seed)
    else:
        print('Error: hash function {0} is not defined.'.format(has))
        sys.exit()

    # Generate password

    base = base64.b64encode(h.digest()).decode("utf-8")  # base64 encode

    if char == ('base64'):  # base64: alphabet, number, +/
        p = base
    elif char == ('an'):  # an: alphabet + number
        p = re.sub(r'[+/=]', "", base)
    elif char == ('a'):  # a: alphabet
        p = re.sub(r'[0-9+/=]', "", base)
    elif char == ('n'):  # n: number
        p = re.sub(r'[a-f]', "", (h.hexdigest()))
    elif char == ('ans'):  # ans: alphabet, number, symbol
        symbol = '#[$-=?@]_!'  # Symbols in additions to + and /
        p = base.replace('=', '')
        a = ord(p[0:1]) % len(symbol)
        symbol = symbol[a:-1] + symbol[0:a]
        for s in symbol:
            p = p.replace(p[0:1], s)[1:-1] + p[0:1]
    elif char == ('ans95'):  # ans95: alphabet, number, 95 symbols (JavaScript version not available)
        h = int.from_bytes(h.digest(), byteorder='big')
        p = ''
        for i in range(plen):
            p = p + chr(h % 95 + 32)
            h = h // 95
    else:
        print('Error: character type {0} is not defined.'.format(char))
        sys.exit()

    return (p[0:plen])


def testcalc():
    for key in [
        ['key', 'sha384', 'an', 10, 'G3RaDVADAu'],
        ['日本語', 'sha512', 'ans', 14, 'c9bJ_LZrJc0[vV'],
        ['BfY1Qf1h2Y,loQKKgc', 'sha3_384', 'base64', 12, 'QvOK53SPiqxy'],
        ['e\4!$P7}V3^YG^Wn~', 'sha3_512', 'a', 15, 'TdWBpQAjBBbwpgk'],
        ['Y#rzp4FTnXEJCH6|)q', 'sha384', 'n', 14, '22974221358045'],
        ['y#h$2qaS?$/h&oaq"hh', 'sha512', 'ans95', 18, 'm9?2P0&vdj\\mg$H"X&'],
    ]:
        password = genpass(key[0].encode('utf-8'), key[1], key[2], int(key[3]))
        assert password == key[4], 'Unexpected password produced.\n' \
            'hash = ' + key[1] + '\nchar = ' + key[2] + '\nlen = ' + str(key[3]) + '\nseed = ' + key[0] \
            + '\nExpected password = ' + \
            key[4] + '\nCalculated password = ' + password
    print('Test completed without error.')
    return


def readpass(site, master):
    if os.path.exists('.passme'):
        ConfFile = '.passme'
    else:
        ConfFile = os.path.expanduser('~/.passme')
    SiteKeyFile = ConfigObj(os.path.expanduser(ConfFile))['SiteKeyFile']
    if not os.path.exists(SiteKeyFile):
        return 'Error: ' + SiteKeyFile + ' not found.'
    sitekey = ConfigObj(SiteKeyFile, encoding='utf-8')
    if site not in sitekey:
        return site + ' not registered in passme.'
    s = sitekey[site]
    seed = (master + s['seed']).encode('utf-8')
    password = genpass(seed, s['hash'], s['char'], int(s['len']))
    return password
