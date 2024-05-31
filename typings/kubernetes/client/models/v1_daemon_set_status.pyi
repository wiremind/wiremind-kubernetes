"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1DaemonSetStatus:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, collision_count=..., conditions=..., current_number_scheduled=..., desired_number_scheduled=..., number_available=..., number_misscheduled=..., number_ready=..., number_unavailable=..., observed_generation=..., updated_number_scheduled=..., local_vars_configuration=...) -> None:
        """V1DaemonSetStatus - a model defined in OpenAPI"""
        ...
    
    @property
    def collision_count(self): # -> None:
        """Gets the collision_count of this V1DaemonSetStatus.  # noqa: E501

        Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.  # noqa: E501

        :return: The collision_count of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @collision_count.setter
    def collision_count(self, collision_count): # -> None:
        """Sets the collision_count of this V1DaemonSetStatus.

        Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.  # noqa: E501

        :param collision_count: The collision_count of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def conditions(self): # -> None:
        """Gets the conditions of this V1DaemonSetStatus.  # noqa: E501

        Represents the latest available observations of a DaemonSet's current state.  # noqa: E501

        :return: The conditions of this V1DaemonSetStatus.  # noqa: E501
        :rtype: list[V1DaemonSetCondition]
        """
        ...
    
    @conditions.setter
    def conditions(self, conditions): # -> None:
        """Sets the conditions of this V1DaemonSetStatus.

        Represents the latest available observations of a DaemonSet's current state.  # noqa: E501

        :param conditions: The conditions of this V1DaemonSetStatus.  # noqa: E501
        :type: list[V1DaemonSetCondition]
        """
        ...
    
    @property
    def current_number_scheduled(self): # -> None:
        """Gets the current_number_scheduled of this V1DaemonSetStatus.  # noqa: E501

        The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :return: The current_number_scheduled of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @current_number_scheduled.setter
    def current_number_scheduled(self, current_number_scheduled): # -> None:
        """Sets the current_number_scheduled of this V1DaemonSetStatus.

        The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :param current_number_scheduled: The current_number_scheduled of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def desired_number_scheduled(self): # -> None:
        """Gets the desired_number_scheduled of this V1DaemonSetStatus.  # noqa: E501

        The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :return: The desired_number_scheduled of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @desired_number_scheduled.setter
    def desired_number_scheduled(self, desired_number_scheduled): # -> None:
        """Sets the desired_number_scheduled of this V1DaemonSetStatus.

        The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :param desired_number_scheduled: The desired_number_scheduled of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def number_available(self): # -> None:
        """Gets the number_available of this V1DaemonSetStatus.  # noqa: E501

        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The number_available of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @number_available.setter
    def number_available(self, number_available): # -> None:
        """Sets the number_available of this V1DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param number_available: The number_available of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def number_misscheduled(self): # -> None:
        """Gets the number_misscheduled of this V1DaemonSetStatus.  # noqa: E501

        The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :return: The number_misscheduled of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @number_misscheduled.setter
    def number_misscheduled(self, number_misscheduled): # -> None:
        """Sets the number_misscheduled of this V1DaemonSetStatus.

        The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/  # noqa: E501

        :param number_misscheduled: The number_misscheduled of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def number_ready(self): # -> None:
        """Gets the number_ready of this V1DaemonSetStatus.  # noqa: E501

        numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition.  # noqa: E501

        :return: The number_ready of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @number_ready.setter
    def number_ready(self, number_ready): # -> None:
        """Sets the number_ready of this V1DaemonSetStatus.

        numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition.  # noqa: E501

        :param number_ready: The number_ready of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def number_unavailable(self): # -> None:
        """Gets the number_unavailable of this V1DaemonSetStatus.  # noqa: E501

        The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The number_unavailable of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @number_unavailable.setter
    def number_unavailable(self, number_unavailable): # -> None:
        """Sets the number_unavailable of this V1DaemonSetStatus.

        The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param number_unavailable: The number_unavailable of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def observed_generation(self): # -> None:
        """Gets the observed_generation of this V1DaemonSetStatus.  # noqa: E501

        The most recent generation observed by the daemon set controller.  # noqa: E501

        :return: The observed_generation of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @observed_generation.setter
    def observed_generation(self, observed_generation): # -> None:
        """Sets the observed_generation of this V1DaemonSetStatus.

        The most recent generation observed by the daemon set controller.  # noqa: E501

        :param observed_generation: The observed_generation of this V1DaemonSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def updated_number_scheduled(self): # -> None:
        """Gets the updated_number_scheduled of this V1DaemonSetStatus.  # noqa: E501

        The total number of nodes that are running updated daemon pod  # noqa: E501

        :return: The updated_number_scheduled of this V1DaemonSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @updated_number_scheduled.setter
    def updated_number_scheduled(self, updated_number_scheduled): # -> None:
        """Sets the updated_number_scheduled of this V1DaemonSetStatus.

        The total number of nodes that are running updated daemon pod  # noqa: E501

        :param updated_number_scheduled: The updated_number_scheduled of this V1DaemonSetStatus.  # noqa: E501
        :type: int
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
    


