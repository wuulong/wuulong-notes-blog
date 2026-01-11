
def try_fix(s):
    print(f"Original: {s}")
    encodings = ['latin-1', 'cp1252', 'utf-8', 'utf-16le', 'utf-16be', 'big5']
    decodings = ['big5', 'gbk', 'utf-8', 'utf-16le', 'utf-16be', 'shift_jis']

    for enc in encodings:
        try:
            b = s.encode(enc)
            for dec in decodings:
                try:
                    res = b.decode(dec)
                    print(f"{enc} -> {dec}: {res}")
                except:
                    pass
        except:
            pass
            
    # Try byte manipulation if the string is actually "Garbage" interpreted as CP1252
    # e.g. "" might be some bytes in another encoding.
    
    # What if the hex code of the characters IS the Big5 hex?
    # char "" is U+D765. 
    # Hex D765 in Big5 is "篪".
    # char "偌" is U+504C.
    # Hex 504C in Big5 is "PL" (ASCII).
    
    # Maybe Shift-JIS? PUA?
    
    chars = list(s)
    print("Chars:", [hex(ord(c)) for c in chars])
    
    # What if we just take the code points and treat them as bytes?
    # Only if all codepoints are < 256... but D765 is big.
    
    # What if the bytes in the file were read as UTF-8, but they were Big5?
    # File has \xee\xb5\xa5 -> U+D765.
    # This means the file physically contains \xee\xb5\xa5.
    # If those bytes \xee\xb5... were meant to be Big5?
    # EE B5 -> 豯.
    
    pass

s = "偌"
try_fix(s)
