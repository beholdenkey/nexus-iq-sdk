# swagger_client.OrganizationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_organization**](OrganizationsApi.md#add_organization) | **POST** /api/v2/organizations | 
[**get_organization**](OrganizationsApi.md#get_organization) | **GET** /api/v2/organizations/{organizationId} | 
[**get_organizations**](OrganizationsApi.md#get_organizations) | **GET** /api/v2/organizations | 

# **add_organization**
> ApiOrganizationDTO add_organization(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
body = swagger_client.ApiOrganizationDTO() # ApiOrganizationDTO |  (optional)

try:
    api_response = api_instance.add_organization(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->add_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiOrganizationDTO**](ApiOrganizationDTO.md)|  | [optional] 

### Return type

[**ApiOrganizationDTO**](ApiOrganizationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> ApiOrganizationDTO get_organization(organization_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
organization_id = 'organization_id_example' # str | 

try:
    api_response = api_instance.get_organization(organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

### Return type

[**ApiOrganizationDTO**](ApiOrganizationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizations**
> ApiOrganizationListDTO get_organizations(organization_name=organization_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrganizationsApi()
organization_name = ['organization_name_example'] # list[str] |  (optional)

try:
    api_response = api_instance.get_organizations(organization_name=organization_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_name** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ApiOrganizationListDTO**](ApiOrganizationListDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

