#SISTEMA DE GESTÃO DE BIBLIOTECA

#Dicionário p/ armazenar os livros
catalogo = {}

#Dicionário p/ armazenar os empréstimos ativos
emprestimosAtivos = {}

#lista p/ armazenar o histórico de transição
historico = {}

# Função: Adicionar livro

def adicionarlivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com código {codigo} já existe")
        return False

    catalogo [codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

adicionarlivro("L001", "Codigo Limpo", "Robert Martin", 2)
