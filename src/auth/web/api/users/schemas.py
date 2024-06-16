from __future__ import annotations

import uuid
from typing import Optional, List, Any

from pydantic import BaseModel


class RoleForUserRetrieveSchema(BaseModel):
    name: str
    alias: str


class PermissionsListForUserRetrieveSchema(BaseModel):
    name: str


class RetrieveUserByIDSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    middle_name: Optional[str]
