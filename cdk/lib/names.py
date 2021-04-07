PROJECT_NAME = "ctfrontier"

CDK_BOOTSTRAP_BUCKET = "ctf-bootstrap-bucket"

LAMBDA_REPOSITORY = "ctf-lambda-repository"
LAMBDA_CODE_BUCKET = "ctf-lambda-code-bucket"

ETL_DOWNLOAD_FUNCTION = "etl-download"

FUNCTIONS = [ETL_DOWNLOAD_FUNCTION]

RAW_DATA_FILES_BUCKET = "raw-data-files"

LAMBDA_RELEASE_ALIAS = "live"
METRIC_NAMESPACE = "log-metrics"
NOTIFICATIONS_TOPIC = "notifications"
