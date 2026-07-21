import re
from datetime import datetime


class StatusService:

    @staticmethod
    def _split_history(historico_status: str) -> list[str]:
        """
        Quebra o histórico em linhas válidas.
        """

        if not historico_status:
            return []

        return [
            linha.strip()
            for linha in str(historico_status).splitlines()
            if linha.strip()
        ]

    @staticmethod
    def recent_statuses(
        historico_status: str,
        limit: int = 3
    ) -> list[str]:
        """
        Retorna os últimos registros do histórico
        (mais recente primeiro).
        """

        statuses = StatusService._split_history(historico_status)

        return statuses[-limit:][::-1]

    @staticmethod
    def last_update_date(
        historico_status: str
    ) -> datetime | None:
        """
        Procura a data mais recente existente no histórico.
        Funciona mesmo se o histórico estiver fora de ordem.
        """

        statuses = StatusService._split_history(historico_status)

        datas = []

        ano_atual = datetime.now().year

        for linha in statuses:

            match = re.search(r"(\d{2})/(\d{2})", linha)

            if not match:
                continue

            dia = int(match.group(1))
            mes = int(match.group(2))

            try:

                data = datetime(ano_atual, mes, dia)

                # Nunca aceitar datas futuras
                if data > datetime.now():
                    data = datetime(ano_atual - 1, mes, dia)

                datas.append(data)

            except ValueError:
                continue

        if not datas:
            return None

        return max(datas)

    @staticmethod
    def days_without_update(
        historico_status: str
    ) -> int:

        data = StatusService.last_update_date(
            historico_status
        )

        if data is None:
            return 999

        return (datetime.now() - data).days

    @staticmethod
    def is_stale(
        historico_status: str,
        max_days: int = 7
    ) -> bool:

        return (
            StatusService.days_without_update(
                historico_status
            ) >= max_days
        )

    @staticmethod
    def repeated_status(
        historico_status: str
    ) -> bool:

        recentes = StatusService.recent_statuses(
            historico_status,
            limit=3
        )

        texto = " ".join(recentes).lower()

        palavras = (
            "mesmo status",
            "sem alteração",
            "sem alteracao",
            "aguardando retorno",
            "aguardando resposta",
        )

        return any(
            palavra in texto
            for palavra in palavras
        )

    @staticmethod
    def indicator(
        historico_status: str
    ) -> tuple[str, str]:

        dias = StatusService.days_without_update(
            historico_status
        )

        if dias >= 15:
            return (
                "🔴",
                f"Sem atualização há {dias} dias"
            )

        if StatusService.repeated_status(
            historico_status
        ):
            return (
                "🟡",
                f"Atualizado há {dias} dias"
            )

        return (
            "🟢",
            f"Atualizado há {dias} dias"
        )