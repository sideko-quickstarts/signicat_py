import pydantic
import typing
import typing_extensions


class Ui(typing_extensions.TypedDict):
    """
    Ui
    """

    language: typing_extensions.NotRequired[
        typing_extensions.Literal["da", "de", "en", "fi", "nb", "nn", "sv"]
    ]


class _SerializerUi(pydantic.BaseModel):
    """
    Serializer for Ui handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    language: typing.Optional[
        typing_extensions.Literal["da", "de", "en", "fi", "nb", "nn", "sv"]
    ] = pydantic.Field(alias="language", default=None)
