"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1LimitRangeSpec:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, limits=..., local_vars_configuration=...) -> None:
        """V1LimitRangeSpec - a model defined in OpenAPI"""
        ...
    
    @property
    def limits(self): # -> None:
        """Gets the limits of this V1LimitRangeSpec.  # noqa: E501

        Limits is the list of LimitRangeItem objects that are enforced.  # noqa: E501

        :return: The limits of this V1LimitRangeSpec.  # noqa: E501
        :rtype: list[V1LimitRangeItem]
        """
        ...
    
    @limits.setter
    def limits(self, limits): # -> None:
        """Sets the limits of this V1LimitRangeSpec.

        Limits is the list of LimitRangeItem objects that are enforced.  # noqa: E501

        :param limits: The limits of this V1LimitRangeSpec.  # noqa: E501
        :type: list[V1LimitRangeItem]
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
    


