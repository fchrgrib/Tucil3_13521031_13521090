def has_destination(arr, destination):
    return arr[destination] > 0


def minimum_edge(arr, arr_all, distance_start_point, idx_end_point):
    index = []
    arr_cpy = []

    for i in range(len(arr)):
        if arr[i] > 0:
            arr_cpy.append(arr[i] + abs(arr_all[i][idx_end_point]) + distance_start_point)
            index.append(i)

    min = arr_cpy[0]
    idx = 0

    for i in range(len(arr_cpy)):
        if min > arr_cpy[i]:
            min = arr_cpy[i]
            idx = i
    return arr[index[idx]], index[idx]


# masukkan arr sebagai matriks ketetanggaan origin sebagai index awal dan destination sebagai index tujuan
def a_star(arr, origin, destination):
    rute = [origin]

    if has_destination(arr[origin], destination):
        rute.append(destination)
        return rute
    else:
        i = origin
        distance_start_point = 0
        while not has_destination(arr[i], destination):
            min, idx = minimum_edge(arr[i], arr, distance_start_point, destination)

            rute.append(idx)
            i = idx

            distance_start_point += min

    rute.append(destination)
    return rute