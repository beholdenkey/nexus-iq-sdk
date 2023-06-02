# swagger_client.LicenseLegalMetadataApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attribution_report_template**](LicenseLegalMetadataApi.md#delete_attribution_report_template) | **DELETE** /api/v2/licenseLegalMetadata/report-template/{id} | 
[**get_all_attribution_report_templates**](LicenseLegalMetadataApi.md#get_all_attribution_report_templates) | **GET** /api/v2/licenseLegalMetadata/report-template | 
[**get_attribution_report_template_by_id**](LicenseLegalMetadataApi.md#get_attribution_report_template_by_id) | **GET** /api/v2/licenseLegalMetadata/report-template/{id} | 
[**get_license_legal_application_html_report**](LicenseLegalMetadataApi.md#get_license_legal_application_html_report) | **GET** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId}/report | 
[**get_license_legal_application_report**](LicenseLegalMetadataApi.md#get_license_legal_application_report) | **GET** /api/v2/licenseLegalMetadata/application/{applicationId} | 
[**get_license_legal_application_report1**](LicenseLegalMetadataApi.md#get_license_legal_application_report1) | **GET** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId} | 
[**get_license_legal_component_report**](LicenseLegalMetadataApi.md#get_license_legal_component_report) | **GET** /api/v2/licenseLegalMetadata/{ownerType}/{ownerId}/component | 
[**get_license_legal_custom_application_html_report**](LicenseLegalMetadataApi.md#get_license_legal_custom_application_html_report) | **POST** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId}/report | 
[**get_license_legal_custom_application_html_report1**](LicenseLegalMetadataApi.md#get_license_legal_custom_application_html_report1) | **POST** /api/v2/licenseLegalMetadata/application/{applicationId}/stage/{stageId}/report/templateId/{templateId} | 
[**get_license_legal_custom_multi_application_html_report1**](LicenseLegalMetadataApi.md#get_license_legal_custom_multi_application_html_report1) | **POST** /api/v2/licenseLegalMetadata/multiApplication/report/templateId/{templateId} | 
[**get_license_legal_multi_application_html_report**](LicenseLegalMetadataApi.md#get_license_legal_multi_application_html_report) | **POST** /api/v2/licenseLegalMetadata/multiApplication/report | 
[**get_license_legal_multi_application_report_from_active_user_filter**](LicenseLegalMetadataApi.md#get_license_legal_multi_application_report_from_active_user_filter) | **POST** /api/v2/licenseLegalMetadata/multiApplication/activeUserFilter/report/templateId/{templateId} | 
[**save_attribution_report_template**](LicenseLegalMetadataApi.md#save_attribution_report_template) | **POST** /api/v2/licenseLegalMetadata/report-template | 

# **delete_attribution_report_template**
> delete_attribution_report_template(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
id = 'id_example' # str | 

try:
    api_instance.delete_attribution_report_template(id)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->delete_attribution_report_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_attribution_report_templates**
> list[AttributionReportTemplateDTO] get_all_attribution_report_templates()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()

try:
    api_response = api_instance.get_all_attribution_report_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_all_attribution_report_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AttributionReportTemplateDTO]**](AttributionReportTemplateDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribution_report_template_by_id**
> AttributionReportTemplateDTO get_attribution_report_template_by_id(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.get_attribution_report_template_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_attribution_report_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AttributionReportTemplateDTO**](AttributionReportTemplateDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_application_html_report**
> str get_license_legal_application_html_report(application_id, stage_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
application_id = 'application_id_example' # str | 
stage_id = 'stage_id_example' # str | 

try:
    api_response = api_instance.get_license_legal_application_html_report(application_id, stage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_application_html_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **stage_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_application_report**
> ApiLicenseLegalApplicationReportDTO get_license_legal_application_report(application_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
application_id = 'application_id_example' # str | 

try:
    api_response = api_instance.get_license_legal_application_report(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_application_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 

### Return type

[**ApiLicenseLegalApplicationReportDTO**](ApiLicenseLegalApplicationReportDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_application_report1**
> ApiLicenseLegalApplicationReportDTO get_license_legal_application_report1(application_id, stage_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
application_id = 'application_id_example' # str | 
stage_id = 'stage_id_example' # str | 

try:
    api_response = api_instance.get_license_legal_application_report1(application_id, stage_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_application_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **stage_id** | **str**|  | 

### Return type

[**ApiLicenseLegalApplicationReportDTO**](ApiLicenseLegalApplicationReportDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_component_report**
> ApiLicenseLegalComponentReportDTO get_license_legal_component_report(owner_type, owner_id, component_identifier=component_identifier, package_url=package_url, hash=hash, identification_source=identification_source, scan_id=scan_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
owner_type = 'owner_type_example' # str | 
owner_id = 'owner_id_example' # str | 
component_identifier = swagger_client.ComponentIdentifier() # ComponentIdentifier |  (optional)
package_url = 'package_url_example' # str |  (optional)
hash = 'hash_example' # str |  (optional)
identification_source = 'identification_source_example' # str |  (optional)
scan_id = 'scan_id_example' # str |  (optional)

try:
    api_response = api_instance.get_license_legal_component_report(owner_type, owner_id, component_identifier=component_identifier, package_url=package_url, hash=hash, identification_source=identification_source, scan_id=scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_component_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_type** | **str**|  | 
 **owner_id** | **str**|  | 
 **component_identifier** | [**ComponentIdentifier**](.md)|  | [optional] 
 **package_url** | **str**|  | [optional] 
 **hash** | **str**|  | [optional] 
 **identification_source** | **str**|  | [optional] 
 **scan_id** | **str**|  | [optional] 

### Return type

[**ApiLicenseLegalComponentReportDTO**](ApiLicenseLegalComponentReportDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_custom_application_html_report**
> str get_license_legal_custom_application_html_report(application_id, stage_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
application_id = 'application_id_example' # str | 
stage_id = 'stage_id_example' # str | 
body = swagger_client.FormDataMultiPart() # FormDataMultiPart |  (optional)

try:
    api_response = api_instance.get_license_legal_custom_application_html_report(application_id, stage_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_custom_application_html_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **stage_id** | **str**|  | 
 **body** | [**FormDataMultiPart**](FormDataMultiPart.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_custom_application_html_report1**
> str get_license_legal_custom_application_html_report1(application_id, stage_id, template_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
application_id = 'application_id_example' # str | 
stage_id = 'stage_id_example' # str | 
template_id = 'template_id_example' # str | 

try:
    api_response = api_instance.get_license_legal_custom_application_html_report1(application_id, stage_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_custom_application_html_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**|  | 
 **stage_id** | **str**|  | 
 **template_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_custom_multi_application_html_report1**
> str get_license_legal_custom_multi_application_html_report1(template_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
template_id = 'template_id_example' # str | 

try:
    api_response = api_instance.get_license_legal_custom_multi_application_html_report1(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_custom_multi_application_html_report1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_multi_application_html_report**
> str get_license_legal_multi_application_html_report()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()

try:
    api_response = api_instance.get_license_legal_multi_application_html_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_multi_application_html_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_legal_multi_application_report_from_active_user_filter**
> str get_license_legal_multi_application_report_from_active_user_filter(template_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
template_id = 'template_id_example' # str | 

try:
    api_response = api_instance.get_license_legal_multi_application_report_from_active_user_filter(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->get_license_legal_multi_application_report_from_active_user_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_attribution_report_template**
> AttributionReportTemplateDTO save_attribution_report_template(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LicenseLegalMetadataApi()
body = swagger_client.AttributionReportTemplateDTO() # AttributionReportTemplateDTO |  (optional)

try:
    api_response = api_instance.save_attribution_report_template(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseLegalMetadataApi->save_attribution_report_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AttributionReportTemplateDTO**](AttributionReportTemplateDTO.md)|  | [optional] 

### Return type

[**AttributionReportTemplateDTO**](AttributionReportTemplateDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

