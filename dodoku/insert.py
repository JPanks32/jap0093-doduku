import hashlib
import random

def _insert(parms):
    result = {'status': 'insert stub'}
    return result

def _find_location(loc):
    cell = loc.split('r')[1].split('c')
    cell[0] = int(cell[0])
    cell[1] = int(cell[1])
    return cell

def _check_input(parms):
    result = True
    try:
        _find_location(parms['cell'])
    except:
        result = False
    try:
        if int(parms['value']) < 1 or int(parms['value']) > 9 or type(parms['value']) is not str:
            result = False
    except:
        pass
    try:
        if len(parms['grid']) != 153:
            result = False
        for val in parms['grid']:
            if val < -9 or val > 9 or type(val) is not int:
                result = False
                break
    except:
        result = False
    try:
        if len(parms['integrity']) != 8 or type(parms['integrity']) is not str:
            result = False
    except:
        result = False
    return result

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
def _find_integrity(grid):
    col_maj = _column_major(grid)
    col_str =_concat_columns(col_maj)
    myHash = hashlib.sha256()
    myHash.update(col_str.encode())
    myHashDigest = myHash.hexdigest()
    result = myHashDigest.lower() 
    return result
