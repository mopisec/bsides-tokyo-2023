#!/usr/bin/env python3

import sys

def deobfuscate(payload: list[str]) -> list[str]:
    result = []
    obstacle_str = payload[-2][34:39]
    for line in payload[:-2]:
        line = line[27:] # delete prologue part
        line = line.replace(obstacle_str, '') # delete obstacle string
        line = line.replace('""', '"') # unescape double quotes
        line = line.replace('" & Vbcrlf', '') # delete '" & Vbcrlf'
        result.append(line.strip())
    return result

def main():
    if len(sys.argv) != 2:
        vbscript_file = './malicious_vbscript.txt' # default
    else:
        vbscript_file = sys.argv[1]
    
    with open(vbscript_file, 'r') as vf:
        payload = vf.readlines()
    
    while 'Replace(' in payload[-2]:
        payload = deobfuscate(payload)
    
    result = '\n'.join(payload)
    print(result)

if __name__ == '__main__':
    main()
