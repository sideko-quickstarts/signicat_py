import pydantic
import typing
import typing_extensions


class Ui(pydantic.BaseModel):
    """
    Ui
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    language: typing.Optional[
        typing_extensions.Literal["da", "de", "en", "fi", "nb", "nn", "sv"]
    ] = pydantic.Field(alias="language", default=None)
