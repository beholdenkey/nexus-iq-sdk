# swagger_client.UsersApi

All URIs are relative to _/_

| Method                               | HTTP request                        | Description |
| ------------------------------------ | ----------------------------------- | ----------- |
| [**add**](UsersApi.md#add)           | **POST** /api/v2/users              |
| [**delete1**](UsersApi.md#delete1)   | **DELETE** /api/v2/users/{username} |
| [**get1**](UsersApi.md#get1)         | **GET** /api/v2/users/{username}    |
| [**get_all2**](UsersApi.md#get_all2) | **GET** /api/v2/users               |
| [**update**](UsersApi.md#update)     | **PUT** /api/v2/users/{username}    |

# **add**

> add(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
body = swagger_client.ApiUserDTO() # ApiUserDTO |  (optional)

try:
    api_instance.add(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->add: %s\n" % e)
```

### Parameters

| Name     | Type                            | Description | Notes      |
| -------- | ------------------------------- | ----------- | ---------- |
| **body** | [**ApiUserDTO**](ApiUserDTO.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete1**

> delete1(username, realm=realm)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
username = 'username_example' # str |
realm = 'Internal' # str |  (optional) (default to Internal)

try:
    api_instance.delete1(username, realm=realm)
except ApiException as e:
    print("Exception when calling UsersApi->delete1: %s\n" % e)
```

### Parameters

| Name         | Type    | Description | Notes                            |
| ------------ | ------- | ----------- | -------------------------------- |
| **username** | **str** |             |
| **realm**    | **str** |             | [optional] [default to Internal] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get1**

> ApiUserDTO get1(username, realm=realm)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
username = 'username_example' # str |
realm = 'Internal' # str |  (optional) (default to Internal)

try:
    api_response = api_instance.get1(username, realm=realm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get1: %s\n" % e)
```

### Parameters

| Name         | Type    | Description | Notes                            |
| ------------ | ------- | ----------- | -------------------------------- |
| **username** | **str** |             |
| **realm**    | **str** |             | [optional] [default to Internal] |

### Return type

[**ApiUserDTO**](ApiUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all2**

> ApiUserListDTO get_all2(realm=realm)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
realm = 'Internal' # str |  (optional) (default to Internal)

try:
    api_response = api_instance.get_all2(realm=realm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_all2: %s\n" % e)
```

### Parameters

| Name      | Type    | Description | Notes                            |
| --------- | ------- | ----------- | -------------------------------- |
| **realm** | **str** |             | [optional] [default to Internal] |

### Return type

[**ApiUserListDTO**](ApiUserListDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**

> ApiUserDTO update(username, body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
username = 'username_example' # str |
body = swagger_client.ApiUserDTO() # ApiUserDTO |  (optional)

try:
    api_response = api_instance.update(username, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update: %s\n" % e)
```

### Parameters

| Name         | Type                            | Description | Notes      |
| ------------ | ------------------------------- | ----------- | ---------- |
| **username** | **str**                         |             |
| **body**     | [**ApiUserDTO**](ApiUserDTO.md) |             | [optional] |

### Return type

[**ApiUserDTO**](ApiUserDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
