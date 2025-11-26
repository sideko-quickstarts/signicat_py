import pydantic
import typing

from .link import Link
from .record_relation_response import RecordRelationResponse
from .system_metadata import SystemMetadata


class RecordResponse(pydantic.BaseModel):
    """
    RecordResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    links: typing.Optional[typing.Dict[str, Link]] = pydantic.Field(
        alias="_links", default=None
    )
    core_data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="coreData", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="metadata", default=None
    )
    relations: typing.Optional[typing.List[RecordRelationResponse]] = pydantic.Field(
        alias="relations", default=None
    )
    system_metadata: typing.Optional[SystemMetadata] = pydantic.Field(
        alias="systemMetadata", default=None
    )
    timestamp_data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="timestampData", default=None
    )
