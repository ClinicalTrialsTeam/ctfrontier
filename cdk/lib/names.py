PROJECT_NAME = "ctfrontier"

CDK_BOOTSTRAP_BUCKET = "ctf-bootstrap-bucket"
LAMBDA_CODE_BUCKET = "ctf-lambda-code-bucket"

LAMBDA_REPOSITORY = "ctf-lambda-repository"
FRONTEND_REPOSITORY = "ctf-frontend-repository"
BACKEND_REPOSITORY = "ctf-backend-repository"

REPOSITORIES = [FRONTEND_REPOSITORY, BACKEND_REPOSITORY]

CLUSTER = "ctf-ecs-cluster"

FRONTEND_SERVICE = "frontend"
FRONTEND_TASK_FAMILY = "react-task"

BACKEND_SERVICE = "backend-service"
BACKEND_TASK_FAMILY = "django-task"
BACKEND_KEY_PAIR = "CtfBackendKeyPair"

FRONTEND_IMAGE = "ctf-frontend"

DATABASE = "aact"
DATABASE_INSTANCE = "ctf-db-instance"

METRIC_NAMESPACE = "log-metrics"
NOTIFICATIONS_TOPIC = "notifications"
