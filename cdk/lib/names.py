PROJECT_NAME = "ctfrontier"
DOMAIN = "ctfrontier.com"

CDK_BOOTSTRAP_BUCKET = "ctf-bootstrap-bucket"
LAMBDA_CODE_BUCKET = "ctf-lambda-code-bucket"

LAMBDA_REPOSITORY = "ctf-lambda-repository"
FRONTEND_REPOSITORY = "ctf-frontend-repository"
BACKEND_REPOSITORY = "ctf-backend-repository"

REPOSITORIES = [FRONTEND_REPOSITORY, BACKEND_REPOSITORY]

CLUSTER = "ctf-ecs-cluster"

FRONTEND_SERVICE = "frontend"
FRONTEND_TASK_FAMILY = "react-task"

BACKEND_SERVICE = "backend"
BACKEND_TASK_FAMILY = "django-task"
BACKEND_KEY_PAIR = "CtfBackendKeyPair"

ETL_DOWNLOAD_FUNCTION = "etl-download"

FRONTEND_IMAGE = "ctf-frontend"

DATABASE = "ctfdatabase"
DATABASE_INSTANCE = "ctf-postgres-db-instance"

FUNCTIONS = [ETL_DOWNLOAD_FUNCTION]

RAW_DATA_FILES_BUCKET = "raw-data-files"

LAMBDA_RELEASE_ALIAS = "live"
METRIC_NAMESPACE = "log-metrics"
NOTIFICATIONS_TOPIC = "notifications"
