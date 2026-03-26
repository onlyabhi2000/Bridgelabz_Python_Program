+-------------------+
|   categories      |
+-------------------+
| PK category_id    |
|    category_name  |
|    description    |
+-------------------+

          ▲
          │
          │ FK
+--------------------+           +--------------------+
|     products       |           |   testproducts     |
+--------------------+           +--------------------+
| PK product_id      |           | PK testproduct_id  |
|    product_name    |           |    product_name    |
| FK category_id     |──────────▶| FK category_id     |
|    unit            |           +--------------------+
|    price           |
+--------------------+


+--------------------+
|    customers       |
+--------------------+
| PK customer_id     |
|    customer_name   |
|    contact_name    |
|    address         |
|    city            |
|    postal_code     |
|    country         |
+--------------------+

          ▲
          │
          │ FK
+--------------------+
|      orders        |
+--------------------+
| PK order_id        |
| FK customer_id     |
|    order_date      |
+--------------------+
          ▲
          │
          │ FK
+-------------------------+
|     order_details       |
+-------------------------+
| PK order_detail_id      |
| FK order_id             |
| FK product_id           |
|    quantity             |
+-------------------------+
