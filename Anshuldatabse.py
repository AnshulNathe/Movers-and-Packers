import psycopg2
from datetime import date

host_name = "localhost"
database_name = "addbms"
user_name = "adbms"
password = "adbms"
port = 5432
con = None
cur = None


# try:py
con = psycopg2.connect(
    host=host_name,
    dbname=database_name,
    user=user_name,
    password=password,
    port=port,
)
print("connected to database")
# except:
    # print("connection is cant be created")
cur = con.cursor()
delete ='''
     drop table if exists bill cascade;
    drop table if exists vehicle cascade;
    drop table if exists shipping_request cascade;
    drop table if exists shipping_type cascade;
    drop table if exists address_base cascade;
    drop table if exists perm_address cascade;
    drop table if exists account cascade;
'''
account= '''
    create table account(
        id integer primary key,
        first_name varchar(20),
        last_name varchar(25),
        email_address varchar(50) unique not null,
        user_name varchar(20) unique not null,
        password varchar(25) not null,
        is_user boolean,
        is_admin boolean,
        is_staff boolean,
        verified_email_address boolean
    );
'''
perm_address= '''
    create table perm_address(
        address_id varchar(60) primary key,
        usr_id integer,
        line_1 varchar(25) not null,
        line_2  varchar(20),
        line_3 varchar(10),
        city varchar(25) not null,
        state varchar(25) not null,
        pincode integer not null,
        document varchar(30) not null,
        is_verified boolean ,
        constraint account_perm_address_fk foreign key(usr_id) references account(id) on delete cascade
    );
'''
address_base= '''
    create table address_base(
        address_id integer primary key,
        usr_id integer,
        line_1 varchar(25) not null,
        line_2  varchar(20),
        line_3 varchar(10),
        city varchar(25) not null,
        state varchar(25) not null,
        pincode integer not null,
        constraint account_adress_fk foreign key(usr_id) references account(id));
'''
shipping_type= '''
    create table shipping_type(
        id integer primary key,
        type_name varchar(20) not null        
    );
'''
shipping_request= '''
    create table shipping_request(
        id integer primary key,
        usr_id integer,
        pick_address  integer not null,
        drop_address integer not null,
        shipping_timestamp varchar(25) not null,
        shipping_type integer not null,
        expense_estimate integer ,
        is_approved boolean,
        constraint shipping_category_fk foreign key(shipping_type) references shipping_type(id) on delete cascade,
        constraint shipping_pick_address_fk foreign key(pick_address) references address_base(address_id) on delete cascade,
        constraint shipping_drop_address_fk foreign key(drop_address) references address_base(address_id) on delete cascade
        );'''
vehicle= '''
    create table vehicle(
        id integer primary key,
        driver_id integer,
        registration_no varchar(15) not null,
        insurance varchar not null,
        constraint account_adress_fk foreign key(driver_id) references account(id));
'''
bill= '''
    create table bill(
        bill_id integer primary key,
        shipping_id integer,
        amount integer not null,
        date_of_generation varchar not null,
        constraint account_adress_fk foreign key(shipping_id) references account(id));
'''
cur.execute(delete)
cur.execute(account)
cur.execute(perm_address)
cur.execute(address_base)
cur.execute(shipping_type)
cur.execute(shipping_request)
cur.execute(vehicle)
cur.execute(bill)

#         id integer primary key,
#         first_name varchar(20),
#         last_name varchar(25),
#         email_address varchar(50) unique not null,
#         user_name varchar(20) unique not null,
#         password varchar(25) not null,
#         is_user boolean,
#         is_admin boolean,
#         is_staff boolean,
#         verified_email_address boolean
acc = [
    ['1','Anshul','Nathe','nathe@2409.com','ans_123','passwd','t','t','t','t'],
    ['2','Gaurav','Bhamare','gaurav@2202.com','gau_869','passwd2','t','f','t','t'],
    ['3','Avinash','Kumar','avi@1809.com','avi_259','passwd3','t','f','f','t'],
    ['4','Yash','Patil','yash@1710.com','yash_639','passwd4','t','f','f','t'],

]

for x in acc:
    account_insert = "insert into account values( " + x[0] + ",'" + x[1] + "','" + x[2] + "','" + x[3] + "','" + x[4] + "','" + x[5] + "','" + x[6] + "','" + x[7] + "','" + x[8] + "','" + x[9]  + "');"    
    cur.execute(account_insert)



#         address_id varchar(60) primary key,
#         usr_id integer,
#         line_1 varchar(25) not null,
#         line_2  varchar(20),
#         line_3 varchar(10),
#         city varchar(25) not null,
#         state varchar(25) not null,
#         pincode integer not null,
#         document varchar(30) not null,
#         is_verified boolean ,
add = [
    ['1','1','nilkanti colony','mohan nagar','navsari','Amravati','Maharashtra','444604','Aadhar card','t'],
    ['2','3','kalyani nagar','near sai temple','VMV Road ','Nashik','Maharashtra','840563','Electrity bill','t'],
    ['3','2','shri nivas','arun colony','ring road','Nagpur','Maharashtra','555206','Aadhar card','t'],
    ['4','4','high street','balewadi','near baner','Pune','Maharashtra','422086','Aadhar card','t']
]

for x in add:
    perm_address_insert = "insert into perm_address values( " + x[0] + "," + x[1] + ",'"  + x[2] + "','" + x[3] + "','" + x[4] + "','" + x[5] + "','" + x[6] + "','" + x[7] + "','" + x[8] + "','" + x[9] + "');"    
    cur.execute(perm_address_insert)





# address_id varchar(60) primary key,
#         usr_id integer,
#         line_1 varchar(25) not null,
#         line_2  varchar(20),
#         line_3 varchar(10),
#         city varchar(25) not null,
#         state varchar(25) not null,
#         pincode integer not null,

base = [
    ['1','4','12A','nilkanti colony','navsari','Amravati','Maharashtra','444604'],
    ['2','3','26B','kalyani nagar','VMV Road ','Nashik','Maharashtra','840563'],
    ['3','3','37G','shri nivas','ring road','Nagpur','Maharashtra','555206'],
    ['4','4','48D','high street','near baner','Pune','Maharashtra','422086'],
]

for x in base:
    address_base_insert = "insert into address_base values( " + x[0] + "," + x[1] + ",'" + x[2] + "','" + x[3] + "','" + x[4] + "','" + x[5] + "','" + x[6] + "','" + x[7] + "');"    
    cur.execute(address_base_insert)


# shipping_type= '''
#     create table shipping_type(
#         id integer primary key,
#         type_name varchar(20) not null,
#         constraint account_adress_fk foreign key(id) references account(id)
        
#     );'''

ship = [
    ['1','house'],
    ['2','bike'],
    ['3','car'],
    ['4','office'],

]

for x in ship:
    shipping_type_insert = "insert into shipping_type values( " + x[0] + ",'" + x[1] + "');"    
    cur.execute(shipping_type_insert)


        # id integer primary key,
        # usr_id integer,
        # pick_address  integer not null,
        # drop_address integer not null,
        # shipping_timestamp varchar(25) not null,
        # shipping_type integer not null,
        # expense_estimate integer ,
        # is_approved boolean,


sreq= [
    ['1','3','2','3',str(date.today()),'1','0','t'],
    ['2','4','1','4',str(date.today()),'2','2000','t'],
    ['3','3','4','1',str(date.today()),'4','25000','t'],
]

for x in sreq:
    shipping_request_insert = "insert into shipping_request values(" + x[0] + "," + x[1] + "," + x[2] + "," + x[3] + ",'" + x[4] + "'," + x[5] + ","  + x[6] + ",'" + x[7] + "');"
    cur.execute(shipping_request_insert)




# vehicle= '''
#     create table vehicle(
#         id integer primary key,
#         driver_id integer,
#         registration_no varchar(15) not null,
#         insurance integer not null,




veh= [
    ['1','1','MH12A4567','PNCF6500'],
    ['2','1','MH45F6783','HGC8563'],
    ['3','2','MP01VB0980','LKJ5556'],
    ['4','2','KA31HD2348','CSX4286'],

]

for x in veh:
    vehicle_insert = "insert into vehicle values( " + x[0] + ",'" + x[1] + "','" + x[2] + "','" + x[3] + "');"    
    cur.execute(vehicle_insert)


# bill= '''
#     create table bill
#         bill_id varchar(20) primary key,
#         shipping_id integer,
#         amount integer not null,
#         date_of_generation integer not null,


bb= [
    ['1','1','4567','24-8-2019'],  
    ['2','2','6783','12-6-2020'],  
    ['3','3','7980','18-1-2021'],  
    ['4','4','2348','2-4-2022'],   

]

for x in bb:
    bill_insert = "insert into bill values( " + x[0] + "," + x[1] + ",'" + x[2] + "','" + x[3] + "');"    
    cur.execute(bill_insert)


con.commit()