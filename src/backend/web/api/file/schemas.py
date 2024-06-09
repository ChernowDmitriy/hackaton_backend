from pydantic import BaseModel


class UploadImageSchemaInput(BaseModel):
    name: str
    path: str
    ext: str
    byte_size: int
