CREATE DATABASE gps_tracking;
USE gps_tracking;
CREATE TABLE gps_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id VARCHAR(20),
    vehicle_number VARCHAR(20),
    datetime_utc DATETIME,
    gps_location TEXT,
    lon DOUBLE,
    lat DOUBLE,
    speed DECIMAL(5,2),
    direction INT,
    engine_status ENUM('ON', 'OFF'),
    odometer BIGINT,
    car_status ENUM('START', 'STOP'),
    vehicle_type VARCHAR(20),
    received_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
