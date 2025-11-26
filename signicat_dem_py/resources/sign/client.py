import httpx
import typing
import typing_extensions

from make_api_request import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from signicat_dem_py.types import models, params


class SignClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def delete_document_collection(
        self,
        *,
        document_collection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a document collection

        Deletes the document collection with the given ID.

        DELETE /document-collections/{documentCollectionId}

        Args:
            document_collection_id: The unique ID of the document collection.
            request_options: Additional options to customize the HTTP request

        Returns:
            The document collection was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.delete_document_collection(
            document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/document-collections/{document_collection_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def delete_document(
        self,
        *,
        document_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Permanently delete a single document and its metadata



        DELETE /documents/{documentId}

        Args:
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful removal of the document

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.delete_document(document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/documents/{document_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def delete_signing_session(
        self,
        *,
        session_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a signing session

        Deletes the signing session with the given ID.

        DELETE /signing-sessions/{sessionId}

        Args:
            session_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            The signing session was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.delete_signing_session(
            session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        self._base_client.request(
            method="DELETE",
            path=f"/signing-sessions/{session_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    def get_document_collection(
        self,
        *,
        document_collection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DocumentCollection:
        """
        Retrieve a document collection

        Returns the document collection with the given ID.

        GET /document-collections/{documentCollectionId}

        Args:
            document_collection_id: The unique ID of the document collection.
            request_options: Additional options to customize the HTTP request

        Returns:
            The document collection was successfully retrieved.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.get_document_collection(
            document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/document-collections/{document_collection_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=models.DocumentCollection,
            request_options=request_options or default_request_options(),
        )

    def get_document(
        self,
        *,
        document_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Retrieve a single document

        GET /documents/{documentId}

        Args:
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            The binary contents of the stored document

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.get_document(document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/documents/{document_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    def get_document_info(
        self,
        *,
        document_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Document:
        """
        Retrieve all information stored about a single document

        GET /documents/{documentId}/metadata

        Args:
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            All available information except for the document itself was successfully retrieved

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.get_document_info(
            document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/documents/{document_id}/metadata",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )

    def list_signing_sessions(
        self,
        *,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaginatedSigningSessionResponse:
        """
        Retrieve a paginated list of signing sessions

        Returns a paginated list of signing sessions, with optional controls for `offset`, `limit` and `sort`.

        GET /signing-sessions

        Args:
            limit: Maximum number of rows to return.
            offset: Number of rows to skip before returning results.
            sort: Sorting field. Default value is -createdAt. E.g., +dueDate
            request_options: Additional options to customize the HTTP request

        Returns:
            The list of signing sessions was successfully retrieved.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.list_signing_sessions()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(offset, type_utils.NotGiven):
            encode_query_param(
                _query,
                "offset",
                to_encodable(item=offset, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(sort, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sort",
                to_encodable(item=sort, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return self._base_client.request(
            method="GET",
            path="/signing-sessions",
            service_name="sign",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaginatedSigningSessionResponse,
            request_options=request_options or default_request_options(),
        )

    def get_signing_session(
        self,
        *,
        session_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SigningSession:
        """
        Retrieve a signing session

        Returns the signing session with the given ID.

        GET /signing-sessions/{sessionId}

        Args:
            session_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            The signing session was successfully retrieved

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.get_signing_session(
            session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return self._base_client.request(
            method="GET",
            path=f"/signing-sessions/{session_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=models.SigningSession,
            request_options=request_options or default_request_options(),
        )

    def update_document_metadata(
        self,
        *,
        document_id: str,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        document_hash: typing.Union[
            typing.Optional[params.DocumentHash], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        filename: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mime_type: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Document:
        """
        Store optional descriptive data about a stored document

        PATCH /documents/{documentId}/metadata

        Args:
            created_at: str
            description: A description of the document for display purposes. Optional metadata about the stored document which the customer can supply.
            document_hash: DocumentHash
            filename: A name to use if the document is to be stored as a file. Optional metadata about the stored document which the customer can supply.
            mime_type: str
            title: A title of the document for display purposes. Optional metadata about the stored document which the customer can supply.
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful update of optional data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.update_document_metadata(
            document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            created_at="2023-04-12T10:30:00Z",
            description="Invoice for order #001",
            filename="invoice_001.pdf",
            mime_type="application/pdf",
            title="Invoice #001",
        )
        ```
        """
        _json = to_encodable(
            item={
                "created_at": created_at,
                "description": description,
                "document_hash": document_hash,
                "filename": filename,
                "mime_type": mime_type,
                "title": title,
            },
            dump_with=params._SerializerUpdateDocument,
        )
        return self._base_client.request(
            method="PATCH",
            path=f"/documents/{document_id}/metadata",
            service_name="sign",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )

    def create_document_collection(
        self,
        *,
        documents: typing.List[params.DocumentReference],
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        output: typing.Union[
            typing.Optional[params.CollectionOutput], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package_to: typing.Union[
            typing.Optional[typing.List[typing_extensions.Literal["PADES_CONTAINER"]]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DocumentCollection:
        """
        Create a new document collection

        Creates new document collection. A document collection is a logical grouping of documents that will be signed together.

        POST /document-collections

        Args:
            id: The unique ID of the document collection.
            output: CollectionOutput
            package_to: A list of formats the collection should be packaged to when all sessions connected to it are signed.
            documents: typing.List[DocumentReference]
            request_options: Additional options to customize the HTTP request

        Returns:
            The document collection was created.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.create_document_collection(
            documents=[
                {
                    "description": "Terms of Service",
                    "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f",
                }
            ],
            id="f05d0dce-a7af-432b-b6b8-e455ab7c0858",
        )
        ```
        """
        _json = to_encodable(
            item={
                "id": id,
                "output": output,
                "package_to": package_to,
                "documents": documents,
            },
            dump_with=params._SerializerDocumentCollection,
        )
        return self._base_client.request(
            method="POST",
            path="/document-collections",
            service_name="sign",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.DocumentCollection,
            request_options=request_options or default_request_options(),
        )

    def upload_document(
        self,
        *,
        content_type: str,
        data: httpx._types.FileTypes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostDocumentResponse:
        """
        Upload a new document

        Uploads the document as a binary stream; MIME type is defined by the
        Content-Type header. The response will be the resulting document reference.


        POST /documents

        Args:
            content_type: Content type header
            data: httpx._types.FileTypes
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful upload, returns new document ID

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.upload_document(
            content_type="string", data=open("uploads/file.pdf", "rb")
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Content-Type"] = str(content_type)
        _content = data
        _content_type = "text/plain"
        return self._base_client.request(
            method="POST",
            path="/documents",
            service_name="sign",
            auth_names=["bearerAuth"],
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.PostDocumentResponse,
            request_options=request_options or default_request_options(),
        )

    def create_signing_session(
        self,
        *,
        data: typing.List[params.SigningSession],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.SigningSession]:
        """
        Create a new signing session

        Creates a new signing session.

        POST /signing-sessions

        Args:
            data: typing.List[SigningSession]
            request_options: Additional options to customize the HTTP request

        Returns:
            The signing session was created.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.sign.create_signing_session(
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
                    "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0852",
                    "sender_display_name": "Corporation incorporated",
                    "sign_text": "Please sign this document",
                    "signature_url": "https://signtest-account.sandbox.signicat.com/sign/?sessionId=8ce3dac2-74b3-429c-adf7-fe6d277186d0",
                    "signing_setup": [
                        {
                            "additional_parameters": {
                                "sbid_end_user_ip": "127.0.0.1",
                                "sbid_flow": "QR",
                            },
                            "identity_providers": [{"idp_name": "string"}],
                            "signing_flow": "AUTHENTICATION_BASED",
                        }
                    ],
                    "title": "Business Process",
                }
            ]
        )
        ```
        """
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerSigningSession]
        )
        return self._base_client.request(
            method="POST",
            path="/signing-sessions",
            service_name="sign",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=typing.List[models.SigningSession],
            request_options=request_options or default_request_options(),
        )


class AsyncSignClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def delete_document_collection(
        self,
        *,
        document_collection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a document collection

        Deletes the document collection with the given ID.

        DELETE /document-collections/{documentCollectionId}

        Args:
            document_collection_id: The unique ID of the document collection.
            request_options: Additional options to customize the HTTP request

        Returns:
            The document collection was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.delete_document_collection(
            document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/document-collections/{document_collection_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def delete_document(
        self,
        *,
        document_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Permanently delete a single document and its metadata



        DELETE /documents/{documentId}

        Args:
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful removal of the document

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.delete_document(
            document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/documents/{document_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def delete_signing_session(
        self,
        *,
        session_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Delete a signing session

        Deletes the signing session with the given ID.

        DELETE /signing-sessions/{sessionId}

        Args:
            session_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            The signing session was successfully deleted

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.delete_signing_session(
            session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        await self._base_client.request(
            method="DELETE",
            path=f"/signing-sessions/{session_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=type(None),
            request_options=request_options or default_request_options(),
        )

    async def get_document_collection(
        self,
        *,
        document_collection_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DocumentCollection:
        """
        Retrieve a document collection

        Returns the document collection with the given ID.

        GET /document-collections/{documentCollectionId}

        Args:
            document_collection_id: The unique ID of the document collection.
            request_options: Additional options to customize the HTTP request

        Returns:
            The document collection was successfully retrieved.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.get_document_collection(
            document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/document-collections/{document_collection_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=models.DocumentCollection,
            request_options=request_options or default_request_options(),
        )

    async def get_document(
        self,
        *,
        document_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> httpx.Response:
        """
        Retrieve a single document

        GET /documents/{documentId}

        Args:
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            The binary contents of the stored document

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.get_document(
            document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/documents/{document_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=httpx.Response,
            request_options=request_options or default_request_options(),
        )

    async def get_document_info(
        self,
        *,
        document_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Document:
        """
        Retrieve all information stored about a single document

        GET /documents/{documentId}/metadata

        Args:
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            All available information except for the document itself was successfully retrieved

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.get_document_info(
            document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/documents/{document_id}/metadata",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )

    async def list_signing_sessions(
        self,
        *,
        limit: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        offset: typing.Union[
            typing.Optional[int], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        sort: typing.Union[
            typing.Optional[typing.List[str]], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PaginatedSigningSessionResponse:
        """
        Retrieve a paginated list of signing sessions

        Returns a paginated list of signing sessions, with optional controls for `offset`, `limit` and `sort`.

        GET /signing-sessions

        Args:
            limit: Maximum number of rows to return.
            offset: Number of rows to skip before returning results.
            sort: Sorting field. Default value is -createdAt. E.g., +dueDate
            request_options: Additional options to customize the HTTP request

        Returns:
            The list of signing sessions was successfully retrieved.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.list_signing_sessions()
        ```
        """
        _query: QueryParams = {}
        if not isinstance(limit, type_utils.NotGiven):
            encode_query_param(
                _query,
                "limit",
                to_encodable(item=limit, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(offset, type_utils.NotGiven):
            encode_query_param(
                _query,
                "offset",
                to_encodable(item=offset, dump_with=int),
                style="form",
                explode=True,
            )
        if not isinstance(sort, type_utils.NotGiven):
            encode_query_param(
                _query,
                "sort",
                to_encodable(item=sort, dump_with=typing.List[str]),
                style="form",
                explode=True,
            )
        return await self._base_client.request(
            method="GET",
            path="/signing-sessions",
            service_name="sign",
            auth_names=["bearerAuth"],
            query_params=_query,
            cast_to=models.PaginatedSigningSessionResponse,
            request_options=request_options or default_request_options(),
        )

    async def get_signing_session(
        self,
        *,
        session_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.SigningSession:
        """
        Retrieve a signing session

        Returns the signing session with the given ID.

        GET /signing-sessions/{sessionId}

        Args:
            session_id: str
            request_options: Additional options to customize the HTTP request

        Returns:
            The signing session was successfully retrieved

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.get_signing_session(
            session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
        )
        ```
        """
        return await self._base_client.request(
            method="GET",
            path=f"/signing-sessions/{session_id}",
            service_name="sign",
            auth_names=["bearerAuth"],
            cast_to=models.SigningSession,
            request_options=request_options or default_request_options(),
        )

    async def update_document_metadata(
        self,
        *,
        document_id: str,
        created_at: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        description: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        document_hash: typing.Union[
            typing.Optional[params.DocumentHash], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        filename: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        mime_type: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        title: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.Document:
        """
        Store optional descriptive data about a stored document

        PATCH /documents/{documentId}/metadata

        Args:
            created_at: str
            description: A description of the document for display purposes. Optional metadata about the stored document which the customer can supply.
            document_hash: DocumentHash
            filename: A name to use if the document is to be stored as a file. Optional metadata about the stored document which the customer can supply.
            mime_type: str
            title: A title of the document for display purposes. Optional metadata about the stored document which the customer can supply.
            document_id: Document ID parameter
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful update of optional data

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.update_document_metadata(
            document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
            created_at="2023-04-12T10:30:00Z",
            description="Invoice for order #001",
            filename="invoice_001.pdf",
            mime_type="application/pdf",
            title="Invoice #001",
        )
        ```
        """
        _json = to_encodable(
            item={
                "created_at": created_at,
                "description": description,
                "document_hash": document_hash,
                "filename": filename,
                "mime_type": mime_type,
                "title": title,
            },
            dump_with=params._SerializerUpdateDocument,
        )
        return await self._base_client.request(
            method="PATCH",
            path=f"/documents/{document_id}/metadata",
            service_name="sign",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.Document,
            request_options=request_options or default_request_options(),
        )

    async def create_document_collection(
        self,
        *,
        documents: typing.List[params.DocumentReference],
        id: typing.Union[
            typing.Optional[str], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        output: typing.Union[
            typing.Optional[params.CollectionOutput], type_utils.NotGiven
        ] = type_utils.NOT_GIVEN,
        package_to: typing.Union[
            typing.Optional[typing.List[typing_extensions.Literal["PADES_CONTAINER"]]],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.DocumentCollection:
        """
        Create a new document collection

        Creates new document collection. A document collection is a logical grouping of documents that will be signed together.

        POST /document-collections

        Args:
            id: The unique ID of the document collection.
            output: CollectionOutput
            package_to: A list of formats the collection should be packaged to when all sessions connected to it are signed.
            documents: typing.List[DocumentReference]
            request_options: Additional options to customize the HTTP request

        Returns:
            The document collection was created.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.create_document_collection(
            documents=[
                {
                    "description": "Terms of Service",
                    "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f",
                }
            ],
            id="f05d0dce-a7af-432b-b6b8-e455ab7c0858",
        )
        ```
        """
        _json = to_encodable(
            item={
                "id": id,
                "output": output,
                "package_to": package_to,
                "documents": documents,
            },
            dump_with=params._SerializerDocumentCollection,
        )
        return await self._base_client.request(
            method="POST",
            path="/document-collections",
            service_name="sign",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=models.DocumentCollection,
            request_options=request_options or default_request_options(),
        )

    async def upload_document(
        self,
        *,
        content_type: str,
        data: httpx._types.FileTypes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.PostDocumentResponse:
        """
        Upload a new document

        Uploads the document as a binary stream; MIME type is defined by the
        Content-Type header. The response will be the resulting document reference.


        POST /documents

        Args:
            content_type: Content type header
            data: httpx._types.FileTypes
            request_options: Additional options to customize the HTTP request

        Returns:
            Successful upload, returns new document ID

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.upload_document(
            content_type="string", data=open("uploads/file.pdf", "rb")
        )
        ```
        """
        _header: typing.Dict[str, str] = {}
        _header["Content-Type"] = str(content_type)
        _content = data
        _content_type = "text/plain"
        return await self._base_client.request(
            method="POST",
            path="/documents",
            service_name="sign",
            auth_names=["bearerAuth"],
            headers=_header,
            content=_content,
            content_type=_content_type,
            cast_to=models.PostDocumentResponse,
            request_options=request_options or default_request_options(),
        )

    async def create_signing_session(
        self,
        *,
        data: typing.List[params.SigningSession],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[models.SigningSession]:
        """
        Create a new signing session

        Creates a new signing session.

        POST /signing-sessions

        Args:
            data: typing.List[SigningSession]
            request_options: Additional options to customize the HTTP request

        Returns:
            The signing session was created.

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.sign.create_signing_session(
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
                    "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0852",
                    "sender_display_name": "Corporation incorporated",
                    "sign_text": "Please sign this document",
                    "signature_url": "https://signtest-account.sandbox.signicat.com/sign/?sessionId=8ce3dac2-74b3-429c-adf7-fe6d277186d0",
                    "signing_setup": [
                        {
                            "additional_parameters": {
                                "sbid_end_user_ip": "127.0.0.1",
                                "sbid_flow": "QR",
                            },
                            "identity_providers": [{"idp_name": "string"}],
                            "signing_flow": "AUTHENTICATION_BASED",
                        }
                    ],
                    "title": "Business Process",
                }
            ]
        )
        ```
        """
        _json = to_encodable(
            item=data, dump_with=typing.List[params._SerializerSigningSession]
        )
        return await self._base_client.request(
            method="POST",
            path="/signing-sessions",
            service_name="sign",
            auth_names=["bearerAuth"],
            json=_json,
            cast_to=typing.List[models.SigningSession],
            request_options=request_options or default_request_options(),
        )
