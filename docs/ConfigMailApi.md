# swagger_client.ConfigMailApi

All URIs are relative to _/_

| Method                                                              | HTTP request                                       | Description |
| ------------------------------------------------------------------- | -------------------------------------------------- | ----------- |
| [**delete_configuration2**](ConfigMailApi.md#delete_configuration2) | **DELETE** /api/v2/config/mail                     |
| [**get_configuration2**](ConfigMailApi.md#get_configuration2)       | **GET** /api/v2/config/mail                        |
| [**set_configuration2**](ConfigMailApi.md#set_configuration2)       | **PUT** /api/v2/config/mail                        |
| [**test_configuration**](ConfigMailApi.md#test_configuration)       | **POST** /api/v2/config/mail/test/{recipientEmail} |

# **delete_configuration2**

> delete_configuration2()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigMailApi()

try:
    api_instance.delete_configuration2()
except ApiException as e:
    print("Exception when calling ConfigMailApi->delete_configuration2: %s\n" % e)
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

# **get_configuration2**

> ApiMailConfigurationDTO get_configuration2()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigMailApi()

try:
    api_response = api_instance.get_configuration2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigMailApi->get_configuration2: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiMailConfigurationDTO**](ApiMailConfigurationDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configuration2**

> set_configuration2(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigMailApi()
body = swagger_client.ApiMailConfigurationDTO() # ApiMailConfigurationDTO |  (optional)

try:
    api_instance.set_configuration2(body=body)
except ApiException as e:
    print("Exception when calling ConfigMailApi->set_configuration2: %s\n" % e)
```

### Parameters

| Name     | Type                                                      | Description | Notes      |
| -------- | --------------------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiMailConfigurationDTO**](ApiMailConfigurationDTO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_configuration**

> test_configuration(recipient_email, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigMailApi()
recipient_email = 'recipient_email_example' # str |
body = swagger_client.ApiMailConfigurationDTO() # ApiMailConfigurationDTO |  (optional)

try:
    api_instance.test_configuration(recipient_email, body=body)
except ApiException as e:
    print("Exception when calling ConfigMailApi->test_configuration: %s\n" % e)
```

### Parameters

| Name                | Type                                                      | Description | Notes      |
| ------------------- | --------------------------------------------------------- | ----------- | ---------- |
| **recipient_email** | **str**                                                   |             |
| **body**            | [**ApiMailConfigurationDTO**](ApiMailConfigurationDTO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
