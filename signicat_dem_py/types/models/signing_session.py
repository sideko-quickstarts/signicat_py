import pydantic
import typing
import typing_extensions

from .pre_authentication import PreAuthentication
from .redirect_settings import RedirectSettings
from .session_document import SessionDocument
from .session_lifecycle import SessionLifecycle
from .session_output import SessionOutput
from .signer import Signer
from .signing_setup import SigningSetup
from .ui import Ui


class SigningSession(pydantic.BaseModel):
    """
    SigningSession
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    documents: typing.List[SessionDocument] = pydantic.Field(
        alias="documents",
    )
    due_date: typing.Optional[str] = pydantic.Field(alias="dueDate", default=None)
    """
    The deadline for signing the document(s). Can be a maximum of 30 days into the future from the current date.
    """
    external_reference: typing.Optional[str] = pydantic.Field(
        alias="externalReference", default=None
    )
    """
    Custom identifier for linking the signing session to your internal process. Passed back in redirect URLs.
    """
    id: typing.Optional[str] = pydantic.Field(alias="id", default=None)
    lifecycle: typing.Optional[SessionLifecycle] = pydantic.Field(
        alias="lifecycle", default=None
    )
    """
    Contains session lifecycle metadata.
    """
    output: typing.Optional[SessionOutput] = pydantic.Field(
        alias="output", default=None
    )
    package_to: typing.Optional[
        typing.List[typing_extensions.Literal["PADES_CONTAINER"]]
    ] = pydantic.Field(alias="packageTo", default=None)
    """
    A list of formats the signing session should be packaged to when signed.
    """
    pre_authentication: typing.Optional[PreAuthentication] = pydantic.Field(
        alias="preAuthentication", default=None
    )
    redirect_settings: typing.Optional[RedirectSettings] = pydantic.Field(
        alias="redirectSettings", default=None
    )
    sender_display_name: typing.Optional[str] = pydantic.Field(
        alias="senderDisplayName", default=None
    )
    """
    The name of the entity that requested the signature. Displayed while signing.
    """
    sign_text: typing.Optional[str] = pydantic.Field(alias="signText", default=None)
    signature_url: typing.Optional[str] = pydantic.Field(
        alias="signatureUrl", default=None
    )
    signer: typing.Optional[Signer] = pydantic.Field(alias="signer", default=None)
    signing_setup: typing.List[SigningSetup] = pydantic.Field(
        alias="signingSetup",
    )
    """
    The user interaction setups for this signing session describing which IDPs are available for the end-user.
    """
    subsequent_to: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="subsequentTo", default=None
    )
    """
    IDs of signing sessions that must be signed before this one.
    """
    title: str = pydantic.Field(
        alias="title",
    )
    ui: typing.Optional[Ui] = pydantic.Field(alias="ui", default=None)
