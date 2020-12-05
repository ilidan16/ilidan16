class MatrixError(ValueError):
    pass

def create_null_matrix(m,n):
    '''Создаёт нулевую матрицу размером m x n'''
    strings = []
    null_matrix = []
    for j in range(n):
        strings.append(0)
    for i in range(m):
        null_matrix.append(strings)
    return Matrix(null_matrix)

class Matrix():
    ''' Класс матриц размером m x n'''
    def __init__(self, matrix=0):
        self.matrix = matrix
        if self.matrix == 0:
            raise MatrixError('Матрица не определена')
        self.m = len(self.matrix)
        self.n = len(self.matrix[0])

    def __str__(self):
        string = ''
        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[i])):
                string += f'{self.matrix[i][j]} '
            string += '\n'
        return string

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise MatrixError('Матрицы имеют разный размер')
        matrix1 = self.matrix.copy()
        matrix_other = other.matrix.copy()
        print(matrix1)
        m = self.m
        n = self.n
        null_matrix = create_null_matrix(m,n)
        for i in range(m):
            for j in range(n):
                null_matrix.matrix[i][j] = matrix1[i][j] + matrix_other[i][j]
        return null_matrix


    def __mul__(left_matrix, right_matrix):
        if left_matrix.n != right_matrix.m:
            raise MatrixError('Произведение для таких матриц не определено')
        left_matrix_copy = left_matrix.matrix.copy()
        right_matrix_copy = right_matrix.matrix.copy()
        result = create_null_matrix(left_matrix.m, right_matrix.n).matrix
        for i in range(left_matrix.m):
            for j in range(right_matrix.n):
                column = []
                for q in range(right_matrix.m):
                    column.append(right_matrix_copy[q][j])
                array = []
                for k, p in zip(left_matrix_copy[i], column):
                    result[i][j] += k*p
                   
        return Matrix(result)
                
                
                
        
        



A = Matrix([
    [1,0,0],
    [0,1,0],
    [0,0,1]
    ])

B = Matrix([
    [2,3,5],
    [2,6,4],
    [8,9,7]
    ])
C = Matrix([
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ])

D = Matrix([
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ])



