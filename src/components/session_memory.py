from src.models import SessionEntry, SessionEntryRole
from typing import List
from src import settings


class SessionMemory:
    def __init__(self):
        self.session_history: List[SessionEntry] = []

    def add_entry(self, role: SessionEntryRole, content: str) -> None:
        self.session_history.append(SessionEntry(role=role, content=content))
        self._apply_max_threshold()

    def format_to_string(self) -> str:
        session_history_list = [
            f"{entry.role.value}: {entry.content}" for entry in self.session_history
        ]
        return "\n" + "\n".join(session_history_list) + "\n"

    def _apply_max_threshold(self):
        while self._estimate_tokens() > settings.HISTORY_TOKEN_LIMIT:
            self.session_history.pop(0)
            self.session_history.pop(0)

    def _estimate_tokens(self):
        total_chars = sum(len(e.content) for e in self.session_history)
        return total_chars // settings.CHARS_PER_TOKEN_RATIO


session_memory = SessionMemory()
