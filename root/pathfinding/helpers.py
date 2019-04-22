def read_file(filename):
    '''read from a file'''
    '''return a list of the lines'''
    mydata = []
    with open(filename) as f:
        for l in f.readlines():
            mydata.append(l)
    return mydata

def str_to_list(data):
    '''convert a stringlist to list'''
    mydata = []
    for d in data:
        mydata.append(eval(d))
    return mydata

def list_to_str(items):
    '''convert a list into a string'''
    result = ""
    for i in items:
        result += str(i) + ""
    return result

'''comments: relative path can not be given to open method
ex:open(../pathfinding/tests.txt) will not work
solution: import os then join the cwd path with the path to be read from
ex: import os
open(os.path.join(os.getcwd(), 'pathfinding/tests.txt'))'''