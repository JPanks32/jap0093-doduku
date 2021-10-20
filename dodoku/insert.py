def _insert(parms):
    result = {'status': 'insert stub'}
    return result

def _find_location(loc):
    r = 1
    c = 1
    return r, c

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

