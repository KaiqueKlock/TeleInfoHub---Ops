import re
from dataclasses import dataclass
from datetime import date, datetime, time


@dataclass
class AgendaItem:
    demand: object
    agenda_date: date
    agenda_time: time | None
    description: str


class AgendaService:

    KEYWORDS = (
    "agenda",
    "agendado",
    "vistoria",
    "visita",
    "ativação",
    "ativacao",
    "janela",
    "instalação",
    "instalacao",
    "confirmada",
    "confirmado",
    )

    DATE_PATTERN = re.compile(
        r"\b(\d{1,2})/(\d{1,2})(?:/(\d{4}))?\b"
    )

    TIME_PATTERN = re.compile(
        r"\b(\d{1,2})(?::(\d{2}))?\s*(?:h|horas?)?\b",
        re.IGNORECASE
    )

    @classmethod
    def extract_agenda(
        cls,
        demands: list
    ) -> list[AgendaItem]:

        agendas = []

        today = date.today()

        for demand in demands:

            status = demand.ultimo_status

            if not status:
                continue

            status_text = str(status).strip()

            if not cls._contains_keyword(status_text):
                continue

            date_match = cls.DATE_PATTERN.search(status_text)

            if not date_match:
                continue

            day = int(date_match.group(1))
            month = int(date_match.group(2))
            year = date_match.group(3)

            if year:
                agenda_year = int(year)

            else:
                agenda_year = today.year

            try:

                agenda_date = date(
                    agenda_year,
                    month,
                    day
                )

            except ValueError:

                continue

            if agenda_date < today:

                continue

            agenda_time = cls._extract_time(status_text)

            agendas.append(
                AgendaItem(
                    demand=demand,
                    agenda_date=agenda_date,
                    agenda_time=agenda_time,
                    description=status_text,
                )
            )

        return sorted(
            agendas,
            key=lambda agenda: (
                agenda.agenda_date,
                agenda.agenda_time or time.min,
            )
        )

    @classmethod
    def _contains_keyword(cls, text: str) -> bool:

        normalized_text = text.lower()

        return any(
            keyword in normalized_text
            for keyword in cls.KEYWORDS
        )

    @classmethod
    def _extract_time(
        cls,
        text: str
    ) -> time | None:

        matches = cls.TIME_PATTERN.findall(text)

        if not matches:
            return None

        hour_text, minute_text = matches[-1]

        hour = int(hour_text)

        minute = (
            int(minute_text)
            if minute_text
            else 0
        )

        if hour > 23 or minute > 59:

            return None

        return time(hour, minute)