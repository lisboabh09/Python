class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


livro1 = Livro('Curso de Python', 'Alcimar Costa')
print(livro1.autor)

livro1.autor = 'José da Silva'
print(livro1.autor)
