from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="Service Booking API",
    description="API for booking various services with provider availability",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "authentication",
            "description": "Authentication operations"
        },
        {
            "name": "services", 
            "description": "Service management operations"
        }
    ],
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add security scheme to Swagger UI
app.swagger_ui_init_oauth = {
    "usePkceWithAuthorizationCodeGrant": True,
    "clientId": "swagger-ui",
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add OpenAPI security scheme
app.openapi_schema = None  # Clear existing schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    
    # Add security scheme
    openapi_schema["components"]["securitySchemes"] = {
        "Bearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Enter the token with the `Bearer: ` prefix, e.g. 'Bearer abcde12345'"
        }
    }
    
    # Add security requirement to all protected endpoints
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            if operation.get("tags") and "authentication" not in operation.get("tags"):
                operation["security"] = [{"Bearer": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi