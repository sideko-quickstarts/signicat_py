
### GET /.ping <a name="signicat"></a>



**API Endpoint**: `GET /.ping`

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.signicat()

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.signicat()

```

### Get statistics for records <a name="get_collection_stats"></a>

Retrieves statistics on records stored in DEM.

**API Endpoint**: `GET /info`

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.get_collection_stats()

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.get_collection_stats()

```

#### Response

##### Type
[Stats](/signicat_dem_py/types/models/stats.py)

##### Example
`{}`

### Get all fields from customerMeta from all records <a name="get_custom_meta_fields_1"></a>

Aggregates all of the customer's records to return a list of all unique keys from the customerMeta field.

**API Endpoint**: `GET /info/custom-fields`

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.get_custom_meta_fields_1()

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.get_custom_meta_fields_1()

```

### Get all fields from customerMeta from all records <a name="get_custom_meta_fields"></a>

Aggregates all of the customer's records to return a list of all unique keys from the customerMeta field.

**API Endpoint**: `GET /info/custom-fields/{type}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `type` | ✓ | Optional parameter that narrows the result down based on the type of record. | `"string"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.get_custom_meta_fields(type_="string")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.get_custom_meta_fields(type_="string")

```

### Get record by ID <a name="get_record_by_id"></a>

Retrieves a specific record by its ID. The given ID must conform to the UUID/GUID standard. <br><em>For example</em>: <code>123e4567-e89b-12d3-a456-556642440000</code><br> Returns everything included in the record entity.

**API Endpoint**: `GET /records/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | Unique identifier for a record. | `"123e4567-e89b-12d3-a456-556642440000"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.get_record_by_id(id="123e4567-e89b-12d3-a456-556642440000")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.get_record_by_id(id="123e4567-e89b-12d3-a456-556642440000")

```

#### Response

##### Type
[RecordResponse](/signicat_dem_py/types/models/record_response.py)

##### Example
`{}`

### Retrieves a generated PDF report for a record <a name="generate_report"></a>

Takes a Record ID as a parameter. It retrieves the record and generates a PDF report for the record.

**API Endpoint**: `GET /reports/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | Unique identifier for a record. | `"123e4567-e89b-12d3-a456-556642440000"` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.generate_report(id="123e4567-e89b-12d3-a456-556642440000")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.generate_report(id="123e4567-e89b-12d3-a456-556642440000")

```

### Update multiple selected records <a name="set_expiry_dates"></a>

Updates the Time to Live (TTL) of selected records by a defined query.<br>The query is built on the MongoDB Query Language (MQL), but it is database-agnostic.<br>

**API Endpoint**: `PATCH /records`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `query` | ✓ |  | `{}` |
| `ttl` | ✓ |  | `123` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.set_expiry_dates(query={}, ttl=123)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.set_expiry_dates(query={}, ttl=123)

```

### Update the expiry of a given record <a name="set_expiry_date"></a>

Specifies when the record will automatically be deleted from the database. Takes an amount of days as a positive integer of 2 or higher and updates the expiry date with the new value.

**API Endpoint**: `PATCH /records/{id}`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `id` | ✓ | Unique identifier for a record. | `"123e4567-e89b-12d3-a456-556642440000"` |
| `ttl` | ✓ |  | `123` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.set_expiry_date(id="123e4567-e89b-12d3-a456-556642440000", ttl=123)

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.set_expiry_date(
    id="123e4567-e89b-12d3-a456-556642440000", ttl=123
)

```

### Create a new record <a name="post_new_record"></a>

Creates a new record. There are four required fields: "type", "metadata", "coreData", "TTL" and two optional fields: "relations" and "auditLevel".<h2>Record Type</h2>You are required to supply a record type in the 'type' parameter when posting a new record.These are the available types: <table>   <tr>       <th>Type name</th>       <th>Description (suggested use)</th>   </tr>   <tr>       <td style='text-align:center;'>GDPR</td>       <td style='text-align:center;'>Can be used for documentation of GDPR compliance.</td>   </tr>   <tr>       <td style='text-align:center;'>TRANSACTION</td>       <td style='text-align:center;'>Can be used for documenting financial transactions.</td>   </tr>   <tr>       <td style='text-align:center;'>LOG_IN</td>       <td style='text-align:center;'>Can be used for documenting users logging in to a system.</td>   </tr>   <tr>       <td style='text-align:center;'>SIGNATURE</td>       <td style='text-align:center;'>Can be used for documenting digital signatures.</td>   </tr>   <tr>       <td style='text-align:center;'>SENSITIVE</td>       <td style='text-align:center;'>Can be used for documenting sensitive information.</td>   </tr>   <tr>       <td style='text-align:center;'>OTHER</td>       <td style='text-align:center;'>Can be used for everything else.</td>   </tr></table><h2>Metadata</h2> Can contain any amount of data which will then be searchable in future queries.<h2>Core Data</h2> Can contain any amount of data which will then be timestamped.<h2>TTL</h2> Time to Live as denoted in amount of days (Int).<h2>Relations</h2> Optional field. List of the IDs (String) of the related records. Default: Empty list<h2>Audit Level</h2> Optional field. Decides which level of timestamping and verification will be applied to the record.<table>   <tr>       <td style='text-align:center;'>SIMPLE</td>       <td style='text-align:center;'>Uses hashing to verify data.</td>   </tr>   <tr>       <td style='text-align:center;'>ADVANCED</td>       <td style='text-align:center;'>Uses TSA to timestamp and verify.</td>   </tr>   <tr>       <td style='text-align:center;'>QUALIFIED</td>       <td style='text-align:center;'>USES QTSA to timestamp and verify. Default if value is not set explicitly</td>   </tr></table>

**API Endpoint**: `POST /records`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `coreData` | ✓ |  | `{}` |
| `metadata` | ✓ |  | `{}` |
| `ttl` | ✓ |  | `123` |
| `type` | ✓ |  | `"string"` |
| `auditLevel` | ✗ |  | `"string"` |
| `relations` | ✗ |  | `["string"]` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.post_new_record(core_data={}, metadata={}, ttl=123, type_="string")

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.post_new_record(
    core_data={}, metadata={}, ttl=123, type_="string"
)

```

#### Response

##### Type
[RecordResponse](/signicat_dem_py/types/models/record_response.py)

##### Example
`{}`

### Query a collection for records matching specified parameters <a name="query"></a>

Queries the database to return a pageable list of records without coreData.<br>If no body is included, the endpoint will return pages of all records.<br>The size and page number as well as sorting and ordering of the returned page is decided by the parameters <code>page</code>, <code>size</code> and <code>sort</code>.<br><br><h2>Request Body</h2><br>The query is built from the request body. The request body is an object containing up to two lists of QueryCondition objects.<br><b>If no lists are provided, the query will return every record in the collection.</b><br><br><table style='width:100%'>   <tr>       <th>List name</th>       <th>Description</th>   </tr>   <tr>       <td>and</td>       <td>Combines the QueryConditions with the logical AND operator. All of the QueryConditions need to return true.</td>   </tr>   <tr>       <td>or</td>       <td>Combines the QueryConditions with the logical OR operator. Only one of the QueryConditions needs to return true.</td>   </tr></table><h2>Query Condition</h2><br>A query condition consists of three parts: <b>field</b>, <b>operator</b> and <b>value</b>.<br><h3>Field</h3><br>The field parameter denotes which field in the database to apply the query condition to.<br><i>Replace '*' with the sub-field you wish to query. For example "metadata.firstName" or "systemMetadata.createdDateTime"</i><br><b>These are the allowed fields:</b><br><table style='width:100%'>   <tr>       <th>Field</th>       <th>Description</th>   </tr>   <tr>       <td>metadata</td>       <td>Metadata added by the user.</td>   </tr>   <tr>       <td>systemMetadata</td>       <td>Metadata added by DEM.</td>   </tr>   <tr>       <td>relations</td>       <td>Any other record relations added by the user.</td>   </tr></table><br><h3>Operator</h3><br>The operator specifies how the condition uses the value to search for records.<br><b>These are the available query operators:</b><br><br><table style='width:100%'>   <tr>       <th>Query Operation</th>       <th>Description</th>   </tr>   <tr>       <td>eq</td>       <td>Checks if the field's value matches the input value exactly.</td>   </tr>   <tr>       <td>ne</td>       <td>Checks if the field's value does not match the input value.</td>   </tr>   <tr>       <td>gt</td>       <td>Checks if the field's value is greater than the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>gte</td>       <td>Checks if the field's value is greater than or equal to the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>lt</td>       <td>Checks if the field's value is less than the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>lte</td>       <td>Checks if the field's value is less than or equal to the input value. Works best with numeric values.</td>   </tr>   <tr>       <td>regex</td>       <td>Checks if the field's value contains the input value using regex. Works best with String values.</td>   </tr>   <tr>       <td>in</td>       <td>Checks if the field's value matches any of the values in the inputted array.</td>   </tr>   <tr>       <td>nin</td>       <td>Checks if the field's value does not match any of the values in the inputted array.</td>   </tr></table><br><h3>Value</h3><br>The value parameter denotes what value the query condition should use. For example: with the EQUAL operator, the value is what the field should be equal to.

**API Endpoint**: `POST /records/query`

#### Parameters

| Parameter | Required | Description | Example |
|-----------|:--------:|-------------|--------|
| `data` | ✗ |  | `{}` |
| `page` | ✗ |  | `123` |
| `size` | ✗ |  | `123` |

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.dem.query()

```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.dem.query()

```
