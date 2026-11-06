import sqlite3

conexao = sqlite3.connect("chamados.db")
cursor = conexao.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    prioridade TEXT NOT NULL,
    status TEXT NOT NULL,
    usuario TEXT NOT NULL
)''')

conexao.close()

def usuario():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    escolha = input("Digite o nome do usuário que você deseja ver o chamado\n").title()
    cursor.execute("SELECT * FROM chamados WHERE usuario = ?", (escolha,))

    resultados = cursor.fetchall()
    for chamado in resultados:
        print(chamado)
    conexao.close()

def prioridade():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    escolha = input("Qual a prioridade do chamado?\nCrítica, Alta, Média ou Baixa\n").capitalize()
    cursor.execute("SELECT * FROM chamados WHERE prioridade = ?", (escolha,))
    resultados = cursor.fetchall()
    for chamado in resultados:
        print(chamado)
    conexao.close()

def urgencia():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM chamados WHERE prioridade = ? AND status = ?", ("Crítica", "Aberto"))
    resultados = cursor.fetchall()
    for chamado in resultados:
        print(chamado)
    conexao.close()

def status():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    escolha = input("Qual o status do chamado?\nAberto, Em progresso ou Fechado\n").capitalize()
    cursor.execute("SELECT * FROM chamados WHERE status = ?", (escolha,))
    resultados = cursor.fetchall()
    for chamado in resultados:
            print(chamado)
    conexao.close()

def criar():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT MAX(id) FROM chamados")
    maior_id = cursor.fetchone()[0]
    novo_id = maior_id + 1 if maior_id is not None else 1

    titulo_tarefa_nova = input("Digite o título da tarefa nova\n").capitalize()
    prioridade_tarefa_nova = input("Digite a prioridade da tarefa nova\n").capitalize()
    status_tarefa_nova = input("Digite o status da tarefa nova\n").capitalize()
    usuario_tarefa_nova = input("Digite o nome do usuário que está com problemas\n").capitalize()

    cursor.execute("INSERT INTO chamados (id, titulo, prioridade, status, usuario) VALUES (?, ?, ?, ?, ?)",
                   (novo_id, titulo_tarefa_nova, prioridade_tarefa_nova, status_tarefa_nova, usuario_tarefa_nova))
    conexao.commit()
    conexao.close()
    print("Chamado criado com sucesso!")

def progresso():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()
    progresso = input("Digite o título do chamado que você deseja fechar\n").capitalize()
    cursor.execute("UPDATE chamados SET status = ? WHERE titulo = ?", ("Em progresso", progresso))
    conexao.commit()
    conexao.close()

def fechar():
    conexao = sqlite3.connect("chamados.db")
    cursor = conexao.cursor()
    fechar = input("Digite o título do chamado que você deseja fechar\n").capitalize()
    cursor.execute("UPDATE chamados SET status = ? WHERE titulo = ?", ("Fechado", fechar))
    conexao.commit()
    conexao.close()

while True:
    print(f"{'-'*20}------------------")
    print(f"{' '*15}SISTEMA")
    print(f"{'-'*20}------------------")
    print("1. Pesquisa por usuário")
    print("2. Pesquisa por prioridade")
    print("3. Pesquisa por status")
    print("4. Chamados urgentes")
    print("5. Abrir chamado")
    print("6. Resolver chamado")
    print("7. Fechar chamado")
    print("0. Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        usuario()
    elif opcao == "2":
        prioridade()
    elif opcao == "3":
        status()
    elif opcao == "4":
        urgencia()
    elif opcao == "5":
        criar()
    elif opcao == "6":
        progresso()
    elif opcao == "7":
        fechar()
    elif opcao == "0":
        print("Saindo do sistema. . .")
        break
    else:
        print("Opção Inválida. Tente novamente.")

# 1. pesquisa por usuário
# 2. pesquisa por prioridade
# 3. pesquisa por status
# 4. chamados urgentes (chamados em "estado críticos" e "em aberto")
# 5. abrir chamado (criar chamado, "em aberto")
# 6. "resolver" chamado (mudar status para "em progresso")
# 7. fechar chamado (mudar status para "fechado")
# 0. sair do sistema