-- Smart Traffic Management System Database Schema & Queries

-- Create Database
CREATE DATABASE IF NOT EXISTS smart_traffic;
USE smart_traffic;

-- Traffic information table
CREATE TABLE IF NOT EXISTS traffic (
    id INT PRIMARY KEY AUTO_INCREMENT,
    road INT NOT NULL,
    vehicle_count INT NOT NULL,
    signal_status VARCHAR(10) NOT NULL,
    emergency BOOLEAN DEFAULT FALSE,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample traffic data
INSERT INTO traffic
(road, vehicle_count, signal_status, emergency)
VALUES
(1, 15, 'RED', FALSE),
(2, 8, 'RED', FALSE),
(3, 25, 'GREEN', FALSE),
(4, 5, 'RED', FALSE);

-- View all traffic data
SELECT * FROM traffic;

-- Find road with highest traffic
SELECT *
FROM traffic
WHERE vehicle_count = (
    SELECT MAX(vehicle_count)
    FROM traffic
);

-- Find emergency vehicles
SELECT *
FROM traffic
WHERE emergency = TRUE;

-- Update traffic count
UPDATE traffic
SET vehicle_count = 30
WHERE road = 3;

-- Change signal
UPDATE traffic
SET signal_status = 'GREEN'
WHERE road = 3;

-- Delete a traffic record
DELETE FROM traffic
WHERE id = 1;
