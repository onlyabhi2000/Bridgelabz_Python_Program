-- SELECT * from bronze.crm_cust_info limit 50;

-- SELECT * FROM bronze.crm_prd_info LIMIT 50;

-- SELECT * from bronze.crm_sales_details LIMIT 50;

-- SELECT * from bronze.erp_cat_g1v2;

-- SELECT * from bronze.erp_cust_az12;

-- SELECT * from bronze.erp_loc_a101


-- SELECT cst_id from bronze.crm_cust_info;




-- \COPY bronze.crm_cust_info
-- FROM '/home/abhishek/Downloads/sql-data-warehouse-project/datasets/source_crm/cust_info.csv'
-- WITH (
--     FORMAT csv,
--     HEADER true,
--     DELIMITER ','
-- );


-- \copy bronze.crm_cust_info 
-- FROM '/home/abhishek/Downloads/sql-data-warehouse-project/datasets/source_crm/cust_info.csv' 
-- WITH (FORMAT csv, HEADER true, DELIMITER ',');

-- CRM -PROD
-- \copy bronze.crm_prd_info
-- FROM '/home/abhishek/Downloads/sql-data-warehouse-project/datasets/source_crm/prd_info.csv'
-- WITH (FORMAT csv, HEADER true, DELIMITER ',');


-- --CRM --SALES
-- \copy bronze.crm_sales_details
-- FROM '/home/abhishek/Downloads/sql-data-warehouse-project/datasets/source_crm/sales_details.csv'
-- WITH (FORMAT csv, HEADER true, DELIMITER ',');



-- --erp -- loc
-- \copy bronze.erp_loc_a101
-- FROM '/home/abhishek/Downloads/sql-data-warehouse-project/datasets/source_erp/LOC_A101.csv'
-- WITH (FORMAT csv, HEADER true, DELIMITER ',');


-- --erp -- cust
-- \copy bronze.erp_cust_az12
-- FROM '/home/abhishek/Downloads/sql-data-warehouse-project/datasets/source_erp/CUST_AZ12.csv'
-- WITH (FORMAT csv, HEADER true, DELIMITER ',');


-- --erp -- cat
-- \copy bronze.erp_cat_g1v2
-- FROM '/home/abhishek/Downloads/sql-data-warehouse-project/datasets/source_erp/PX_CAT_G1V2.csv'
-- WITH (FORMAT csv, HEADER true, DELIMITER ',');



-----------------  Silver layer -------------------------

-- 1. Check for null and dublicates in the primary key
-- because primary key should not be null or dublicate


-- SELECT cst_id , count(*)
-- from silver.crm_cust_info
-- GROUP BY cst_id 
-- HAVING count(*)>1 or cst_id is NULL;


-- Now have to decide which one have to keep and which one have to remove from the dublicated data.
-- so for this  continue with most recent data or row with most consistent data
-- SELECT * FROM
-- (SELECT *,
-- row_number() OVER (PARTITION BY cst_id ORDER BY cst_create_date DESC ) as flag_last
-- FROM bronze.crm_cust_info)
-- WHERE flag_last =1;



-- Now chek for unwanted spaces in the string column

-- SELECT cst_first_name
-- FROM bronze.crm_cust_info
-- WHERE cst_first_name != TRIM(cst_first_name);



-- Now need to transform the data which consists of trimmed  extra spaces and no null/ dublicate primary key


-- SELECT 
--     cst_id,
--     cst_key,
--     TRIM(cst_first_name) AS cst_first_name,
--     TRIM(cst_last_name) AS cst_last_name,
--     cst_marital_status,
--     cst_gndr,
--     cst_create_date
-- FROM (
--     SELECT *,
--            ROW_NUMBER() OVER (PARTITION BY cst_id ORDER BY cst_create_date DESC) AS flag_last
--     FROM bronze.crm_cust_info
-- ) sub
-- WHERE flag_last = 1;


-- Now need to check the cosistency of the  maretial status and gender column

-- SELECT DISTINCT cst_marital_status , count(*) cst_marital_status
-- FROM bronze.crm_cust_info
-- GROUP BY cst_marital_status;


-- SELECT DISTINCT cst_gndr , count(*) cst_gndr
-- FROM bronze.crm_cust_info
-- GROUP BY cst_gndr;


-- For gender column where null occure we have to make it NA


-- SELECT 
--     cst_id,
--     cst_key,
--     TRIM(cst_first_name) AS cst_first_name,
--     TRIM(cst_last_name) AS cst_last_name,

--     CASE 
--         WHEN UPPER(TRIM(cst_marital_status)) = 'S' THEN 'Single'
--         WHEN UPPER(TRIM(cst_marital_status)) = 'M' THEN 'Married'
--         ELSE 'NA'
--     END AS marital_status,

--     CASE 
--         WHEN cst_gndr IS NULL THEN 'N/A'
--         ELSE cst_gndr
--     END AS cst_gndr,

--     cst_create_date
-- FROM (
--     SELECT *,
--            ROW_NUMBER() OVER (PARTITION BY cst_id ORDER BY cst_create_date DESC) AS flag_last
--     FROM bronze.crm_cust_info
-- ) sub
-- WHERE flag_last = 1;




-- SELECT count(*) FROM silver.crm_cust_info;

-- TRUNCATE TABLE silver.crm_cust_info;



-- now insert the cleaned data into the silver layer

-- Step 1: Truncate the silver table
-- TRUNCATE TABLE silver.crm_cust_info;

-- Step 2: Insert the latest, cleaned data
-- TRUNCATE TABLE silver.crm_cust_info;

-- INSERT INTO silver.crm_cust_info (
--     cst_id,
--     cst_key,
--     cst_first_name,
--     cst_last_name,
--     cst_marital_status,
--     cst_gndr,
--     cst_create_date,
--     dwh_create_date
-- )
-- SELECT 
--     cst_id,
--     cst_key,
--     TRIM(cst_first_name) AS cst_first_name,
--     TRIM(cst_last_name) AS cst_last_name,

--     CASE 
--         WHEN UPPER(TRIM(cst_marital_status)) = 'S' THEN 'Single'
--         WHEN UPPER(TRIM(cst_marital_status)) = 'M' THEN 'Married'
--         ELSE 'NA'
--     END AS cst_marital_status,

--     CASE 
--         WHEN cst_gndr IS NULL THEN 'N/A'
--         ELSE cst_gndr
--     END AS cst_gndr,

--     cst_create_date,
--     CURRENT_DATE AS dwh_create_date
-- FROM (
--     SELECT *,
--            ROW_NUMBER() OVER (PARTITION BY cst_id ORDER BY cst_create_date DESC) AS flag_last
--     FROM bronze.crm_cust_info
-- ) sub
-- WHERE flag_last = 1;




-- SELECT * FROM silver.crm_cust_info;


---Next step to verify  the data in silver layer


SELECT cst_id , count(*)
from silver.crm_cust_info
GROUP BY cst_id 
HAVING count(*)>1 or cst_id is NULL;

-- DELETE FROM silver.crm_cust_info
-- WHERE cst_id IS NULL;


---- Now at this point we have cleaned tranformed data loaded in the  Silver later - crm_cust_info table 





--NExt step is to remove extra spaces across all the columns to make data consistent.



