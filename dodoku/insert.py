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
    row = cell[0]
    col = cell[1]
    cell.append(0)
    if row < 4:
        if col < 4:
            cell[2] = 1
        elif col < 7:
            cell[2] = 2
        elif col < 10:
            cell[2] = 3
    elif row < 7:
        if col < 4:
            cell[2] = 4
        elif col < 7:
            cell[2] = 5
        elif col < 10:
            cell[2] = 6
    elif row < 10:
        if col < 4:
            cell[2] = 7
        elif col < 7:
            cell[2] = 8
        elif col < 10:
            cell[2] = 9
        elif col < 13:
            cell[2] = 10
        elif col < 16:
            cell[2] = 11
    elif row < 13:
        if col < 10:
            cell[2] = 12
        elif col < 13:
            cell[2] = 13
        elif col < 16:
            cell[2] = 14
    elif row < 16:
        if col < 10:
            cell[2] = 15
        elif col < 13:
            cell[2] = 16
        elif col < 16:
            cell[2] = 17
    return cell

def _find_index(loc):
    cell = _find_location(loc)
    row = cell[0] - 1
    col = cell[1] - 1
    index = 0
    if row < 6:
        index = row * 9 + col
    elif row < 9:
        index = 54 + (row - 6) * 15 + col
    elif row < 15:
        index = 99 + (row - 9) * 9 + col - 6
    return index
    
def _check_input(parms):
    result = True
    try:
        cell = _find_location(parms['cell'])
        row = cell[0]
        col = cell[1]
        if row < 1 or col < 1 or row > 15 or col > 15:
            result = False
        elif row < 7 and col > 9:
            result = False
        elif row > 9 and col < 7:
            result = False
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

#returns -2 for fixed hint, -1 for conflict, 1 for success
def _can_insert(val, loc, grid):
    blocks, rows, cols = _organize(grid)
    index = _find_index(loc)
    cell = _find_location(loc)
    row = cell[0] - 1
    col = cell[1] - 1
    block = cell[2] - 1
    if grid[index] < 0:
        return -2
    if val in rows[row] or val * -1 in rows[row]:
        return -1
    elif val in cols[col] or val * -1 in cols[col]:
        return -1
    elif val in blocks[block] or val * -1 in blocks[block]:
        return -1
   # if val 
    return 1

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
