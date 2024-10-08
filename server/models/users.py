from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    email: str
    password: str
    is_admin: bool
    created_at: str
    updated_at: str
