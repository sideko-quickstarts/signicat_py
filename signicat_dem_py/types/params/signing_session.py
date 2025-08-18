import pydantic
import typing
import typing_extensions

from .pre_authentication import PreAuthentication, _SerializerPreAuthentication
from .redirect_settings import RedirectSettings, _SerializerRedirectSettings
from .session_document import SessionDocument, _SerializerSessionDocument
from .session_lifecycle import SessionLifecycle, _SerializerSessionLifecycle
from .session_output import SessionOutput, _SerializerSessionOutput
from .signer import Signer, _SerializerSigner
from .signing_setup import SigningSetup, _SerializerSigningSetup
from .ui import Ui, _SerializerUi


class SigningSession(typing_extensions.TypedDict):
    """
    SigningSession
    """

    documents: typing_extensions.Required[typing.List[SessionDocument]]

    due_date: typing_extensions.NotRequired[str]
    """
    The deadline for signing the document(s). Can be a maximum of 30 days into the future from the current date.
    """

    external_reference: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Custom identifier for linking the signing session to your internal process. Passed back in redirect URLs.
    """

    id: typing_extensions.NotRequired[str]

    lifecycle: typing_extensions.NotRequired[SessionLifecycle]
    """
    Contains session lifecycle metadata.
    """

    output: typing_extensions.NotRequired[SessionOutput]

    package_to: typing_extensions.NotRequired[
        typing.List[typing_extensions.Literal["PADES_CONTAINER"]]
    ]
    """
    A list of formats the signing session should be packaged to when signed.
    """

    pre_authentication: typing_extensions.NotRequired[PreAuthentication]

    redirect_settings: typing_extensions.NotRequired[RedirectSettings]

    sender_display_name: typing_extensions.NotRequired[str]
    """
    The name of the entity that requested the signature. Displayed while signing.
    """

    sign_text: typing_extensions.NotRequired[str]

    signature_url: typing_extensions.NotRequired[str]

    signer: typing_extensions.NotRequired[Signer]

    signing_setup: typing_extensions.Required[typing.List[SigningSetup]]
    """
    The user interaction setups for this signing session describing which IDPs are available for the end-user.
    """

    subsequent_to: typing_extensions.NotRequired[typing.List[str]]
    """
    IDs of signing sessions that must be signed before this one.
    """

    title: typing_extensions.Required[str]

    ui: typing_extensions.NotRequired[Ui]


class _SerializerSigningSession(pydantic.BaseModel):
    """
    Serializer for SigningSession handling case conversions
    and file omissions as dictated by the API
    """

    model_config = pydantic.ConfigDict(
        populate_by_name=True,
    )

    documents: typing.List[_SerializerSessionDocument] = pydantic.Field(
        alias="documents",
    )
    due_date: typing.Optional[str] = pydantic.Field(alias="dueDate", default=None)
    external_reference: typing.Optional[str] = pydantic.Field(
        alias="externalReference", default=None
    )
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    lifecycle: typing.Optional[_SerializerSessionLifecycle] = pydantic.Field(
        alias="lifecycle", default=None
    )
    output: typing.Optional[_SerializerSessionOutput] = pydantic.Field(
        alias="output", default=None
    )
    package_to: typing.Optional[
        typing.List[typing_extensions.Literal["PADES_CONTAINER"]]
    ] = pydantic.Field(alias="packageTo", default=None)
    pre_authentication: typing.Optional[_SerializerPreAuthentication] = pydantic.Field(
        alias="preAuthentication", default=None
    )
    redirect_settings: typing.Optional[_SerializerRedirectSettings] = pydantic.Field(
        alias="redirectSettings", default=None
    )
    sender_display_name: typing.Optional[str] = pydantic.Field(
        alias="senderDisplayName", default=None
    )
    sign_text: typing.Optional[str] = pydantic.Field(alias="signText", default=None)
    signature_url: typing.Optional[str] = pydantic.Field(
        alias="signatureUrl", default=None
    )
    signer: typing.Optional[_SerializerSigner] = pydantic.Field(
        alias="signer", default=None
    )
    signing_setup: typing.List[_SerializerSigningSetup] = pydantic.Field(
        alias="signingSetup",
    )
    subsequent_to: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="subsequentTo", default=None
    )
    title: str = pydantic.Field(
        alias="title",
    )
    ui: typing.Optional[_SerializerUi] = pydantic.Field(alias="ui", default=None)
