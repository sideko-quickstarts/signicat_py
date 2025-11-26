import typing

from make_api_request import (
    AsyncBaseClient,
    BinaryResponse,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from signicat_dem_py.types import models, params


class DemClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def signicat(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        GET /.ping

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.signicat()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/.ping",
            service_name="dem",
            cast_to=str,
            request_options=request_options or default_request_options(),
        )

    def get_collection_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Stats:
        """
        Get statistics for records

        Retrieves statistics on records stored in DEM.

        GET /info

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.get_collection_stats()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/info",
            service_name="dem",
            cast_to=models.Stats,
            request_options=request_options or default_request_options(),
        )

    def get_custom_meta_fields_1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Get all fields from customerMeta from all records

        Aggregates all of the customer's records to return a list of all unique keys from the customerMeta field.

        GET /info/custom-fields

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.get_custom_meta_fields_1()
        ```
        """
        return self._base_client.request(
            method="GET",
            path="/info/custom-fields",
            service_name="dem",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get_custom_meta_fields(
        self, *, type_: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Get all fields from customerMeta from all records

        Aggregates all of the customer's records to return a list of all unique keys from the customerMeta field.

        GET /info/custom-fields/{type}

        Args:
            type_: Optional parameter that narrows the result down based on the type of record.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.get_custom_meta_fields(type_="string")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/info/custom-fields/{type_}",
            service_name="dem",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def get_record_by_id(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.RecordResponse:
        """
        Get record by ID

        Retrieves a specific record by its ID. The given ID must conform to the UUID/GUID standard. <br><em>For example</em>: <code>123e4567-e89b-12d3-a456-556642440000</code><br> Returns everything included in the record entity.

        GET /records/{id}

        Args:
            id: Unique identifier for a record.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.get_record_by_id(id="123e4567-e89b-12d3-a456-556642440000")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/records/{id}",
            service_name="dem",
            cast_to=models.RecordResponse,
            request_options=request_options or default_request_options(),
        )

    def generate_report(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Retrieves a generated PDF report for a record

        Takes a Record ID as a parameter. It retrieves the record and generates a PDF report for the record.

        GET /reports/{id}

        Args:
            id: Unique identifier for a record.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.generate_report(id="123e4567-e89b-12d3-a456-556642440000")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/reports/{id}",
            service_name="dem",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    def set_expiry_dates(
        self,
        *,
        query: params.QueryRequestBody,
        ttl: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Update multiple selected records

        Updates the Time to Live (TTL) of selected records by a defined query.<br>The query is built on the MongoDB Query Language (MQL), but it is database-agnostic.<br>

        PATCH /records

        Args:
            query: An object containing up to three lists of <code>QueryCondition</code> objects. Each list represents a logic operator used to bind the <code>QueryCondition</code> objects into a statement. <br>The <code>'and'</code> list executes the QueryCondition objects with a logical AND operator, all conditions must be met. <br> The <code>'or'</code> list executes the QueryCondition objects with a logical OR operator, at least one of the conditions must be met. <br> The <code>'not'</code> list is currently not in use, but it will in the future execute the QueryCondition objects with a logical NOR operator.
            ttl: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.set_expiry_dates(query={}, ttl=123)
        ```
        """
        _json = to_encodable(
            item={"query": query, "ttl": ttl},
            dump_with=params._SerializerBatchUpdateTtlRequest,
        )
        return self._base_client.request(
            method="PATCH",
            path="/records",
            service_name="dem",
            json=_json,
            cast_to=str,
            request_options=request_options or default_request_options(),
        )

    def set_expiry_date(
        self,
        *,
        id: str,
        ttl: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the expiry of a given record

        Specifies when the record will automatically be deleted from the database. Takes an amount of days as a positive integer of 2 or higher and updates the expiry date with the new value.

        PATCH /records/{id}

        Args:
            id: Unique identifier for a record.
            ttl: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful, no content returned

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.set_expiry_date(id="123e4567-e89b-12d3-a456-556642440000", ttl=123)
        ```
        """
        _json = to_encodable(
            item={"ttl": ttl}, dump_with=params._SerializerSetExpiryDateRequest
        )
        self._base_client.request(
            method="PATCH",
            path=f"/records/{id}",
            service_name="dem",
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def post_new_record(
        self,
        *,
        core_data: typing.Dict[str, typing.Any],
        metadata: typing.Dict[str, typing.Any],
        ttl: int,
        type_: str,
        audit_level: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        relations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RecordResponse:
        """
        Create a new record

        Creates a new record. There are four required fields: "type", "metadata", "coreData", "TTL" and two optional fields: "relations" and "auditLevel".<h2>Record Type</h2>You are required to supply a record type in the 'type' parameter when posting a new record.These are the available types: <table>   <tr>       <th>Type name</th>       <th>Description (suggested use)</th>   </tr>   <tr>       <td style='text-align:center;'>GDPR</td>       <td style='text-align:center;'>Can be used for documentation of GDPR compliance.</td>   </tr>   <tr>       <td style='text-align:center;'>TRANSACTION</td>       <td style='text-align:center;'>Can be used for documenting financial transactions.</td>   </tr>   <tr>       <td style='text-align:center;'>LOG_IN</td>       <td style='text-align:center;'>Can be used for documenting users logging in to a system.</td>   </tr>   <tr>       <td style='text-align:center;'>SIGNATURE</td>       <td style='text-align:center;'>Can be used for documenting digital signatures.</td>   </tr>   <tr>       <td style='text-align:center;'>SENSITIVE</td>       <td style='text-align:center;'>Can be used for documenting sensitive information.</td>   </tr>   <tr>       <td style='text-align:center;'>OTHER</td>       <td style='text-align:center;'>Can be used for everything else.</td>   </tr></table><h2>Metadata</h2> Can contain any amount of data which will then be searchable in future queries.<h2>Core Data</h2> Can contain any amount of data which will then be timestamped.<h2>TTL</h2> Time to Live as denoted in amount of days (Int).<h2>Relations</h2> Optional field. List of the IDs (String) of the related records. Default: Empty list<h2>Audit Level</h2> Optional field. Decides which level of timestamping and verification will be applied to the record.<table>   <tr>       <td style='text-align:center;'>SIMPLE</td>       <td style='text-align:center;'>Uses hashing to verify data.</td>   </tr>   <tr>       <td style='text-align:center;'>ADVANCED</td>       <td style='text-align:center;'>Uses TSA to timestamp and verify.</td>   </tr>   <tr>       <td style='text-align:center;'>QUALIFIED</td>       <td style='text-align:center;'>USES QTSA to timestamp and verify. Default if value is not set explicitly</td>   </tr></table>

        POST /records

        Args:
            audit_level: str
            relations: typing.List[str]
            core_data: typing.Dict[str, typing.Any]
            metadata: typing.Dict[str, typing.Any]
            ttl: int
            type_: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Record has been created and posted to the database.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.post_new_record(core_data={}, metadata={}, ttl=123, type_="string")
        ```
        """
        _json = to_encodable(
            item={
                "audit_level": audit_level,
                "relations": relations,
                "core_data": core_data,
                "metadata": metadata,
                "ttl": ttl,
                "type_": type_,
            },
            dump_with=params._SerializerRecordRequest,
        )
        return self._base_client.request(
            method="POST",
            path="/records",
            service_name="dem",
            json=_json,
            cast_to=models.RecordResponse,
            request_options=request_options or default_request_options(),
        )

    def query(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.QueryRequestBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Query a collection for records matching specified parameters

        Queries the database to return a pageable list of records without coreData.<br>If no body is included, the endpoint will return pages of all records.<br>The size and page number as well as sorting and ordering of the returned page is decided by the parameters <code>page</code>, <code>size</code> and <code>sort</code>.<br><br><h2>Request Body</h2><br>The query is built from the request body. The request body is an object containing up to two lists of QueryCondition objects.<br><b>If no lists are provided, the query will return every record in the collection.</b><br><br><table style='width:100%'>   <tr>       <th>List name</th>       <th>Description</th>   </tr>   <tr>       <td>and</td>       <td>Combines the QueryConditions with the logical AND operator. All of the QueryConditions need to return true.</td>   </tr>   <tr>       <td>or</td>       <td>Combines the QueryConditions with the logical OR operator. Only one of the QueryConditions needs to return true.</td>   </tr></table><h2>Query Condition</h2><br>A query condition consists of three parts: <b>field</b>, <b>operator</b> and <b>value</b>.<br><h3>Field</h3><br>The field parameter denotes which field in the database to apply the query condition to.<br><i>Replace '*' with the sub-field you wish to query. For example "metadata.firstName" or "systemMetadata.createdDateTime"</i><br><b>These are the allowed fields:</b><br><table style='width:100%'>   <tr>       <th>Field</th>       <th>Description</th>   </tr>   <tr>       <td>metadata</td>       <td>Metadata added by the user.</td>   </tr>   <tr>       <td>systemMetadata</td>       <td>Metadata added by DEM.</td>   </tr>   <tr>       <td>relations</td>       <td>Any other record relations added by the user.</td>   </tr></table><br><h3>Operator</h3><br>The operator specifies how the condition uses the value to search for records.<br><b>These are the available query operators:</b><br><br><table style='width:100%'>   <tr>       <th>Query Operation</th>       <th>Description</th>   </tr>   <tr>       <td>eq</td>       <td>Checks if the field's value matches the input value exactly.</td>   </tr>   <tr>       <td>ne</td>       <td>Checks if the field's value does not match the input value.</td>   </tr>   <tr>       <td>gt</td>       <td>Checks if the field's value is greater than the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>gte</td>       <td>Checks if the field's value is greater than or equal to the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>lt</td>       <td>Checks if the field's value is less than the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>lte</td>       <td>Checks if the field's value is less than or equal to the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>regex</td>       <td>Checks if the field's value contains the input value using regex. Works best with String values.</td>   </tr>   <tr>       <td>in</td>       <td>Checks if the field's value matches any of the values in the inputted array.</td>   </tr>   <tr>       <td>nin</td>       <td>Checks if the field's value does not match any of the values in the inputted array.</td>   </tr></table><br><h3>Value</h3><br>The value parameter denotes what value the query condition should use. For example: with the EQUAL operator, the value is what the field should be equal to.

        POST /records/query

        Args:
            data: An object containing up to three lists of <code>QueryCondition</code> objects. Each list represents a logic operator used to bind the <code>QueryCondition</code> objects into a statement. <br>The <code>'and'</code> list executes the QueryCondition objects with a logical AND operator, all conditions must be met. <br> The <code>'or'</code> list executes the QueryCondition objects with a logical OR operator, at least one of the conditions must be met. <br> The <code>'not'</code> list is currently not in use, but it will in the future execute the QueryCondition objects with a logical NOR operator.
            page: int
            size: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.dem.query()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "size",
                to_encodable(item=size, dump_with=int),
                style="form",
                explode=True,
            )
        _json = (
            to_encodable(item=data, dump_with=params._SerializerQueryRequestBody)
            if data
            else None
        )
        return self._base_client.request(
            method="POST",
            path="/records/query",
            service_name="dem",
            query_params=_query,
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )


class AsyncDemClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def signicat(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        GET /.ping

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            OK

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.signicat()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/.ping",
            service_name="dem",
            cast_to=str,
            request_options=request_options or default_request_options(),
        )

    async def get_collection_stats(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> models.Stats:
        """
        Get statistics for records

        Retrieves statistics on records stored in DEM.

        GET /info

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.get_collection_stats()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/info",
            service_name="dem",
            cast_to=models.Stats,
            request_options=request_options or default_request_options(),
        )

    async def get_custom_meta_fields_1(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Get all fields from customerMeta from all records

        Aggregates all of the customer's records to return a list of all unique keys from the customerMeta field.

        GET /info/custom-fields

        Args:
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.get_custom_meta_fields_1()
        ```
        """
        return await self._base_client.request(
            method="GET",
            path="/info/custom-fields",
            service_name="dem",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_custom_meta_fields(
        self, *, type_: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Get all fields from customerMeta from all records

        Aggregates all of the customer's records to return a list of all unique keys from the customerMeta field.

        GET /info/custom-fields/{type}

        Args:
            type_: Optional parameter that narrows the result down based on the type of record.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.get_custom_meta_fields(type_="string")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/info/custom-fields/{type_}",
            service_name="dem",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_record_by_id(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> models.RecordResponse:
        """
        Get record by ID

        Retrieves a specific record by its ID. The given ID must conform to the UUID/GUID standard. <br><em>For example</em>: <code>123e4567-e89b-12d3-a456-556642440000</code><br> Returns everything included in the record entity.

        GET /records/{id}

        Args:
            id: Unique identifier for a record.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.get_record_by_id(id="123e4567-e89b-12d3-a456-556642440000")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/records/{id}",
            service_name="dem",
            cast_to=models.RecordResponse,
            request_options=request_options or default_request_options(),
        )

    async def generate_report(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> BinaryResponse:
        """
        Retrieves a generated PDF report for a record

        Takes a Record ID as a parameter. It retrieves the record and generates a PDF report for the record.

        GET /reports/{id}

        Args:
            id: Unique identifier for a record.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.generate_report(id="123e4567-e89b-12d3-a456-556642440000")
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/reports/{id}",
            service_name="dem",
            cast_to=BinaryResponse,
            request_options=request_options or default_request_options(),
        )

    async def set_expiry_dates(
        self,
        *,
        query: params.QueryRequestBody,
        ttl: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Update multiple selected records

        Updates the Time to Live (TTL) of selected records by a defined query.<br>The query is built on the MongoDB Query Language (MQL), but it is database-agnostic.<br>

        PATCH /records

        Args:
            query: An object containing up to three lists of <code>QueryCondition</code> objects. Each list represents a logic operator used to bind the <code>QueryCondition</code> objects into a statement. <br>The <code>'and'</code> list executes the QueryCondition objects with a logical AND operator, all conditions must be met. <br> The <code>'or'</code> list executes the QueryCondition objects with a logical OR operator, at least one of the conditions must be met. <br> The <code>'not'</code> list is currently not in use, but it will in the future execute the QueryCondition objects with a logical NOR operator.
            ttl: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.set_expiry_dates(query={}, ttl=123)
        ```
        """
        _json = to_encodable(
            item={"query": query, "ttl": ttl},
            dump_with=params._SerializerBatchUpdateTtlRequest,
        )
        return await self._base_client.request(
            method="PATCH",
            path="/records",
            service_name="dem",
            json=_json,
            cast_to=str,
            request_options=request_options or default_request_options(),
        )

    async def set_expiry_date(
        self,
        *,
        id: str,
        ttl: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update the expiry of a given record

        Specifies when the record will automatically be deleted from the database. Takes an amount of days as a positive integer of 2 or higher and updates the expiry date with the new value.

        PATCH /records/{id}

        Args:
            id: Unique identifier for a record.
            ttl: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful, no content returned

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.set_expiry_date(
            id="123e4567-e89b-12d3-a456-556642440000", ttl=123
        )
        ```
        """
        _json = to_encodable(
            item={"ttl": ttl}, dump_with=params._SerializerSetExpiryDateRequest
        )
        await self._base_client.request(
            method="PATCH",
            path=f"/records/{id}",
            service_name="dem",
            json=_json,
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def post_new_record(
        self,
        *,
        core_data: typing.Dict[str, typing.Any],
        metadata: typing.Dict[str, typing.Any],
        ttl: int,
        type_: str,
        audit_level: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        relations: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.RecordResponse:
        """
        Create a new record

        Creates a new record. There are four required fields: "type", "metadata", "coreData", "TTL" and two optional fields: "relations" and "auditLevel".<h2>Record Type</h2>You are required to supply a record type in the 'type' parameter when posting a new record.These are the available types: <table>   <tr>       <th>Type name</th>       <th>Description (suggested use)</th>   </tr>   <tr>       <td style='text-align:center;'>GDPR</td>       <td style='text-align:center;'>Can be used for documentation of GDPR compliance.</td>   </tr>   <tr>       <td style='text-align:center;'>TRANSACTION</td>       <td style='text-align:center;'>Can be used for documenting financial transactions.</td>   </tr>   <tr>       <td style='text-align:center;'>LOG_IN</td>       <td style='text-align:center;'>Can be used for documenting users logging in to a system.</td>   </tr>   <tr>       <td style='text-align:center;'>SIGNATURE</td>       <td style='text-align:center;'>Can be used for documenting digital signatures.</td>   </tr>   <tr>       <td style='text-align:center;'>SENSITIVE</td>       <td style='text-align:center;'>Can be used for documenting sensitive information.</td>   </tr>   <tr>       <td style='text-align:center;'>OTHER</td>       <td style='text-align:center;'>Can be used for everything else.</td>   </tr></table><h2>Metadata</h2> Can contain any amount of data which will then be searchable in future queries.<h2>Core Data</h2> Can contain any amount of data which will then be timestamped.<h2>TTL</h2> Time to Live as denoted in amount of days (Int).<h2>Relations</h2> Optional field. List of the IDs (String) of the related records. Default: Empty list<h2>Audit Level</h2> Optional field. Decides which level of timestamping and verification will be applied to the record.<table>   <tr>       <td style='text-align:center;'>SIMPLE</td>       <td style='text-align:center;'>Uses hashing to verify data.</td>   </tr>   <tr>       <td style='text-align:center;'>ADVANCED</td>       <td style='text-align:center;'>Uses TSA to timestamp and verify.</td>   </tr>   <tr>       <td style='text-align:center;'>QUALIFIED</td>       <td style='text-align:center;'>USES QTSA to timestamp and verify. Default if value is not set explicitly</td>   </tr></table>

        POST /records

        Args:
            audit_level: str
            relations: typing.List[str]
            core_data: typing.Dict[str, typing.Any]
            metadata: typing.Dict[str, typing.Any]
            ttl: int
            type_: str
            request_options: Additional options to customize the HTTP request

        Returns:
            Record has been created and posted to the database.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.post_new_record(
            core_data={}, metadata={}, ttl=123, type_="string"
        )
        ```
        """
        _json = to_encodable(
            item={
                "audit_level": audit_level,
                "relations": relations,
                "core_data": core_data,
                "metadata": metadata,
                "ttl": ttl,
                "type_": type_,
            },
            dump_with=params._SerializerRecordRequest,
        )
        return await self._base_client.request(
            method="POST",
            path="/records",
            service_name="dem",
            json=_json,
            cast_to=models.RecordResponse,
            request_options=request_options or default_request_options(),
        )

    async def query(
        self,
        *,
        data: typing.Union[
            typing.Optional[params.QueryRequestBody], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        page: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        size: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Query a collection for records matching specified parameters

        Queries the database to return a pageable list of records without coreData.<br>If no body is included, the endpoint will return pages of all records.<br>The size and page number as well as sorting and ordering of the returned page is decided by the parameters <code>page</code>, <code>size</code> and <code>sort</code>.<br><br><h2>Request Body</h2><br>The query is built from the request body. The request body is an object containing up to two lists of QueryCondition objects.<br><b>If no lists are provided, the query will return every record in the collection.</b><br><br><table style='width:100%'>   <tr>       <th>List name</th>       <th>Description</th>   </tr>   <tr>       <td>and</td>       <td>Combines the QueryConditions with the logical AND operator. All of the QueryConditions need to return true.</td>   </tr>   <tr>       <td>or</td>       <td>Combines the QueryConditions with the logical OR operator. Only one of the QueryConditions needs to return true.</td>   </tr></table><h2>Query Condition</h2><br>A query condition consists of three parts: <b>field</b>, <b>operator</b> and <b>value</b>.<br><h3>Field</h3><br>The field parameter denotes which field in the database to apply the query condition to.<br><i>Replace '*' with the sub-field you wish to query. For example "metadata.firstName" or "systemMetadata.createdDateTime"</i><br><b>These are the allowed fields:</b><br><table style='width:100%'>   <tr>       <th>Field</th>       <th>Description</th>   </tr>   <tr>       <td>metadata</td>       <td>Metadata added by the user.</td>   </tr>   <tr>       <td>systemMetadata</td>       <td>Metadata added by DEM.</td>   </tr>   <tr>       <td>relations</td>       <td>Any other record relations added by the user.</td>   </tr></table><br><h3>Operator</h3><br>The operator specifies how the condition uses the value to search for records.<br><b>These are the available query operators:</b><br><br><table style='width:100%'>   <tr>       <th>Query Operation</th>       <th>Description</th>   </tr>   <tr>       <td>eq</td>       <td>Checks if the field's value matches the input value exactly.</td>   </tr>   <tr>       <td>ne</td>       <td>Checks if the field's value does not match the input value.</td>   </tr>   <tr>       <td>gt</td>       <td>Checks if the field's value is greater than the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>gte</td>       <td>Checks if the field's value is greater than or equal to the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>lt</td>       <td>Checks if the field's value is less than the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>lte</td>       <td>Checks if the field's value is less than or equal to the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>regex</td>       <td>Checks if the field's value contains the input value using regex. Works best with String values.</td>   </tr>   <tr>       <td>in</td>       <td>Checks if the field's value matches any of the values in the inputted array.</td>   </tr>   <tr>       <td>nin</td>       <td>Checks if the field's value does not match any of the values in the inputted array.</td>   </tr></table><br><h3>Value</h3><br>The value parameter denotes what value the query condition should use. For example: with the EQUAL operator, the value is what the field should be equal to.

        POST /records/query

        Args:
            data: An object containing up to three lists of <code>QueryCondition</code> objects. Each list represents a logic operator used to bind the <code>QueryCondition</code> objects into a statement. <br>The <code>'and'</code> list executes the QueryCondition objects with a logical AND operator, all conditions must be met. <br> The <code>'or'</code> list executes the QueryCondition objects with a logical OR operator, at least one of the conditions must be met. <br> The <code>'not'</code> list is currently not in use, but it will in the future execute the QueryCondition objects with a logical NOR operator.
            page: int
            size: int
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful operation

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.dem.query()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(page, type_utils.NotGiven):
            encode_query_param(
                _query,
                "page",
                to_encodable(item=page, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(size, type_utils.NotGiven):
            encode_query_param(
                _query,
                "size",
                to_encodable(item=size, dump_with=int),
                style="form",
                explode=True,
            )
        _json = (
            to_encodable(item=data, dump_with=params._SerializerQueryRequestBody)
            if data
            else None
        )
        return await self._base_client.request(
            method="POST",
            path="/records/query",
            service_name="dem",
            query_params=_query,
            json=_json,
            cast_to=typing.Dict[str, typing.Any],
            request_options=request_options or default_request_options(),
        )
