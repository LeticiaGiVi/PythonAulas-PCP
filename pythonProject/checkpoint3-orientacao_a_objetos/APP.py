from models import Lead
from stages import DEFAULT_STAGE
from repo import LeadRepository


class CRMApp:
    def __init__(self):
        self.lead_backend = LeadRepository()

    def add_lead(self):
        name = input("Nome: ")
        company = input("empresa: ")
        email = input("e-mail: ")

        lead = Lead(name, company, email, DEFAULT_STAGE)
        modeled_lead = lead.lead_model()

        self.lead_backend.create_lead(modeled_lead)
        print("Lead adicionado")

    def list_leads(self):
        self.lead_backend.list_leads()

    def search_lead(self):
        user_search = input("Buscar por: ").strip().lower()
        if not user_search:
            print("consulta vazia, tente novamente")
            self.search_lead()
            return

        self.lead_backend.search_lead(user_search)

    def export_leads(self):
        path_csv = self.lead_backend.export_csv()
        if path_csv is None:
            print("Erro ao exportar o CSV.. tente fechar o arquivo")
        else:
            print(f"CSV exportado para {path_csv}")

    def print_menu(self):
        print("\n Mini CRM de Leads - (Adicionar/Listar)")
        print("[1] Adicionar Lead")
        print("[2] Listar leads")
        print("[3] Buscar leads por (nome/empresa/email)")
        print("[4] Salvar leads como csv")
        print("[0] Sair")

    def run(self):
        while True:
            self.print_menu()
            op = input("Escolha: ")
            if op == "1":
                self.add_lead()
            elif op == "2":
                self.list_leads()
            elif op == "3":
                self.search_lead()
            elif op == "4":
                self.export_leads()
            elif op == "0":
                print("Saindo...")
                break
            else:
                print("opção invalida")


if __name__ == "__main__":
    app = CRMApp()
    app.run()