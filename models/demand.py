from dataclasses import dataclass

from config import EXCEL_COLUMNS


@dataclass
class Demand:

    operadora: str
    grupo_demanda: str
    projeto: str

    status: str
    empresa_responsavel: str
    ultimo_status: str

    ponto_focal: str
    historico_status: str

    imovel: str
    endereco: str
    cidade: str
    uf: str

    id: str

    monitoramento_cpfl: str
    ip_fg40f: str

    servico: str
    banda: str

    prazo: str

    termo_aceite: str

    projeto_cpfl: str
    planta_cpfl: str

    chamado_faturamento: str

    @staticmethod
    def _value(row: dict, field: str):
        """
        Retorna o valor da coluna correspondente ao campo.
        Caso a coluna não exista, retorna string vazia.
        """
        return row.get(EXCEL_COLUMNS[field], "")

    @classmethod
    def from_excel_row(cls, row: dict) -> "Demand":

        return cls(
            operadora=cls._value(row, "operadora"),
            grupo_demanda=cls._value(row, "grupo_demanda"),
            projeto=cls._value(row, "projeto"),

            status=cls._value(row, "status"),
            empresa_responsavel=cls._value(row, "empresa_responsavel"),
            ultimo_status=cls._value(row, "ultimo_status"),

            ponto_focal=cls._value(row, "ponto_focal"),
            historico_status=cls._value(row, "historico_status"),

            imovel=cls._value(row, "imovel"),
            endereco=cls._value(row, "endereco"),
            cidade=cls._value(row, "cidade"),
            uf=cls._value(row, "uf"),

            id=cls._value(row, "id"),

            monitoramento_cpfl=cls._value(row, "monitoramento_cpfl"),
            ip_fg40f=cls._value(row, "ip_fg40f"),

            servico=cls._value(row, "servico"),
            banda=cls._value(row, "banda"),

            prazo=cls._value(row, "prazo"),

            termo_aceite=cls._value(row, "termo_aceite"),

            projeto_cpfl=cls._value(row, "projeto_cpfl"),
            planta_cpfl=cls._value(row, "planta_cpfl"),

            chamado_faturamento=cls._value(row, "chamado_faturamento"),
        )