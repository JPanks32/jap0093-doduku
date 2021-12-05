import hashlib
import random
from pip._vendor.pyparsing import col

def _insert(parms):
    result_err = {'status': 'insert stub'}
    result ={'grid':'','integrity':'','status':'ok'}
    try:
        parms['grid'] = _parse_grid(parms['grid'])
    except:
        result_err['status'] = 'error: invalid grid'
        return result_err
    valid_input =_check_input(parms)
    if not valid_input == 1:
        if valid_input == -1:
            result_err['status'] = 'error: invalid cell reference'
        elif valid_input == -2:
            result_err['status'] = 'error: missing cell reference'
        elif valid_input == -3:
            result_err['status'] = 'error: invalid value'
        elif valid_input == -4:
            result_err['status'] = 'error: integrity mismatch'
        
        #result_err['status'] = 'error: invalid input'
        return result_err 
    value = 0
    try:
        value = int(parms['value'])
    except:
        pass
    grid = parms['grid']
    loc = parms['cell']
    valid = _can_insert(value, loc, grid)
    if valid == 1:
        grid = _change_val(value, loc, grid)
        result['grid'] = grid
    elif valid == -1:
        result['status'] = 'warning'
        grid = _change_val(value, loc, grid)
        result['grid'] = grid
    elif valid == -2:
        result_err['status'] = 'error: attempt to change fixed hint'
        return result_err 
    integrity = _find_integrity(grid)
    rand = random.randint(0, 55)
    integrity = integrity[rand:rand+8]
    result['integrity'] = integrity
    
    return result

def _parse_grid(grid_str):
    grid_str = grid_str.split('[')[1].split(']')[0].split(',')
    grid = [0]*153
    for index in range(153):
        grid[index] = int(grid_str[index])
    return grid
    
def _find_location(loc):
    leng = len(loc)
    col_index = 2
    cell = [-1,-1,-1]
    if leng != 4:
        col_index = 3
        if leng == 5:
            if not ((loc[1:3].isdigit() and loc[4].isdigit()) or (loc[1].isdigit() and loc[3:5].isdigit())):
                return cell
            if not loc[1:3].isdigit():
                col_index = 2
        elif leng == 6:
            if not ((loc[1:3].isdigit() and loc[4:6].isdigit())):
                return cell
        else:
            return cell
    if str.lower(str(loc[0])) != 'r' or str.lower(str(loc[col_index])) != 'c':
        return cell
    else:
        cell[0] = int(loc[1:col_index])
        cell[1] = int(loc[col_index + 1:leng])
    row = cell[0]
    col = cell[1]
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


  
#-1 for invalid cell reference
#-2 for missing cell ref
#-3 for invalid value
#-4 for integrity issues

def _check_input(parms):
    result = 1
    try:
        cell = _find_location(parms['cell'])
        row = cell[0]
        col = cell[1]
        if row < 1 or col < 1 or row > 15 or col > 15:
            result = -1
        elif row < 7 and col > 9:
            result = -1
        elif row > 9 and col < 7:
            result = -1
    except:
        result = -2
    if 'value' in parms:
        try:
            if parms['value'] != None:
                if int(parms['value']) < 1 or int(parms['value']) > 9 or type(parms['value']) is not str:
                    result = -3
        except:
            result = -3
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
            result = -4
        elif parms['integrity'] not in _find_integrity(parms['grid']):
            print(_find_integrity(parms['grid']))
            result = -5
    except:
        result = -6
    return result

#returns -2 for fixed hint, -1 for conflict, 1 for success

def _can_insert(val, loc, grid):
    blocks, rows, cols = _organize(grid)
    index = _find_index(loc)
    if grid[index] < 0:
        return -2
    if val == 0:
        return 1
    cell = _find_location(loc)
    row = cell[0] - 1
    col = cell[1] - 1
    block = cell[2] - 1
    if block < 8:
        if len(rows[row]) == 15:
            _rows = rows[row][0:9]
        else:
            _rows = rows[row]
        if len(cols[col]) == 15:
            _cols = cols[col][0:9]
        else:
            _cols = cols[col]
    elif block > 8:
        if len(rows[row]) == 15:
            _rows = rows[row][6:15]
        else:
            _rows = rows[row]
        if len(cols[col]) == 15:
            _cols = cols[col][6:15]
        else:
            _cols = cols[col]
    else:
        _rows = rows[row]
        _cols = cols[col]
    if val in rows[row] or val * -1 in rows[row]:
        return -1
    elif val in cols[col] or val * -1 in cols[col]:
        return -1
    elif val in blocks[block] or val * -1 in blocks[block]:
        return -1
    return 1

def _change_val(val, loc, grid):
    index = _find_index(loc)
    grid[index] = val
    return grid

def _organize(grid):
    col_maj = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    row_maj = [[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 15,[0]* 15,[0]* 15,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9,[0]* 9]
    block_row_maj = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
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
#
def _find_integrity(grid):
    block, row, cols = _organize(grid)
    col_maj = []
    for col in cols:
        for num in col:
            col_maj.append(num)
    col_str =_concat_columns(col_maj)
    myHash = hashlib.sha256()
    myHash.update(col_str.encode())
    myHashDigest = myHash.hexdigest()
    result = myHashDigest.lower() 
    return result
