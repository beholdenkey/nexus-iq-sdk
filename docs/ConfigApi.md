# swagger_client.ConfigApi

All URIs are relative to _/_

| Method                                                        | HTTP request                                 | Description |
| ------------------------------------------------------------- | -------------------------------------------- | ----------- |
| [**delete_configuration**](ConfigApi.md#delete_configuration) | **DELETE** /api/v2/config                    |
| [**disable_feature**](ConfigApi.md#disable_feature)           | **DELETE** /api/v2/config/features/{feature} |
| [**enabled_feature**](ConfigApi.md#enabled_feature)           | **POST** /api/v2/config/features/{feature}   |
| [**get_configuration**](ConfigApi.md#get_configuration)       | **GET** /api/v2/config                       |
| [**set_configuration**](ConfigApi.md#set_configuration)       | **PUT** /api/v2/config                       |

# **delete_configuration**

> delete_configuration(\_property=\_property)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
_property = ['_property_example'] # list[str] |  (optional)

try:
    api_instance.delete_configuration(_property=_property)
except ApiException as e:
    print("Exception when calling ConfigApi->delete_configuration: %s\n" % e)
```

### Parameters

| Name           | Type                    | Description | Notes      |
| -------------- | ----------------------- | ----------- | ---------- |
| **\_property** | [**list[str]**](str.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_feature**

> disable_feature(feature)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
feature = 'feature_example' # str |

try:
    api_instance.disable_feature(feature)
except ApiException as e:
    print("Exception when calling ConfigApi->disable_feature: %s\n" % e)
```

### Parameters

| Name        | Type    | Description | Notes |
| ----------- | ------- | ----------- | ----- |
| **feature** | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enabled_feature**

> enabled_feature(feature)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
feature = 'feature_example' # str |

try:
    api_instance.enabled_feature(feature)
except ApiException as e:
    print("Exception when calling ConfigApi->enabled_feature: %s\n" % e)
```

### Parameters

| Name        | Type    | Description | Notes |
| ----------- | ------- | ----------- | ----- |
| **feature** | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration**

> dict(str, object) get_configuration(\_property=\_property)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
_property = ['_property_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_configuration(_property=_property)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_configuration: %s\n" % e)
```

### Parameters

| Name           | Type                    | Description | Notes      |
| -------------- | ----------------------- | ----------- | ---------- |
| **\_property** | [**list[str]**](str.md) |             | [optional] |

### Return type

**dict(str, object)**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration**

> set_configuration(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigApi()
body = NULL # dict(str, object) |  (optional)

try:
    api_instance.set_configuration(body=body)
except ApiException as e:
    print("Exception when calling ConfigApi->set_configuration: %s\n" % e)
```

### Parameters

| Name     | Type                             | Description | Notes      |
| -------- | -------------------------------- | ----------- | ---------- |
| **body** | [**dict(str, object)**](dict.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
