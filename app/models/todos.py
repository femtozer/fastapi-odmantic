import enum
from typing import Optional

from odmantic import Model


class TodoPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


class Todo(Model):
    title: str
    description: Optional[str]
    priority: TodoPriority
