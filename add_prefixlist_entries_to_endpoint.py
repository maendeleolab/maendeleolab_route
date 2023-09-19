#!/usr/bin/env python3
from maendeleolab_lib import *

usage = '''
As of now 9/19/2023, you cannot reference a prefix-list to target an interface endpoint in a VPC route table.
This script is a workaround to give AWS builders the flexibility to add entries from the prefix list
to the VPC route table pointing at an interface endpoint.

Replace 'private_sec' with the name of the prefix list name
Replace 'eni-xxxx' with the interface ID
Replace 'DEFAULT' with the name of the route table
'''

for route in build_prefix_list.get_prefix_list_entries(build_prefix_list.get_prefix_list_id('private_sec', 'us-east-1'), 'us-east-1'):
    make_route_to_interface_id(
        Interface_id='eni-xxxx', # This can be the interface id of a gateway load balancer endpoint
        Destination_network=route,
        Route_table_Id=get_RouteTableId('DEFAULT','us-east-1'), # Route table name based on tag name
        Region='us-east-1',
    )
