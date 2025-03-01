import numpy as np
from functools import reduce

def 十(*args):
  return np.sum(args)

def 一(*args):
  return args[0] - np.sum(args[1:])


def 乛(*args):
  arg_list = list(args)
  arg_list.reverse()
#   return reduce(lambda x,y: 一(x,y) if x == args[0] else 一(y,x), arg_list)
  return reduce(lambda x,y: y -x, arg_list)

def ϵ(tree):
  return reduce(lambda x,y: x + (ϵ(y) if isinstance(y, list) else [y]), tree, [])

def γ(func, lst):
    """Group elements of a list by the result of applying func to each element.
    
    Uses a reduce operation for a purely functional approach.
    """
    return reduce(
        lambda acc, item: {
            **acc,  # Unpack existing dictionary
            func(item): acc.get(func(item), []) + [item]  # Add new item to appropriate group
        },
        lst,  # Input list
        {}    # Initial accumulator (empty dictionary)
    )