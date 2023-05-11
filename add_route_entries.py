#!/usr/bin/env python3
import routes_list
from maendeleolab_lib import *


for route in routes_list.useast1_app_list:
    make_route_to_interface_id(
        Interface_id='eni-0fffeeff0cd7f8de9', # This can be the interface id of a gateway load balancer endpoint
        Destination_network=route,
        Route_table_Id=get_RouteTableId('DEFAULT','us-east-1'), # Route table name based on tag name
        Region='us-east-1',
    )
