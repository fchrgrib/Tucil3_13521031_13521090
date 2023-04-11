import os


#file reader otomatis membaca txt di folder test di file graph.txt
def file_reader():
    matrix = []
    coordinate = []
    test = ""

    with open(os.path.abspath("../test/graph.txt"), 'r') as f:
        test = f.read()
    split_new_line = test.split("\n")

    for i in range(len(split_new_line)//2):
        coordinate.append([int(split_new_line[i][0]), int(split_new_line[i][2])])

    for i in range(len(split_new_line)//2 ,len(split_new_line)):
        matrix.append(split_new_line[i].split(" "))

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = int(matrix[i][j])

    return coordinate, matrix