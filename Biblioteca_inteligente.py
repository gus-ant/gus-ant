# Parte 1: Lógica do Programa (Modelos e Biblioteca)
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.situacao = 'Disponível'
        self.devolucao = ''
        self.aluno = ''
        self.matricula = ''

class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.usuarios = {}

    def cadastrar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def cadastrar_usuario(self, usuario):
        self.usuarios[usuario.matricula] = usuario

    def consultar_livro(self, titulo):
        return self.livros.get(titulo, None)

    def consultar_matricula(self, matricula):
        return self.usuarios.get(matricula, None)

    def alterar_status(self, titulo, matricula, situacao, data_devolucao=''):
        livro = self.consultar_livro(titulo)
        if livro and matricula in self.usuarios:
            if situacao == 'Emprestado':
                livro.situacao = 'Emprestado'
                livro.matricula = matricula
                livro.aluno = self.usuarios[matricula].nome
                livro.devolucao = data_devolucao
            elif situacao == 'Devolvido':
                livro.situacao = 'Disponível'
                livro.matricula = ''
                livro.aluno = ''
                livro.devolucao = ''
