# coding: utf-8

"""
    Penguin Statistics - REST APIs

    Backend APIs for Arknights drop rate statistics website 'Penguin Statistics': https://penguin-stats.io/  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: alvissreimu@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MatrixQueryResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'matrix': 'list[DropMatrixElement]'
    }

    attribute_map = {
        'matrix': 'matrix'
    }

    def __init__(self, matrix=None):  # noqa: E501
        """MatrixQueryResponse - a model defined in Swagger"""  # noqa: E501

        self._matrix = None
        self.discriminator = None

        if matrix is not None:
            self.matrix = matrix

    @property
    def matrix(self):
        """Gets the matrix of this MatrixQueryResponse.  # noqa: E501

        All elements in the result matrix  # noqa: E501

        :return: The matrix of this MatrixQueryResponse.  # noqa: E501
        :rtype: list[DropMatrixElement]
        """
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        """Sets the matrix of this MatrixQueryResponse.

        All elements in the result matrix  # noqa: E501

        :param matrix: The matrix of this MatrixQueryResponse.  # noqa: E501
        :type: list[DropMatrixElement]
        """

        self._matrix = matrix

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(MatrixQueryResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MatrixQueryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
