# swagger_client.RoleMembershipsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_role_memberships_application_or_organization**](RoleMembershipsApi.md#get_role_memberships_application_or_organization) | **GET** /api/v2/roleMemberships/{ownerType}/{internalOwnerId} | 
[**get_role_memberships_global_or_repository_container**](RoleMembershipsApi.md#get_role_memberships_global_or_repository_container) | **GET** /api/v2/roleMemberships/{ownerType} | 
[**grant_role_membership_application_or_organization**](RoleMembershipsApi.md#grant_role_membership_application_or_organization) | **PUT** /api/v2/roleMemberships/{ownerType}/{internalOwnerId}/role/{roleId}/{memberType}/{memberName} | 
[**grant_role_membership_global_or_repository_container**](RoleMembershipsApi.md#grant_role_membership_global_or_repository_container) | **PUT** /api/v2/roleMemberships/{ownerType}/role/{roleId}/{memberType}/{memberName} | 
[**revoke_role_membership_application_or_organization**](RoleMembershipsApi.md#revoke_role_membership_application_or_organization) | **DELETE** /api/v2/roleMemberships/{ownerType}/{internalOwnerId}/role/{roleId}/{memberType}/{memberName} | 
[**revoke_role_membership_global_or_repository_container**](RoleMembershipsApi.md#revoke_role_membership_global_or_repository_container) | **DELETE** /api/v2/roleMemberships/{ownerType}/role/{roleId}/{memberType}/{memberName} | 

# **get_role_memberships_application_or_organization**
> ApiRoleMemberMappingListDTO get_role_memberships_application_or_organization(owner_type, internal_owner_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoleMembershipsApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 

try:
    api_response = api_instance.get_role_memberships_application_or_organization(owner_type, internal_owner_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleMembershipsApi->get_role_memberships_application_or_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 

### Return type

[**ApiRoleMemberMappingListDTO**](ApiRoleMemberMappingListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_memberships_global_or_repository_container**
> ApiRoleMemberMappingListDTO get_role_memberships_global_or_repository_container(owner_type)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoleMembershipsApi()
owner_type = 'owner_type_example' # str | 

try:
    api_response = api_instance.get_role_memberships_global_or_repository_container(owner_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleMembershipsApi->get_role_memberships_global_or_repository_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 

### Return type

[**ApiRoleMemberMappingListDTO**](ApiRoleMemberMappingListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_role_membership_application_or_organization**
> grant_role_membership_application_or_organization(owner_type, internal_owner_id, role_id, member_type, member_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoleMembershipsApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
role_id = 'role_id_example' # str | 
member_type = 'member_type_example' # str | 
member_name = 'member_name_example' # str | 

try:
    api_instance.grant_role_membership_application_or_organization(owner_type, internal_owner_id, role_id, member_type, member_name)
except ApiException as e:
    print("Exception when calling RoleMembershipsApi->grant_role_membership_application_or_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **role_id** | **str**|  | 
 **member_type** | **str**|  | 
 **member_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_role_membership_global_or_repository_container**
> grant_role_membership_global_or_repository_container(owner_type, role_id, member_type, member_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoleMembershipsApi()
owner_type = 'owner_type_example' # str | 
role_id = 'role_id_example' # str | 
member_type = 'member_type_example' # str | 
member_name = 'member_name_example' # str | 

try:
    api_instance.grant_role_membership_global_or_repository_container(owner_type, role_id, member_type, member_name)
except ApiException as e:
    print("Exception when calling RoleMembershipsApi->grant_role_membership_global_or_repository_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **role_id** | **str**|  | 
 **member_type** | **str**|  | 
 **member_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_role_membership_application_or_organization**
> revoke_role_membership_application_or_organization(owner_type, internal_owner_id, role_id, member_type, member_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoleMembershipsApi()
owner_type = 'owner_type_example' # str | 
internal_owner_id = 'internal_owner_id_example' # str | 
role_id = 'role_id_example' # str | 
member_type = 'member_type_example' # str | 
member_name = 'member_name_example' # str | 

try:
    api_instance.revoke_role_membership_application_or_organization(owner_type, internal_owner_id, role_id, member_type, member_name)
except ApiException as e:
    print("Exception when calling RoleMembershipsApi->revoke_role_membership_application_or_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **internal_owner_id** | **str**|  | 
 **role_id** | **str**|  | 
 **member_type** | **str**|  | 
 **member_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_role_membership_global_or_repository_container**
> revoke_role_membership_global_or_repository_container(owner_type, role_id, member_type, member_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RoleMembershipsApi()
owner_type = 'owner_type_example' # str | 
role_id = 'role_id_example' # str | 
member_type = 'member_type_example' # str | 
member_name = 'member_name_example' # str | 

try:
    api_instance.revoke_role_membership_global_or_repository_container(owner_type, role_id, member_type, member_name)
except ApiException as e:
    print("Exception when calling RoleMembershipsApi->revoke_role_membership_global_or_repository_container: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **role_id** | **str**|  | 
 **member_type** | **str**|  | 
 **member_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

