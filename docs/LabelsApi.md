# swagger_client.LabelsApi

All URIs are relative to _/_

| Method                                                              | HTTP request                                                              | Description |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------- | ----------- |
| [**add_label**](LabelsApi.md#add_label)                             | **POST** /api/v2/labels/{ownerType}/{ownerId}                             |
| [**delete_label**](LabelsApi.md#delete_label)                       | **DELETE** /api/v2/labels/{ownerType}/{ownerId}/{labelId}                 |
| [**get_applicable_contexts**](LabelsApi.md#get_applicable_contexts) | **GET** /api/v2/labels/{ownerType}/{ownerId}/applicable/context/{labelId} |
| [**get_applicable_labels**](LabelsApi.md#get_applicable_labels)     | **GET** /api/v2/labels/{ownerType}/{ownerId}/applicable                   |
| [**get_labels**](LabelsApi.md#get_labels)                           | **GET** /api/v2/labels/{ownerType}/{ownerId}                              |
| [**update_label**](LabelsApi.md#update_label)                       | **PUT** /api/v2/labels/{ownerType}/{ownerId}                              |

# **add_label**

> ApiLabelDTO add_label(owner_type, owner_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LabelsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
body = swagger_client.ApiLabelDTO() # ApiLabelDTO |  (optional)

try:
    api_response = api_instance.add_label(owner_type, owner_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->add_label: %s\n" % e)
```

### Parameters

| Name           | Type                              | Description | Notes      |
| -------------- | --------------------------------- | ----------- | ---------- |
| **owner_type** | **str**                           |             |
| **owner_id**   | **str**                           |             |
| **body**       | [**ApiLabelDTO**](ApiLabelDTO.md) |             | [optional] |

### Return type

[**ApiLabelDTO**](ApiLabelDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_label**

> delete_label(owner_type, owner_id, label_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LabelsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
label_id = 'label_id_example' # str |

try:
    api_instance.delete_label(owner_type, owner_id, label_id)
except ApiException as e:
    print("Exception when calling LabelsApi->delete_label: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
| -------------- | ------- | ----------- | ----- |
| **owner_type** | **str** |             |
| **owner_id**   | **str** |             |
| **label_id**   | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicable_contexts**

> ApplicableContext get_applicable_contexts(owner_type, owner_id, label_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LabelsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
label_id = 'label_id_example' # str |

try:
    api_response = api_instance.get_applicable_contexts(owner_type, owner_id, label_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_applicable_contexts: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
| -------------- | ------- | ----------- | ----- |
| **owner_type** | **str** |             |
| **owner_id**   | **str** |             |
| **label_id**   | **str** |             |

### Return type

[**ApplicableContext**](ApplicableContext.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicable_labels**

> ApplicableLabels get_applicable_labels(owner_type, owner_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LabelsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |

try:
    api_response = api_instance.get_applicable_labels(owner_type, owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_applicable_labels: %s\n" % e)
```

### Parameters

| Name           | Type    | Description | Notes |
| -------------- | ------- | ----------- | ----- |
| **owner_type** | **str** |             |
| **owner_id**   | **str** |             |

### Return type

[**ApplicableLabels**](ApplicableLabels.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_labels**

> list[ApiLabelDTO] get_labels(owner_type, owner_id, inherit=inherit)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LabelsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
inherit = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_labels(owner_type, owner_id, inherit=inherit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_labels: %s\n" % e)
```

### Parameters

| Name           | Type     | Description | Notes                         |
| -------------- | -------- | ----------- | ----------------------------- |
| **owner_type** | **str**  |             |
| **owner_id**   | **str**  |             |
| **inherit**    | **bool** |             | [optional] [default to false] |

### Return type

[**list[ApiLabelDTO]**](ApiLabelDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_label**

> ApiLabelDTO update_label(owner_type, owner_id, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LabelsApi()
owner_type = 'owner_type_example' # str |
owner_id = 'owner_id_example' # str |
body = swagger_client.ApiLabelDTO() # ApiLabelDTO |  (optional)

try:
    api_response = api_instance.update_label(owner_type, owner_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->update_label: %s\n" % e)
```

### Parameters

| Name           | Type                              | Description | Notes      |
| -------------- | --------------------------------- | ----------- | ---------- |
| **owner_type** | **str**                           |             |
| **owner_id**   | **str**                           |             |
| **body**       | [**ApiLabelDTO**](ApiLabelDTO.md) |             | [optional] |

### Return type

[**ApiLabelDTO**](ApiLabelDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
