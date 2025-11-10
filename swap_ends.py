def swap_ends(L, k):
    new_list = L.copy()
    if k <= 0 or k > (len(L) / 2) or len(L) == 0:
        return (new_list, 0)

    else:
        new_list[:k] = L[-(k):]
        new_list[(-k):] = L[:k]

        return (new_list, k)
