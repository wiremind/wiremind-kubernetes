"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V2beta2ContainerResourceMetricSource:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, container=..., name=..., target=..., local_vars_configuration=...) -> None:
        """V2beta2ContainerResourceMetricSource - a model defined in OpenAPI"""
        ...
    
    @property
    def container(self): # -> None:
        """Gets the container of this V2beta2ContainerResourceMetricSource.  # noqa: E501

        container is the name of the container in the pods of the scaling target  # noqa: E501

        :return: The container of this V2beta2ContainerResourceMetricSource.  # noqa: E501
        :rtype: str
        """
        ...
    
    @container.setter
    def container(self, container): # -> None:
        """Sets the container of this V2beta2ContainerResourceMetricSource.

        container is the name of the container in the pods of the scaling target  # noqa: E501

        :param container: The container of this V2beta2ContainerResourceMetricSource.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this V2beta2ContainerResourceMetricSource.  # noqa: E501

        name is the name of the resource in question.  # noqa: E501

        :return: The name of this V2beta2ContainerResourceMetricSource.  # noqa: E501
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this V2beta2ContainerResourceMetricSource.

        name is the name of the resource in question.  # noqa: E501

        :param name: The name of this V2beta2ContainerResourceMetricSource.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def target(self): # -> None:
        """Gets the target of this V2beta2ContainerResourceMetricSource.  # noqa: E501


        :return: The target of this V2beta2ContainerResourceMetricSource.  # noqa: E501
        :rtype: V2beta2MetricTarget
        """
        ...
    
    @target.setter
    def target(self, target): # -> None:
        """Sets the target of this V2beta2ContainerResourceMetricSource.


        :param target: The target of this V2beta2ContainerResourceMetricSource.  # noqa: E501
        :type: V2beta2MetricTarget
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
    


