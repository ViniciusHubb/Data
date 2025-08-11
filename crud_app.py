contatos = []

def listar_contatos():
    print("\n--- Contatos ---")
    if not contatos:
        print("(Nenhum contato cadastrado)")
        return
    for i, contato in enumerate(contatos):
        print(f"Índice {i}: {contato['nome']} | {contato['telefone']} | {contato['email']}")

def cadastrar_contato():
    print("\n-- Novo Contato --")
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()
    
    contatos.append({
        "nome": nome,
        "telefone": telefone,
        "email": email
    })
    print("Contato cadastrado com sucesso!")


def atualizar_contato():
    listar_contatos()
    if not contatos:
        return
    
    try:
        indice = int(input("Digite o índice do contato para atualizar: "))
        contato = contatos[indice]
    except (ValueError, IndexError):
        print("Erro: Índice inválido.")
        return

    print("Deixe em branco para manter o valor atual.")
    novo_nome = input(f"Nome [{contato['nome']}]: ").strip()
    novo_telefone = input(f"Telefone [{contato['telefone']}]: ").strip()
    novo_email = input(f"Email [{contato['email']}]: ").strip()

    if novo_nome:
        contato['nome'] = novo_nome
    if novo_telefone:
        contato['telefone'] = novo_telefone
    if novo_email:
        contato['email'] = novo_email
    
    print("Contato atualizado!")


def excluir_contato():
    listar_contatos()
    if not contatos:
        return

    try:
        indice = int(input("Digite o índice do contato para excluir: "))
        contatos.pop(indice)
        print("Contato excluído com sucesso!")
    except (ValueError, IndexError):
        print("Erro: Índice inválido.")


def menu():
    """Função principal que exibe o menu e gerencia o loop do programa."""
    while True:
        print("\n--- Agenda ---")
        print("1. Cadastrar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contato")
        print("4. Excluir Contato")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            cadastrar_contato()
        elif opcao == '2':
            listar_contatos()
        elif opcao == '3':
            atualizar_contato()
        elif opcao == '4':
            excluir_contato()
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()