from dataclasses import dataclass


@dataclass(slots=True)
class Post:
    userId: int
    id: int
    title: str
    body: str
