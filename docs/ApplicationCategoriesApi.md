# swagger_client.ApplicationCategoriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_tag**](ApplicationCategoriesApi.md#add_tag) | **POST** /api/v2/applicationCategories/organization/{organizationId} | 
[**delete_tag**](ApplicationCategoriesApi.md#delete_tag) | **DELETE** /api/v2/applicationCategories/organization/{organizationId}/{tagId} | 
[**get_applicable_tags**](ApplicationCategoriesApi.md#get_applicable_tags) | **GET** /api/v2/applicationCategories/organization/{organizationId}/applicable | 
[**get_applicable_tags_by_application_public_id**](ApplicationCategoriesApi.md#get_applicable_tags_by_application_public_id) | **GET** /api/v2/applicationCategories/application/{applicationPublicId}/applicable | 
[**get_application_applicable_tags**](ApplicationCategoriesApi.md#get_application_applicable_tags) | **GET** /api/v2/applicationCategories/application/{applicationPublicId} | 
[**get_applied_policy_tags**](ApplicationCategoriesApi.md#get_applied_policy_tags) | **GET** /api/v2/applicationCategories/organization/{organizationId}/policy | 
[**get_applied_tags**](ApplicationCategoriesApi.md#get_applied_tags) | **GET** /api/v2/applicationCategories/organization/{organizationId}/applied | 
[**get_tags**](ApplicationCategoriesApi.md#get_tags) | **GET** /api/v2/applicationCategories/organization/{organizationId} | 
[**get_tags_used_by_applications**](ApplicationCategoriesApi.md#get_tags_used_by_applications) | **GET** /api/v2/applicationCategories/application | 
[**update_tag**](ApplicationCategoriesApi.md#update_tag) | **PUT** /api/v2/applicationCategories/organization/{organizationId} | 

# **add_tag**
> ApiApplicationCategoryDTO add_tag(organization_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
organization_id = 'organization_id_example' # str | 
body = swagger_client.ApiApplicationCategoryDTO() # ApiApplicationCategoryDTO |  (optional)

try:
    api_response = api_instance.add_tag(organization_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->add_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **body** | [**ApiApplicationCategoryDTO**](ApiApplicationCategoryDTO.md)|  | [optional] 

### Return type

[**ApiApplicationCategoryDTO**](ApiApplicationCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag**
> delete_tag(organization_id, tag_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
organization_id = 'organization_id_example' # str | 
tag_id = 'tag_id_example' # str | 

try:
    api_instance.delete_tag(organization_id, tag_id)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->delete_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **tag_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicable_tags**
> ApplicableTagsDTO get_applicable_tags(organization_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
organization_id = 'organization_id_example' # str | 

try:
    api_response = api_instance.get_applicable_tags(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->get_applicable_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**ApplicableTagsDTO**](ApplicableTagsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicable_tags_by_application_public_id**
> list[ApiApplicationCategoryDTO] get_applicable_tags_by_application_public_id(application_public_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
application_public_id = 'application_public_id_example' # str | 

try:
    api_response = api_instance.get_applicable_tags_by_application_public_id(application_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->get_applicable_tags_by_application_public_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_public_id** | **str**|  | 

### Return type

[**list[ApiApplicationCategoryDTO]**](ApiApplicationCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_applicable_tags**
> ApplicableTagsDTO get_application_applicable_tags(application_public_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
application_public_id = 'application_public_id_example' # str | 

try:
    api_response = api_instance.get_application_applicable_tags(application_public_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->get_application_applicable_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_public_id** | **str**|  | 

### Return type

[**ApplicableTagsDTO**](ApplicableTagsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applied_policy_tags**
> list[PolicyTag] get_applied_policy_tags(organization_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
organization_id = 'organization_id_example' # str | 

try:
    api_response = api_instance.get_applied_policy_tags(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->get_applied_policy_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**list[PolicyTag]**](PolicyTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applied_tags**
> AppliedTagsDTO get_applied_tags(organization_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
organization_id = 'organization_id_example' # str | 

try:
    api_response = api_instance.get_applied_tags(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->get_applied_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**AppliedTagsDTO**](AppliedTagsDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags**
> list[ApiApplicationCategoryDTO] get_tags(organization_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
organization_id = 'organization_id_example' # str | 

try:
    api_response = api_instance.get_tags(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->get_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**list[ApiApplicationCategoryDTO]**](ApiApplicationCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_used_by_applications**
> list[ApiApplicationCategoryDTO] get_tags_used_by_applications()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()

try:
    api_response = api_instance.get_tags_used_by_applications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->get_tags_used_by_applications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiApplicationCategoryDTO]**](ApiApplicationCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag**
> ApiApplicationCategoryDTO update_tag(organization_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApplicationCategoriesApi()
organization_id = 'organization_id_example' # str | 
body = swagger_client.ApiApplicationCategoryDTO() # ApiApplicationCategoryDTO |  (optional)

try:
    api_response = api_instance.update_tag(organization_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationCategoriesApi->update_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 
 **body** | [**ApiApplicationCategoryDTO**](ApiApplicationCategoryDTO.md)|  | [optional] 

### Return type

[**ApiApplicationCategoryDTO**](ApiApplicationCategoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

