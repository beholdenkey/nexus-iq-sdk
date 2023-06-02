# swagger_client.RolesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_roles**](RolesApi.md#get_roles) | **GET** /api/v2/roles | 

# **get_roles**
> ApiRoleListDTO get_roles()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RolesApi()

try:
    api_response = api_instance.get_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiRoleListDTO**](ApiRoleListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

