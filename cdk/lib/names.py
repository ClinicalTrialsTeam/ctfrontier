PROJECT_NAME = "ctfrontier"

CDK_BOOTSTRAP_BUCKET = "ctf-bootstrap-bucket"
LAMBDA_CODE_BUCKET = "ctf-lambda-code-bucket"

LAMBDA_REPOSITORY = "ctf-lambda-repository"
FRONTEND_REPOSITORY = "ctf-frontend-repository"

REPOSITORIES = [LAMBDA_REPOSITORY, FRONTEND_REPOSITORY]

ETL_DOWNLOAD_FUNCTION = "etl-download"

FRONTEND_IMAGE = "ctf-frontend"

FUNCTIONS = [ETL_DOWNLOAD_FUNCTION]

RAW_DATA_FILES_BUCKET = "raw-data-files"

LAMBDA_RELEASE_ALIAS = "live"
METRIC_NAMESPACE = "log-metrics"
NOTIFICATIONS_TOPIC = "notifications"
