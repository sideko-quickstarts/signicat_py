import pydantic
import typing
import typing_extensions


class SessionPackage(typing_extensions.TypedDict):
    """
    Contains session package metadata
    """

    package_id: typing_extensions.NotRequired[str]

    package_type: typing_extensions.NotRequired[
        typing_extensions.Literal["PADES_CONTAINER"]
    ]

    result_document_id: typing_extensions.NotRequired[str]


class _SerializerSessionPackage(pydantic.BaseModel):
    """
    Serializer for SessionPackage handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    package_id: typing.Optional[str] = pydantic.Field(alias="packageId", default=None)
    package_type: typing.Optional[typing_extensions.Literal["PADES_CONTAINER"]] = (
        pydantic.Field(alias="packageType", default=None)
    )
    result_document_id: typing.Optional[str] = pydantic.Field(
        alias="resultDocumentId", default=None
    )
