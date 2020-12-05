class MatrixError(ValueError):
    pass

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





A = Matrix([
    [2,3,5],
    [2,7,9],
    [4,7,3]
    ])
        
