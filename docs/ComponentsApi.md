# swagger_client.ComponentsApi

All URIs are relative to _/_

| Method                                                                                                  | HTTP request                                                                                    | Description |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------- |
| [**delete_component_label**](ComponentsApi.md#delete_component_label)                                   | **DELETE** /api/v2/components/{componentHash}/labels/{labelName}/{ownerType}s/{internalOwnerId} |
| [**get_component_details**](ComponentsApi.md#get_component_details)                                     | **POST** /api/v2/components/details                                                             |
| [**get_component_versions**](ComponentsApi.md#get_component_versions)                                   | **POST** /api/v2/components/versions                                                            |
| [**get_suggested_remediation_for_component**](ComponentsApi.md#get_suggested_remediation_for_component) | **POST** /api/v2/components/remediation/{ownerType}/{ownerId}                                   |
| [**set_component_label**](ComponentsApi.md#set_component_label)                                         | **POST** /api/v2/components/{componentHash}/labels/{labelName}/{ownerType}s/{internalOwnerId}   |

# **delete_component_label**

> delete_component_label(owner_type, internal_owner_id, component_hash, label_name)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
owner_type = 'owner_type_example' # str |
internal_owner_id = 'internal_owner_id_example' # str |
component_hash = 'component_hash_example' # str |
label_name = 'label_name_example' # str |

try:
    api_instance.delete_component_label(owner_type, internal_owner_id, component_hash, label_name)
except ApiException as e:
    print("Exception when calling ComponentsApi->delete_component_label: %s\n" % e)
```

### Parameters

| Name                  | Type    | Description | Notes |
| --------------------- | ------- | ----------- | ----- |
| **owner_type**        | **str** |             |
| **internal_owner_id** | **str** |             |
| **component_hash**    | **str** |             |
| **label_name**        | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_details**

> ApiComponentDetailsResultDTOV2 get_component_details(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
body = swagger_client.ApiComponentDetailsRequestDTOV2() # ApiComponentDetailsRequestDTOV2 |  (optional)

try:
    api_response = api_instance.get_component_details(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_component_details: %s\n" % e)
```

### Parameters

| Name     | Type                                                                      | Description | Notes      |
| -------- | ------------------------------------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiComponentDetailsRequestDTOV2**](ApiComponentDetailsRequestDTOV2.md) |             | [optional] |

### Return type

[**ApiComponentDetailsResultDTOV2**](ApiComponentDetailsResultDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_versions**

> list[str] get_component_versions(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
body = swagger_client.ApiComponentOrPurlIdentifierDTOV2() # ApiComponentOrPurlIdentifierDTOV2 |  (optional)

try:
    api_response = api_instance.get_component_versions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_component_versions: %s\n" % e)
```

### Parameters

| Name     | Type                                                                          | Description | Notes      |
| -------- | ----------------------------------------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiComponentOrPurlIdentifierDTOV2**](ApiComponentOrPurlIdentifierDTOV2.md) |             | [optional] |

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_suggested_remediation_for_component**

> ApiComponentRemediationDTO get_suggested_remediation_for_component(owner_type, owner_id, body=body, stage_id=stage_id, identification_source=identification_source, scan_id=scan_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
body = swagger_client.ApiComponentDTOV2() # ApiComponentDTOV2 |  (optional)
stage_id = 'stage_id_example' # str |  (optional)
identification_source = 'identification_source_example' # str |  (optional)
scan_id = 'scan_id_example' # str |  (optional)

try:
    api_response = api_instance.get_suggested_remediation_for_component(owner_type, owner_id, body=body, stage_id=stage_id, identification_source=identification_source, scan_id=scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentsApi->get_suggested_remediation_for_component: %s\n" % e)
```

### Parameters

| Name                      | Type                                          | Description | Notes      |
| ------------------------- | --------------------------------------------- | ----------- | ---------- |
| **owner_type**            | **str**                                       |             |
| **owner_id**              | **str**                                       |             |
| **body**                  | [**ApiComponentDTOV2**](ApiComponentDTOV2.md) |             | [optional] |
| **stage_id**              | **str**                                       |             | [optional] |
| **identification_source** | **str**                                       |             | [optional] |
| **scan_id**               | **str**                                       |             | [optional] |

### Return type

[**ApiComponentRemediationDTO**](ApiComponentRemediationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_component_label**

> set_component_label(owner_type, internal_owner_id, component_hash, label_name)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ComponentsApi()
owner_type = 'owner_type_example' # str |
internal_owner_id = 'internal_owner_id_example' # str |
component_hash = 'component_hash_example' # str |
label_name = 'label_name_example' # str |

try:
    api_instance.set_component_label(owner_type, internal_owner_id, component_hash, label_name)
except ApiException as e:
    print("Exception when calling ComponentsApi->set_component_label: %s\n" % e)
```

### Parameters

| Name                  | Type    | Description | Notes |
| --------------------- | ------- | ----------- | ----- |
| **owner_type**        | **str** |             |
| **internal_owner_id** | **str** |             |
| **component_hash**    | **str** |             |
| **label_name**        | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
