#!/usr/bin/env python3

from maendeleolab_lib import *

#Add your regions to this list
maendeleolab_infra=[
        'us-east-1',
        'us-west-2',
        ]

#Add route table names that you want to delete to this list
route_table_list=[
        'NetworkDev1_Private',
        'NetworkDev1_Public',
        ]

#Delete and route entries from route tables in the above list
for route_id in route_table_list:
    erase_route_entries(get_RouteTableId(route_id), 'us-east-1')
    erase_route_entries(get_RouteTableId(route_id), 'us-west-2')

#Delete route tables in all regions referenced in maendeleolab_infra list  
for region in maendeleolab_infra:
    erase_routes(region)

# -------------------- End -----------------------
