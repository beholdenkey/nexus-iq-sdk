# swagger_client.ConfigReverseProxyAuthenticationApi

All URIs are relative to _/_

| Method                                                                                    | HTTP request                                         | Description |
| ----------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------- |
| [**delete_configuration4**](ConfigReverseProxyAuthenticationApi.md#delete_configuration4) | **DELETE** /api/v2/config/reverseProxyAuthentication |
| [**get_configuration4**](ConfigReverseProxyAuthenticationApi.md#get_configuration4)       | **GET** /api/v2/config/reverseProxyAuthentication    |
| [**set_configuration4**](ConfigReverseProxyAuthenticationApi.md#set_configuration4)       | **PUT** /api/v2/config/reverseProxyAuthentication    |

# **delete_configuration4**

> delete_configuration4()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigReverseProxyAuthenticationApi()

try:
    api_instance.delete_configuration4()
except ApiException as e:
    print("Exception when calling ConfigReverseProxyAuthenticationApi->delete_configuration4: %s\n" % e)
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

# **get_configuration4**

> ApiReverseProxyAuthenticationConfigurationDTO get_configuration4()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigReverseProxyAuthenticationApi()

try:
    api_response = api_instance.get_configuration4()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigReverseProxyAuthenticationApi->get_configuration4: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiReverseProxyAuthenticationConfigurationDTO**](ApiReverseProxyAuthenticationConfigurationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration4**

> set_configuration4(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigReverseProxyAuthenticationApi()
body = swagger_client.ApiReverseProxyAuthenticationConfigurationDTO() # ApiReverseProxyAuthenticationConfigurationDTO |  (optional)

try:
    api_instance.set_configuration4(body=body)
except ApiException as e:
    print("Exception when calling ConfigReverseProxyAuthenticationApi->set_configuration4: %s\n" % e)
```

### Parameters

| Name     | Type                                                                                                  | Description | Notes      |
| -------- | ----------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiReverseProxyAuthenticationConfigurationDTO**](ApiReverseProxyAuthenticationConfigurationDTO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
