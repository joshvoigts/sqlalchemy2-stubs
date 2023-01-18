from typing import Any
from typing import Optional

from ... import types as sqltypes

class JSONPathType(sqltypes.JSON.JSONPathType):
    def bind_processor(self, dialect: Any): ...
    def literal_processor(self, dialect: Any): ...

class JSON(sqltypes.JSON):
    astext_type: Any = ...
    def __init__(
        self, none_as_null: bool = ..., astext_type: Optional[Any] = ...
    ) -> None: ...
    class Comparator(sqltypes.JSON.Comparator):
        @property
        def astext(self): ...
    comparator_factory: Any = ...

class JSONB(JSON):
    class Comparator(JSON.Comparator):
        def has_key(self, other: Any): ...
        def has_all(self, other: Any): ...
        def has_any(self, other: Any): ...
        def contains(self, other: Any, **kwargs: Any): ...
        def contained_by(self, other: Any): ...
    comparator_factory: Any = ...
