import pydantic
import typing

from .session_package import SessionPackage
from .session_signature import SessionSignature


class SessionOutput(pydantic.BaseModel):
    """
    SessionOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    packages: typing.Optional[typing.List[SessionPackage]] = pydantic.Field(
        alias="packages", default=None
    )
    signatures: typing.Optional[typing.List[SessionSignature]] = pydantic.Field(
        alias="signatures", default=None
    )
