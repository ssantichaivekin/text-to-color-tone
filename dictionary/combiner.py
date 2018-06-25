'''
This file defines functions that helps us combine functions and
obtain new functions that is the product of the two combined
functions.
'''

def func_and(funcA, funcB) :
    '''
    Receive two functions, each accepting one word and returning a
    boolean. Return a function that accepts a word and return True
    if both the two parameter functions eveluate to true. Return
    False otherwise.
    '''
    return lambda x: funcA(x) and funcB(x)

def name_concat(nameA, nameB) :
    '''
    Concatenate the two names with a dash - in the middle.
    '''
    return nameA + '-' + nameB

def group_product(func_op, name_op, listfuncA, listfuncB) :
    '''
    Param -
    func_op : function that specifies how to merge two functions.
    name_op : function that specifies how to merge two names.
    listfuncA, B : list of dictionaries, each dict containing two
      parameters {'name' : name, 'func' : func}
    Return -
    a list of function of size len(A) * len(B) as the product of
    two lists. Each product is calculated using func_op and 
    name_op. The product is also in the format
    {'name' : name, 'func' : func}
    '''
    all_func_dict = []
    for funcA_dict in listfuncA :
        for funcB_dict in listfuncB :
            nameA = funcA_dict['name']
            nameB = funcB_dict['name']
            funcA = funcA_dict['func']
            funcB = funcB_dict['func']
            nameAB = name_op(nameA, nameB)
            funcAB = func_op(funcA, funcB)
            all_func_dict += [{'name': nameAB, 'func':funcAB}]
    return all_func_dict

if __name__ == '__main__' :
    listfuncA = [
        {'name' : 'odd', 'func': lambda x: x % 2 == 1},
        {'name' : 'greaterthan2', 'func': lambda x: x > 2}
    ]
    listfuncB = [
        {'name': 'div3', 'func': lambda x: x % 3 == 0 },
        {'name': 'div5', 'func': lambda x: x % 5 == 0 }
    ]
    list_all_func = group_product(func_and, name_concat, listfuncA, listfuncB)
    assert len(list_all_func) == 4
    checked = False
    for funcdict in list_all_func :
        if funcdict['name'] == 'odd-div3' :
            checked = True
            f = funcdict['func']
            assert f(5) == False
            assert f(6) == False
            assert f(7) == False
            assert f(8) == False
            assert f(9) == True
    assert checked == True



