from typing import List

# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

def encode_strings(strs: List[str]) -> str:
    delimiter = '#'
    encoded = ''.join(f"{delimiter}{len(s)}{delimiter}{s}" for s in strs)
    return encoded

def decode_strings(encoded: str) -> List[str]:
    string_array = []
    i = 0

    while i < len(encoded):
            if (encoded[i] == '#'):
                 i += 1            
            
            digit = ''
            while (encoded[i].isdigit()):
                digit += encoded[i] 
                i += 1
            string_len = int(digit)
            
            i += 1
            string_array.append(encoded[i:i + string_len]) 
            i += string_len
        
    return string_array

import struct

def encode_binary(strs: List[str]) -> str:
    result = b''
    for s in strs:
        encoded_length = struct.pack('>I', len(s))
        result += encoded_length + s.encode('utf-8')
    return result

def decode_binary(encoded: str) -> List[str]:
    string_array = []
    i = 0

    while i < len(encoded):
        length = struct.unpack('>I', encoded[i:i + 4])[0]
        i += 4
        string_array.append(encoded[i:i + length].decode('utf-8'))
        i += length
    return string_array