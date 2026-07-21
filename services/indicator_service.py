from services.status_service import StatusService


class IndicatorService:

    @staticmethod
    def get_indicator(demand) -> tuple[str, str]:
        """
        Retorna o indicador visual baseado apenas
        no tempo desde a última atualização.

        🟢 0 a 2 dias
        🟡 3 a 7 dias
        🔴 acima de 7 dias
        """

        dias = StatusService.days_without_update(
            demand.historico_status
        )

        if dias <= 2:

            return (
                "🟢",
                f"Atualizado há {dias} dia"
                if dias == 1
                else f"Atualizado há {dias} dias"
            )

        elif dias <= 5:

            return (
                "🟡",
                f"Atualizado há {dias} dias"
            )

        else:

            return (
                "🔴",
                f"Sem atualização há {dias} dias"
            )