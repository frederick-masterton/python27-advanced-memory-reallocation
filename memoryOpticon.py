#Python 2.7
#Memory allocation measurement and optimization

'''This function will call return the size in memory of different objects
using the has_atr sys function
'''

import sys
import memory_profiler
import psutil

#@profile
def show_sizeof(x, level=0):
    print '\t' * level, x.__class__, sys.getsizeof(x), x
    return '\t' * level, x.__class__, sys.getsizeof(x), x
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, levl + 1)
            else:
                for xx in x:
                   show_sizeof(xx, level + 1)


#For the same object; x32 memory allocations are less than x64 memory allocations.

#Consider the following.

show_sizeof({})
show_sizeof({1:'a',2:'b',3:'c'})
show_sizeof(())
show_sizeof((1,2,3))
show_sizeof([])
show_sizeof([1,2,3])

#How python handles objects in memory is by defining a hash key for each object
#If they're identical theyre's no need for more memory because the hash keys say their the same
print ' These lists have the same hash key:\n list1 = [1,2,3] \n list2 = [1,2,3] \n list3 = list1 \n '

list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

#Much better to have a large list and constantly change its values than
#Python never releases memory that integers,floats,lists and dictionaries use because
#_ they're not covered under pymalloc




