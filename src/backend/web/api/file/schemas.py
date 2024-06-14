from pydantic import BaseModel


class UploadDatasetSchemaInput(BaseModel):
    name: str
    path: str
    ext: str
    byte_size: int
