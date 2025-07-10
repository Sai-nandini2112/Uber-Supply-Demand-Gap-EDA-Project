--#1 Total Trips by Status
SELECT Status, COUNT(*) AS total_requests
FROM uber_requests
GROUP BY Status;
--# Insight: Overall trip completion vs cancellation vs “no cars”.

--#2 Hourly Demand & Fulfillment
SELECT hour,
       COUNT(*) AS total_requests,
       SUM(CASE WHEN Status = 'Trip Completed' THEN 1 ELSE 0 END) AS completed,
       SUM(CASE WHEN Status != 'Trip Completed' THEN 1 ELSE 0 END) AS unfulfilled
FROM uber_requests
GROUP BY hour
ORDER BY hour;

--#Insight: See where fulfillment drops (peak hours, like 5–9 AM).

--#3 Pickup Point vs Status
SELECT [Pickup point], Status, COUNT(*) AS request_count
FROM uber_requests
GROUP BY [Pickup point], Status;

--Insight: City or Airport — which faces more cancellations or gaps.

--#4 Daypart vs Fulfilled

SELECT daypart,
       SUM(CASE WHEN Fulfilled = 'Yes' THEN 1 ELSE 0 END) AS fulfilled,
       SUM(CASE WHEN Fulfilled = 'No' THEN 1 ELSE 0 END) AS unfulfilled
FROM uber_requests
GROUP BY daypart
ORDER BY unfulfilled DESC;

--Insight: Which part of the day has highest demand-supply gap.

--#5 Fulfillment Rate by Hour

SELECT hour,
       ROUND(SUM(CASE WHEN Fulfilled = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS fulfillment_rate
FROM uber_requests
GROUP BY hour
ORDER BY fulfillment_rate ASC;

--Insight: Pinpoint hours with the worst fulfillment %.

--#6 Top 3 hours with most unfulfilled requests:
SELECT hour, COUNT(*) AS unfulfilled
FROM uber_requests
WHERE Fulfilled = 'No'
GROUP BY hour
ORDER BY unfulfilled DESC
LIMIT 3;

--#7 Weekday trend
SELECT weekday, COUNT(*) AS total
FROM uber_requests
GROUP BY weekday;

