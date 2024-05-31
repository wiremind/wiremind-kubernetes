"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1ObjectFieldSelector:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, api_version=..., field_path=..., local_vars_configuration=...) -> None:
        """V1ObjectFieldSelector - a model defined in OpenAPI"""
        ...
    
    @property
    def api_version(self): # -> None:
        """Gets the api_version of this V1ObjectFieldSelector.  # noqa: E501

        Version of the schema the FieldPath is written in terms of, defaults to \"v1\".  # noqa: E501

        :return: The api_version of this V1ObjectFieldSelector.  # noqa: E501
        :rtype: str
        """
        ...
    
    @api_version.setter
    def api_version(self, api_version): # -> None:
        """Sets the api_version of this V1ObjectFieldSelector.

        Version of the schema the FieldPath is written in terms of, defaults to \"v1\".  # noqa: E501

        :param api_version: The api_version of this V1ObjectFieldSelector.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def field_path(self): # -> None:
        """Gets the field_path of this V1ObjectFieldSelector.  # noqa: E501

        Path of the field to select in the specified API version.  # noqa: E501

        :return: The field_path of this V1ObjectFieldSelector.  # noqa: E501
        :rtype: str
        """
        ...
    
    @field_path.setter
    def field_path(self, field_path): # -> None:
        """Sets the field_path of this V1ObjectFieldSelector.

        Path of the field to select in the specified API version.  # noqa: E501

        :param field_path: The field_path of this V1ObjectFieldSelector.  # noqa: E501
        :type: str
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
    


