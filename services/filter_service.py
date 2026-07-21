from models.demand import Demand


class FilterService:

    @staticmethod
    def pending_demands(
        demands: list[Demand]
    ) -> list[Demand]:
        """
        Retorna apenas as demandas com status Pendente.
        """

        return [
            demand
            for demand in demands
            if str(demand.status).strip().lower() == "pendente"
        ]