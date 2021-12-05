import dodoku.insert as insert

def _recommend(parms):
    result ={'recommendation':[], 'status':'ok'}
    result_err = {'status': 'error: 6'}
    try:
        print(parms['grid'])
        parms['grid'] = insert._parse_grid(parms['grid'])
    except:
        result_err['status'] = 'error: invalid grid'
        return result_err
    print(parms['grid'])
    valid_input = _validateParms(parms)
    if not valid_input == 1:
        print('rtr')
        print(valid_input)
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
    result['recommendation'] = values
    return result

def _validateParms(parms):
    return insert._check_input(parms)

def _identifyValues(cell, grid):
    result = []
    for val in range(1,10):
        if insert._can_insert(val, cell, grid) == 1:
            result.append(val)
    return result




