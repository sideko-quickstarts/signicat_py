import pydantic
import typing

from .link import Link


class Links(pydantic.BaseModel):
    """
    Links
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    __pydantic_extra__: typing.Dict[str, Link]
