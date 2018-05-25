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
    return

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
    name_op.
    '''
    return
