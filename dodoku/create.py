import hashlib
import random
def _create(parms):
    result = {'grid': '', 'status': 'create stub', 'integrity': ''}
    result['status'] = 'ok'

    if parms['level'] == '2':
        result['grid'] = [
            0,-6,0,0,0,0,0,-5,-9,
            -9,-3,0,-4,-8,0,0,0,0,
            0,0,0,0,0,-7,-3,0,0,
            0,-5,0,0,-1,0,0,-4,-6,
            0,0,0,0,0,-6,0,-9,0,
            0,-8,-1,-2,0,0,0,0,0,
            0,0,0,0,-7,0,0,0,0,
            0,0,0,0,-5,0,-8,0,-4,
            0,0,-1,0,0,0,-7,0,0,
            -6,0,-2,0,-9,0,0,0,0,
            0,0,0,0,-5,0,0,0,0,
            0,0,0,0,0,-9,-5,-3,0,
            0,-7,0,-4,0,0,0,0,0,
            -5,-8,0,0,-1,0,0,-9,0,
            0,0,-2,-1,0,0,0,0,0,
            0,0,0,0,-9,-8,0,-6,-1,
            -6,-1,0,0,0,0,0,-7,0
            ]
    integ = _hash(result['grid'])  
    print(integ)
    short_start = random.randint(0, len(integ) - 8)
    short_integ = ''
    for short_fill in range(short_start, short_start + 8):
        short_integ += integ[short_fill]
    result['integrity'] = short_integ
    return result

def _column_major(grid):
    arr = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    result = []
    colCount = 0
    for i in range(0, 53):
        arr[colCount].append(grid[i])
        colCount += 1
        if colCount > 8:
            colCount = 0
    colCount = 0
    for i in range(54,98):
        arr[colCount].append(grid[i])
        colCount += 1
        if colCount > 14:
            colCount = 0
    colCount = 6
    for i in range(99, 152):
        arr[colCount].append(grid[i])
        colCount += 1
        if colCount > 14:
            colCount = 6
    for col in arr:
        for num in col:
            result.append(num)
    return result


def _concat_columns(cols):
    result = ""
    for num in cols:
        result += str(num)
    return result
        
        
def _hash(grid):
    col_maj = _column_major(grid)
    col_str =_concat_columns(col_maj)
    myHash = hashlib.sha256()
    myHash.update(col_str.encode())
    myHashDigest = myHash.hexdigest()
    result = myHashDigest.lower()
    
    return result
