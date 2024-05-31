"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V2beta1ResourceMetricStatus:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, current_average_utilization=..., current_average_value=..., name=..., local_vars_configuration=...) -> None:
        """V2beta1ResourceMetricStatus - a model defined in OpenAPI"""
        ...
    
    @property
    def current_average_utilization(self): # -> None:
        """Gets the current_average_utilization of this V2beta1ResourceMetricStatus.  # noqa: E501

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.  # noqa: E501

        :return: The current_average_utilization of this V2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @current_average_utilization.setter
    def current_average_utilization(self, current_average_utilization): # -> None:
        """Sets the current_average_utilization of this V2beta1ResourceMetricStatus.

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  It will only be present if `targetAverageValue` was set in the corresponding metric specification.  # noqa: E501

        :param current_average_utilization: The current_average_utilization of this V2beta1ResourceMetricStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def current_average_value(self): # -> None:
        """Gets the current_average_value of this V2beta1ResourceMetricStatus.  # noqa: E501

        currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the \"pods\" metric source type. It will always be set, regardless of the corresponding metric specification.  # noqa: E501

        :return: The current_average_value of this V2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        ...
    
    @current_average_value.setter
    def current_average_value(self, current_average_value): # -> None:
        """Sets the current_average_value of this V2beta1ResourceMetricStatus.

        currentAverageValue is the current value of the average of the resource metric across all relevant pods, as a raw value (instead of as a percentage of the request), similar to the \"pods\" metric source type. It will always be set, regardless of the corresponding metric specification.  # noqa: E501

        :param current_average_value: The current_average_value of this V2beta1ResourceMetricStatus.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def name(self): # -> None:
        """Gets the name of this V2beta1ResourceMetricStatus.  # noqa: E501

        name is the name of the resource in question.  # noqa: E501

        :return: The name of this V2beta1ResourceMetricStatus.  # noqa: E501
        :rtype: str
        """
        ...
    
    @name.setter
    def name(self, name): # -> None:
        """Sets the name of this V2beta1ResourceMetricStatus.

        name is the name of the resource in question.  # noqa: E501

        :param name: The name of this V2beta1ResourceMetricStatus.  # noqa: E501
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
    


