def saddle_points(array):
    s_p = set()
    maxs = [max(i) for i in array]
    cols = [column(array, i) for i in len(array[0])]
        y = min([i[array.index(x)] for i in array])
        if x == y:
            s_p.add((array.index(i), array.index(i).index(x) ))
    return s_p
    
def column(matrix, i):
    return [row[i] for row in matrix]
    
#move through row +1 until end, compare to next column (+i)
