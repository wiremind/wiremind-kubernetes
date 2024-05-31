"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1ResourceRule:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, api_groups=..., resource_names=..., resources=..., verbs=..., local_vars_configuration=...) -> None:
        """V1ResourceRule - a model defined in OpenAPI"""
        ...
    
    @property
    def api_groups(self): # -> None:
        """Gets the api_groups of this V1ResourceRule.  # noqa: E501

        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  \"*\" means all.  # noqa: E501

        :return: The api_groups of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        ...
    
    @api_groups.setter
    def api_groups(self, api_groups): # -> None:
        """Sets the api_groups of this V1ResourceRule.

        APIGroups is the name of the APIGroup that contains the resources.  If multiple API groups are specified, any action requested against one of the enumerated resources in any API group will be allowed.  \"*\" means all.  # noqa: E501

        :param api_groups: The api_groups of this V1ResourceRule.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def resource_names(self): # -> None:
        """Gets the resource_names of this V1ResourceRule.  # noqa: E501

        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  \"*\" means all.  # noqa: E501

        :return: The resource_names of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        ...
    
    @resource_names.setter
    def resource_names(self, resource_names): # -> None:
        """Sets the resource_names of this V1ResourceRule.

        ResourceNames is an optional white list of names that the rule applies to.  An empty set means that everything is allowed.  \"*\" means all.  # noqa: E501

        :param resource_names: The resource_names of this V1ResourceRule.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def resources(self): # -> None:
        """Gets the resources of this V1ResourceRule.  # noqa: E501

        Resources is a list of resources this rule applies to.  \"*\" means all in the specified apiGroups.  \"*/foo\" represents the subresource 'foo' for all resources in the specified apiGroups.  # noqa: E501

        :return: The resources of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        ...
    
    @resources.setter
    def resources(self, resources): # -> None:
        """Sets the resources of this V1ResourceRule.

        Resources is a list of resources this rule applies to.  \"*\" means all in the specified apiGroups.  \"*/foo\" represents the subresource 'foo' for all resources in the specified apiGroups.  # noqa: E501

        :param resources: The resources of this V1ResourceRule.  # noqa: E501
        :type: list[str]
        """
        ...
    
    @property
    def verbs(self): # -> None:
        """Gets the verbs of this V1ResourceRule.  # noqa: E501

        Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :return: The verbs of this V1ResourceRule.  # noqa: E501
        :rtype: list[str]
        """
        ...
    
    @verbs.setter
    def verbs(self, verbs): # -> None:
        """Sets the verbs of this V1ResourceRule.

        Verb is a list of kubernetes resource API verbs, like: get, list, watch, create, update, delete, proxy.  \"*\" means all.  # noqa: E501

        :param verbs: The verbs of this V1ResourceRule.  # noqa: E501
        :type: list[str]
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
    


