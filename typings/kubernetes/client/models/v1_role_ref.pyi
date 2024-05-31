"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1RoleRef:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, api_group=..., kind=..., name=..., local_vars_configuration=...) -> None:
        """V1RoleRef - a model defined in OpenAPI"""
        ...
    
    @property
    def api_group(self): # -> None:
        """Gets the api_group of this V1RoleRef.  # noqa: E501

        APIGroup is the group for the resource being referenced  # noqa: E501

        :return: The api_group of this V1RoleRef.  # noqa: E501
        :rtype: str
        """
        ...
    
    @api_group.setter
    def api_group(self, api_group): # -> None:
        """Sets the api_group of this V1RoleRef.

        APIGroup is the group for the resource being referenced  # noqa: E501

        :param api_group: The api_group of this V1RoleRef.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def kind(self): # -> None:
        """Gets the kind of this V1RoleRef.  # noqa: E501

        Kind is the type of resource being referenced  # noqa: E501

        :return: The kind of this V1RoleRef.  # noqa: E501
        :rtype: str
        """
        ...
    
    @kind.setter
    def kind(self, kind): # -> None:
        """Sets the kind of this V1RoleRef.

        Kind is the type of resource being referenced  # noqa: E501

        :param kind: The kind of this V1RoleRef.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this V1RoleRef.  # noqa: E501

        Name is the name of resource being referenced  # noqa: E501

        :return: The name of this V1RoleRef.  # noqa: E501
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this V1RoleRef.

        Name is the name of resource being referenced  # noqa: E501

        :param name: The name of this V1RoleRef.  # noqa: E501
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
    


