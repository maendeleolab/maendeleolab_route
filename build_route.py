#!/usr/bin/python3

Goal = '''
to create route/s in aws
Author: Pat@Maendeleolab
'''

#Module imports
import logging, sys, os, json
from datetime import datetime
from time import sleep

#Path to local home and user folder
FPATH = os.environ.get('ENV_FPATH')

#logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ',\
                                                                        filename=FPATH+'/maendeleolab_route/route.log', level=logging.INFO)

#adding flexibility for regions
def region_id(name='us-east-1'):
                return name # e.g: 'us-east-1'

def verify_route(route_name, region='us-east-1'):
        ''' Verifies if route name already exists '''
        try:
                output = os.popen('aws ec2 describe-route-tables --filters Name=tag:Name,Values=' + route_name + ' --region '+ region).read()
                route_data = json.loads(str(output))
                if len(route_data['RouteTables']) > 0:
                        print(route_name + ' already exists!...')
                        return 1
        except Exception as err:
                logging.info(err)
                print('Logging "verify_route" in route.log...')

#create route table
def make_route_table(**kwargs):
        try:
                if verify_route(kwargs['Route_table_name'],kwargs['Region']) == 1:
                        pass
                else:
                        os.system("aws ec2 create-route-table \
                                --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=" + kwargs['Route_table_name'] + "},\
                                                                          {Key=" + kwargs['Tag_key'] + ",Value=" + kwargs['Tag_value'] + "}]'\
                                --vpc-id " + kwargs['Vpc_Id'] + "\
                                --region " + kwargs['Region'] 
                        )
                        logging.info('Created route:' + kwargs['Route_table_name'])
                        print(f'Created route: {kwargs["Route_table_name"]} in {kwargs["Region"]}...')
        except Exception as err:
                logging.info(err)
                print('Logging "make_route_table" error in route.log...')

#create route 
def make_route_to_transit_gateway(**kwargs):
        try:
                os.system("aws ec2 create-route \
                        --destination-cidr-block " + kwargs['Destination_network'] + "\
                        --transit-gateway-id " + kwargs['Transit_gateway_id'] + "\
                        --route-table-id " + kwargs['Route_table_Id'] + "\
                        --region " + kwargs['Region'] 
                )
                logging.info('Created route for destination network:' + kwargs['Destination_network'] + ' in route table:' + kwargs['Route_table_Id'])
                print(f'Added route entry: {kwargs["Destination_network"]} in route table: {kwargs["Route_table_Id"]} in {kwargs["Region"]}...')
        except Exception as err:
                logging.info(err)
                print('Logging "make_route_to_transit_gateway" error in route.log...')

def make_pl_route_to_transit_gateway(**kwargs):
        try:
                os.system("aws ec2 create-route \
                        --destination-prefix-list-id " + kwargs['Destination_prefix_list'] + "\
                        --transit-gateway-id " + kwargs['Transit_gateway_id'] + "\
                        --route-table-id " + kwargs['Route_table_Id'] + "\
                        --region " + kwargs['Region'] 
                )
                logging.info('Created route for destination prefix list:' + kwargs['Destination_prefix_list'] + ' in route table:' + kwargs['Route_table_Id'])
                print(f'Added route entries list: {kwargs["Destination_prefix_list"]} in route table: {kwargs["Route_table_Id"]} in {kwargs["Region"]}...')
        except Exception as err:
                logging.info(err)
                print('Logging "make_prefix_list_route_to_transit_gateway" error in route.log...')

def make_route_to_nat_gateway(**kwargs):
        try:
                os.system("aws ec2 create-route \
                        --route-table-id "      + kwargs['Route_table_Id'] + " \
                        --destination-cidr-block " + kwargs['Destination_network'] + " \
                        --nat-gateway-id " + kwargs['Nat_gateway_id'] + " \
                        --region " + kwargs['Region'] 
                )
                logging.info('Created route for destination network:' + kwargs['Destination_network'] + ' in route table:' + kwargs['Route_table_Id'])
                print('Added route entry: {kwargs["Destination_network"]} in route table: {kwargs["Route_table_Id"] in {kwargs["Region"]}...')
        except Exception as err:
                logging.info(err)
                print('Logging "make_route_to_nat_gateway" error in route.log...')

def make_route_to_gateway(**kwargs): #gateway can be a virtual private gateway or internet gateway
        try:
                os.system("aws ec2 create-route \
                        --gateway-id " + kwargs['Gateway_id'] + "\
                        --destination-cidr-block " + kwargs['Destination_network'] + "\
                        --route-table-id " + kwargs['Route_table_Id'] + "\
                        --region " + kwargs['Region'] 
                )
                logging.info('Created route for destination network:' + kwargs['Destination_network'] + ' in route table:' + kwargs['Route_table_Id'])
                print(f'Added route entry: {kwargs["Destination_network"]} in route table: {kwargs["Route_table_Id"]} in {kwargs["Region"]}...')
        except Exception as err:
                logging.info(err)
                print('Logging "make_route_to_gateway" error in route.log...')

def make_route_to_vpc_peering(**kwargs): 
        try:
                os.system("aws ec2 create-route \
                        --vpc-peering-connection-id " + kwargs['Vpc_peering_id'] + "\
                        --destination-cidr-block " + kwargs['Destination_network'] + "\
                        --route-table-id " + kwargs['Route_table_Id'] + "\
                        --region " + kwargs['Region'] 
                )
                logging.info('Created route for destination network:' + kwargs['Destination_network'] + ' in route table:' + kwargs['Route_table_Id'])
                print(f'Added route entry: {kwargs["Destination_network"]} in route table: {kwargs["Route_table_Id"]} in {kwargs["Region"]}...')
        except Exception as err:
                logging.info(err)
                print('Logging "make_route_to_vpc_peering" error in route.log...')

def make_route_to_interface_id(**kwargs):
        try:
                os.system("aws ec2 create-route \
                        --network-interface-id " + kwargs['Interface_id'] + "\
                        --destination-cidr-block " + kwargs['Destination_network'] + "\
                        --route-table-id " + kwargs['Route_table_Id'] + "\
                        --region " + kwargs['Region'] 
                )
                logging.info('Created route for destination network:' + kwargs['Destination_network'] + ' in route table:' + kwargs['Route_table_Id'])
                print(f'Added route entry: {kwargs["Destination_network"]} in route table: {kwargs["Route_table_Id"]} in {kwargs["Region"]}...')
        except Exception as err:
                logging.info(err)
                print('Logging "make_route_to_interface_id" error in route.log...')

def make_route_to_instance_id(**kwargs):
        os.system("aws ec2 create-route \
                --instance-id " + kwargs['Instance_id'] + "\
                --destination-cidr-block " + kwargs['Destination_network'] + "\
                --route-table-id " + kwargs['Route_table_Id'] + "\
                --region " + kwargs['Region'] 
        )
        logging.info('Created route for destination network:' + kwargs['Destination_network'] + ' in route table:' + kwargs['Route_table_Id'])

def get_RouteTableId(route_table_name, region='us-east-1'):
        ''' Gets resource id from json output and can be used in deploy scripts '''
        try:
                output = os.popen('aws ec2 describe-route-tables --filters Name=tag:Name,Values=' + route_table_name + " --region "+ region).read()
                route_table_data = json.loads(str(output))
                data = route_table_data['RouteTables'][0]['RouteTableId']
                return data
        except Exception as err:
                logging.info(err)
                print('Logging "get_RouteTableId" to route.log...')

def get_AssociationId(route_table_name, region='us-east-1'):
        ''' Gets resource id from json output and can be used in deploy scripts '''
        output = os.popen('aws ec2 describe-route-tables --filter --route-table-ids ' + route_table_name + " --region "+ region).read()
        route_table_data = json.loads(str(output))
        data = route_table_data['RouteTables'][0]['Associations']
        return data

def make_association(**kwargs):
        os.system("aws ec2 associate-route-table \
                --route-table-id " + kwargs['Route_table_name'] + " \
                --subnet-id " + kwargs['Subnet_name'] + " \
                --region " + kwargs['Region']
        )

def disassociation_route(**kwargs):
        os.system("aws ec2 disassociate-route-table \
                ----association-id " + kwargs['AssociationId'] + " \
                --region " + kwargs['Region']
        )

def destroy_route(Route_id,region='us-east-1'):
        try:
                os.system('aws ec2 delete-route-table --route-table-id ' + Route_id + ' --region '+ region)
                logging.info('Deleted Route Id: ' + Route_id + ' in region: ' + region)
        except Exception as err:
                print('Logging "destroy_route" error to route.log...')
                logging.info(err)

def erase_route_entries(route_table, region='us-east-1'):
        try:
                ''' Deletes route entries '''
                output = os.popen('aws ec2 describe-route-tables  --region ' + region).read()
                route_data = json.loads(str(output))
                for data in route_data['RouteTables']:
                    #print(data['RouteTableId'])
                    if data['RouteTableId'] == route_table:
                        print(f'Delete route entries in {route_table}...')
                        for entry in data['Routes']:
                            #logging.info('Logging erase_route_entries: ' + data)
                            print(f'Removing {entry["DestinationCidrBlock"]} from {route_table}...')
                            os.system('aws ec2 delete-route --destination-cidr-block '+ entry["DestinationCidrBlock"] + '\
                                    --route-table-id '+ route_table)

                new_data = json.dumps(data, indent=2)
                print(new_data)
        except Exception as err:
                logging.info(err)
                print('Logging error to route.log...')

def erase_routes(region='us-east-1'):
        try:
                ''' Deletes all routes that do not have any dependencies '''
                output = os.popen('aws ec2 describe-route-tables  --region ' + region).read()
                route_data = json.loads(str(output))
                for data in route_data['RouteTables']:
                        print('Delete: ' + data['RouteTableId'])
                        logging.info('Logging erase_routes: ' + data['RouteTableId'])
                        destroy_route(data['RouteTableId'], region=region)

                new_data = json.dumps(data, indent=2)
                print(new_data)
        except Exception as err:
                logging.info(err)
                print('Logging error to route.log...')

# ------------------------------------------ End -----------------------------------------------

