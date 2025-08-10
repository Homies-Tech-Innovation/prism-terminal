from src import settings
from src.models import ExitCode


class HistoryFilter:
    BLACK_LISTED_CMDS = settings.BLACK_LISTED_CMDS

    def process_interaction(
        self,
        input: str,
        status: ExitCode,
    ) -> bool:
        # Error Preservation
        if status.exit_code != 0:
            return True

        # Command Blacklist Filter
        first_word = input.split(maxsplit=1)[0].lower()
        if first_word in self.BLACK_LISTED_CMDS:
            return False

        # Sensitive Data Protection
        # Skipped for MVP

        return True


history_filter = HistoryFilter()
