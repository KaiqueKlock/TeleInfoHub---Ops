import streamlit as st

from services.excel_service import ExcelService
from services.filter_service import FilterService
from services.agenda_service import AgendaService
from services.status_service import StatusService
from services.indicator_service import IndicatorService

st.set_page_config(
    page_title="Operations Hub",
    page_icon="📡",
    layout="wide"
)


st.title("📡 Operations Hub")


excel_service = ExcelService("data/FollowUp.xlsx")

demands = excel_service.load_demands()

pending_demands = FilterService.pending_demands(demands)

agendas = AgendaService.extract_agenda(demands)


# ==========================================================
# AGENDA OPERACIONAL
# ==========================================================




st.subheader("📅 Agenda Operacional")


if not agendas:

    st.info("Nenhuma agenda futura identificada.")

else:

    agenda_columns = st.columns(2)

    for index, agenda in enumerate(agendas):

        demand = agenda.demand

        column = agenda_columns[index % 2]

        with column:

            with st.container(border=True):

                if agenda.agenda_time:

                    agenda_date = (
                        agenda.agenda_date.strftime(
                            "%d/%m/%Y"
                        )
                    )

                    agenda_time = (
                        agenda.agenda_time.strftime(
                            "%H:%M"
                        )
                    )

                    st.markdown(
                        f"### 📅 {agenda_date} "
                        f"às {agenda_time}"
                    )

                else:

                    st.markdown(
                        f"### 📅 "
                        f"{agenda.agenda_date.strftime('%d/%m/%Y')}"
                    )

                st.write(
                    f"📍 **{demand.cidade}**"
                )

                st.write(
                    f"🏢 **{demand.endereco}**"
                )

                st.divider()

                st.write(
                    f"🏢 **Operadora:** "
                    f"{demand.operadora}"
                )

                if demand.monitoramento_cpfl:

                    st.write(
                        f"🔑 **Designação:** "
                        f"{demand.monitoramento_cpfl}"
                    )

                else:

                    st.write(
                        f"🔑 **ID:** "
                        f"{demand.id}"
                    )

                st.write(
                    f"🌐 **Serviço:** "
                    f"{demand.servico}"
                )

                st.write(
                    f"📶 **Banda:** "
                    f"{demand.banda}"
                )

                st.divider()

                st.write(
                    f"📝 **{agenda.description}**"
                )

# ==========================================================
# PENDÊNCIAS
# ==========================================================

st.divider()

st.subheader("🔴 Pendências Operacionais")

st.write(
    f"{len(pending_demands)} pendências encontradas."
)


if not pending_demands:

    st.success("Nenhuma pendência encontrada.")

else:

    operators = sorted(
        {
            demand.operadora
            for demand in pending_demands
        }
    )

    for operator in operators:

        operator_demands = [
            demand
            for demand in pending_demands
            if demand.operadora == operator
        ]

        st.divider()

        st.header(
            f"🔴 {operator} — "
            f"{len(operator_demands)} pendências"
        )

        columns = st.columns(3)

        for index, demand in enumerate(
            operator_demands
        ):

            column = columns[index % 3]

            with column:

                with st.container(border=True):
                    icone, descricao = IndicatorService.get_indicator(demand)
                    icone, descricao = IndicatorService.get_indicator(demand)

                    
                    st.subheader(
                        f"{icone} {demand.cidade}"
                    )
                    st.write(descricao)
                    
                    if demand.monitoramento_cpfl:

                        st.write(
                            f"**Designação:** "
                            f"{demand.monitoramento_cpfl}"
                        )

                    else:

                        st.write(
                            f"**ID:** {demand.id}"
                        )

                    st.write(
                        f"**Endereço:** "
                        f"{demand.endereco}"
                    )

                    recent_statuses = StatusService.recent_statuses(
                        demand.historico_status, limit=5
                    )

                    st.markdown("### 📝 Últimas atualizações")

                    if recent_statuses:

                        for status in recent_statuses:

                            st.write(
                                f"• {status}"
                            )

                    else:

                        st.info(
                            "Nenhum histórico de status disponível."
                        )

                    st.info(
                        demand.ultimo_status
                    )

                    st.write(
                        f"**Responsabilidade atual:** "
                        f"{demand.empresa_responsavel}"
                    )