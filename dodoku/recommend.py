import dodoku.insert as insert

def _recommend(parms):
    result = {'status': 'recommend stub'}
    result_err = {'status': 'error: '}
    try:
        parms['grid'] = _loadGrid(parms['grid'])
    except:
        result_err['status'] = 'error: invalid grid'
        return result_err
    valid_input = _validateParms(parms)
    if not valid_input == 1:
        if valid_input == -1:
            result_err['status'] = 'error: invalid cell reference'
        elif valid_input == -2:
            result_err['status'] = 'error: missing cell reference'
        elif valid_input == -4:
            result_err['status'] = 'error: integrity mismatch'
        
        #result_err['status'] = 'error: invalid input'
        return result_err 
    
    grid = parms['grid']
    loc = parms['cell']
    values = _identifyValues(loc, grid)
    return result

def _validateParms(parms):
    return insert._check_input(parms)

def _loadGrid(grid):
    
    return grid

def _identifyValues(cell, grid):