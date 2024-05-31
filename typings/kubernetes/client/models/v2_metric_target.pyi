"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V2MetricTarget:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, average_utilization=..., average_value=..., type=..., value=..., local_vars_configuration=...) -> None:
        """V2MetricTarget - a model defined in OpenAPI"""
        ...
    
    @property
    def average_utilization(self): # -> None:
        """Gets the average_utilization of this V2MetricTarget.  # noqa: E501

        averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type  # noqa: E501

        :return: The average_utilization of this V2MetricTarget.  # noqa: E501
        :rtype: int
        """
        ...
    
    @average_utilization.setter
    def average_utilization(self, average_utilization): # -> None:
        """Sets the average_utilization of this V2MetricTarget.

        averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type  # noqa: E501

        :param average_utilization: The average_utilization of this V2MetricTarget.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def average_value(self): # -> None:
        """Gets the average_value of this V2MetricTarget.  # noqa: E501

        averageValue is the target value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :return: The average_value of this V2MetricTarget.  # noqa: E501
        :rtype: str
        """
        ...
    
    @average_value.setter
    def average_value(self, average_value): # -> None:
        """Sets the average_value of this V2MetricTarget.

        averageValue is the target value of the average of the metric across all relevant pods (as a quantity)  # noqa: E501

        :param average_value: The average_value of this V2MetricTarget.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def type(self): # -> None:
        """Gets the type of this V2MetricTarget.  # noqa: E501

        type represents whether the metric type is Utilization, Value, or AverageValue  # noqa: E501

        :return: The type of this V2MetricTarget.  # noqa: E501
        :rtype: str
        """
        ...
    
    @type.setter
    def type(self, type): # -> None:
        """Sets the type of this V2MetricTarget.

        type represents whether the metric type is Utilization, Value, or AverageValue  # noqa: E501

        :param type: The type of this V2MetricTarget.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def value(self): # -> None:
        """Gets the value of this V2MetricTarget.  # noqa: E501

        value is the target value of the metric (as a quantity).  # noqa: E501

        :return: The value of this V2MetricTarget.  # noqa: E501
        :rtype: str
        """
        ...
    
    @value.setter
    def value(self, value): # -> None:
        """Sets the value of this V2MetricTarget.

        value is the target value of the metric (as a quantity).  # noqa: E501

        :param value: The value of this V2MetricTarget.  # noqa: E501
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
    


