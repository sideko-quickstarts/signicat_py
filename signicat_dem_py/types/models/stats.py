import pydantic
import typing


class Stats(pydantic.BaseModel):
    """
    Stats
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    avg_record_size: typing.Optional[str] = pydantic.Field(
        alias="avgRecordSize", default=None
    )
    collection_size: typing.Optional[str] = pydantic.Field(
        alias="collectionSize", default=None
    )
    total_records: typing.Optional[int] = pydantic.Field(
        alias="totalRecords", default=None
    )
    total_records_by_type: typing.Optional[typing.Dict[str, typing.Any]] = (
        pydantic.Field(alias="totalRecordsByType", default=None)
    )
