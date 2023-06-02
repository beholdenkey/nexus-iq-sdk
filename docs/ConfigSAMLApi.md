# swagger_client.ConfigSAMLApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_saml_configuration**](ConfigSAMLApi.md#delete_saml_configuration) | **DELETE** /api/v2/config/saml | 
[**get_metadata**](ConfigSAMLApi.md#get_metadata) | **GET** /api/v2/config/saml/metadata | 
[**get_saml_configuration**](ConfigSAMLApi.md#get_saml_configuration) | **GET** /api/v2/config/saml | 

# **delete_saml_configuration**
> delete_saml_configuration()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigSAMLApi()

try:
    api_instance.delete_saml_configuration()
except ApiException as e:
    print("Exception when calling ConfigSAMLApi->delete_saml_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata**
> str get_metadata()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigSAMLApi()

try:
    api_response = api_instance.get_metadata()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigSAMLApi->get_metadata: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saml_configuration**
> ApiSamlConfigurationResponseDTO get_saml_configuration()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigSAMLApi()

try:
    api_response = api_instance.get_saml_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigSAMLApi->get_saml_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiSamlConfigurationResponseDTO**](ApiSamlConfigurationResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

