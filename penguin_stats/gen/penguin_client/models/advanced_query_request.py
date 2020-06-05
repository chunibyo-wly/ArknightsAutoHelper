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


class AdvancedQueryRequest(object):
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
        'queries': 'list[SingleQuery]'
    }

    attribute_map = {
        'queries': 'queries'
    }

    def __init__(self, queries=None):  # noqa: E501
        """AdvancedQueryRequest - a model defined in Swagger"""  # noqa: E501

        self._queries = None
        self.discriminator = None

        if queries is not None:
            self.queries = queries

    @property
    def queries(self):
        """Gets the queries of this AdvancedQueryRequest.  # noqa: E501

        The list of queries.  # noqa: E501

        :return: The queries of this AdvancedQueryRequest.  # noqa: E501
        :rtype: list[SingleQuery]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this AdvancedQueryRequest.

        The list of queries.  # noqa: E501

        :param queries: The queries of this AdvancedQueryRequest.  # noqa: E501
        :type: list[SingleQuery]
        """

        self._queries = queries

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
        if issubclass(AdvancedQueryRequest, dict):
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
        if not isinstance(other, AdvancedQueryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
