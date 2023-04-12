import os


#file reader otomatis membaca txt di folder test di file graph.txt
def file_reader(test):
    split_new_line = test.split("\n")

    matrix = []
    coordinate = []
    index = int(test[0])+1

    for i in range(1, index):
        coordinate.append([float(split_new_line[i][0]), float(split_new_line[i][2])])

    for i in range(index, 2*index-1):
        matrix.append(split_new_line[i].split(" "))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = float(matrix[i][j])

    return coordinate, matrix
