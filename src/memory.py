"""
memory.py
-----------
Conversation Memory
"""

from collections import defaultdict
from threading import Lock


class ConversationMemory:
    def __init__(self, max_messages=10):
        self.sessions = defaultdict(list)
        self.max_messages = max_messages
        self.lock = Lock()

    def add_message(self, session_id, role, content):
        with self.lock:
            self.sessions[session_id].append({
                "role": role,
                "content": content
            })

            self.sessions[session_id] = (
                self.sessions[session_id][-self.max_messages:]
            )

    def get_history(self, session_id):
        with self.lock:
            return list(self.sessions.get(session_id, []))

    def clear(self, session_id):
        with self.lock:
            self.sessions.pop(session_id, None)


conversation_memory = ConversationMemory()