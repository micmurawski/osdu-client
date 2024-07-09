# generated by datamodel-codegen:
#   filename:  swagger.yaml
#   timestamp: 2024-07-09T19:33:12+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, conint, constr


class SchemaIdentity(BaseModel):
    authority: constr(regex=r'^[\w\-\.]+$') = Field(
        ..., description='Entity authority', example='osdu'
    )
    source: constr(regex=r'^[\w\-\.]+$') = Field(
        ..., description='Entity source', example='wks'
    )
    entityType: constr(regex=r'^[\w\-\.]+$') = Field(
        ..., description='EntityType Code', example='wellbore'
    )
    schemaVersionMajor: int = Field(
        ..., description='Major Schema Version Number', example=1
    )
    schemaVersionMinor: int = Field(
        ..., description='Minor Schema Version Number', example=1
    )
    schemaVersionPatch: int = Field(
        ..., description='Patch Schema Version Number', example=0
    )
    id: Optional[str] = Field(
        None,
        description='A read-only system defined id used for referencing of a schema.',
        example='osdu:wks:wellbore:1.0.0',
    )


class Status(Enum):
    PUBLISHED = 'PUBLISHED'
    OBSOLETE = 'OBSOLETE'
    DEVELOPMENT = 'DEVELOPMENT'


class Scope(Enum):
    INTERNAL = 'INTERNAL'
    SHARED = 'SHARED'


class SchemaInfo(BaseModel):
    schemaIdentity: SchemaIdentity
    createdBy: Optional[str] = Field(
        None,
        description='The user who created the schema. This value is taken from API caller token.',
        example='user@opendes.com',
    )
    dateCreated: Optional[datetime] = Field(
        None,
        description='The UTC date time of the entity creation',
        example='2019-05-23T11:16:03Z',
    )
    status: Status = Field(
        ...,
        description='Schema lifecycle status',
        example='PUBLISHED',
        title='SchemaStatus',
    )
    scope: Optional[Scope] = Field(
        None,
        description=' Schema Scope - is it internal or shared. This is a system defined attribute based on partition-id passed.',
        example='INTERNAL',
        title='Schema Scope',
    )
    supersededBy: Optional[SchemaIdentity] = None


class SchemaRequest(BaseModel):
    schemaInfo: SchemaInfo
    schema_: Dict[str, Any] = Field(..., alias='schema')


class AppError(BaseModel):
    code: Optional[int] = None
    reason: Optional[str] = None
    message: Optional[str] = None


class SchemaInfoResponse(BaseModel):
    schemaInfos: Optional[List[SchemaInfo]] = None
    offset: Optional[conint(ge=0)] = Field(
        None, description='The offset for the next query'
    )
    count: Optional[conint(ge=0)] = Field(
        None, description='The number of schema versions in this response'
    )
    totalCount: Optional[conint(ge=0)] = Field(
        None, description='The total number of entity type codes in the repositories'
    )


class ConnectedOuterService(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None


class VersionInfo(BaseModel):
    groupId: Optional[str] = None
    artifactId: Optional[str] = None
    version: Optional[str] = None
    buildTime: Optional[str] = None
    branch: Optional[str] = None
    commitId: Optional[str] = None
    commitMessage: Optional[str] = None
    connectedOuterServices: Optional[List[ConnectedOuterService]] = None
