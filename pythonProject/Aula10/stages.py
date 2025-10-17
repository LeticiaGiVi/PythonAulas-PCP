from datetime import date

STAGES = ["novo"] # por enquanto so tem o 1 estagio("novo")

def lead_model(name, company, email):
    """modela / estrutura  um lead como um dicionario"""
    return {
        "name": name,
        "company": company,
        "email": email,
        "stage":"novo",
        "created": date.today().isoformat()
    }