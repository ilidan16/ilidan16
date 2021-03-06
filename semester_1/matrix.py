class MatrixError(ValueError):
    pass

def create_null_matrix(m,n):
    return Matrix([[0]*n for _ in range(m)])
#==============================================================
class Matrix():
    ''' Класс матриц размером m x n'''
    def __init__(self, body=0):
        if body == 0:
            raise MatrixError('Вы не определили матрицу')
        self.body = body
        self.m = len(body)
        self.n = len(body[0])

    def __str__(self):
        string = ''
        for i in range(self.m): 
            for j in range(self.n):
                string += f'{self.body[i][j]} '
            string += '\n'
        return string

    def __add__(self, other):
        if self.m != other.m or self.n != other.n:
            raise MatrixError('Матрицы имеют разный размер')
        matrix1 = self.body.copy()
        other_matrix = other.body.copy()
        null_matrix = create_null_matrix(self.m,self.n)
        for i in range(self.m):
            for j in range(self.n):
                null_matrix.body[i][j] = matrix1[i][j] + other_matrix[i][j]
        return null_matrix
    
    def __mul__(left_matrix, right_matrix):
        if left_matrix.n != right_matrix.m:
            raise MatrixError('Произведение для таких матриц не определено')
        left_matrix_copy = left_matrix.body.copy()
        right_matrix_copy = right_matrix.body.copy()
        result = create_null_matrix(left_matrix.m, right_matrix.n).body
        for i in range(left_matrix.m):
            for j in range(right_matrix.n):
                column = []
                for q in range(right_matrix.m):
                    column.append(right_matrix_copy[q][j])
                for k, p in zip(left_matrix_copy[i], column):
                    result[i][j] += k*p     
        return Matrix(result)

    def transpose(self):
        '''Транспонирование матрицы'''
        copy = self.body.copy()
        result = create_null_matrix(self.m,self.n).body
        for i in range(self.m):
            for j in range(self.n):
                result[i][j] = copy[j][i]
        return Matrix(result)
#==============================================================
"""
A = Matrix([
    [5,3,6],
    [4,2,1],
    [2,5,2]
    ])

E = Matrix([
    [1,0,0],
    [0,1,0],
    [0,0,1]
    ])

C = Matrix([
    [0,1,2],
    [0,0,3],
    [0,0,0]
    ])

B = Matrix([
    [1,2,1],
    [3,1,5],
    [3,4,1]
    ])
"""
