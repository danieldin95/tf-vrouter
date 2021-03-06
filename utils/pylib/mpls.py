#
# Copyright (c) 2019 Juniper Networks, Inc. All rights reserved.
#

import constants
from object_base import *

from vr_py_sandesh.vr_py.ttypes import *


class Mpls(ObjectBase, vr_mpls_req):
    """
    Mpls class to create mpls object

    Mandatory Parameters:
    --------------------
    mr_label : int
        Mpls label

    Optional Parameters:
    -------------------
    mr_rid : int
        Mpls request id
    mr_nhid : int
        Mpls nexthop id
    """

    def __init__(self, mr_label, mr_rid=0, mr_nhid=None):
        super(Mpls, self).__init__()
        vr_mpls_req.__init__(self)
        self.h_op = constants.SANDESH_OPER_ADD
        self.mr_label = mr_label
        self.mr_rid = mr_rid
        if mr_nhid:
            self.mr_nhid = mr_nhid
        self.sreq_class = vr_mpls_req.__name__

    def label(self):
        """Returns mr_label"""
        return self.mr_label

    def get(self, key):
        """
        Queries vrouter and return the key value from the response xml file
        """
        self.h_op = constants.SANDESH_OPER_GET
        return super(Mpls, self).get(key)

    def get_mr_label(self):
        """
        Queries vrouter and returns the mr_label value from the response
        xml file
        """
        return int(self.get('mr_label'))

    def delete(self):
        self.h_op = constants.SANDESH_OPER_DEL
        super(Mpls, self).delete()
