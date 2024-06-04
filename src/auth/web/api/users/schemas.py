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
    id: uuid.UUID
    email: str
    first_name: str
    last_name: str
    middle_name: Optional[str]
    roles: List[RoleForUserRetrieveSchema]
    permissions: List[str]

    @classmethod
    def model_validate(
        cls,
        obj: Any,
        *,
        strict: bool | None = None,
        from_attributes: bool | None = None,
        context: dict[str, Any] | None = None,
    ):
        if hasattr(obj, "roles") and obj.roles is not None:
            permissions = [
                permission.name
                for role in obj.roles
                for permission in role.permissions
            ]
            obj.permissions = permissions

        return cls.__pydantic_validator__.validate_python(
            obj, strict=strict, from_attributes=from_attributes, context=context
        )
