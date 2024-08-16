# Parte 2: Interface Gráfica (Tkinter)

import tkinter as tk
from tkinter import ttk, messagebox
from parte1 import Biblioteca, Livro, Usuario  # Certifique-se de que o arquivo "parte1.py" está no mesmo diretório


class BibliotecaApp(tk.Tk):
    def __init__(self, biblioteca):
        super().__init__()
        self.title("Biblioteca")
        self.geometry("400x500")
        self.biblioteca = biblioteca
        self.create_widgets()

    def create_widgets(self):
        # Cadastro de Livro
        frame_livro = ttk.LabelFrame(self, text="Cadastrar Livro")
        frame_livro.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_livro, text="Nome do Livro:").grid(row=0, column=0)
        self.entry_livro = ttk.Entry(frame_livro)
        self.entry_livro.grid(row=0, column=1)

        ttk.Button(frame_livro, text="Cadastrar", command=self.cadastrar_livro).grid(row=1, column=0, columnspan=2)

        # Cadastro de Usuário
        frame_usuario = ttk.LabelFrame(self, text="Cadastrar Usuário")
        frame_usuario.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_usuario, text="Nome:").grid(row=0, column=0)
        self.entry_nome = ttk.Entry(frame_usuario)
        self.entry_nome.grid(row=0, column=1)

        ttk.Label(frame_usuario, text="Matrícula:").grid(row=1, column=0)
        self.entry_matricula = ttk.Entry(frame_usuario)
        self.entry_matricula.grid(row=1, column=1)

        ttk.Button(frame_usuario, text="Cadastrar", command=self.cadastrar_usuario).grid(row=2, column=0, columnspan=2)

        # Alteração de Status do Livro
        frame_status = ttk.LabelFrame(self, text="Alterar Status do Livro")
        frame_status.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_status, text="Matrícula do Aluno:").grid(row=0, column=0)
        self.entry_matricula_status = ttk.Entry(frame_status)
        self.entry_matricula_status.grid(row=0, column=1)

        ttk.Label(frame_status, text="Nome do Livro:").grid(row=1, column=0)
        self.entry_livro_status = ttk.Entry(frame_status)
        self.entry_livro_status.grid(row=1, column=1)

        ttk.Label(frame_status, text="Situação:").grid(row=2, column=0)
        self.combo_situacao = ttk.Combobox(frame_status, values=["Emprestado", "Devolvido"])
        self.combo_situacao.grid(row=2, column=1)

        ttk.Label(frame_status, text="Data de Devolução:").grid(row=3, column=0)
        self.entry_devolucao = ttk.Entry(frame_status)
        self.entry_devolucao.grid(row=3, column=1)

        ttk.Button(frame_status, text="Alterar", command=self.alterar_status).grid(row=4, column=0, columnspan=2)

        # Consulta de Livro
        frame_consulta = ttk.LabelFrame(self, text="Consultar Livro")
        frame_consulta.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_consulta, text="Nome do Livro:").grid(row=0, column=0)
        self.entry_consulta = ttk.Entry(frame_consulta)
        self.entry_consulta.grid(row=0, column=1)

        ttk.Button(frame_consulta, text="Consultar", command=self.consultar_livro).grid(row=1, column=0, columnspan=2)

        # Ver Livros Cadastrados
        ttk.Button(self, text="Ver Livros Cadastrados", command=self.ver_livros_cadastrados).pack(pady=10)

    def cadastrar_livro(self):
        nome_livro = self.entry_livro.get()
        if nome_livro:
            self.biblioteca.cadastrar_livro(Livro(nome_livro))
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            self.entry_livro.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "O nome do livro não pode estar vazio!")

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        if nome and matricula.isdigit():
            matricula = int(matricula)
            if self.biblioteca.consultar_matricula(matricula) is None:
                self.biblioteca.cadastrar_usuario(Usuario(nome, matricula))
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                self.entry_nome.delete(0, tk.END)
                self.entry_matricula.delete(0, tk.END)
            else:
                messagebox.showwarning("Erro", "Já existe um usuário com essa matrícula!")
        else:
            messagebox.showwarning("Erro", "Nome ou matrícula inválidos!")

    def alterar_status(self):
        matricula = self.entry_matricula_status.get()
        livro = self.entry_livro_status.get()
        status = self.combo_situacao.get()
        data_devolucao = self.entry_devolucao.get()

        if matricula.isdigit() and livro:
            matricula = int(matricula)
            self.biblioteca.alterar_status(livro, matricula, status, data_devolucao)
            messagebox.showinfo("Sucesso", "Status do livro alterado com sucesso!")
        else:
            messagebox.showwarning("Erro", "Dados inválidos!")

    def consultar_livro(self):
        livro = self.entry_consulta.get()
        livro_obj = self.biblioteca.consultar_livro(livro)
        if livro_obj:
            messagebox.showinfo("Consulta de Livro",
                                f"Livro: {livro}\nAluno: {livro_obj.aluno}\nMatrícula: {livro_obj.matricula}\nSituação: {livro_obj.situacao}\nDevolução: {livro_obj.devolucao}")
        else:
            messagebox.showwarning("Erro", "Livro não encontrado!")

    def ver_livros_cadastrados(self):
        livros = "\n".join([livro for livro in self.biblioteca.livros])
        if livros:
            messagebox.showinfo("Livros Cadastrados", livros)
        else:
            messagebox.showinfo("Livros Cadastrados", "Nenhum livro cadastrado.")


if __name__ == "__main__":
    biblioteca = Biblioteca()
    app = BibliotecaApp(biblioteca)
    app.mainloop()
