import pydantic
import typing
import typing_extensions


class SessionPackage(pydantic.BaseModel):
    """
    Contains session package metadata
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    package_id: typing.Optional[str] = pydantic.Field(alias="packageId", default=None)
    package_type: typing.Optional[typing_extensions.Literal["PADES_CONTAINER"]] = (
        pydantic.Field(alias="packageType", default=None)
    )
    result_document_id: typing.Optional[str] = pydantic.Field(
        alias="resultDocumentId", default=None
    )
