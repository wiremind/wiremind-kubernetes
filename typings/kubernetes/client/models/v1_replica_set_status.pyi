"""
This type stub file was generated by pyright.
"""

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.24
    Generated by: https://openapi-generator.tech
"""
class V1ReplicaSetStatus:
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    openapi_types = ...
    attribute_map = ...
    def __init__(self, available_replicas=..., conditions=..., fully_labeled_replicas=..., observed_generation=..., ready_replicas=..., replicas=..., local_vars_configuration=...) -> None:
        """V1ReplicaSetStatus - a model defined in OpenAPI"""
        ...
    
    @property
    def available_replicas(self): # -> None:
        """Gets the available_replicas of this V1ReplicaSetStatus.  # noqa: E501

        The number of available replicas (ready for at least minReadySeconds) for this replica set.  # noqa: E501

        :return: The available_replicas of this V1ReplicaSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @available_replicas.setter
    def available_replicas(self, available_replicas): # -> None:
        """Sets the available_replicas of this V1ReplicaSetStatus.

        The number of available replicas (ready for at least minReadySeconds) for this replica set.  # noqa: E501

        :param available_replicas: The available_replicas of this V1ReplicaSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def conditions(self): # -> None:
        """Gets the conditions of this V1ReplicaSetStatus.  # noqa: E501

        Represents the latest available observations of a replica set's current state.  # noqa: E501

        :return: The conditions of this V1ReplicaSetStatus.  # noqa: E501
        :rtype: list[V1ReplicaSetCondition]
        """
        ...
    
    @conditions.setter
    def conditions(self, conditions): # -> None:
        """Sets the conditions of this V1ReplicaSetStatus.

        Represents the latest available observations of a replica set's current state.  # noqa: E501

        :param conditions: The conditions of this V1ReplicaSetStatus.  # noqa: E501
        :type: list[V1ReplicaSetCondition]
        """
        ...
    
    @property
    def fully_labeled_replicas(self): # -> None:
        """Gets the fully_labeled_replicas of this V1ReplicaSetStatus.  # noqa: E501

        The number of pods that have labels matching the labels of the pod template of the replicaset.  # noqa: E501

        :return: The fully_labeled_replicas of this V1ReplicaSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, fully_labeled_replicas): # -> None:
        """Sets the fully_labeled_replicas of this V1ReplicaSetStatus.

        The number of pods that have labels matching the labels of the pod template of the replicaset.  # noqa: E501

        :param fully_labeled_replicas: The fully_labeled_replicas of this V1ReplicaSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def observed_generation(self): # -> None:
        """Gets the observed_generation of this V1ReplicaSetStatus.  # noqa: E501

        ObservedGeneration reflects the generation of the most recently observed ReplicaSet.  # noqa: E501

        :return: The observed_generation of this V1ReplicaSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @observed_generation.setter
    def observed_generation(self, observed_generation): # -> None:
        """Sets the observed_generation of this V1ReplicaSetStatus.

        ObservedGeneration reflects the generation of the most recently observed ReplicaSet.  # noqa: E501

        :param observed_generation: The observed_generation of this V1ReplicaSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def ready_replicas(self): # -> None:
        """Gets the ready_replicas of this V1ReplicaSetStatus.  # noqa: E501

        readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition.  # noqa: E501

        :return: The ready_replicas of this V1ReplicaSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @ready_replicas.setter
    def ready_replicas(self, ready_replicas): # -> None:
        """Sets the ready_replicas of this V1ReplicaSetStatus.

        readyReplicas is the number of pods targeted by this ReplicaSet with a Ready Condition.  # noqa: E501

        :param ready_replicas: The ready_replicas of this V1ReplicaSetStatus.  # noqa: E501
        :type: int
        """
        ...
    
    @property
    def replicas(self): # -> None:
        """Gets the replicas of this V1ReplicaSetStatus.  # noqa: E501

        Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller  # noqa: E501

        :return: The replicas of this V1ReplicaSetStatus.  # noqa: E501
        :rtype: int
        """
        ...
    
    @replicas.setter
    def replicas(self, replicas): # -> None:
        """Sets the replicas of this V1ReplicaSetStatus.

        Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/#what-is-a-replicationcontroller  # noqa: E501

        :param replicas: The replicas of this V1ReplicaSetStatus.  # noqa: E501
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
    


