-- SELECT * FROM silver.crm_cust_info LIMIT 10;


-- SELECT cst_last_name FROM silver.crm_cust_info
-- WHERE cst_last_name !=TRIM(cst_last_name);



-- SELECT prd_id , prd_key , prd_nm , prd_cost , prd_line , prd_start_dt , prd_end_dt
-- FROM bronze.crm_prd_info;


--Checking primary key is not null or dublicate

-- SELECT prd_id , count(*)
-- from bronze.crm_prd_info
-- GROUP BY prd_id 
-- HAVING count(*)>1 or prd_id is NULL;







-- will create a different column prd_key by extracting the cat_id from it
-- reason is we can join this with the erp category table 

-- SELECT prd_id , 
-- prd_key , 
-- SUBSTRING(prd_key , 1 , 5) AS cat_id,
-- prd_nm ,
-- prd_cost , 
-- prd_line , 
-- prd_start_dt , 
-- prd_end_dt
-- FROM bronze.crm_prd_info;


-- but the format in erp cat table is EO_CR  but while extarcting we got the format as EO-CR
--So need to transform the data for the consistency and to join 


-- SELECT prd_id , 
-- prd_key , 
-- REPLACE(SUBSTRING(prd_key , 1 , 5), '-' , '_') AS cat_id,
-- prd_nm ,
-- prd_cost , 
-- prd_line , 
-- prd_start_dt , 
-- prd_end_dt
-- FROM bronze.crm_prd_info;




-- Now filter out the unmatched data from the erp category table after transformation
SELECT prd_id , 
prd_key , 
REPLACE(SUBSTRING(prd_key , 1 , 5), '-' , '_') AS cat_id,
prd_nm ,
prd_cost , 
prd_line , 
prd_start_dt , 
prd_end_dt
FROM bronze.crm_prd_info
WHERE REPLACE(SUBSTRING(prd_key , 1 , 5), '-' , '_') NOT IN
(SELECT DISTINCT id FROM bronze.erp_cat_g1v2)


-- SELECT * from bronze.erp_cat_g1v2 LIMIT 100;


