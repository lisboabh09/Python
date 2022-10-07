'''
Uma classe é uma estrutura que abstrai um conjunto de objetos com características similares.
'''


class Livro:

    def __init__(self, titulo, autor, editora, isbn, ano):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.isbn = isbn
        self.ano = ano

    def __str__(self):
        return 'Titulo: %s, Autor: %s, Editora: %s, ISBN: %s, Ano: %s' % \
                (self.titulo, self.autor, self.editora, self.isbn, self.ano)









