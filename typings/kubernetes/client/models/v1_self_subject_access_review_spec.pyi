"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1SelfSubjectAccessReviewSpec:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, non_resource_attributes=..., resource_attributes=..., local_vars_configuration=...) -> None:
        """V1SelfSubjectAccessReviewSpec - a model defined in OpenAPI"""
        ...
    
    @property
    def non_resource_attributes(self): # -> None:
        """Gets the non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501


        :return: The non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1NonResourceAttributes
        """
        ...
    
    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes): # -> None:
        """Sets the non_resource_attributes of this V1SelfSubjectAccessReviewSpec.


        :param non_resource_attributes: The non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type: V1NonResourceAttributes
        """
        ...
    
    @property
    def resource_attributes(self): # -> None:
        """Gets the resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501


        :return: The resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1ResourceAttributes
        """
        ...
    
    @resource_attributes.setter
    def resource_attributes(self, resource_attributes): # -> None:
        """Sets the resource_attributes of this V1SelfSubjectAccessReviewSpec.


        :param resource_attributes: The resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type: V1ResourceAttributes
        """
        ...
    
    def to_dict(self): # -> dict[Any, Any]:
        """Returns the model properties as a dict"""
        ...
    
    def to_str(self): # -> str:
        """Returns the string representation of the model"""
        ...
    
    def __repr__(self): # -> str:
        """For `print` and `pprint`"""
        ...
    
    def __eq__(self, other) -> bool:
        """Returns true if both objects are equal"""
        ...
    
    def __ne__(self, other) -> bool:
        """Returns true if both objects are not equal"""
        ...
    


