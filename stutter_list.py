#tail recursive stutter_list algorithm
#first solution:
'''
def stutter_list(lst):
    _stutter_list(lst, 0)
    
def _stutter_list(lst, index):
    if index >= len(lst):
        return
    else:
        lst.insert(index, lst[index])
        _stutter_list(lst, index + 2)
'''
#second solution:

def stutter_list(lst):
    _sl(lst, 2*len(lst))
    
def _sl(lst, size):
    if len(lst)==size or not lst:
        return
    else:
        firstElement = lst.pop(0)
        lst.append(firstElement)
        lst.append(firstElement)
        _sl(lst, size)

