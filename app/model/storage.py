from typing import Any
from pydantic import BaseModel


class ReqKVModel(BaseModel):
    key: str
    value: Any

class ResKVModel(BaseModel):
    key: str
    value: Any
