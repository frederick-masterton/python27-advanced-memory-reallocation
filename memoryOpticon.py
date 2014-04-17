#Python 2.7
#Memory allocation measurement and optimization

'''This function will call return the size in memory of different objects
using the has_atr sys function
'''

import sys

def show_sizeof(x, level=0):
    print '\t' * level, x.__class__, sys.getsizeof(x), x
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_sizeof(xx, levl + 1)
            else:
                for xx in x:
                    show_sizeof(xx, level + 1)


#For the same object; x32 memory allocations are less than x64 memory allocations.

#Consider the following.
print 'Empty Dictionary :%d' % show_sizeof({})
print 'Full Dictionary :%d' % show_sizeof({})

print 'Empty tuple :%d' % show_sizeof(())
print 'Full tuple :%d' % show_sizeof(())

print 'Empty list :%d' % show_sizeof([])
print 'Full list :%d' % show_sizeof([1,2,3,4,5])


