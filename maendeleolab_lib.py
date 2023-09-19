#!/usr/bin/env python3

import os, sys, pprint
from build_route import region_id, make_route_table, get_RouteTableId, make_association
from build_route import make_route_to_transit_gateway, make_route_to_nat_gateway 
from build_route import make_route_to_gateway, make_route_to_interface_id
from build_route import destroy_route, erase_routes, erase_route_entries, delete_route_entries
FPATH = os.environ.get('ENV_FPATH') #ENV_FPATH is in your environment variable file
sys.path.append(FPATH+'/maendeleolab_vpc')
import build_vpc
sys.path.append(FPATH+'/maendeleolab_subnet')
import build_subnet
sys.path.append(FPATH+'/maendeleolab_prefixList')
import build_prefix_list
#sys.path.append(FPATH+'/maendeleolab_transitGateway')
#import build_transit_gateway
#sys.path.append(FPATH+'/maendeleolab_natGateway')
#import build_nat_gateway
#sys.path.append(FPATH+'/maendeleolab_internetGateway')
#import build_igw
#sys.path.append(FPATH+'/maendeleolab_networkInterface')
#import build_network_interfaces

# ----------------------- End ---------------------
