from pathlib import Path
import json, csv

class LeadRepository:

    def __init__(self):
        self.DATA_DIR = Path(__file__).resolve().parent / "data"
        self.DATA_DIR.mkdir(exist_ok=True)
        self.DB_PATH = self.DATA_DIR / "leads.json"

    def _load(self):
        if not self.DB_PATH.exists():
            return []

        try:
            return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads):
        self.DB_PATH.write_text(
            json.dumps(leads, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def create_lead(self, lead):
        leads_loaded = self._load()
        leads_loaded.append(lead)
        self._save(leads_loaded)

    def read_leads(self):
        return self._load()

    def export_csv(self):
        path_csv = self.DATA_DIR / "leads.csv"
        leads = self._load()
        try:
            with path_csv.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "company", "email", "stage", "created"])
                writer.writeheader()
                for lead in leads:
                    writer.writerow(lead)
            return path_csv
        except PermissionError:
            return None