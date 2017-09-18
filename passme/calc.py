import hashlib, base64
import sys, re
    
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
        print ('Error: hash function {0} is not defined.'.format(has))
        sys.exit()
    
    # Generate password
    
    base = base64.b64encode(h.digest()).decode("utf-8") # base64 encode
    
    if char == ('base64'): # base64: alphabet, number, +/
        p = base
    elif char == ('an'): # an: alphabet + number
        p = re.sub(r'[+/=]',"", base)
    elif char == ('a'): # a: alphabet
        p = re.sub(r'[0-9+/=]',"", base)
    elif char == ('n'): # n: number
        p = re.sub(r'[a-f]',"", (h.hexdigest()))
    elif char == ('ans'): # ans: alphabet, number, symbol
        symbol = '#[$-=?@]_!' # Symbols in additions to + and / 
        p = base.replace('=','')
        a = ord(p[0:1]) % len(symbol)
        symbol = symbol[a:-1] + symbol[0:a]
        for s in symbol: 
            p = p.replace(p[0:1], s)[1:-1] + p[0:1]
    elif char == ('ans95'): # ans95: alphabet, number, 95 symbols (JavaScript version not available)
        h = int.from_bytes(h.digest(), byteorder='big')
        p = ''
        for i in range(plen):
            p = p + chr(h % 95 + 32)
            h = h // 95
    else:
        print ('Error: character type {0} is not defined.'.format(char))
        sys.exit()
    
    return (p[0:plen])
