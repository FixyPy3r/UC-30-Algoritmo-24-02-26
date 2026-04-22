# SISTEMA DE CADASTRO DE ALUNOS
# Projeto: Entrada, Processamento e Saída de Dados

# CONSTANTES (valores fixos que não mudam no programa)

min_idade = 4
max_idade = 19
turmas = ["A", "B"]

# LISTA PRINCIPAL (estrutura que armazena os alunos)
# Cada aluno é um dicionário com: nome, idade e turma

lista_alunos = []

# FUNÇÕES

def validar_nome(nome):
    """
    Valida se o nome do aluno é aceitável.
    Regras: não pode ser vazio e deve ter pelo menos 2 caracteres.
    Retorna True (válido) ou False (inválido).
    """
    # Remove espaços extras das pontas e verifica o tamanho
    if len(nome.strip()) >= 2:
        return True
    else:
        return False


def validar_idade(idadetxt):
    """
    Valida se a idade digitada é um número inteiro
    dentro do intervalo permitido.
    Retorna True (válido) ou False (inválido).
    """
    # Tenta converter o texto para número inteiro
    try:
        idade = int(idadetxt)
        # Verifica se está dentro do intervalo permitido
        if min_idade <= idade <= max_idade:
            return True
        else:
            return False
    except ValueError:
        # Se não conseguiu converter, não é um número
        return False


def validar_turma(turma):
    # Verifica se a turma digitada está na lista de turmas válidas.
    if turma.upper() in turmas:
        return True
    else:
        return False


def validar_dados(nome, idadetxt, turma):
    # Verifica se todos os dados são válidos e retorna True ou False
    nome_ok  = validar_nome(nome)
    idade_ok = validar_idade(idadetxt)
    turma_ok = validar_turma(turma)

    # Todos precisam ser válidos para ser True
    if nome_ok and idade_ok and turma_ok:
        return True
    else:
        return False


def salvar_aluno(nome, idadetxt, turma):
    # Criamos um dicionário a partir dos dados do aluno e colocamos na lista geral
    novo_aluno = {
        "nome":  nome.strip().title(),  # .title() coloca a 1ª letra maiúscula
        "idade": int(idadetxt),
        "turma": turma.upper()
    }
    # Adicionamos à lista
    lista_alunos.append(novo_aluno)


def cadastrar_aluno():
    print("Cadastrar um Novo Aluno")
    print(f" Turmas disponíveis: {', '.join(turmas)}")
    print(f" Idade permitida: {min_idade} a {max_idade} anos")

    # Repetição, fica pedindo dados continuamente
    continuar = True
    while continuar:

        # Dados
        nome     = input("\n Digite o nome do aluno: ")
        idadetxt = input("  Digite a idade do aluno: ")
        turma    = input("Digite a turma do aluno: ")

        # Validação
        dados_validos = validar_dados(nome, idadetxt, turma)

        # Condicional
        if dados_validos:
            salvar_aluno(nome, idadetxt, turma)

            print("\n Aluno cadastrado!")

            resposta = input("\n Deseja cadastrar outro aluno? (S/N): ")

            # Define se vai executar o loop
            if resposta.upper() == "S":
                continuar = True
            else:
                continuar = False

        else:
            # Se os dados forem inválidos, mostra o erro e volta o loop
            print("\n Erro: Dados inválidos! Verifique novamente:")
            print("- Nome deve ter pelo menos 2 caracteres")
            print(f"- Idade deve ser um número entre {min_idade} e {max_idade}")
            print(f"- Turma deve ser uma de: {', '.join(turmas)}")


def listar_alunos():
    print("Lista dos Alunos")

    if len(lista_alunos) == 0:
        print("\n Nenhum aluno cadastrado.")

    else:
        # Imprime os itens da lista, caso haja, e suas respectivas informações
        print(f"\n  Total de alunos cadastrados: {len(lista_alunos)}\n")
        print(f"  {'n':<4} {'Nome':<25} {'Idade':<8} {'Turma':<6}")

        # Usamos enumerate para ter o número de ordem (índice + 1)
        for i, aluno in enumerate(lista_alunos):
            numero = i + 1
            # Imprime os dados de cada aluno
            print(f"  {numero:<4} {aluno['nome']:<25} {aluno['idade']:<8} {aluno['turma']:<6}")


def buscar_aluno():
    print("Buscar Aluno")
    busca = input("\n Digite o nome do aluno a buscar: ").strip().lower()

    # Variável que guarda o aluno se for encontrado
    aluno_encontrado = None

    # Olha cada aluno da lista
    for aluno in lista_alunos:
        # Procura o nome ignorando a formatação
        if aluno["nome"].lower() == busca:
            aluno_encontrado = aluno
            break

    # Se o aluno for encontrado, mostra os dados
    if aluno_encontrado is not None:
        print("\n Aluno encontrado!\n")
        print(f"  Nome : {aluno_encontrado['nome']}")
        print(f"  Idade: {aluno_encontrado['idade']} anos")
        print(f"  Turma: {aluno_encontrado['turma']}")
    else:
        print(f"\n Erro: Aluno '{busca}' não encontrado na lista.")


def mostrar_menu():
    # Menu
    print("Sistema de Cadastro dos Alunos")
    print("  1 - Cadastrar aluno")
    print("  2 - Listar alunos")
    print("  3 - Buscar aluno")
    print("  4 - Sair")

    opcao = input("  Escolha uma opção: ")
    return opcao


def main():
    print("\n  Bem-vindo ao Sistema de Cadastro de Alunos!")

    while True:

        # Mostra o menu e captura a opção
        opcao = mostrar_menu()

        if opcao == "1":
            cadastrar_aluno()

        elif opcao == "2":
            listar_alunos()

        elif opcao == "3":
            buscar_aluno()

        elif opcao == "4":
            print("\n Encerrando o sistema...")
            print("Tchau!\n")
            break
        else:
            print("\n Digite um número de 1 a 4!")

if __name__ == "__main__":
    main()

