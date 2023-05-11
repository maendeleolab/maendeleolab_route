#!/usr/bin/env python3
import delete_routes_list
from maendeleolab_lib import *


for route in delete_routes_list.useast1_app_list:
    delete_route_entries(
        get_RouteTableId('DEFAULT','us-east-1'), # route_table 
        route, # route entry 
        'us-east-1', # region
    )
