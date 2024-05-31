"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1alpha1StorageVersionCondition:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, last_transition_time=..., message=..., observed_generation=..., reason=..., status=..., type=..., local_vars_configuration=...) -> None:
        """V1alpha1StorageVersionCondition - a model defined in OpenAPI"""
        ...
    
    @property
    def last_transition_time(self): # -> None:
        """Gets the last_transition_time of this V1alpha1StorageVersionCondition.  # noqa: E501

        Last time the condition transitioned from one status to another.  # noqa: E501

        :return: The last_transition_time of this V1alpha1StorageVersionCondition.  # noqa: E501
        :rtype: datetime
        """
        ...
    
    @last_transition_time.setter
    def last_transition_time(self, last_transition_time): # -> None:
        """Sets the last_transition_time of this V1alpha1StorageVersionCondition.

        Last time the condition transitioned from one status to another.  # noqa: E501

        :param last_transition_time: The last_transition_time of this V1alpha1StorageVersionCondition.  # noqa: E501
        :type: datetime
        """
        ...
    
    @property
    def message(self): # -> None:
        """Gets the message of this V1alpha1StorageVersionCondition.  # noqa: E501

        A human readable message indicating details about the transition.  # noqa: E501

        :return: The message of this V1alpha1StorageVersionCondition.  # noqa: E501
        :rtype: str
        """
        ...
    
    @message.setter
    def message(self, message): # -> None:
        """Sets the message of this V1alpha1StorageVersionCondition.

        A human readable message indicating details about the transition.  # noqa: E501

        :param message: The message of this V1alpha1StorageVersionCondition.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def observed_generation(self): # -> None:
        """Gets the observed_generation of this V1alpha1StorageVersionCondition.  # noqa: E501

        If set, this represents the .metadata.generation that the condition was set based upon.  # noqa: E501

        :return: The observed_generation of this V1alpha1StorageVersionCondition.  # noqa: E501
        :rtype: int
        """
        ...
    
    @observed_generation.setter
    def observed_generation(self, observed_generation): # -> None:
        """Sets the observed_generation of this V1alpha1StorageVersionCondition.

        If set, this represents the .metadata.generation that the condition was set based upon.  # noqa: E501

        :param observed_generation: The observed_generation of this V1alpha1StorageVersionCondition.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def reason(self): # -> None:
        """Gets the reason of this V1alpha1StorageVersionCondition.  # noqa: E501

        The reason for the condition's last transition.  # noqa: E501

        :return: The reason of this V1alpha1StorageVersionCondition.  # noqa: E501
        :rtype: str
        """
        ...
    
    @reason.setter
    def reason(self, reason): # -> None:
        """Sets the reason of this V1alpha1StorageVersionCondition.

        The reason for the condition's last transition.  # noqa: E501

        :param reason: The reason of this V1alpha1StorageVersionCondition.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def status(self): # -> None:
        """Gets the status of this V1alpha1StorageVersionCondition.  # noqa: E501

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :return: The status of this V1alpha1StorageVersionCondition.  # noqa: E501
        :rtype: str
        """
        ...
    
    @status.setter
    def status(self, status): # -> None:
        """Sets the status of this V1alpha1StorageVersionCondition.

        Status of the condition, one of True, False, Unknown.  # noqa: E501

        :param status: The status of this V1alpha1StorageVersionCondition.  # noqa: E501
        :type: str
        """
        ...
    
    @property
    def type(self): # -> None:
        """Gets the type of this V1alpha1StorageVersionCondition.  # noqa: E501

        Type of the condition.  # noqa: E501

        :return: The type of this V1alpha1StorageVersionCondition.  # noqa: E501
        :rtype: str
        """
        ...
    
    @type.setter
    def type(self, type): # -> None:
        """Sets the type of this V1alpha1StorageVersionCondition.

        Type of the condition.  # noqa: E501

        :param type: The type of this V1alpha1StorageVersionCondition.  # noqa: E501
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
    


