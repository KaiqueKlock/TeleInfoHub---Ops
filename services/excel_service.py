from pathlib import Path

import pandas as pd

from models.demand import Demand


class ExcelService:
    """
    Responsável por ler a planilha de Follow Up.
    """

    def __init__(self, excel_path: str):
        self.excel_path = Path(excel_path)

        if not self.excel_path.exists():
            raise FileNotFoundError(
                f"Arquivo não encontrado: {self.excel_path}"
            )

    def get_dataframe(self) -> pd.DataFrame:


        df = pd.read_excel(
            self.excel_path,
            sheet_name="BASE"
    )

        df.columns = df.columns.str.strip()

        df = df.fillna("")

        return df

    def load_demands(self) -> list[Demand]:
        """
        Converte todas as linhas da planilha em objetos Demand.
        """

        dataframe = self.get_dataframe()

        demands = []

        for row in dataframe.to_dict(orient="records"):
            demands.append(Demand.from_excel_row(row))

        return demands