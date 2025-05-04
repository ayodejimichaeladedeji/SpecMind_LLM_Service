from pydantic import BaseModel
from typing import Any, Optional

class APIResponse(BaseModel):
    isSuccess: bool
    body: Optional[Any] = None
    message: Optional[str] = None
    errorMessage: Optional[str] = None