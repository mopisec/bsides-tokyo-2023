import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: ' + sys.argv[0] + ' <VBSCRIPT_FILE>')
        exit()
    
    with open(sys.argv[1], 'r') as vf:
        stage_one = vf.readlines()
    
    stage_two = []
    del_list = ['EVUCQUJ8D4 = EVUCQUJ8D4 & "', '" & Vbcrlf', '63WKZ', '\n']
    for line in stage_one[:-2]:
        for del_elem in del_list:
            line = line.replace(del_elem, '')
        line = line.replace('""', '"')
        stage_two.append(line)
    
    stage_three = []
    del_list = ['VZUMLKCQLE = VZUMLKCQLE & "', '" & Vbcrlf', 'PLIZ]', '\n']
    for line in stage_two[:-2]:
        for del_elem in del_list:
            line = line.replace(del_elem, '')
        line = line.replace('""', '"')
        stage_three.append(line)
    
    result = '\n'.join(stage_three)
    print(result)

if __name__ == '__main__':
    main()
