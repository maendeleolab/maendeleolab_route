#!/usr/bin/env python3

import os, sys, pprint
from build_route import region_id, make_route_table, get_RouteTableId, make_association
from build_route import make_route_to_transit_gateway, make_route_to_nat_gateway 
from build_route import make_route_to_gateway, make_route_to_interface_id
from build_route import destroy_route, erase_routes, erase_route_entries
FPATH = os.environ.get('ENV_FPATH') #ENV_FPATH is in your environment variable file
sys.path.append(FPATH+'/maendeleolab_route/vpc')
import build_vpc
sys.path.append(FPATH+'/maendeleolab_route/subnets')
import build_subnet
sys.path.append(FPATH+'/maendeleolab_route/transit_gateway')
import build_transit_gateway
sys.path.append(FPATH+'/maendeleolab_route/nat_gateway')
import build_nat_gateway
sys.path.append(FPATH+'/maendeleolab_route/internet_gateway')
import build_igw
sys.path.append(FPATH+'/maendeleolab_route/network_interfaces')
import build_network_interfaces

# ----------------------- End ---------------------
