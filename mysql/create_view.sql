use roqad;
-- ALTER TABLE devices CHANGE device_id __device_id varchar(50);

create view request_device AS 
select *
from
    requests
        JOIN
    devices
where
    requests.device_id = devices.__device_id
LIMIT 0 , 100