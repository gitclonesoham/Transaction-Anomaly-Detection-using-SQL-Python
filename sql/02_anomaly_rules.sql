WITH stats AS (
    SELECT
        AVG(sales) AS avg_sales,
        STDDEV(sales) AS std_sales,
        AVG(discount) AS avg_discount
    FROM sales
)
SELECT
    s.order_id,
    s.customer_id,
    s.sales,
    s.discount,
    s.profit,
    CASE
        WHEN s.sales > (stats.avg_sales + 3 * stats.std_sales)
            THEN 'High Value Order'
        WHEN s.discount > (stats.avg_discount * 2)
            AND s.profit < 0
            THEN 'High Discount, Low Profit'
        ELSE 'Normal'
    END AS anomaly_type
FROM sales s
CROSS JOIN stats
WHERE
    s.sales > (stats.avg_sales + 3 * stats.std_sales)
    OR (s.discount > (stats.avg_discount * 2) AND s.profit < 0);
