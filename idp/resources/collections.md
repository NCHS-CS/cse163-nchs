---
title: Collections
---

#  Collections

This is a _cheatsheet_ of Python's collection classes.
- [Collections](#collections)
  - [Summary Comparison](#summary-comparison)
  - [List](#list)
  - [Tuple](#tuple)
  - [Set](#set)
  - [Dictionary](#dictionary)
  - [Simple Comprehensions](#simple-comprehensions)

## Summary Comparison

| Action         | List                                                                 | Tuple                                                                                  | Set                                                                                 | Dictionary                                                                                      |
|----------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Create         | `a = []`<br>`a = list()`<br>`a = [1, 2]`                             | `t = ()` # empty<br>`t = tuple()`<br>`t = (1, 2)`                                      | `s = set()`<br>`s = {1, 2}`                                                         | `d = {}`<br>`d = dict()`<br>`d = {k1:v1, k2:v2}`<br>`d = dict(dict2)`                          |
| Add / Insert   | `a.append(obj)`<br>`a.insert(idx, obj)`                              | `t = t + (obj,)`                                                                      | `s.add(3)`                                                                          | `d['b'] = 2`                                                                                    |
| Contains       | `if obj in a`                                                        | `if obj in t`                                                                         | `if obj in s`                                                                       | `if key in d`                                                                                   |
| Remove         | `a.remove(obj)`<br>`a.pop(index)`<br>`a.pop()`                       | **NA**                                                                                | `s.remove(obj)`<br>`s.pop()`<br>`s.discard('value')`                                 | `d.pop(key)`<br>`d.pop(key, def_val)`<br>`del d[key]`<br>`d.popitem()`                         |
| Get / Set      | `v = a[index]`                                                       | `v = t[index]`<br>`i1, i2 = t`<br>`i1, *mid, i2 = t`<br>`i1, *last = t`                | **NA**                                                                              | `v = d['a']`<br>`v = d.get('a', v)`                                                            |

## List

| Operation   | API                                                                                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Create      | `my_list = []`<br>`my_list = [x ** 2 for x in [1, 3, 5, 7]]` # comprehension<br>`my_list = list()`  # constructor<br>`my_list = list(iterable)` # construct list from any iterable |
| Add         | `my_list.append(5)`<br>`my_list.append(list2)` # my_list has list2 as the last item                                                         |
| Remove      | `my_list.remove('value')`  # inplace, no return value<br>`last = my_list.pop()`  # return and inplace remove last item in the list<br>`value = my_list.pop(index)`<br>`del list[index]`   # inplace, no return value |
| Contains    | `if 'value' in my_list:` # **in** operator                                                                                                  |
| Get         | `n = my_list[index]`                                                                                                                        |
| Set         | `my_list[index] = value`                                                                                                                    |
| Size        | `len(my_list)` # **len** is built-in function                                                                                               |
| Insert      | `my_list.insert(index, value)`                                                                                                              |
| Extend      | `my_list.extend(list2)` # add all items in list2, not list2 as an item<br>`my_list += [5, 4, 3]` # extends the list with items in the other list<br># don't confuse **append** with **extend** |
| Remove all  | `my_list.clear()`<br>`my_list = []`<br>`del my_list[:]`                                                                                     |
| indexOf     | `my_list.index('value')`<br>`my_list.index('value', startIndex)`<br>`my_list.index('value', startIndex, endIndex)`                          |
| Sort        | `my_list.sort()` # inplace sorting<br>`my_list = sorted(my_list)` # reassignment                                                           |
| Reverse     | `rev_list = my_list.reverse()`<br>`rev_list = my_list[::-1]`<br>`rev_list = list(reversed(my_list))` # reversed returns an iterator<br>`sorted_rev_list = sorted(my_list, reverse=True)` |
| Copy        | `cloned_list = list.copy()` # recall reference semantics                                                                                   |

## Tuple

| Operation   | API                                                                                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Create      | `t = tuple()`<br>`t = (1, )`  # need the comma to differentiate from an integer<br>`t = (1, 2)`  # constructor<br>`t = tuple(iterable)` # construct tuple from any iterable |
| Add         | `t = t + (3, )` # tuples are immutable!<br>`t += (3, )` # same as above with shorthand operator<br>`t = (*t, 3)` # same as above, but uses **unpacking** |
| Remove      | # cannot remove since tuples are immutable<br>`t = t[1:]` # use slicing to create new tuple                                                 |
| Contains    | `if 'value' in t:` # **in** operator                                                                                                        |
| Get         | `n = t[index]`                                                                                                                              |
| Set         | **NA**  # cannot set since tuples are immutable                                                                                             |
| Size        | `len(t)` # **len** is built-in function                                                                                                     |
| Insert      | # cannot insert since tuples are immutable<br># we can concatenate with the **+** operator<br>`t = t[index] + (3, ) + t[index:]`            |
| Extend      | # **+** operator will concatenate which is extend<br>`t += t2` # concatenate add all items in t2<br>`t += (*t2, )` # same as above but using unpacking |
| Remove all  | `t = tuple()` # construct an empty tuple                                                                                                    |
| indexOf     | `t.index('value')`<br>`t.index('value', startIndex)`<br>`t.index('value', startIndex, endIndex)`                                            |
| Sort        | `t = tuple(sorted(t))` # sorted returns a list, recreate tuple                                                                              |
| Reverse     | `rev_t = t[::-1]` # fastest <br>`rev_t = tuple(reversed(t))` # reversed returns an iterator<br>`sorted_rev_t = tuple(sorted(t, reverse=True))` |
| Copy        | `cloned_t = tuple(t)` # recall reference semantics<br>`cloned_t = (*t, )` # copy via unpacking                                              |

## Set

| Operation   | API                                                                                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Create      | `my_set = set()`  # constructor<br>`my_set = set(iteratable)` # create set from any iterable<br>`my_set = { x**2 for x in range(11) }` # comprehension<br># Note: empty `{}` creates a **dictionary** not a set |
| Add         | `my_set.add(5)`<br>`my_set.update({1, 2, 3})`  # inplace union of the sets                                                                  |
| Remove      | `my_set.remove('value')`  # raise error if not found<br>`my_set.discard('value')`  # no error raised if not found<br>`my_set.pop()` # remove a RANDOM item from the set<br>`my_set.difference_update(set2)`  # inplace removes set2 items<br>`diff_set = my_set - remove_set` # difference operator |
| Contains    | `if value in my_set:` # **in** operator                                                                                                     |
| Size        | `len(my_set)` # **len** is built-in function                                                                                                |
| Remove All  | `my_set.clear()`<br>`my_set = set()`                                                                                                        |
| Union       | `my_set = set1.union(set2)` # union does not change the set<br>`my_set = s1 | s2` # same as above                                           |
| Intersection| `my_set = s1.intersection(s2)`  # does not change the set<br>`my_set = s1 & s2` # same as above                                             |
| Difference  | `my_set = s1.difference(s2)` # difference does not change the set<br>`my_set = s1 - s2` # same as above                                    |
| Copy        | `clone_set = my_set.copy()` # recall reference semantics                                                                                    |
| Get         | **NA** Can only determine if item is **in** set or not                                                                                      |
| Set         | **NA** Cannot set the value of a specific element                                                                                           |
| Insert      | **NA** Just add the object to the set. There is no order of elements.                                                                       |
| indexOf / Sort / Reverse | **NA** There is no order in a set                                                                                              |

## Dictionary

| Operation   | API                                                                                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| Create      | `d = dict()`<br>`d = {}` # empty dictionary<br>`d = {k1:v1}` # initialize a set with 1 key/value pair                                       |
| Add         | `d[key] = value` # adds or sets the value<br>`d.update(dict2)` # inplace addition of all items in dict2<br>`d = { **d1, **d2 }` # creates with all unpacked items of d1 & d2 |
| Remove      | `last = d.popitem()`  # return & remove the last item inserted<br>`item = d.pop(key)` # return value & remove item at key<br>`del d[key]` # remove item at key, returns None |
| Contains    | `if key in d:` # **in** operator. Finds **key** only                                                                                        |
| Get         | `value = d[key]` # raises error if no key<br>`value = d.get(key, def_value)` # avoids error if not found                                    |
| Set         | `d[key] = value` # adds or sets the value<br>`d.setdefault(key, def_value)` # sets only if key not in d. returns d[key]                     | 
| Size        | `len(d)` # **len** is built-in function                                                                                                     |
| Insert      | **NA** # dictionary order cannot change                                                                                                     |
| Extend      | `d.update(dict2)` # inplace addition of all items in dict2                                                                                  |
| Remove All  | `d.clear()`<br>`d = dict()`                                                                                                                 |
| indexOf     | # No easy way. Must iterate through values<br>`key = [k for k, v in d.items() if v == target][0]` # error if not present                    |
| Sort        | # python retains original order of dictionary. recreate dictionary<br>`sorted_d = { key:d[key] for key in sorted(d.keys()) }`               |
| Reverse     | `rev_dict = { k:d[k] for k in reversed(d.keys())}`                                                                                          |
| Copy        | `clone_dict = d.copy()`                                                                                                                     |
| Misc        | `my_dict.keys()`<br>`my_dict.values()`<br>`my_dict.items()`                                                                                 |

## Simple Comprehensions
```python
# list comprehension
my_list = [ n for n in range(100) ]

# set comprehension
my_set = { n for n in range(100) }

# dictionary comprehensions & construction
my_dict = { key: value for key, value in zip(range(10), range(10, 20)) } 
my_dict = dict( zip([k for k in range(10)], [v for v in range(10,20)]))
values = [ 6, 4, 2, 1, 3, 5]
my_dict = { key: values[key] for key in range(len(values)) }
my_dict = { key: value for key, value in enumerate(values) }

# There is NO tuple comprehension
```
