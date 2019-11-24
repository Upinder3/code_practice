def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    result = []
    result.append(tuple(pool[i] for i in indices[:r]))
    print(result)
    w_cnt = 0
    while n:
        print("while loop number: {} ==================================================".format(w_cnt))
        for i in reversed(range(r)):
            print("i :",i)
            print("cycles", cycles)
            print("indices", indices)
            cycles[i] -= 1
            print("cycles before if", cycles)
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
                print("cycles in if", cycles)
                print("indices in if", indices)
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print("j ", j)
                print("indices in else", indices)
                result.append(tuple(pool[i] for i in indices[:r]))
                print("result so far", result)
                break
        else:
            break
        w_cnt +=1
    return result

print(permutations([1,2,3]))
