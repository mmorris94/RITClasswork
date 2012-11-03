


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
    if isinstance(aMap, EmptyMap):
        aMap = mkNonEmptyMap(mkEmptyMap(),key,val,mkEmptyMap())
    elif aMap.key == key:
        aMap.val = val
    elif aMap.key < key:
        aMap = mapInsert(key, val, aMap.left)
    elif aMap.key > key:
        aMap = mapInsert(key, val, aMap.right)
    elif isinstance(aMap, EmptyMap):
        aMap = mkNonEmptyMap(mkEmptyMap(),key,val,mkEmptyMap())

    return aMap

def main():
	aMap = mkNonEmptyMap(mkNonEmptyMap(mkEmptyMap(),'eight',8,mkEmptyMap()),'five',5,mkNonEmptyMap(mkEmptyMap(),'four',4,mkEmptyMap()))
	print(aMap.val)
	if isinstance(aMap.left, EmptyMap) is False:
		print(aMap.left.val)
	if isinstance(aMap.right,EmptyMap) is False:
		print(aMap.right.val)

main()


