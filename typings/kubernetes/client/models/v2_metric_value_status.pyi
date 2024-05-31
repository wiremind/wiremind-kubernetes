"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V2MetricValueStatus:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, average_utilization=..., average_value=..., value=..., local_vars_configuration=...) -> None:
        """V2MetricValueStatus - a model defined in OpenAPI"""
        ...
    
    @property
    def average_utilization(self): # -> None:
        """Gets the average_utilization of this V2MetricValueStatus.  # noqa: E501

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :return: The average_utilization of this V2MetricValueStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @average_utilization.setter
    def average_utilization(self, average_utilization): # -> None:
        """Sets the average_utilization of this V2MetricValueStatus.

        currentAverageUtilization is the current value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.  # noqa: E501

        :param average_utilization: The average_utilization of this V2MetricValueStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def average_value(self): # -> None:
        """Gets the average_value of this V2MetricValueStatus.  # noqa: E501

        averageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :return: The average_value of this V2MetricValueStatus.  # noqa: E501
        :rtype: str
        """
        ...
    
    @average_value.setter
    def average_value(self, average_value): # -> None:
        """Sets the average_value of this V2MetricValueStatus.

        averageValue is the current value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :param average_value: The average_value of this V2MetricValueStatus.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def value(self): # -> None:
        """Gets the value of this V2MetricValueStatus.  # noqa: E501

        value is the current value of the metric (as a quantity).  # noqa: E501

        :return: The value of this V2MetricValueStatus.  # noqa: E501
        :rtype: str
        """
        ...
    
    @value.setter
    def value(self, value): # -> None:
        """Sets the value of this V2MetricValueStatus.

        value is the current value of the metric (as a quantity).  # noqa: E501

        :param value: The value of this V2MetricValueStatus.  # noqa: E501
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
    


