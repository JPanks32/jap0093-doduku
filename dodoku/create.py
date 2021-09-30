import hashlib
import random
def _create(parms):
    result = {'grid': '', 'status': '', 'integrity': ''}
    lvl = 'level'
    
    
    if (len(list(parms)) == 1 and list(parms)[0] == 'op') or list(parms)[1] != 'level' or parms[lvl] == '1' or parms[lvl] == '' or parms[lvl] == None:
        result['status'] = 'ok'
        result['grid'] = [
            0,-2,0,0,-1,0,0,-4,0,
            -8,0,-1,-9,0,0,0,0,-5,
            0,0,0,0,-3,0,0,-1,0,
            0,-3,0,0,0,0,-4,0,-6,
            -5,0,-9,0,0,0,0,0,-7,
            0,0,0,0,0,0,-2,-8,0,
            -2,0,0,-6,0,0,0,0,0,
            0,-1,-4,0,-6,0,0,0,-6,
            0,0,-3,0,0,0,-2,0,0,
            -1,0,-9,0,-4,0,-5,-7,0,
            0,0,0,0,0,-7,0,0,-5,
            0,0,-6,0,0,0,0,-9,0,
            -2,0,0,0,0,0,-4,0,-8,
            -7,0,-9,0,0,0,0,0,0,
            0,-5,0,0,-9,0,0,0,0,
            -4,0,0,-6,0,-3,-9,0,0,
            0,-6,0,0,-5,0,0,-3,-1
            ]
    elif parms[lvl] == '2':
        result['status'] = 'ok'
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
    elif parms[lvl] == '3':
        result['status'] = 'ok'
        result['grid'] = [
            0,0,0,0,-6,0,0,0,0,0,0,0,-4,0,-9,0,0,0,0,0,-9,-7,0,-5,-1,0,0,0,-5,-2,0,-7,0,-8,-9,0,-9,0,0,
            -5,0,-2,0,0,-4,0,-8,-3,0,-4,0,-7,-2,0,0,0,-1,-2,0,-8,0,0,0,0,-3,0,0,0,0,0,0,0,-6,0,-4,0,0,0,-8,0,
            -7,0,0,0,0,0,0,0,-5,0,0,0,0,-1,0,-6,-3,0,0,0,-9,-8,0,-5,0,-1,-2,0,-2,0,0,-7,0,-1,0,0,-3,0,-4,-3,0,-8,0,
            -6,-5,0,0,0,-7,-3,0,-5,-9,0,0,0,0,0,-4,0,-2,0,0,0,0,0,0,0,-6,0,0,0,0
            ]
    if result['status'] != 'ok': 
        try:
            x = parms[lvl]
            if(x != '1' and x != '2' and x != '3'):
                result['status'] = "error"
        except:
            result['status'] = "error"
    if result['status'] == 'ok':
        integ = _hash(result['grid'])  
        short_start = random.randint(0, len(integ) - 8)
        short_integ = ''
        for short_fill in range(short_start, short_start + 8):
            short_integ += integ[short_fill]
            result['integrity'] = short_integ
    return result

#It divides up the board into sections with equal-length rows, then iterates through them, filling in a different
    #array for each column.
#It then combines all the arrays into one array for the numbers
def _column_major(grid):
    arr = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    result = []
    colCount = 0
    for i in range(0, 54):
        arr[colCount].append(grid[i])
        colCount += 1
        if colCount > 8:
            colCount = 0
    colCount = 0
    for i in range(54,99):
        arr[colCount].append(grid[i])
        colCount += 1
        if colCount > 14:
            colCount = 0
    colCount = 6
    for i in range(99, 153):
        arr[colCount].append(grid[i])
        colCount += 1
        if colCount > 14:
            colCount = 6

    for col in arr:
        for num in col:
            result.append(num)
    return result

#It concatinates all of the strings in the array into one string
def _concat_columns(cols):
    result = ""
    for num in cols:
        result += str(num)
    return result
        
#it hash sha256 the grid provided by passing it through two other methods to turn it into
    #a column-major string, then casts the hash function on it        
def _hash(grid):
    col_maj = _column_major(grid)
    col_str =_concat_columns(col_maj)
    myHash = hashlib.sha256()
    myHash.update(col_str.encode())
    myHashDigest = myHash.hexdigest()
    result = myHashDigest.lower()
    
    return result
