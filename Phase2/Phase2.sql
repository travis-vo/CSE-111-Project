CREATE TABLE Customer
    (c_name varchar(255) NOT NULL,
    c_phone varchar(255) NOT NULL,
    c_address varchar(255) NOT NULL,
    c_ordernumber INT,
    c_custkey INT);

CREATE TABLE Brand
    (b_brandkey INT,
    b_name varchar(255) NOT NULL,
    b_price FLOAT);

CREATE TABLE Model
    (m_modelkey INT,
    m_name varchar(255) NOT NULL,
    m_brandkey INT,
    m_weight FLOAT,
    m_price FLOAT);

CREATE TABLE extraPackages
    (e_packkey INT,
    e_name varchar(255) NOT NULL,
    e_modelkey INT,
    e_price FLOAT);

CREATE TABLE estimatedQuote
    (q_total varchar(255) NOT NULL,
    q_quotekey INT,
    q_brandkey INT,
    q_comments varchar(255) NOT NULL);

CREATE TABLE verifiedQuote
    (vq_total varchar(255) NOT NULL,
    vq_quotekey INT,
    vq_vquotekey INT,
    vq_custkey INT,
    vq_comments varchar(255) NOT NULL); 


INSERT INTO Customer
VALUES('Bismark', '123-456-7890', '111 Boardfish Rd',1000,1),
('Iowa', '234-567-8901', '222 Catfish Rd',1001,2),
('Kongo', '345-678-9012', '333 Dogfish Rd',1002,3),
('Henry', '456-789-0123', '444 Maplefish Rd',1003,4),
('Caroline', '567-890-1234', '555 Bluefish Rd',1004,5);

INSERT INTO Brand
VALUES(50, 'Toyota', 2500.00),
(51, 'Ford', 2750.00),
(52, 'Mercedes', 4000.00),
(53, 'Jeep',2000.00),
(54, 'Honda',3000.00),
(55, 'Mazda',3250.00);

INSERT INTO Model
Values(100, 'Corolla', 50, 3030, 17425.00),
(101, 'RAV4', 50, 3512.5, 21050.00),
(102, 'Mustang', 51, 3678.5, 24405.00),
(103, 'Fusion', 51, 3613, 20420.00),
(104, 'AMG GT', 52, 4447, 85900.00),
(105, 'GLE SUV', 52, 4810.5, 50750.00),
(106, 'Wrangler', 53, 4209.5 ,26315.00),
(107, 'Renegade', 53, 3294, 20850.00),
(108, 'Accord', 54, 3290, 21770.00),
(109, 'Civic', 54, 2891.5, 18050.00),
(110, 'MX-5 Miata', 55, 2372, 23330.00),
(111, 'Mazda6', 55, 3509.5, 21075.00);


INSERT INTO extraPackages
Values(200, 'LE Convenience', 100, 1000.00),
(201, 'SE Premium', 100, 3000.00),
(202, 'XLE Grader Convenience', 101, 2500.00),
(203, 'XLE Grader Weather', 101, 2850.00),
(204, 'GT Performance', 102, 4350.00),
(205, 'Carbon Sport Interior', 102, 2750.00),
(206, 'All-Wheel-Drive', 103, 3250.00),
(207, 'Co-Pilot360', 103, 4000.00),
(208, 'Aerodynamics', 104, 2850.00),
(209, 'Lane Tracking', 104, 875.00),
(210, 'Comfort', 105, 850.00),
(211, 'Driver Assistance', 105, 1500.00),
(212, 'Heavy-Duty Electrical', 106, 795.00),
(213, 'Smokers', 106,30.00),
(214, 'Advanced Technology', 107, 1295.00),
(215, 'Uconnect 8.4', 107, 1395.00),
(216, 'All-Season Protection', 108, 424.00),
(217, 'Accord Protection', 108, 314.00),
(218, 'All-Season ProPack', 109, 394.00),
(219, 'Civic Protection', 109, 287.00),
(220, 'NONE', 110, 0.00),
(221, 'NONE', 111, 0.00);

INSERT INTO estimatedQuote
Values('qtotal1', 300, 50,'Toyota Brand'),
('qtotal2', 301, 51,'Ford Brand'),
('qtotal3', 302, 52,'Mercedes Brand'),
('qtotal4', 303, 53,'Jeep Brand'),
('qtotal4', 304, 54,'Honda Brand');

INSERT INTO verifiedQuote
Values('54356', 300, 400, 1,'finalized coating'),
('23626', 301, 401, 2,'finalized touches'),
('63624', 302, 402, 3,'finalized everything'),
('1476845', 303, 403, 4,'polished'),
('786585', 304, 404, 5,'looks amazing'),
('84769', 306, 406, 2,'wow');