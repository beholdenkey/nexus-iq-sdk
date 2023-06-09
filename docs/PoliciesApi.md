# swagger_client.PoliciesApi

All URIs are relative to _/_

| Method                                          | HTTP request             | Description |
| ----------------------------------------------- | ------------------------ | ----------- |
| [**get_policies**](PoliciesApi.md#get_policies) | **GET** /api/v2/policies |

# **get_policies**

> ApiPolicyListDTO get_policies()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PoliciesApi()

try:
    api_response = api_instance.get_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PoliciesApi->get_policies: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiPolicyListDTO**](ApiPolicyListDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
