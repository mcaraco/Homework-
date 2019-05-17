-- create database RidershipData;
use RidershipData;
create table cleaned (
	primary key(id),
    Years int,
    BasePay float,
    Benefits float,
    TotalPay float,
    Riders float,
    id int auto_increment not null
    );
    
    use ridershipdata;
    select * from cleaned;
    