
### Delete a document collection <a name="delete_document_collection"></a>

Deletes the document collection with the given ID.

**API Endpoint**: `DELETE /document-collections/{documentCollectionId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `documentCollectionId` | ✓ | The unique ID of the document collection. | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.delete_document_collection(
    document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.delete_document_collection(
    document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

### Permanently delete a single document and its metadata <a name="delete_document"></a>



**API Endpoint**: `DELETE /documents/{documentId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `documentId` | ✓ | Document ID parameter | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.delete_document(document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.delete_document(
    document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

### Delete a signing session <a name="delete_signing_session"></a>

Deletes the signing session with the given ID.

**API Endpoint**: `DELETE /signing-sessions/{sessionId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `sessionId` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.delete_signing_session(
    session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.delete_signing_session(
    session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

### Retrieve a document collection <a name="get_document_collection"></a>

Returns the document collection with the given ID.

**API Endpoint**: `GET /document-collections/{documentCollectionId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `documentCollectionId` | ✓ | The unique ID of the document collection. | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.get_document_collection(
    document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.get_document_collection(
    document_collection_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Response

##### Type
[DocumentCollection](/signicat_dem_py/types/models/document_collection.py)

##### Example
`{"documents": [{"description": "Terms of Service", "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f"}], "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0858"}`

### Retrieve a single document <a name="get_document"></a>



**API Endpoint**: `GET /documents/{documentId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `documentId` | ✓ | Document ID parameter | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.get_document(document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.get_document(document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

### Retrieve all information stored about a single document <a name="get_document_info"></a>



**API Endpoint**: `GET /documents/{documentId}/metadata`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `documentId` | ✓ | Document ID parameter | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.get_document_info(document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.get_document_info(
    document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Response

##### Type
[Document](/signicat_dem_py/types/models/document.py)

##### Example
`{"created_at": "2023-04-12T10:30:00Z", "description": "Invoice for order #001", "document_id": "d1234567-89ab-cdef-0123-456789abcdef", "filename": "invoice_001.pdf", "mime_type": "application/pdf", "title": "Invoice #001"}`

### Retrieve a paginated list of signing sessions <a name="list_signing_sessions"></a>

Returns a paginated list of signing sessions, with optional controls for `offset`, `limit` and `sort`.

**API Endpoint**: `GET /signing-sessions`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `limit` | ✗ | Maximum number of rows to return. | `123` |
| `offset` | ✗ | Number of rows to skip before returning results. | `123` |
| `sort` | ✗ | Sorting field. Default value is -createdAt. E.g., +dueDate | `["string"]` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.list_signing_sessions()

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.list_signing_sessions()

```

#### Response

##### Type
[PaginatedSigningSessionResponse](/signicat_dem_py/types/models/paginated_signing_session_response.py)

##### Example
`{"count": 100, "limit": 100, "offset": 0, "total": 1000}`

### Retrieve a signing session <a name="get_signing_session"></a>

Returns the signing session with the given ID.

**API Endpoint**: `GET /signing-sessions/{sessionId}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `sessionId` | ✓ |  | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.get_signing_session(session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.get_signing_session(
    session_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"
)

```

#### Response

##### Type
[SigningSession](/signicat_dem_py/types/models/signing_session.py)

##### Example
`{"documents": [{"action": "SIGN", "document_collection_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0853", "document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0857"}], "due_date": "2025-04-01T17:32:28Z", "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0852", "sender_display_name": "Corporation incorporated", "sign_text": "Please sign this document", "signature_url": "https://signtest-account.sandbox.signicat.com/sign/?sessionId=8ce3dac2-74b3-429c-adf7-fe6d277186d0", "signing_setup": [{"additional_parameters": {}, "identity_providers": [{"idp_name": "string"}], "signing_flow": "AUTHENTICATION_BASED"}], "title": "Business Process"}`

### Store optional descriptive data about a stored document <a name="update_document_metadata"></a>



**API Endpoint**: `PATCH /documents/{documentId}/metadata`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `documentId` | ✓ | Document ID parameter | `"3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a"` |
| `createdAt` | ✗ |  | `"2023-04-12T10:30:00Z"` |
| `description` | ✗ | A description of the document for display purposes. Optional metadata about the stored document which the customer can supply. | `"Invoice for order #001"` |
| `documentHash` | ✗ |  | `{"hash_algorithm": "SHA256"}` |
| `filename` | ✗ | A name to use if the document is to be stored as a file. Optional metadata about the stored document which the customer can supply. | `"invoice_001.pdf"` |
| `mimeType` | ✗ |  | `"application/pdf"` |
| `title` | ✗ | A title of the document for display purposes. Optional metadata about the stored document which the customer can supply. | `"Invoice #001"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.update_document_metadata(
    document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    created_at="2023-04-12T10:30:00Z",
    description="Invoice for order #001",
    filename="invoice_001.pdf",
    mime_type="application/pdf",
    title="Invoice #001",
)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.update_document_metadata(
    document_id="3e4666bf-d5e5-4aa7-b8ce-cefe41c7568a",
    created_at="2023-04-12T10:30:00Z",
    description="Invoice for order #001",
    filename="invoice_001.pdf",
    mime_type="application/pdf",
    title="Invoice #001",
)

```

#### Response

##### Type
[Document](/signicat_dem_py/types/models/document.py)

##### Example
`{"created_at": "2023-04-12T10:30:00Z", "description": "Invoice for order #001", "document_id": "d1234567-89ab-cdef-0123-456789abcdef", "filename": "invoice_001.pdf", "mime_type": "application/pdf", "title": "Invoice #001"}`

### Create a new document collection <a name="create_document_collection"></a>

Creates new document collection. A document collection is a logical grouping of documents that will be signed together.

**API Endpoint**: `POST /document-collections`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `documents` | ✓ |  | `[{"description": "Terms of Service", "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f"}]` |
| `id` | ✗ | The unique ID of the document collection. | `"f05d0dce-a7af-432b-b6b8-e455ab7c0858"` |
| `output` | ✗ |  | `{}` |
| `packageTo` | ✗ | A list of formats the collection should be packaged to when all sessions connected to it are signed. | `["PADES_CONTAINER"]` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.create_document_collection(
    documents=[
        {
            "description": "Terms of Service",
            "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f",
        }
    ],
    id="f05d0dce-a7af-432b-b6b8-e455ab7c0858",
)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.create_document_collection(
    documents=[
        {
            "description": "Terms of Service",
            "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f",
        }
    ],
    id="f05d0dce-a7af-432b-b6b8-e455ab7c0858",
)

```

#### Response

##### Type
[DocumentCollection](/signicat_dem_py/types/models/document_collection.py)

##### Example
`{"documents": [{"description": "Terms of Service", "document_id": "15197b79-6333-4fa5-9e4c-23b9392a838f"}], "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0858"}`

### Upload a new document <a name="upload_document"></a>

Uploads the document as a binary stream; MIME type is defined by the
Content-Type header. The response will be the resulting document reference.


**API Endpoint**: `POST /documents`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `Content-Type` | ✓ | Content type header | `"string"` |
| `data` | ✓ |  | `open("uploads/file.pdf", "rb")` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.upload_document(
    content_type="string", data=open("uploads/file.pdf", "rb")
)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.upload_document(
    content_type="string", data=open("uploads/file.pdf", "rb")
)

```

#### Response

##### Type
[PostDocumentResponse](/signicat_dem_py/types/models/post_document_response.py)

##### Example
`{"created_at": "2023-04-12T10:30:00Z", "document_id": "d1234567-89ab-cdef-0123-456789abcdef", "mime_type": "application/pdf"}`

### Create a new signing session <a name="create_signing_session"></a>

Creates a new signing session.

**API Endpoint**: `POST /signing-sessions`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✓ |  | `[{"documents": [{"action": "SIGN", "document_collection_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0853", "document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0857"}], "due_date": "2025-04-01T17:32:28Z", "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0852", "sender_display_name": "Corporation incorporated", "sign_text": "Please sign this document", "signature_url": "https://signtest-account.sandbox.signicat.com/sign/?sessionId=8ce3dac2-74b3-429c-adf7-fe6d277186d0", "signing_setup": [{"additional_parameters": {}, "identity_providers": [{"idp_name": "string"}], "signing_flow": "AUTHENTICATION_BASED"}], "title": "Business Process"}]` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.sign.create_signing_session(
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
                    "additional_parameters": {},
                    "identity_providers": [{"idp_name": "string"}],
                    "signing_flow": "AUTHENTICATION_BASED",
                }
            ],
            "title": "Business Process",
        }
    ]
)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.sign.create_signing_session(
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
                    "additional_parameters": {},
                    "identity_providers": [{"idp_name": "string"}],
                    "signing_flow": "AUTHENTICATION_BASED",
                }
            ],
            "title": "Business Process",
        }
    ]
)

```

#### Response

##### Type
List of [SigningSession](/signicat_dem_py/types/models/signing_session.py)

##### Example
`[{"documents": [{"action": "SIGN", "document_collection_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0853", "document_id": "f05d0dce-a7af-432b-b6b8-e455ab7c0857"}], "due_date": "2025-04-01T17:32:28Z", "id": "f05d0dce-a7af-432b-b6b8-e455ab7c0852", "sender_display_name": "Corporation incorporated", "sign_text": "Please sign this document", "signature_url": "https://signtest-account.sandbox.signicat.com/sign/?sessionId=8ce3dac2-74b3-429c-adf7-fe6d277186d0", "signing_setup": [{"additional_parameters": {}, "identity_providers": [{"idp_name": "string"}], "signing_flow": "AUTHENTICATION_BASED"}], "title": "Business Process"}]`
