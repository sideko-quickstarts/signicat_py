import httpx
import io
import pydantic
import pytest
import typing

from signicat_dem_py import AsyncClient, Client
from signicat_dem_py.environment import SIDEKO_MOCK_SERVER
from signicat_dem_py.types import models


def test_create_signing_session_201_success_all_params() -> None:
    """Tests a POST request to the /signing-sessions endpoint.

    Operation: create_signing_session
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : typing.List[models.SigningSession]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.create_signing_session(
        data=[
            {
                "documents": [
                    {
                        "action": "SIGN",
                        "document_collection_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0853",
                        "document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0857",
                    }
                ],
                "due_date": "2025-04-01T17:32:28Z",
                "external_reference": "string",
                "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0852",
                "lifecycle": {"state": "BLOCKED", "state_is_final": True},
                "output": {
                    "packages": [
                        {
                            "package_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                            "package_type": "PADES_CONTAINER",
                            "result_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                        }
                    ],
                    "signatures": [
                        {
                            "document_collection_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0854",
                            "original_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0856",
                            "result_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0855",
                            "signature_type": "PADES",
                        }
                    ],
                },
                "package_to": ["PADES_CONTAINER"],
                "pre_authentication": {"enabled": True},
                "redirect_settings": {
                    "cancel": "http://example.com/cancel",
                    "error": "http://example.com/error",
                    "success": "http://example.com/complete",
                },
                "sender_display_name": "Corporation incorporated",
                "sign_text": "Please sign this document",
                "signature_url": "https://signtest-account.sandbox.signicat.com/sign/?sessionId=8ce3dac2-74b3-429c-adf7-fe6d277186d0",
                "signer": {
                    "email": "mail@example.org",
                    "mobile": "+47 123 45 678",
                    "national_identification_number": "string",
                    "validations": ["NATIONAL_IDENTIFICATION_NUMBER"],
                },
                "signing_setup": [
                    {
                        "additional_parameters": {
                            "sbid_end_user_ip": "127.0.0.1",
                            "sbid_flow": "QR",
                        },
                        "identity_providers": [{"idp_name": "string"}],
                        "signing_flow": "AUTHENTICATION_BASED",
                        "vendor": "AUDKENNI",
                    }
                ],
                "subsequent_to": ["f05d0dce-a7af-432b-b6b8-e455ab7c0858"],
                "title": "Business Process",
                "ui": {"language": "da"},
            }
        ]
    )
    try:
        pydantic.TypeAdapter(typing.List[models.SigningSession]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_signing_session_201_success_all_params() -> None:
    """Tests a POST request to the /signing-sessions endpoint.

    Operation: create_signing_session
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : typing.List[models.SigningSession]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.create_signing_session(
        data=[
            {
                "documents": [
                    {
                        "action": "SIGN",
                        "document_collection_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0853",
                        "document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0857",
                    }
                ],
                "due_date": "2025-04-01T17:32:28Z",
                "external_reference": "string",
                "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0852",
                "lifecycle": {"state": "BLOCKED", "state_is_final": True},
                "output": {
                    "packages": [
                        {
                            "package_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                            "package_type": "PADES_CONTAINER",
                            "result_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                        }
                    ],
                    "signatures": [
                        {
                            "document_collection_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0854",
                            "original_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0856",
                            "result_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0855",
                            "signature_type": "PADES",
                        }
                    ],
                },
                "package_to": ["PADES_CONTAINER"],
                "pre_authentication": {"enabled": True},
                "redirect_settings": {
                    "cancel": "http://example.com/cancel",
                    "error": "http://example.com/error",
                    "success": "http://example.com/complete",
                },
                "sender_display_name": "Corporation incorporated",
                "sign_text": "Please sign this document",
                "signature_url": "https://signtest-account.sandbox.signicat.com/sign/?sessionId=8ce3dac2-74b3-429c-adf7-fe6d277186d0",
                "signer": {
                    "email": "mail@example.org",
                    "mobile": "+47 123 45 678",
                    "national_identification_number": "string",
                    "validations": ["NATIONAL_IDENTIFICATION_NUMBER"],
                },
                "signing_setup": [
                    {
                        "additional_parameters": {
                            "sbid_end_user_ip": "127.0.0.1",
                            "sbid_flow": "QR",
                        },
                        "identity_providers": [{"idp_name": "string"}],
                        "signing_flow": "AUTHENTICATION_BASED",
                        "vendor": "AUDKENNI",
                    }
                ],
                "subsequent_to": ["f05d0dce-a7af-432b-b6b8-e455ab7c0858"],
                "title": "Business Process",
                "ui": {"language": "da"},
            }
        ]
    )
    try:
        pydantic.TypeAdapter(typing.List[models.SigningSession]).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_upload_document_200_success_all_params() -> None:
    """Tests a POST request to the /documents endpoint.

    Operation: upload_document
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PostDocumentResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.upload_document(
        content_type="string", data=io.BytesIO(b"123")
    )
    try:
        pydantic.TypeAdapter(models.PostDocumentResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_upload_document_200_success_all_params() -> None:
    """Tests a POST request to the /documents endpoint.

    Operation: upload_document
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PostDocumentResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.upload_document(
        content_type="string", data=b"123"
    )
    try:
        pydantic.TypeAdapter(models.PostDocumentResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_create_document_collection_201_success_all_params() -> None:
    """Tests a POST request to the /document-collections endpoint.

    Operation: create_document_collection
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.DocumentCollection

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.create_document_collection(
        documents=[
            {
                "description": "Terms of Service",
                "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f",
            }
        ],
        id="f05d0dce-a7af-432b-b6b8-e455ab7c0858",
        output={
            "packages": [
                {
                    "package_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                    "package_type": "PADES_CONTAINER",
                    "result_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                }
            ]
        },
        package_to=["PADES_CONTAINER"],
    )
    try:
        pydantic.TypeAdapter(models.DocumentCollection).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_create_document_collection_201_success_all_params() -> None:
    """Tests a POST request to the /document-collections endpoint.

    Operation: create_document_collection
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.DocumentCollection

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.create_document_collection(
        documents=[
            {
                "description": "Terms of Service",
                "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f",
            }
        ],
        id="f05d0dce-a7af-432b-b6b8-e455ab7c0858",
        output={
            "packages": [
                {
                    "package_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                    "package_type": "PADES_CONTAINER",
                    "result_document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0863",
                }
            ]
        },
        package_to=["PADES_CONTAINER"],
    )
    try:
        pydantic.TypeAdapter(models.DocumentCollection).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_update_document_metadata_200_success_all_params() -> None:
    """Tests a PATCH request to the /documents/{documentId}/metadata endpoint.

    Operation: update_document_metadata
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Document

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.update_document_metadata(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        created_at="2023-04-12T10:30:00Z",
        description="Invoice for order #001",
        document_hash={"hash": "string", "hash_algorithm": "SHA256"},
        filename="invoice_001.pdf",
        mime_type="application/pdf",
        title="Invoice #001",
    )
    try:
        pydantic.TypeAdapter(models.Document).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_update_document_metadata_200_success_all_params() -> None:
    """Tests a PATCH request to the /documents/{documentId}/metadata endpoint.

    Operation: update_document_metadata
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Document

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.update_document_metadata(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
        created_at="2023-04-12T10:30:00Z",
        description="Invoice for order #001",
        document_hash={"hash": "string", "hash_algorithm": "SHA256"},
        filename="invoice_001.pdf",
        mime_type="application/pdf",
        title="Invoice #001",
    )
    try:
        pydantic.TypeAdapter(models.Document).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_signing_session_200_success_all_params() -> None:
    """Tests a GET request to the /signing-sessions/{sessionId} endpoint.

    Operation: get_signing_session
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.SigningSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.get_signing_session(
        session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.SigningSession).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_signing_session_200_success_all_params() -> None:
    """Tests a GET request to the /signing-sessions/{sessionId} endpoint.

    Operation: get_signing_session
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.SigningSession

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.get_signing_session(
        session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.SigningSession).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_signing_sessions_200_success_required_only() -> None:
    """Tests a GET request to the /signing-sessions endpoint.

    Operation: list_signing_sessions
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaginatedSigningSessionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.list_signing_sessions()
    try:
        pydantic.TypeAdapter(models.PaginatedSigningSessionResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_signing_sessions_200_success_required_only() -> None:
    """Tests a GET request to the /signing-sessions endpoint.

    Operation: list_signing_sessions
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaginatedSigningSessionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.list_signing_sessions()
    try:
        pydantic.TypeAdapter(models.PaginatedSigningSessionResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_list_signing_sessions_200_success_all_params() -> None:
    """Tests a GET request to the /signing-sessions endpoint.

    Operation: list_signing_sessions
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.PaginatedSigningSessionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.list_signing_sessions(limit=123, offset=123, sort=["string"])
    try:
        pydantic.TypeAdapter(models.PaginatedSigningSessionResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_list_signing_sessions_200_success_all_params() -> None:
    """Tests a GET request to the /signing-sessions endpoint.

    Operation: list_signing_sessions
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.PaginatedSigningSessionResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.list_signing_sessions(
        limit=123, offset=123, sort=["string"]
    )
    try:
        pydantic.TypeAdapter(models.PaginatedSigningSessionResponse).validate_python(
            response
        )
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_document_info_200_success_all_params() -> None:
    """Tests a GET request to the /documents/{documentId}/metadata endpoint.

    Operation: get_document_info
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Document

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.get_document_info(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.Document).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_document_info_200_success_all_params() -> None:
    """Tests a GET request to the /documents/{documentId}/metadata endpoint.

    Operation: get_document_info
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Document

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.get_document_info(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.Document).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_document_200_success_all_params() -> None:
    """Tests a GET request to the /documents/{documentId} endpoint.

    Operation: get_document
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.get_document(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert isinstance(response, httpx.Response)


@pytest.mark.asyncio
async def test_await_get_document_200_success_all_params() -> None:
    """Tests a GET request to the /documents/{documentId} endpoint.

    Operation: get_document
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : httpx.Response

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.get_document(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert isinstance(response, httpx.Response)


def test_get_document_collection_200_success_all_params() -> None:
    """Tests a GET request to the /document-collections/{documentCollectionId} endpoint.

    Operation: get_document_collection
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.DocumentCollection

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.get_document_collection(
        document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.DocumentCollection).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_document_collection_200_success_all_params() -> None:
    """Tests a GET request to the /document-collections/{documentCollectionId} endpoint.

    Operation: get_document_collection
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.DocumentCollection

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.get_document_collection(
        document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    try:
        pydantic.TypeAdapter(models.DocumentCollection).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_delete_signing_session_204_success_all_params() -> None:
    """Tests a DELETE request to the /signing-sessions/{sessionId} endpoint.

    Operation: delete_signing_session
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.delete_signing_session(
        session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_signing_session_204_success_all_params() -> None:
    """Tests a DELETE request to the /signing-sessions/{sessionId} endpoint.

    Operation: delete_signing_session
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.delete_signing_session(
        session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None


def test_delete_document_204_success_all_params() -> None:
    """Tests a DELETE request to the /documents/{documentId} endpoint.

    Operation: delete_document
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.delete_document(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_document_204_success_all_params() -> None:
    """Tests a DELETE request to the /documents/{documentId} endpoint.

    Operation: delete_document
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.delete_document(
        document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None


def test_delete_document_collection_204_success_all_params() -> None:
    """Tests a DELETE request to the /document-collections/{documentCollectionId} endpoint.

    Operation: delete_document_collection
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Synchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.sign.delete_document_collection(
        document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_delete_document_collection_204_success_all_params() -> None:
    """Tests a DELETE request to the /document-collections/{documentCollectionId} endpoint.

    Operation: delete_document_collection
    Test Case ID: success_all_params
    Expected Status: 204
    Mode: Asynchronous execution

    Empty response expected

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.sign.delete_document_collection(
        document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
    )
    assert response is None
