PROJECT_NAME = "ctfrontier"

CDK_BOOTSTRAP_BUCKET = "ctf-bootstrap-bucket"
LAMBDA_CODE_BUCKET = "ctf-lambda-code-bucket"

DATA_UPDATE_FUNCTION = "data-update"

LAMBDA_REPOSITORY = "ctf-lambda-repository"
FRONTEND_REPOSITORY = "ctf-frontend-repository"
BACKEND_REPOSITORY = "ctf-backend-repository"
ETL_REPOSITORY = "ctf-etl-repository"

REPOSITORIES = [FRONTEND_REPOSITORY, BACKEND_REPOSITORY, ETL_REPOSITORY]

CLUSTER = "ctf-ecs-cluster"

FRONTEND_SERVICE = "frontend-service"
FRONTEND_TASK_FAMILY = "react-task"

BACKEND_SERVICE = "backend-service"
BACKEND_TASK_FAMILY = "django-task"
BACKEND_KEY_PAIR = "CtfBackendKeyPair"

ETL_SERVICE = "etl-service"
ETL_TASK_FAMILY = "etl-task"

FRONTEND_IMAGE = "ctf-frontend"

DATABASE = "aact"
DATABASE_SECRET = "CtfPostgresSecret"

LAMBDA_RELEASE_ALIAS = "live"
