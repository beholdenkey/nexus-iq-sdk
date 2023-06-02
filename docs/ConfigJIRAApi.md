# swagger_client.ConfigJIRAApi

All URIs are relative to _/_

| Method                                                              | HTTP request                   | Description |
| ------------------------------------------------------------------- | ------------------------------ | ----------- |
| [**delete_configuration1**](ConfigJIRAApi.md#delete_configuration1) | **DELETE** /api/v2/config/jira |
| [**get_configuration1**](ConfigJIRAApi.md#get_configuration1)       | **GET** /api/v2/config/jira    |
| [**set_configuration1**](ConfigJIRAApi.md#set_configuration1)       | **PUT** /api/v2/config/jira    |

# **delete_configuration1**

> delete_configuration1()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigJIRAApi()

try:
    api_instance.delete_configuration1()
except ApiException as e:
    print("Exception when calling ConfigJIRAApi->delete_configuration1: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration1**

> ApiJiraConfigurationDTO get_configuration1()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigJIRAApi()

try:
    api_response = api_instance.get_configuration1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigJIRAApi->get_configuration1: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiJiraConfigurationDTO**](ApiJiraConfigurationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration1**

> set_configuration1(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigJIRAApi()
body = swagger_client.JsonNode() # JsonNode |  (optional)

try:
    api_instance.set_configuration1(body=body)
except ApiException as e:
    print("Exception when calling ConfigJIRAApi->set_configuration1: %s\n" % e)
```

### Parameters

| Name     | Type                        | Description | Notes      |
| -------- | --------------------------- | ----------- | ---------- |
| **body** | [**JsonNode**](JsonNode.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
