# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1DataVolumeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'content_type': 'str',
        'pvc': 'V1PersistentVolumeClaimSpec',
        'source': 'V1alpha1DataVolumeSource'
    }

    attribute_map = {
        'content_type': 'contentType',
        'pvc': 'pvc',
        'source': 'source'
    }

    def __init__(self, content_type=None, pvc=None, source=None):
        """
        V1alpha1DataVolumeSpec - a model defined in Swagger
        """

        self._content_type = None
        self._pvc = None
        self._source = None

        if content_type is not None:
          self.content_type = content_type
        self.pvc = pvc
        self.source = source

    @property
    def content_type(self):
        """
        Gets the content_type of this V1alpha1DataVolumeSpec.
        DataVolumeContentType options: \"kubevirt\", \"archive\"

        :return: The content_type of this V1alpha1DataVolumeSpec.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this V1alpha1DataVolumeSpec.
        DataVolumeContentType options: \"kubevirt\", \"archive\"

        :param content_type: The content_type of this V1alpha1DataVolumeSpec.
        :type: str
        """

        self._content_type = content_type

    @property
    def pvc(self):
        """
        Gets the pvc of this V1alpha1DataVolumeSpec.
        PVC is the PVC specification

        :return: The pvc of this V1alpha1DataVolumeSpec.
        :rtype: V1PersistentVolumeClaimSpec
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """
        Sets the pvc of this V1alpha1DataVolumeSpec.
        PVC is the PVC specification

        :param pvc: The pvc of this V1alpha1DataVolumeSpec.
        :type: V1PersistentVolumeClaimSpec
        """
        if pvc is None:
            raise ValueError("Invalid value for `pvc`, must not be `None`")

        self._pvc = pvc

    @property
    def source(self):
        """
        Gets the source of this V1alpha1DataVolumeSpec.
        Source is the src of the data for the requested DataVolume

        :return: The source of this V1alpha1DataVolumeSpec.
        :rtype: V1alpha1DataVolumeSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this V1alpha1DataVolumeSpec.
        Source is the src of the data for the requested DataVolume

        :param source: The source of this V1alpha1DataVolumeSpec.
        :type: V1alpha1DataVolumeSource
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1DataVolumeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
