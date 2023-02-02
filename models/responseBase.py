from pydantic.generics import GenericModel
from typing import Generic, Optional, TypeVar

T = TypeVar("T")

class ResponseBase(GenericModel,Generic[T]):
    code:str
    status:str
    message:str
    data:Optional[T]