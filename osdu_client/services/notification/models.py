# generated by datamodel-codegen:
#   filename:  swagger.yaml
#   timestamp: 2024-07-12T07:32:20+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ResponseEntity(BaseModel):
    body: Optional[Dict[str, Any]] = None
    statusCode: Optional[str] = None
    statusCodeValue: Optional[int] = None


class ConnectedOuterService(BaseModel):
    name: Optional[str] = Field(None, description="Connected outer service name.")
    version: Optional[str] = Field(None, description="Connected outer service version.")


class VersionInfo(BaseModel):
    groupId: Optional[str] = Field(None, description="Maven artifact group ID.")
    actifactId: Optional[str] = Field(None, description="Maven artifact ID.")
    version: Optional[str] = Field(None, description="Maven artifact version")
    buildTime: Optional[str] = Field(None, description="Maven artifact build time")
    branch: Optional[str] = Field(None, description="Current git branch")
    commitId: Optional[str] = Field(None, description="Latest commit hash")
    commitMessage: Optional[str] = Field(None, description="Latest commit message")
    connectedOuterServices: Optional[List[ConnectedOuterService]] = Field(
        None, description="Connected outer services information"
    )
