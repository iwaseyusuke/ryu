# Copyright (C) 2018 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

from ryu.ofproto import ofproto_v1_0_parser


def generate(parser_name):
    parser = sys.modules[parser_name]

    def add_attr(key, value):
        value.__module__ = parser.__name__  # Necessary for stringify stuff
        setattr(parser, key, value)

    _classes = [
        ofproto_v1_0_parser.NXTSetControllerId,
    ]
    for cls in _classes:
        add_attr(cls.__name__, cls)
