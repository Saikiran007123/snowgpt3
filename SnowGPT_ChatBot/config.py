# snowflake_user = "VINAYKUMAR"
# snowflake_password = "Vinay@123"
# snowflake_account = "fysuwth-ffb68347"
# snowflake_warehouse = "COMPUTE_WH"
# snowflake_database = "SNOWGPT_DB"
# snowflake_schema = "snowgpt_schema"
# stage_name = "snowgpt_stage"

snowflake_user = "SNOWGPT"
snowflake_password = "SnowGPT@202308"
snowflake_account = "anblicksorg_aws.us-east-1"
snowflake_warehouse = "SNOWGPT_WH"
snowflake_database = "SNOWGPT_DB"
snowflake_schema = "STG"
stage_name = "snowgpt_s3_stage"

query = "SELECT DISTINCT GET_PRESIGNED_URL(@snowgpt_s3_stage, METADATA$FILENAME) FROM @snowgpt_s3_stage"

api_key = "30b05cc6-2aed-42b4-83dd-967358f305bc"
environment = "asia-southeast1-gcp-free"

index_name="aws"

openai_api_key="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"

# os.environ["OPENAI_API_KEY"] = "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"
# cursor.execute(f"LIST {stage_file_path}")
# cursor.execute("SELECT $1 FROM @snowgpt_db.snowgpt_schema.snowgpt_stage/sampleTextFile.txt")