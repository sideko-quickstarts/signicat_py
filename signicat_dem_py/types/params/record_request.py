import pydantic
import typing
import typing_extensions


class RecordRequest(typing_extensions.TypedDict):
    """
    Object containing the user-defined datums that are stored in a record. This plus the system-defined data forms a record.
    """

    audit_level: typing_extensions.NotRequired[str]

    core_data: typing_extensions.Required[typing.Dict[str, typing.Any]]

    metadata: typing_extensions.Required[typing.Dict[str, typing.Any]]

    relations: typing_extensions.NotRequired[typing.List[str]]

    ttl: typing_extensions.Required[int]

    type_: typing_extensions.Required[str]


class _SerializerRecordRequest(pydantic.BaseModel):
    """
    Serializer for RecordRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    audit_level: typing.Optional[str] = pydantic.Field(alias="auditLevel", default=None)
    core_data: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="coreData",
    )
    metadata: typing.Dict[str, typing.Any] = pydantic.Field(
        alias="metadata",
    )
    relations: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="relations", default=None
    )
    ttl: int = pydantic.Field(
        alias="ttl",
    )
    type_: str = pydantic.Field(
        alias="type",
    )
