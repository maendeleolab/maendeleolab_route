# maendeleolab_route
![GitHub commit activity](https://img.shields.io/github/last-commit/maendeleolab/maendeleolab_route)

<img src="/images/banner.png" width=400>


## [Context](#Context)

- This repo was built to create route tables, add route entries and remove routes. 

- It can be used on any Linux environment in AWS or on-premises. 

- Install Python 3.6.9 (or higher) and awscli version 2.

- The scripts are idempotent.

- The line above means, if the resource is tagged with a name that already exists, it will not create another one.

## [Prerequisites](#Prerequisites)

- Please watch the [requirements steps](https://www.youtube.com/watch?v=gMM-d1uZ0Ks&t=12s)

- It helps to be familiar with Linux basics commands.

- Must have awscli version 2 and Python 3.6.9 (or higher) installed.

- I recommend dedicating an instance (or on-premises server) to programmatically run the scripts.  

- Assign a role with programmatic access to the instance/server default profile.

- Run this command 'export ENV_FPATH="folder-path" ' 

- Replace folder-path with your folder location (this is the folder, where you will download the repo). 

See the example below.

```
export ENV_FPATH="/home/ubuntu"
```

## [Dependencies](#Dependencies)
### The deploy script needs to access the build scripts in the following projects. 
- [maendeleolab_vpc](https://github.com/maendeleolab/maendeleolab_vpc) 
- [maendeleolab_subnet](https://github.com/maendeleolab/maendeleolab_subnet)

## [Walk-through](#Walk-through)

**1**  - Make sure to comply with the prerequisites mentioned above.

**2**  - Update and install the latest packages of your Linux distribution system.

**3**  - Clone this repo to the instance/server using the syntax below.

```
git clone https://github.com/maendeleolab/maendeleolab_route.git
```

**4**  - cd to folder maendeleolab_route

```
cd maendeleolab_route
```

**5**  - List the files in the folder with the **ls** command. It should match the files below.

**Note:** A file named **route.log** will be created to store the scripts logs, when you run the script for the first time.

Remember to use it to monitor your environment or troubleshoot an issue.

```
├── LICENSE
├── README.md
├── add_route_entries.py
├── build_route.py
├── delete_resources.py
├── delete_routes_list.py
├── deploy_NetworkDev1.py
├── maendeleolab_lib.py
├── remove_route_entries.py
├── route.log
└── routes_list.py
```

**6**  - I recommend running the script **deploy_NetworkDev1.py** to see what the expected results look like.

The script will create route tables in your VPC.

This script will become your single source of truth for your route tables. 

```
./deploy_NetworkDev1.py or python3 deploy_NetworkDev1.py
```

**7**  - Verify the expected results are present in the console. 

**8**  - Run the script again to verify idempotency is working as expected. 

**9**  - Route tables list resources do not cost you anything, but in case you decide to delete them. You can run the script **delete_resources.py**
	
**Note:** The script deletes all route table resources that do not have any dependencies. 
	
This means, if the route table name doesn't have any subnets and route entries associated to it. 

```
./delete_resources.py or python3 delete_resources.py
```

**11** - If you get to this step, congratulations for being brave to do it! 

- [] **Additonal scripts usage**

You can use **routes_list.py** to define your route entries like prefix list.</br>
```
# Examples of routes lists
useast1_app_list = ['10.1.33.0/24', '10.11.3.0/24', '10.0.3.0/24']
useast1_dev_list = ['100.1.33.0/24', '100.11.3.0/24', '100.0.3.0/24']
```

Use **add_route_entries.py** to add routes to route tables.</br>
You specify the ENI ID, the routes list, the tag name of the route table and the region.</br>
```
# Replace the eni id with yours and 'DEFAULT' with the tage name of your route table.
for route in routes_list.useast1_app_list:
    make_route_to_interface_id(
        Interface_id='eni-0ffgeeff0dd7f8dc9', # This can be the interface id of a gateway load balancer endpoint
        Destination_network=route,
        Route_table_Id=get_RouteTableId('DEFAULT','us-east-1'), # Route table name based on tag name
        Region='us-east-1',
    )
# When ready execute this command
./add_route_entries.py
``` 

Use **delete_routes_list.py** to define the route entries list to delete from a route table.
```
useast1_app_list = ['10.1.33.0/24', ]
useast1_dev_list = ['100.1.33.0/24', '100.0.3.0/24']
```

Use **delete_route_entries.py** to delete routes from route tables.</br>
You specify the ENI ID, the routes list, the tag name of the route table and the region.</br>
```
# Replace the eni id with yours and 'DEFAULT' with the tage name of your route table.
for route in delete_routes_list.useast1_app_list:
    delete_route_entries(
        get_RouteTableId('DEFAULT','us-east-1'), # route_table
        route, # route entry
        'us-east-1', # region
    )
# When ready execute this command
./delete_route_entries.py
```

## [Support](#Support)
If you find this script useful, please support it with a shout out on your favorite social media platform!

![Twitter](https://img.shields.io/twitter/follow/maendeleolab?style=social)
```
Twitter : @maendeleolab
Instagram : @maendeleolab
```
## [License](#License)
GNU GENERAL PUBLIC LICENSE

