# ===========================================================================
# Bronze Layer Ingestion Config (Databricks / Lakehouse)

# Purpose:
#   - Centralize what raw data to ingest for the Bronze layer
#   - Loop over configs and make it easier to add / remove sources or files without changing the logic
# Design goals:
#   - Store the data as close to the source as possible
#   - Preserve the raw values
#   - Keep its lineage clear from the source system to the raw table

# BASE_PATH: the root folder where the Bronze raw files live.
BASE_PATH = "/Volumes/workspace/bronze/raw_files"

# INGESTION_CONFIG consists of a list of dictionaries, each dictionary is a config for a source file.
INGESTION_CONFIG = [
    # These files come from the CRM and are treated as raw inputs.
    # The ingestion job can use "source": "crm" to:
    #   - route logging messages ("crm ingest started", etc.)
    #   - add metadata columns (ingestion_time, source_system, file_name)
    #   - apply consistent Bronze conventions for CRM inputs
     {
        "source": "crm",
        "path": f"{BASE_PATH}/source_crm/cust_info.csv",
        "table": "crm_cust_info_raw"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_crm/prd_info.csv",
        "table": "crm_prd_info_raw"
    },
    {
        "source": "crm",
        "path": f"{BASE_PATH}/source_crm/sales_details.csv",
        "table": "crm_sales_details_raw"
    },
    # These files come from the ERP.
    # ERP often uses internal naming codes (AZ12, A101, etc.)
    # Keeping those codes in the raw table name can preserve source meaning.
    {
        "source": "erp",
        "path": f"{BASE_PATH}/source_erp/CUST_AZ12.csv",
        "table": "erp_cust_az12_raw"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/source_erp/LOC_A101.csv",
        "table": "erp_loc_a101_raw"
    },
    {
        "source": "erp",
        "path": f"{BASE_PATH}/source_erp/PX_CAT_G1V2.csv",
        "table": "erp_px_cat_g1v2_raw"
    }
]