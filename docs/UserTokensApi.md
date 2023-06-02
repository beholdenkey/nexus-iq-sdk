# swagger_client.UserTokensApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_token**](UserTokensApi.md#create_user_token) | **POST** /api/v2/userTokens/currentUser | 
[**delete_current_user_token**](UserTokensApi.md#delete_current_user_token) | **DELETE** /api/v2/userTokens/currentUser | 
[**delete_user_token_by_user_code**](UserTokensApi.md#delete_user_token_by_user_code) | **DELETE** /api/v2/userTokens/userCode/{userCode} | 
[**get_user_token_by_username_and_realm_id**](UserTokensApi.md#get_user_token_by_username_and_realm_id) | **GET** /api/v2/userTokens/{username} | 
[**get_user_token_exists_for_current_user**](UserTokensApi.md#get_user_token_exists_for_current_user) | **GET** /api/v2/userTokens/currentUser/hasToken | 
[**get_user_tokens_by_created_between_and_realm_id**](UserTokensApi.md#get_user_tokens_by_created_between_and_realm_id) | **GET** /api/v2/userTokens | 
[**purge_user_tokens**](UserTokensApi.md#purge_user_tokens) | **DELETE** /api/v2/userTokens/purge | 

# **create_user_token**
> ApiUserTokenDTO create_user_token()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserTokensApi()

try:
    api_response = api_instance.create_user_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokensApi->create_user_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiUserTokenDTO**](ApiUserTokenDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_current_user_token**
> delete_current_user_token()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserTokensApi()

try:
    api_instance.delete_current_user_token()
except ApiException as e:
    print("Exception when calling UserTokensApi->delete_current_user_token: %s\n" % e)
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

# **delete_user_token_by_user_code**
> delete_user_token_by_user_code(user_code)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserTokensApi()
user_code = 'user_code_example' # str | 

try:
    api_instance.delete_user_token_by_user_code(user_code)
except ApiException as e:
    print("Exception when calling UserTokensApi->delete_user_token_by_user_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_code** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token_by_username_and_realm_id**
> ApiUserTokenDTO get_user_token_by_username_and_realm_id(username, realm=realm)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserTokensApi()
username = 'username_example' # str | 
realm = 'Internal' # str |  (optional) (default to Internal)

try:
    api_response = api_instance.get_user_token_by_username_and_realm_id(username, realm=realm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokensApi->get_user_token_by_username_and_realm_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **realm** | **str**|  | [optional] [default to Internal]

### Return type

[**ApiUserTokenDTO**](ApiUserTokenDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_token_exists_for_current_user**
> ApiUserTokenExistsDTO get_user_token_exists_for_current_user()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserTokensApi()

try:
    api_response = api_instance.get_user_token_exists_for_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokensApi->get_user_token_exists_for_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiUserTokenExistsDTO**](ApiUserTokenExistsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_tokens_by_created_between_and_realm_id**
> list[ApiUserTokenDTO] get_user_tokens_by_created_between_and_realm_id(created_after=created_after, created_before=created_before, realm=realm)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserTokensApi()
created_after = 'created_after_example' # str |  (optional)
created_before = 'created_before_example' # str |  (optional)
realm = 'Internal' # str |  (optional) (default to Internal)

try:
    api_response = api_instance.get_user_tokens_by_created_between_and_realm_id(created_after=created_after, created_before=created_before, realm=realm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserTokensApi->get_user_tokens_by_created_between_and_realm_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **str**|  | [optional] 
 **created_before** | **str**|  | [optional] 
 **realm** | **str**|  | [optional] [default to Internal]

### Return type

[**list[ApiUserTokenDTO]**](ApiUserTokenDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_user_tokens**
> purge_user_tokens()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserTokensApi()

try:
    api_instance.purge_user_tokens()
except ApiException as e:
    print("Exception when calling UserTokensApi->purge_user_tokens: %s\n" % e)
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

