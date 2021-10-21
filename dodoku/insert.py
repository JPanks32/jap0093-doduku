import hashlib
import random
from pip._vendor.pyparsing import col

def _insert(parms):
    result = {'status': 'insert stub'}
    return result

def _find_location(loc):
    cell = loc.split('r')[1].split('c')
    cell[0] = int(cell[0])
    cell[1] = int(cell[1])
    return cell

def _find_index(loc):
    cell = _find_location(loc)
    row = cell[0] - 1
    col = cell[1] - 1
    index = 0
    
    return index
    
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

def _organize(grid):
    col_maj = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    row_maj = [[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 15,[0]* 15,[0]* 15,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9]
    block_row_maj = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    result = []
    rowCount = 0
    colCount = 0
    for i in range(0, 54):
        rowCount = int((i -(i % 9)) / 9)
        row_maj[rowCount][colCount] = grid[i]
        col_maj[colCount].append(grid[i])
        
        
        if rowCount < 3:
            if colCount < 3:
                block_row_maj[0].append(grid[i])
            elif colCount < 6:
                block_row_maj[1].append(grid[i])
            elif colCount < 9:
                block_row_maj[2].append(grid[i])
        elif rowCount < 6:
            if colCount < 3:
                block_row_maj[3].append(grid[i])
            elif colCount < 6:
                block_row_maj[4].append(grid[i])
            elif colCount < 9:
                block_row_maj[5].append(grid[i])
        colCount += 1
        
        if colCount > 8:
            colCount = 0
    colCount = 0
    for i in range(54,99):
        rowCount = int((i-54 - ((i-54) % 15)) / 15) + 6
        row_maj[rowCount][colCount] = grid[i]
        col_maj[colCount].append(grid[i])
        if rowCount < 9:
            if colCount < 3:
                block_row_maj[6].append(grid[i])
            elif colCount < 6:
                block_row_maj[7].append(grid[i])
            elif colCount < 9:
                block_row_maj[8].append(grid[i])
            elif colCount < 12:
                block_row_maj[9].append(grid[i])
            elif colCount < 15:
                block_row_maj[10].append(grid[i])
                
        colCount += 1      
        if colCount > 14:
            colCount = 0
            
    colCount = 6
    for i in range(99, 153):
        rowCount = int((i-99 - ((i-99) % 9)) / 9) + 9
        row_maj[rowCount][colCount - 6] = grid[i]
        col_maj[colCount].append(grid[i])
        
        if rowCount < 12:
            if colCount < 9:
                block_row_maj[11].append(grid[i])
            elif colCount < 12:
                block_row_maj[12].append(grid[i])
            elif colCount < 15:
                block_row_maj[13].append(grid[i])
        elif rowCount < 15:
            if colCount < 9:
                block_row_maj[14].append(grid[i])
            elif colCount < 12:
                block_row_maj[15].append(grid[i])
            elif colCount < 15:
                block_row_maj[16].append(grid[i])
        colCount += 1
        if colCount > 14:
            colCount = 6

    return block_row_maj, row_maj, col_maj

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
