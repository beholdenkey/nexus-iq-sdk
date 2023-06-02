# swagger_client.ConfigArtifactoryConnectionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_artifactory_connection**](ConfigArtifactoryConnectionApi.md#add_artifactory_connection) | **POST** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId} | 
[**delete_artifactory_connection**](ConfigArtifactoryConnectionApi.md#delete_artifactory_connection) | **DELETE** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId} | 
[**get_artifactory_connection**](ConfigArtifactoryConnectionApi.md#get_artifactory_connection) | **GET** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId} | 
[**get_owner_artifactory_connection**](ConfigArtifactoryConnectionApi.md#get_owner_artifactory_connection) | **GET** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId} | 
[**test_artifactory_connection**](ConfigArtifactoryConnectionApi.md#test_artifactory_connection) | **POST** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/test | 
[**test_artifactory_connection1**](ConfigArtifactoryConnectionApi.md#test_artifactory_connection1) | **POST** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId}/test | 
[**update_artifactory_connection**](ConfigArtifactoryConnectionApi.md#update_artifactory_connection) | **PUT** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId}/{artifactoryConnectionId} | 
[**update_owner_artifactory_connection_status**](ConfigArtifactoryConnectionApi.md#update_owner_artifactory_connection_status) | **PUT** /api/v2/config/artifactoryConnection/{ownerType}/{internalOwnerId} | 

# **add_artifactory_connection**
> ApiArtifactoryConnectionDTO add_artifactory_connection(owner_type, internal_owner_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
body = swagger_client.ApiArtifactoryConnectionDTO() # ApiArtifactoryConnectionDTO |  (optional)

try:
    api_response = api_instance.add_artifactory_connection(owner_type, internal_owner_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->add_artifactory_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **body** | [**ApiArtifactoryConnectionDTO**](ApiArtifactoryConnectionDTO.md)|  | [optional] 

### Return type

[**ApiArtifactoryConnectionDTO**](ApiArtifactoryConnectionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_artifactory_connection**
> delete_artifactory_connection(owner_type, internal_owner_id, artifactory_connection_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
artifactory_connection_id = 'artifactory_connection_id_example' # str | 

try:
    api_instance.delete_artifactory_connection(owner_type, internal_owner_id, artifactory_connection_id)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->delete_artifactory_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **artifactory_connection_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifactory_connection**
> ApiArtifactoryConnectionDTO get_artifactory_connection(owner_type, internal_owner_id, artifactory_connection_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
artifactory_connection_id = 'artifactory_connection_id_example' # str | 

try:
    api_response = api_instance.get_artifactory_connection(owner_type, internal_owner_id, artifactory_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->get_artifactory_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **artifactory_connection_id** | **str**|  | 

### Return type

[**ApiArtifactoryConnectionDTO**](ApiArtifactoryConnectionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owner_artifactory_connection**
> ApiOwnerArtifactoryConnectionDTO get_owner_artifactory_connection(owner_type, internal_owner_id, inherit=inherit)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
inherit = false # bool |  (optional) (default to false)

try:
    api_response = api_instance.get_owner_artifactory_connection(owner_type, internal_owner_id, inherit=inherit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->get_owner_artifactory_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **inherit** | **bool**|  | [optional] [default to false]

### Return type

[**ApiOwnerArtifactoryConnectionDTO**](ApiOwnerArtifactoryConnectionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_artifactory_connection**
> ApiStatusDTO test_artifactory_connection(owner_type, internal_owner_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
body = swagger_client.ApiArtifactoryConnectionDTO() # ApiArtifactoryConnectionDTO |  (optional)

try:
    api_response = api_instance.test_artifactory_connection(owner_type, internal_owner_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->test_artifactory_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **body** | [**ApiArtifactoryConnectionDTO**](ApiArtifactoryConnectionDTO.md)|  | [optional] 

### Return type

[**ApiStatusDTO**](ApiStatusDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_artifactory_connection1**
> ApiStatusDTO test_artifactory_connection1(owner_type, internal_owner_id, artifactory_connection_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
artifactory_connection_id = 'artifactory_connection_id_example' # str | 

try:
    api_response = api_instance.test_artifactory_connection1(owner_type, internal_owner_id, artifactory_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->test_artifactory_connection1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **artifactory_connection_id** | **str**|  | 

### Return type

[**ApiStatusDTO**](ApiStatusDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_artifactory_connection**
> ApiArtifactoryConnectionDTO update_artifactory_connection(owner_type, internal_owner_id, artifactory_connection_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
artifactory_connection_id = 'artifactory_connection_id_example' # str | 
body = swagger_client.ApiArtifactoryConnectionDTO() # ApiArtifactoryConnectionDTO |  (optional)

try:
    api_response = api_instance.update_artifactory_connection(owner_type, internal_owner_id, artifactory_connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->update_artifactory_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **artifactory_connection_id** | **str**|  | 
 **body** | [**ApiArtifactoryConnectionDTO**](ApiArtifactoryConnectionDTO.md)|  | [optional] 

### Return type

[**ApiArtifactoryConnectionDTO**](ApiArtifactoryConnectionDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_owner_artifactory_connection_status**
> update_owner_artifactory_connection_status(owner_type, internal_owner_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigArtifactoryConnectionApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
body = swagger_client.ApiArtifactoryConnectionStatusRequestDTO() # ApiArtifactoryConnectionStatusRequestDTO |  (optional)

try:
    api_instance.update_owner_artifactory_connection_status(owner_type, internal_owner_id, body=body)
except ApiException as e:
    print("Exception when calling ConfigArtifactoryConnectionApi->update_owner_artifactory_connection_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **body** | [**ApiArtifactoryConnectionStatusRequestDTO**](ApiArtifactoryConnectionStatusRequestDTO.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

