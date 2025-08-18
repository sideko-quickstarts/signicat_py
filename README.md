
# Signicat API Demo Python SDK

#### Synchronous Client

```python
from os import getenv
from signicat_dem_py import Client

client = Client(token=getenv("API_TOKEN"))
```

#### Asynchronous Client

```python
from os import getenv
from signicat_dem_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
```

## Module Documentation and Snippets

### [dem](signicat_dem_py/resources/dem/README.md)

* [generate_report](signicat_dem_py/resources/dem/README.md#generate_report) - Retrieves a generated PDF report for a record
* [get_collection_stats](signicat_dem_py/resources/dem/README.md#get_collection_stats) - Get statistics for records
* [get_custom_meta_fields](signicat_dem_py/resources/dem/README.md#get_custom_meta_fields) - Get all fields from customerMeta from all records
* [get_custom_meta_fields_1](signicat_dem_py/resources/dem/README.md#get_custom_meta_fields_1) - Get all fields from customerMeta from all records
* [get_record_by_id](signicat_dem_py/resources/dem/README.md#get_record_by_id) - Get record by ID
* [post_new_record](signicat_dem_py/resources/dem/README.md#post_new_record) - Create a new record
* [query](signicat_dem_py/resources/dem/README.md#query) - Query a collection for records matching specified parameters
* [set_expiry_date](signicat_dem_py/resources/dem/README.md#set_expiry_date) - Update the expiry of a given record
* [set_expiry_dates](signicat_dem_py/resources/dem/README.md#set_expiry_dates) - Update multiple selected records
* [signicat](signicat_dem_py/resources/dem/README.md#signicat) - GET /.ping

### [sign](signicat_dem_py/resources/sign/README.md)

* [create_document_collection](signicat_dem_py/resources/sign/README.md#create_document_collection) - Create a new document collection
* [create_signing_session](signicat_dem_py/resources/sign/README.md#create_signing_session) - Create a new signing session
* [delete_document](signicat_dem_py/resources/sign/README.md#delete_document) - Permanently delete a single document and its metadata
* [delete_document_collection](signicat_dem_py/resources/sign/README.md#delete_document_collection) - Delete a document collection
* [delete_signing_session](signicat_dem_py/resources/sign/README.md#delete_signing_session) - Delete a signing session
* [get_document](signicat_dem_py/resources/sign/README.md#get_document) - Retrieve a single document
* [get_document_collection](signicat_dem_py/resources/sign/README.md#get_document_collection) - Retrieve a document collection
* [get_document_info](signicat_dem_py/resources/sign/README.md#get_document_info) - Retrieve all information stored about a single document
* [get_signing_session](signicat_dem_py/resources/sign/README.md#get_signing_session) - Retrieve a signing session
* [list_signing_sessions](signicat_dem_py/resources/sign/README.md#list_signing_sessions) - Retrieve a paginated list of signing sessions
* [update_document_metadata](signicat_dem_py/resources/sign/README.md#update_document_metadata) - Store optional descriptive data about a stored document
* [upload_document](signicat_dem_py/resources/sign/README.md#upload_document) - Upload a new document

<!-- MODULE DOCS END -->
