import pydantic
import typing

from .session_package import SessionPackage


class CollectionOutput(pydantic.BaseModel):
    """
    CollectionOutput
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    packages: typing.Optional[typing.List[SessionPackage]] = pydantic.Field(
        alias="packages", default=None
    )
