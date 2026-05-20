USE superstore_db;
-- Project 2: Customer & Category SQL Analysis
-- Dataset: Superstore Orders (9,694 rows)


-- Query 1: Who are our top 10 most valuable customers by total sales and profit?
-- Key Finding: Customers with average discounts above 0.20 consistently show negative or near-zero profit margins.
-- Recommendation: Cap customer discounts at 20% maximum.

SELECT 
    customer_name, 
    ROUND(SUM(sales), 2) AS total_sales, 
    ROUND(SUM(profit), 2) AS total_profit, 
    ROUND((SUM(profit) / SUM(sales) * 100), 2) AS profit_margin,
    ROUND(AVG(discount), 2) AS average_discount
FROM orders
GROUP BY customer_name
HAVING total_sales > 5000
ORDER BY profit_margin ASC;

-- Query 2: Which product category/sub-category generates the most losses?
-- Key Finding: Tables is the most unprofitable sub-category overall (-$17,725 total loss, -8.56% margin).
-- Machines appears profitable overall ($3,384) but specific customers receiving 50% discounts and above are nearly wiping out all profit in that category.
-- Recommendation: Eliminate discounts above 40% on Machines and investigate Tables pricing and cost structure.

SELECT 
    category, 
    sub_category, 
    ROUND(SUM(sales), 2) AS total_sales, 
    ROUND(SUM(profit), 2) AS total_profit, 
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin
FROM orders
GROUP BY category, sub_category
ORDER BY profit_margin ASC;

-- Query 3: Which region and category combination is most and least profitable?
-- Key Finding: Central + Furniture is the worst region/category combination at -1.59% margin. West + Office Supplies leads at 24.01%.
-- Furniture is unprofitable across ALL regions — this is a systemic pricing problem, not a regional one. Central's Technology margin (19.77%) confirms the region itself is not broken.
-- Recommendation: Cap furniture discounts at 20% maximum company-wide. Review furniture pricing strategy and consider discontinuing consistently unprofitable sub-categories like Tables (-8.56% margin).

SELECT 
    region, 
    category, 
    ROUND(SUM(sales), 2) AS total_sales, 
    ROUND(SUM(profit), 2) AS total_profit, 
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin
FROM orders
GROUP BY region, category
ORDER BY profit_margin ASC;

