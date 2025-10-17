from stages import lead_model
import repo

def main():
    while True:
        print_menu()
        op = input("Escolha: ")
        if op == "1":
            add_lead()
        elif op == "2":
            list_leads()
        elif op == "2":
            print("Ate logo")
            break
        else:
            print("opção invalida")
            break


def add_lead():
    name = input("Nome: ")
    company = input("empresa: ")
    email = input("e-mail: ")
    repo.create_lead(lead_model(name,company, email))
    print(lead_model(name, company, email))
    print("Lead adicionado")

def list_leads():
    print("listar Lead")

def print_menu():
    print("\n Mini CRM de Leads - (Adicionar/Listar)")
    print("[1]Adicionar Lead")
    print(" [2]Listar leads")
    print("[0]Sair")

if __name__ == "__main__":
    main()