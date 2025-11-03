from models import Lead
from stages import DEFAULT_STAGE
from repo import LeadRepository

lead_backend = LeadRepository()

def add_lead():
    name = input("Nome: ")
    company = input("empresa: ")
    email = input("e-mail: ")

    lead = Lead(name, company, email, DEFAULT_STAGE)
    modeled_lead = lead.lead_model()

    lead_backend.create_lead(modeled_lead)
    print("Lead adicionado")


def list_leads():
    leads = lead_backend.read_leads()
    if not leads:
        print("Nenhum dado cadastrado")
        return

    print(f"\n ## | {'Nome':<20}| {'Empresa':<20}| {'E-mail':<20}")
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead['name']:<20}| {lead['company']:<20}| {lead['email']:<20}")

def search_lead():
    user_search = input("Buscar por: ").strip().lower()
    if not user_search:
        print("consulta vazia, tente novamente")
        search_lead()

    leads = lead_backend.read_leads()
    results = []
    for lead in leads:
        lead_str = f"{lead['name']}{lead['company']}{lead['email']}".lower()
        if user_search in lead_str:
            results.append(lead)

    if not results:
        print("nenhum resultado encontrado")
        return

    print(f"\n ## | {'Nome':<20}| {'Empresa':<20}| {'E-mail':<20}")
    for i, lead in enumerate(results):
        print(f"{i:02d} | {lead['name']:<20}| {lead['company']:<20}| {lead['email']:<20}")


def export_leads():
    path_csv = lead_backend.export_csv()
    if path_csv is None:
        print("Erro ao exportar o CSV.. tente fechar o arquivo")
    else:
        print(f"CSV exportado para {path_csv}")

def print_menu():
    print("\n Mini CRM de Leads - (Adicionar/Listar)")
    print("[1] Adicionar Lead")
    print("[2] Listar leads")
    print("[3] Buscar leads por (nome/empresa/email)")
    print("[4] Salvar leads como csv")
    print("[0] Sair")


def main():
    while True:
        print_menu()
        op = input("Escolha: ")
        if op == "1":
            add_lead()
        elif op == "2":
            list_leads()
        elif op == "3":
            search_lead()
        elif op == "4":
            export_leads()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("opção invalida")

if __name__ == "__main__":
    main()