from fastapi import APIRouter, HTTPException, Security, Query
from typing import List, Optional
from datetime import datetime
from app.core.security import get_current_user, get_admin_user
from app.models.models import Service
from app.models.user import User, MessageResponse
from app.db.fake_db import services_db

router = APIRouter()

@router.get("/", response_model=List[Service])
async def get_services(
    current_user: User = Security(get_current_user),
    service_type: Optional[str] = Query(None, description="Filter services by type"),
    date: Optional[str] = Query(None, description="Filter availability by date (YYYY-MM-DD)")
):
    """
    Get all services with optional filtering by type and date.
    """
    filtered_services = services_db.copy()
    
    if service_type:
        filtered_services = [
            s for s in filtered_services
            if s["type"].lower() == service_type.lower()
        ]
    
    if date:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            filtered_services = [
                {
                    **s,
                    "availability": [
                        a for a in s["availability"]
                        if a["date"] == date
                    ]
                }
                for s in filtered_services
            ]
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Invalid date format. Use YYYY-MM-DD"
            )
    
    return filtered_services

@router.get("/{service_id}", response_model=Service)
async def get_service_by_id(
    service_id: int,
    current_user: User = Security(get_current_user),
    date: Optional[str] = Query(None, description="Filter availability by date (YYYY-MM-DD)")
):
    """
    Get a specific service by ID with optional date filtering.
    """
    service = next(
        (s for s in services_db if s["id"] == service_id),
        None
    )
    
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    if date:
        try:
            datetime.strptime(date, "%Y-%m-%d")
            service = {
                **service,
                "availability": [
                    a for a in service["availability"]
                    if a["date"] == date
                ]
            }
        except ValueError:
            raise HTTPException(
                status_code=400,
                detail="Invalid date format. Use YYYY-MM-DD"
            )
    
    return service

@router.post("/", response_model=Service)
async def add_service(
    service: Service,
    current_user: User = Security(get_admin_user)
):
    """
    Add a new service. Requires admin privileges.
    """
    if any(s["id"] == service.id for s in services_db):
        raise HTTPException(
            status_code=400,
            detail="Service with this ID already exists"
        )
    
    service_dict = service.dict()
    services_db.append(service_dict)
    return service_dict

@router.put("/{service_id}", response_model=Service)
async def update_service(
    service_id: int,
    service_update: Service,
    current_user: User = Security(get_admin_user)
):
    """
    Update an existing service. Requires admin privileges.
    """
    service_idx = next(
        (idx for idx, s in enumerate(services_db) if s["id"] == service_id),
        None
    )
    
    if service_idx is None:
        raise HTTPException(status_code=404, detail="Service not found")
    
    service_dict = service_update.dict()
    services_db[service_idx] = service_dict
    return service_dict

@router.delete("/{service_id}", response_model=MessageResponse)
async def delete_service(
    service_id: int,
    current_user: User = Security(get_admin_user)
):
    """
    Delete a service. Requires admin privileges.
    """
    service_idx = next(
        (idx for idx, s in enumerate(services_db) if s["id"] == service_id),
        None
    )
    
    if service_idx is None:
        raise HTTPException(status_code=404, detail="Service not found")
    
    services_db.pop(service_idx)
    return {"message": "Service deleted successfully"}