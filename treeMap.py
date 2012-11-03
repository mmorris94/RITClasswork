


class EmptyMap():
    __slots__= ()

class NonEmptyMap():
    __slots__ = ('left','key','val','right')

def mkEmptyMap():
    return EmptyMap()

def mkNonEmptyMap(left, key, val, right):
    aMap = NonEmptyMap()
    aMap.left = left
    aMap.key = key
    aMap.val = val
    aMap.right = right
    return aMap

def mapInsert(key, val, aMap):
    while isinstance(aMap, EmptyMap) is False:
        if aMap.key == key:
            aMap.val = val
            break
        elif aMap.key < key:
            aMap = aMap.left
        elif aMap.key > key:
            aMap = aMap.right

    if isinstance(aMap, EmptyMap):
        aMap = mkNonEmptyMap(mkEmptyMap(),key,val,mkEmptyMap())

    return aMap
