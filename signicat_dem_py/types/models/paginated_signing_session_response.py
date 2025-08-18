import pydantic
import typing

from .signing_session import SigningSession


class PaginatedSigningSessionResponse(pydantic.BaseModel):
    """
    PaginatedSigningSessionResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    count: typing.Optional[int] = pydantic.Field(alias="count", default=None)
    """
    Number of items in current page
    """
    data: typing.Optional[typing.List[SigningSession]] = pydantic.Field(
        alias="data", default=None
    )
    limit: typing.Optional[int] = pydantic.Field(alias="limit", default=None)
    """
    Number of items per page
    """
    offset: typing.Optional[int] = pydantic.Field(alias="offset", default=None)
    """
    Page number
    """
    total: typing.Optional[int] = pydantic.Field(alias="total", default=None)
    """
    Total number of items
    """
