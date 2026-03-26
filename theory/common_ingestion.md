**Project Explanation (Sample Answer)**

“In my current role, I work on a data ingestion and analytics platform where we collect security and network data from different OEM devices such as Versa and Fortinet.

The main goal of the project is to ingest logs from multiple network devices, normalize the data, and store it for analytics and monitoring purposes.

My responsibility is mainly on the Python-based ingestion framework. Each OEM integration has an adapter, mapper, and pipeline layer.
The adapter is responsible for calling external APIs or collecting device logs, the mapper transforms the raw OEM response into our internal standardized format, and the pipeline handles processing, logging, and storing the normalized data into the database.

For example, recently I worked on integrating Fortinet Web URL Summary data. I implemented the ingestion logic that fetches data from the Fortinet API, processes the response, and maps fields like device ID, entity type, category, and threat information into our internal schema so it can be consumed by downstream analytics systems.

I also worked on debugging ingestion pipelines, adding proper logging, error handling, and validation, because sometimes APIs return inconsistent or duplicate data. My work involved identifying where duplication was happening in the pipeline and ensuring the mapper produces clean structured output.

Overall, the project is focused on building scalable and reliable ingestion pipelines that convert raw security device data into a standardized format for monitoring and analytics.”






###########################################################################################################



**Tell me about your project**

“I worked on a platform called MDM Integration Platform and Performance Monitoring System. The goal of this platform is to automatically discover network devices, collect operational data from them, and monitor their performance and health.

The system integrates with enterprise MDM services to retrieve device configuration details and operational metadata. Using this information, our platform performs automated device discovery and continuously monitors device performance.

My role was mainly focused on the backend development using Python and FastAPI. I developed several REST APIs that provide device insights, validation results, and performance metrics to other internal systems.

I also worked on building data ingestion pipelines that process the collected device data and store it in ArangoDB and Elasticsearch. ArangoDB is used for storing structured operational data, while Elasticsearch is used for search and analytics so that users can quickly query device information.

Another part of my work involved implementing cron-based workflows to automate discovery tasks. Some discovery jobs run daily, while others run in near real-time depending on the device monitoring requirements.

Additionally, I implemented alarm generation logic which analyzes device metrics and triggers alerts whenever SLA violations or abnormal device behavior is detected.

Overall, the platform helps network teams automatically discover devices, monitor their performance, and detect potential issues early, improving operational visibility and reliability.





####################################################################################################################

**Challenge 1 – Handling Large Volumes of Device Data**

“One challenge I faced was handling large volumes of device telemetry and log data coming from network appliances. The API responses sometimes contained thousands of records, and processing them directly using standard Python loops was slow.

To solve this, I started using Pandas and Polars for efficient data transformation. These libraries allowed us to perform vectorized operations and process large datasets much faster than traditional iterative approaches. After transforming the data, the pipeline would store the normalized records in ArangoDB and Elasticsearch for further analysis. This significantly improved the performance of the ingestion pipeline.”



**Challenge 2 – Normalizing Data from Different OEM Devices**

“Another challenge was that different OEM systems like Versa and Fortinet return data in different formats. Field names, structures, and sometimes even data types varied between APIs.

To address this, we implemented a mapper layer in the ingestion pipeline. The mapper converts raw OEM responses into a standard internal schema used by our platform. I worked on defining these mappings and adding validation checks so that inconsistent data could be handled safely. This made the system easier to extend when integrating new devices.



**Challenge 3 – Duplicate Data in the Ingestion Pipeline**

“At one point, we noticed that the ingestion pipeline was generating duplicate records. The API responses looked correct, but the final stored output contained repeated entries.

To debug this, I added detailed logging inside the adapter and mapper stages of the pipeline. By tracing the logs step by step, I identified that the transformation logic was being executed multiple times for the same dataset due to how the pipeline processed the response.

After identifying the root cause, I updated the logic and added checks to ensure each record was processed only once. This improved the data quality and stability of the pipeline.”