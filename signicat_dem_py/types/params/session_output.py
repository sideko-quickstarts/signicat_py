import pydantic
import typing
import typing_extensions

from .session_package import SessionPackage, _SerializerSessionPackage
from .session_signature import SessionSignature, _SerializerSessionSignature


class SessionOutput(typing_extensions.TypedDict):
    """
    SessionOutput
    """

    packages: typing_extensions.NotRequired[
        typing.Optional[typing.List[SessionPackage]]
    ]

    signatures: typing_extensions.NotRequired[
        typing.Optional[typing.List[SessionSignature]]
    ]


class _SerializerSessionOutput(pydantic.BaseModel):
    """
    Serializer for SessionOutput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    packages: typing.Optional[typing.List[_SerializerSessionPackage]] = pydantic.Field(
        alias="packages", default=None
    )
    signatures: typing.Optional[typing.List[_SerializerSessionSignature]] = (
        pydantic.Field(alias="signatures", default=None)
    )
