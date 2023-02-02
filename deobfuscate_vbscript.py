#!/usr/bin/env python3

import sys

DEL_LIST = ['EVUCQUJ8D4 = EVUCQUJ8D4 & "', 'VZUMLKCQLE = VZUMLKCQLE & "', '" & Vbcrlf', '63WKZ', 'PLIZ]', '\n']

def deobfuscate(payload: list[str]) -> list[str]:
    result = []
    for line in payload[:-2]:
        for del_elem in DEL_LIST:
            line = line.replace(del_elem, '')
        line = line.replace('""', '"') # unescape double quotes
        result.append(line)
    return result

def main():
    if len(sys.argv) != 2:
        vbscript_file = './malicious_vbscript.txt' # default
    else:
        vbscript_file = sys.argv[1]
    
    with open(vbscript_file, 'r') as vf:
        stage_one = vf.readlines()
    
    stage_two = deobfuscate(stage_one)
    stage_three = deobfuscate(stage_two)
    
    result = '\n'.join(stage_three)
    print(result)

if __name__ == '__main__':
    main()
