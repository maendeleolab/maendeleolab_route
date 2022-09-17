#!/usr/bin/env python3

from maendeleolab_lib import *

maendeleolab_infra = [
    'us-east-1',
    'us-west-2',
    ]

for region in maendeleolab_infra:
    #Creates private route table NetworkDev1_Private
    make_route_table(
        Route_table_name='NetworkDev1_Private',
        Vpc_Id=build_vpc.get_VpcId('NetworkDev1',region),
        Tag_key='Type',
        Tag_value='not-billable',
        Region=region
    )
    #Creates explicit route association to availability private zone 1 and 2
    make_association(
        Route_table_name=get_RouteTableId('NetworkDev1_Private',region),
        Subnet_name=build_subnet.get_SubnetId('NetworkDev1_Priv_1a',region),
        Region=region,
    )
    make_association(
        Route_table_name=get_RouteTableId('NetworkDev1_Private',region),
        Subnet_name=build_subnet.get_SubnetId('NetworkDev1_Priv_1b',region),
        Region=region
    )

    #Creates private route table NetworkDev1_Public
    make_route_table(
        Route_table_name='NetworkDev1_Public',
        Vpc_Id=build_vpc.get_VpcId('NetworkDev1',region),
        Tag_key='Type',
        Tag_value='not-billable',
        Region=region
    )
    #Creates explicit route association to availability public zone 1 and 2
    make_association(
        Route_table_name=get_RouteTableId('NetworkDev1_Public',region),
        Subnet_name=build_subnet.get_SubnetId('NetworkDev1_Pub_1a',region),
        Region=region,
    )
    make_association(
        Route_table_name=get_RouteTableId('NetworkDev1_Public',region),
        Subnet_name=build_subnet.get_SubnetId('NetworkDev1_Pub_1b',region),
        Region=region,
    )

# --------------------------- End -------------------------------


