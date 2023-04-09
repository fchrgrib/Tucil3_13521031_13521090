from queue import PriorityQueue


# masukkan arr sebagai matriks ketetanggaan origin sebagai index awal dan destination sebagai index tujuan
def csu(arr, origin, destination):
    rute = [origin]

    if arr[origin][destination] > 0:
        rute.append(destination)
        return rute
    else:
        temp_arr = [origin]
        prioqueue = PriorityQueue()
        prioqueue.put((abs(arr[origin][destination]), 0, temp_arr))
        count = 1
        temp = prioqueue.get()

        while arr[temp[2][len(temp[2]) - 1]][destination] != 0:

            for i in range(len(arr[temp[2][len(temp[2]) - 1]])):
                if arr[temp[2][len(temp[2]) - 1]][i] > 0:
                    temp_push = temp[2].copy()
                    temp_push.append(i)

                    prioqueue.put((abs(arr[i][destination]), count, temp_push.copy()))
                    count += 1
                    temp_push.clear()
            if prioqueue.empty():
                break
            temp = prioqueue.get()

        rute = temp[2]
        if prioqueue.empty() and rute[len(rute - 1)] != destination:
            return []
    return rute
