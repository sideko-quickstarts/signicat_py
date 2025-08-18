import pydantic
import typing
import typing_extensions

from .session_package import SessionPackage, _SerializerSessionPackage


class CollectionOutput(typing_extensions.TypedDict):
    """
    CollectionOutput
    """

    packages: typing_extensions.NotRequired[
        typing.Optional[typing.List[SessionPackage]]
    ]


class _SerializerCollectionOutput(pydantic.BaseModel):
    """
    Serializer for CollectionOutput handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    packages: typing.Optional[typing.List[_SerializerSessionPackage]] = pydantic.Field(
        alias="packages", default=None
    )
