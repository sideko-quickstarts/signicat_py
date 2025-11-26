import pydantic
import pytest
import typing

from make_api_request import BinaryResponse
from signicat_dem_py import AsyncClient, Client
from signicat_dem_py.environment import SIDEKO_MOCK_SERVER
from signicat_dem_py.types import models


def test_query_200_success_required_only() -> None:
    """Tests a POST request to the /records/query endpoint.

    Operation: query
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.query(
        data={
            "and_": [{"field": "string", "operator": "string", "value": "{}"}],
            "not_": [{"field": "string", "operator": "string", "value": "{}"}],
            "or_": [{"field": "string", "operator": "string", "value": "{}"}],
        }
    )
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_query_200_success_required_only() -> None:
    """Tests a POST request to the /records/query endpoint.

    Operation: query
    Test Case ID: success_required_only
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.query(
        data={
            "and_": [{"field": "string", "operator": "string", "value": "{}"}],
            "not_": [{"field": "string", "operator": "string", "value": "{}"}],
            "or_": [{"field": "string", "operator": "string", "value": "{}"}],
        }
    )
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_query_200_success_all_params() -> None:
    """Tests a POST request to the /records/query endpoint.

    Operation: query
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.query(
        data={
            "and_": [{"field": "string", "operator": "string", "value": "{}"}],
            "not_": [{"field": "string", "operator": "string", "value": "{}"}],
            "or_": [{"field": "string", "operator": "string", "value": "{}"}],
        },
        page=123,
        size=123,
    )
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_query_200_success_all_params() -> None:
    """Tests a POST request to the /records/query endpoint.

    Operation: query
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : typing.Dict[str, typing.Any]

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.query(
        data={
            "and_": [{"field": "string", "operator": "string", "value": "{}"}],
            "not_": [{"field": "string", "operator": "string", "value": "{}"}],
            "or_": [{"field": "string", "operator": "string", "value": "{}"}],
        },
        page=123,
        size=123,
    )
    try:
        pydantic.TypeAdapter(typing.Dict[str, typing.Any]).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_post_new_record_201_success_all_params() -> None:
    """Tests a POST request to the /records endpoint.

    Operation: post_new_record
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Synchronous execution

    Response : models.RecordResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.post_new_record(
        core_data={},
        metadata={},
        ttl=123,
        type_="string",
        audit_level="string",
        relations=["string"],
    )
    try:
        pydantic.TypeAdapter(models.RecordResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_post_new_record_201_success_all_params() -> None:
    """Tests a POST request to the /records endpoint.

    Operation: post_new_record
    Test Case ID: success_all_params
    Expected Status: 201
    Mode: Asynchronous execution

    Response : models.RecordResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.post_new_record(
        core_data={},
        metadata={},
        ttl=123,
        type_="string",
        audit_level="string",
        relations=["string"],
    )
    try:
        pydantic.TypeAdapter(models.RecordResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_set_expiry_date_204_success_all_params() -> None:
    """Tests a PATCH request to the /records/{id} endpoint.

    Operation: set_expiry_date
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
    response = client.dem.set_expiry_date(
        id="123e4567-e89b-12d3-a456-556642440000", ttl=123
    )
    assert response is None


@pytest.mark.asyncio
async def test_await_set_expiry_date_204_success_all_params() -> None:
    """Tests a PATCH request to the /records/{id} endpoint.

    Operation: set_expiry_date
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
    response = await client.dem.set_expiry_date(
        id="123e4567-e89b-12d3-a456-556642440000", ttl=123
    )
    assert response is None


def test_set_expiry_dates_200_success_all_params() -> None:
    """Tests a PATCH request to the /records endpoint.

    Operation: set_expiry_dates
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : str

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.set_expiry_dates(
        query={
            "and_": [{"field": "string", "operator": "string", "value": "{}"}],
            "not_": [{"field": "string", "operator": "string", "value": "{}"}],
            "or_": [{"field": "string", "operator": "string", "value": "{}"}],
        },
        ttl=123,
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_set_expiry_dates_200_success_all_params() -> None:
    """Tests a PATCH request to the /records endpoint.

    Operation: set_expiry_dates
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : str

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.set_expiry_dates(
        query={
            "and_": [{"field": "string", "operator": "string", "value": "{}"}],
            "not_": [{"field": "string", "operator": "string", "value": "{}"}],
            "or_": [{"field": "string", "operator": "string", "value": "{}"}],
        },
        ttl=123,
    )
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_generate_report_200_success_all_params() -> None:
    """Tests a GET request to the /reports/{id} endpoint.

    Operation: generate_report
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.generate_report(id="123e4567-e89b-12d3-a456-556642440000")
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_generate_report_200_success_all_params() -> None:
    """Tests a GET request to the /reports/{id} endpoint.

    Operation: generate_report
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.generate_report(
        id="123e4567-e89b-12d3-a456-556642440000"
    )
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_get_record_by_id_200_success_all_params() -> None:
    """Tests a GET request to the /records/{id} endpoint.

    Operation: get_record_by_id
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.RecordResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.get_record_by_id(id="123e4567-e89b-12d3-a456-556642440000")
    try:
        pydantic.TypeAdapter(models.RecordResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_record_by_id_200_success_all_params() -> None:
    """Tests a GET request to the /records/{id} endpoint.

    Operation: get_record_by_id
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.RecordResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.get_record_by_id(
        id="123e4567-e89b-12d3-a456-556642440000"
    )
    try:
        pydantic.TypeAdapter(models.RecordResponse).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_get_custom_meta_fields_200_success_all_params() -> None:
    """Tests a GET request to the /info/custom-fields/{type} endpoint.

    Operation: get_custom_meta_fields
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.get_custom_meta_fields(type_="string")
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_custom_meta_fields_200_success_all_params() -> None:
    """Tests a GET request to the /info/custom-fields/{type} endpoint.

    Operation: get_custom_meta_fields
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.get_custom_meta_fields(type_="string")
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_get_custom_meta_fields_1_200_success_all_params() -> None:
    """Tests a GET request to the /info/custom-fields endpoint.

    Operation: get_custom_meta_fields_1
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.get_custom_meta_fields_1()
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_custom_meta_fields_1_200_success_all_params() -> None:
    """Tests a GET request to the /info/custom-fields endpoint.

    Operation: get_custom_meta_fields_1
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : BinaryResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.get_custom_meta_fields_1()
    is_valid_binary = isinstance(response, BinaryResponse)
    assert is_valid_binary, "failed response type check"


def test_get_collection_stats_200_success_all_params() -> None:
    """Tests a GET request to the /info endpoint.

    Operation: get_collection_stats
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.Stats

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.get_collection_stats()
    try:
        pydantic.TypeAdapter(models.Stats).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_collection_stats_200_success_all_params() -> None:
    """Tests a GET request to the /info endpoint.

    Operation: get_collection_stats
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.Stats

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.get_collection_stats()
    try:
        pydantic.TypeAdapter(models.Stats).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


def test_signicat_200_success_all_params() -> None:
    """Tests a GET request to the /.ping endpoint.

    Operation: signicat
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Synchronous execution

    Response : str

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = client.dem.signicat()
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"


@pytest.mark.asyncio
async def test_await_signicat_200_success_all_params() -> None:
    """Tests a GET request to the /.ping endpoint.

    Operation: signicat
    Test Case ID: success_all_params
    Expected Status: 200
    Mode: Asynchronous execution

    Response : str

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(token="API_TOKEN", environment=SIDEKO_MOCK_SERVER)
    response = await client.dem.signicat()
    try:
        pydantic.TypeAdapter(str).validate_python(response)
        is_valid_response_schema = True
    except pydantic.ValidationError:
        is_valid_response_schema = False
    assert is_valid_response_schema, "failed response type check"
