import pydantic
import typing_extensions

from .query_request_body import QueryRequestBody, _SerializerQueryRequestBody


class BatchUpdateTtlRequest(typing_extensions.TypedDict):
    """
    Object containing the user-defined query and new TTL value.
    """

    query: typing_extensions.Required[QueryRequestBody]
    """
    An object containing up to three lists of <code>QueryCondition</code> objects. Each list represents a logic operator used to bind the <code>QueryCondition</code> objects into a statement. <br>The <code>'and'</code> list executes the QueryCondition objects with a logical AND operator, all conditions must be met. <br> The <code>'or'</code> list executes the QueryCondition objects with a logical OR operator, at least one of the conditions must be met. <br> The <code>'not'</code> list is currently not in use, but it will in the future execute the QueryCondition objects with a logical NOR operator.
    """

    ttl: typing_extensions.Required[int]


class _SerializerBatchUpdateTtlRequest(pydantic.BaseModel):
    """
    Serializer for BatchUpdateTtlRequest handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    query: _SerializerQueryRequestBody = pydantic.Field(
        alias="query",
    )
    ttl: int = pydantic.Field(
        alias="ttl",
    )
