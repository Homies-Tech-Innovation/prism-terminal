from src.models import SessionEntry, SessionEntryRole
from typing import List
from src import MAX_TOKENS


class SessionMemory:
    def __init__(self):
        self.session_history: List[SessionEntry] = []

    def add_entry(self, role: SessionEntryRole, content: str) -> bool:
        self.session_history.append(SessionEntry(role=role, content=content))
        self._apply_max_threshold()
        return True

    def format_to_string(self) -> str:
        session_history_list = [
            f"{entry.role.value}: {entry.content}" for entry in self.session_history
        ]
        return "\n" + "\n".join(session_history_list) + "\n"

    def _apply_max_threshold(self):
        while self._estimate_tokens() > MAX_TOKENS:
            self.session_history.pop(0)
            self.session_history.pop(0)

    def _estimate_tokens(self):
        total_chars = sum(len(e.content) for e in self.session_history)
        return total_chars // 4


session_memory = SessionMemory()

# Usage Example:
# session_memory.add_entry(SessionEntryRole.USER, "Content") -> True
# session_memory.format_to_string() -> str
