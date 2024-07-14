# generated by datamodel-codegen:
#   filename:  swagger.yaml
#   timestamp: 2024-07-12T07:32:18+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, confloat, conint


class Point(BaseModel):
    latitude: Optional[confloat(ge=-90.0, le=90.0)] = None
    longitude: Optional[float] = None


class Polygon(BaseModel):
    points: Optional[List[Point]] = None


class OrderEnum(Enum):
    ASC = "ASC"
    DESC = "DESC"


class SortQuery(BaseModel):
    field: Optional[List[str]] = None
    order: Optional[List[OrderEnum]] = None
    filter: Optional[List[str]] = None


class CursorQueryResponse(BaseModel):
    cursor: Optional[str] = None
    results: Optional[List[Dict[str, Dict[str, Any]]]] = None
    totalCount: Optional[int] = None


class AppError(BaseModel):
    code: Optional[int] = None
    reason: Optional[str] = None
    message: Optional[str] = None


class AggregationResponse(BaseModel):
    key: Optional[str] = None
    count: Optional[int] = None


class QueryResponse(BaseModel):
    results: Optional[List[Dict[str, Dict[str, Any]]]] = None
    aggregations: Optional[List[AggregationResponse]] = None
    totalCount: Optional[int] = None


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


class ByBoundingBox(BaseModel):
    topLeft: Point
    bottomRight: Point


class ByDistance(BaseModel):
    distance: Optional[confloat(le=9.223372036854776e18)] = None
    point: Point


class ByGeoPolygon(BaseModel):
    points: List[Point]


class ByIntersection(BaseModel):
    polygons: List[Polygon]


class ByWithinPolygon(BaseModel):
    points: List[Point]


class SpatialFilter(BaseModel):
    field: str
    byBoundingBox: Optional[ByBoundingBox] = None
    byDistance: Optional[ByDistance] = None
    byGeoPolygon: Optional[ByGeoPolygon] = None
    byIntersection: Optional[ByIntersection] = None
    byWithinPolygon: Optional[ByWithinPolygon] = None


class QueryRequest(BaseModel):
    kind: Dict[str, Any]
    limit: Optional[conint(ge=0)] = None
    query: Optional[str] = None
    highlightedFields: Optional[List[str]] = None
    returnedFields: Optional[List[str]] = None
    sort: Optional[SortQuery] = None
    queryAsOwner: Optional[bool] = None
    trackTotalCount: Optional[bool] = None
    spatialFilter: Optional[SpatialFilter] = None
    aggregateBy: Optional[str] = None
    offset: Optional[conint(ge=0)] = None


class CursorQueryRequest(BaseModel):
    kind: Dict[str, Any]
    limit: Optional[conint(ge=0)] = None
    query: Optional[str] = None
    highlightedFields: Optional[List[str]] = None
    returnedFields: Optional[List[str]] = None
    sort: Optional[SortQuery] = None
    queryAsOwner: Optional[bool] = None
    trackTotalCount: Optional[bool] = None
    spatialFilter: Optional[SpatialFilter] = None
    cursor: Optional[str] = None