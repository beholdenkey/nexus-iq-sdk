# swagger_client.ConfigCrowdApi

All URIs are relative to _/_

| Method                                                                                             | HTTP request                       | Description |
| -------------------------------------------------------------------------------------------------- | ---------------------------------- | ----------- |
| [**delete_crowd_configuration**](ConfigCrowdApi.md#delete_crowd_configuration)                     | **DELETE** /api/v2/config/crowd    |
| [**get_crowd_configuration**](ConfigCrowdApi.md#get_crowd_configuration)                           | **GET** /api/v2/config/crowd       |
| [**insert_or_update_crowd_configuration**](ConfigCrowdApi.md#insert_or_update_crowd_configuration) | **PUT** /api/v2/config/crowd       |
| [**test_crowd_configuration**](ConfigCrowdApi.md#test_crowd_configuration)                         | **POST** /api/v2/config/crowd/test |

# **delete_crowd_configuration**

> delete_crowd_configuration()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigCrowdApi()

try:
    api_instance.delete_crowd_configuration()
except ApiException as e:
    print("Exception when calling ConfigCrowdApi->delete_crowd_configuration: %s\n" % e)
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

# **get_crowd_configuration**

> ApiCrowdConfigurationDTO get_crowd_configuration()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigCrowdApi()

try:
    api_response = api_instance.get_crowd_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigCrowdApi->get_crowd_configuration: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiCrowdConfigurationDTO**](ApiCrowdConfigurationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insert_or_update_crowd_configuration**

> insert_or_update_crowd_configuration(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigCrowdApi()
body = swagger_client.ApiCrowdConfigurationDTO() # ApiCrowdConfigurationDTO |  (optional)

try:
    api_instance.insert_or_update_crowd_configuration(body=body)
except ApiException as e:
    print("Exception when calling ConfigCrowdApi->insert_or_update_crowd_configuration: %s\n" % e)
```

### Parameters

| Name     | Type                                                        | Description | Notes      |
| -------- | ----------------------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiCrowdConfigurationDTO**](ApiCrowdConfigurationDTO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_crowd_configuration**

> ApiStatusDTO test_crowd_configuration(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigCrowdApi()
body = swagger_client.ApiCrowdConfigurationDTO() # ApiCrowdConfigurationDTO |  (optional)

try:
    api_response = api_instance.test_crowd_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigCrowdApi->test_crowd_configuration: %s\n" % e)
```

### Parameters

| Name     | Type                                                        | Description | Notes      |
| -------- | ----------------------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiCrowdConfigurationDTO**](ApiCrowdConfigurationDTO.md) |             | [optional] |

### Return type

[**ApiStatusDTO**](ApiStatusDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
