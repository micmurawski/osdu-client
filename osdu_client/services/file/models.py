# generated by datamodel-codegen:
#   filename:  swagger.yaml
#   timestamp: 2024-07-12T07:32:21+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, constr, RootModel, ConfigDict


class Location(BaseModel):
    SignedURL: Optional[str] = Field(None, example="GCS signed URL")
    FileSource: Optional[str] = Field(
        None, description="Relative location of file", example="AXB564XVCY\\SHVCU7632"
    )


class EndianEnum(str, Enum):
    BIG_LITTLE = "BIG LITTLE"


class FileSourceInfo(BaseModel):
    Name: Optional[str] = Field(None, description="user-friendly file name.")
    PreloadFilePath: Optional[str] = Field(
        None,
        description="File system path to the data file as it existed before loading to the data platform",
    )
    FileSource: str = Field(
        ..., description="Relative file path for the data in the file"
    )
    PreloadFileCreateUser: Optional[str] = Field(
        None,
        description="Optional user name or reference, who created the file prior to up-loading to the platform.",
    )
    PreloadFileCreateDate: Optional[str] = Field(
        None,
        description="Optional create date and time of the file prior to uploading to the platform.",
    )
    PreloadFileModifyUser: Optional[str] = Field(
        None,
        description="Optional user name or reference, who last modified the file prior to up-loading to the platform.",
    )
    PreloadFileModifyDate: Optional[str] = Field(
        None,
        description="Optional last modified date and time of the file prior to up-loading to the platform.",
    )
    FileSize: Optional[str] = Field(
        None,
        description="Length of file in bytes. Implemented as string. The value must be convertible to a long integer (sizes can become very large).",
    )
    EncodingFormatTypeID: Optional[
        constr(
            pattern=r"^srn:<namespace>:reference-data\\/EncodingFormatType:[^:]+:[0-9]*$"
        )
    ] = Field(None, description="Encoding Format Type ID")

    model_config = ConfigDict(use_enum_values=True)


class DatasetProperties(BaseModel):
    FileSourceInfo: FileSourceInfo


class ExtensionProperties(BaseModel):
    kind: Optional[str] = Field(
        None,
        description="The schema ID for this schema fragment",
        example="os:npd:csvFileExtDetails:1.0.0",
        title="Extension Schema ID",
    )


class DownloadResponse(BaseModel):
    SignedURL: Optional[str] = None


class FileMetadataResponse(BaseModel):
    Id: Optional[str] = None


class DeliveryGetFileSignedURLRequest(BaseModel):
    srn: Optional[List[str]] = Field(None, description="A list of SRNs to fetch")


class Processed(BaseModel):
    signedUrl: Optional[str] = None


class DeliveryGetFileSignedURLResponse(BaseModel):
    unprocessed: Optional[List[str]] = Field(
        None, description="A list of SRNs which could not be processed"
    )
    processed: Optional[Dict[str, Processed]] = Field(
        None, description="Each key is equal to an SRN that was able to be processed"
    )


class FileID(RootModel[str]):
    root: constr(pattern=r"^[\w,\s-]+(\.\w+)?$")


class DateTime(RootModel[datetime]):
    root: datetime


class Driver(Enum):
    GCP = "GCP"
    AWS = "AWS"


class FileLocation(BaseModel):
    FileID: Optional[FileID] = None
    Driver: Optional[Driver] = None
    Location: Optional[str] = None
    CreatedAt: Optional[datetime] = None
    CreatedBy: Optional[str] = None


class Acl(BaseModel):
    viewers: List[str] = Field(
        ...,
        description="List of valid groups which will have view/read privileges over the record.",
    )
    owners: List[str] = Field(
        ...,
        description="List of valid groups which will have write privileges over the record.",
    )


class Legal(BaseModel):
    legaltags: Optional[List[str]] = Field(
        None,
        description="The list of legal tags, see compliance API.",
        title="Legal Tags",
    )
    otherRelevantDataCountries: Optional[List[str]] = Field(
        None,
        description="The list of other relevant data countries using the ISO 2-letter codes, see compliance API.",
        title="Other Relevant Data Countries",
    )
    status: Optional[str] = Field(
        None, description="The legal status.", title="Legal Status"
    )


class FileSourceInfoObject(BaseModel):
    Name: Optional[str] = Field(None, description="user-friendly file name.")
    PreloadFilePath: Optional[str] = Field(
        None,
        description="File system path to the data file as it existed before loading to the data platform",
    )
    FileSource: Optional[str] = Field(
        None, description="Relative file path for the data in the file"
    )
    PreloadFileCreateUser: Optional[str] = Field(
        None,
        description="Optional user name or reference, who created the file prior to up-loading to the platform.",
    )
    PreloadFileCreateDate: Optional[str] = Field(
        None,
        description="Optional create date and time of the file prior to uploading to the platform.",
    )
    PreloadFileModifyUser: Optional[str] = Field(
        None,
        description="Optional user name or reference, who last modified the file prior to up-loading to the platform.",
    )
    PreloadFileModifyDate: Optional[str] = Field(
        None,
        description="Optional last modified date and time of the file prior to up-loading to the platform.",
    )
    FileSize: Optional[str] = Field(
        None,
        description="Length of file in bytes. Implemented as string. The value must be convertible to a long integer (sizes can become very large).",
    )
    EncodingFormatTypeID: Optional[
        constr(
            pattern=r"^srn:<namespace>:reference-data\\/EncodingFormatType:[^:]+:[0-9]*$"
        )
    ] = Field(None, description="Encoding Format Type ID")
    Checksum: Optional[constr(pattern=r"^([0-9a-fA-F]{2})+$")] = Field(
        None,
        description="Checksum of file bytes - a hexadecimal number with even number of bytes.",
    )
    ChecksumAlgorithm: Optional[str] = Field(
        None, description="The name of the checksum algorithm e.g. MD5, SHA-256."
    )


class Kind(Enum):
    CRS = "CRS"
    Unit = "Unit"
    Measurement = "Measurement"
    AzimuthReference = "AzimuthReference"
    DateTime = "DateTime"


class MetaItem(BaseModel):
    kind: Kind = Field(
        ...,
        description="The kind of reference, unit, measurement, CRS or azimuth reference.",
        title="Reference Kind",
    )
    name: Optional[str] = Field(
        None,
        description="The name of the CRS or the symbol/name of the unit",
        example='["NAD27 * OGP-Usa Conus / North Dakota South [32021,15851]","ft"]',
        title="Name or Symbol",
    )
    persistableReference: str = Field(
        ...,
        description="The persistable reference string uniquely identifying the CRS or Unit",
        example='{"scaleOffset":{"scale":0.3048006096012192,"offset":0.0},"symbol":"ftUS","baseMeasurement":{"ancestry":"Length","type":"UM"},"type":"USO"}',
        title="Persistable Reference",
    )
    propertyNames: Optional[List[str]] = Field(
        None,
        description='The list of property names, to which this meta data item provides Unit/CRS context to. Data structures, which come in a single frame of reference, can register the property name, others require a full path like "data.structureA.propertyB" to define a unique context.',
        example=["elevationFromMsl", '"totalDepthMdDriller', "wellHeadProjected"],
        title="Attribute Names",
    )
    propertyValues: Optional[List[str]] = Field(
        None,
        description="The list of property values, to which this meta data item provides Unit/CRS context to. Typically a unit symbol is a value to a data structure; this symbol is then registered in this propertyValues array and the persistableReference provides the absolute reference.",
        example=["F", "ftUS", "deg"],
        title="Attribute Names",
    )
    uncertainty: Optional[float] = Field(
        None,
        description="The uncertainty of the values measured given the unit or CRS unit.",
        title="Uncertainty",
    )


class ToManyRelationship(BaseModel):
    confidences: Optional[List[float]] = Field(
        None,
        description="The confidences of the relationships. Keep all the arrays ordered and aligned.",
        title="Relationship Confidences",
    )
    ids: Optional[List[str]] = Field(
        None,
        description="The ids of the related objects. It is populated for an explicit relationship where the target entity is present as a record in the data ecosystem. Keep all the arrays ordered and aligned.",
        title="Related Object Id",
    )
    names: Optional[List[str]] = Field(
        None,
        description="The names or natural keys of the related objects. Keep all the arrays ordered and aligned.",
        title="Related Object Names",
    )
    versions: Optional[List[float]] = Field(
        None,
        description="The specific version numbers of the related instances. This is only specified if a specific version is required. If not populated the last version is implied. Keep all the arrays ordered and aligned.",
        title="To Many Relationship",
    )


class ToOneRelationship(BaseModel):
    confidence: Optional[float] = Field(
        None,
        description="The confidence of the relationship. If the property is absent a well-known relation is implied.",
        example=1,
        title="Relationship Confidence",
    )
    id: Optional[str] = Field(
        None,
        description="The id of the related object in the Data Ecosystem. If set, the id has priority over the natural key in the name property.",
        example="data_partition:namespace:entity_845934c40e8d922bc57b678990d55722",
        title="Related Object Id",
    )
    name: Optional[str] = Field(
        None,
        description="The name or natural key of the related object. This property is required if the target object id could not (yet) be identified.",
        example="Survey ST2016",
        title="Related Object Name",
    )
    version: Optional[float] = Field(
        None,
        description="The version number of the related entity. If no version number is specified, the last version is implied.",
        title="Entity Version Number",
    )


class LinkList(RootModel[Optional[Dict[str, List[str]]]]):
    root: Optional[Dict[str, List[str]]] = Field(
        None,
        description="An array of one or more entity references in the data lake.",
        title="Link List",
    )


class Error(BaseModel):
    message: Optional[str] = None
    reason: Optional[str] = None
    domain: Optional[str] = None


class ConnectedOuterService(BaseModel):
    name: Optional[str] = Field(None, description="Connected outer service name.")
    version: Optional[str] = Field(None, description="Connected outer service version.")


class StorageLocation(BaseModel):
    CSP_SPECIFIC_PROPERTY_1: Optional[str] = None
    CSP_SPECIFIC_PROPERTY_2: Optional[str] = None
    CSP_SPECIFIC_PROPERTY_3: Optional[str] = None


class StorageInstructionsResponse(BaseModel):
    providerKey: Optional[str] = Field(None, example="AZURE")
    storageLocation: Optional[StorageLocation] = None


class RetrievalProperties(BaseModel):
    CSP_SPECIFIC_PROPERTY_1: Optional[str] = None
    CSP_SPECIFIC_PROPERTY_2: Optional[str] = None
    CSP_SPECIFIC_PROPERTY_3: Optional[str] = None


class Dataset(BaseModel):
    datasetRegistryId: Optional[str] = Field(
        None,
        example="opendes:dataset--FileCollection.Generic:8118591ee2a24eada7152e54b369e99a",
    )
    retrievalProperties: Optional[RetrievalProperties] = None
    providerKey: Optional[str] = Field(None, example="AZURE")


class RetrievalInstructionsResponse(BaseModel):
    datasets: Optional[List[Dataset]] = None


class CopyDmsResponseItem(BaseModel):
    success: Optional[bool] = None
    datasetBlobStoragePath: Optional[str] = None


class CopyDmsResponse(RootModel[List[CopyDmsResponseItem]]):
    root: List[CopyDmsResponseItem]


class LocationRequest(BaseModel):
    FileID: Optional[FileID] = None


class LocationResponse(BaseModel):
    FileID: Optional[FileID] = None
    Location: Optional[Dict[str, str]] = Field(
        None, example={"SignedURL": "GCS signed URL"}
    )


class SourceLocationResponse(BaseModel):
    FileID: Optional[FileID] = None
    Location: Optional[Location] = None


class DatasetProperties1(BaseModel):
    FileCollectionPath: str = Field(
        ...,
        description="The mandatory path to the file collection. A FileCollectionPath should represent folder level access to a set of files.",
    )
    IndexFilePath: Optional[str] = Field(
        None, description="An optional path to an index file."
    )
    FileSourceInfo: Optional[List[FileSourceInfoObject]] = None


class FileCollections(BaseModel):
    Name: str = Field(
        ...,
        description="An optional name of the dataset, e.g. a user friendly file or file collection name.",
    )
    Description: Optional[str] = Field(
        None, description="An optional, textual description of the dataset."
    )
    TotalSize: Optional[constr(pattern=r"^[0-9]+$")] = Field(
        None,
        description="Total size of the dataset in bytes; for files it is the same as declared in FileSourceInfo.FileSize or the sum of all individual files. Implemented as string. The value must be convertible to a long integer (sizes can become very large).",
    )
    EncodingFormatTypeID: Optional[
        constr(
            pattern=r"^srn:<namespace>:reference-data\\/EncodingFormatType:[^:]+:[0-9]*$"
        )
    ] = Field(None, description="Encoding Format Type ID")
    SchemaFormatTypeID: Optional[
        constr(
            pattern=r"^srn:<namespace>:reference-data\\/SchemaFormatType:[^:]+:[0-9]*$"
        )
    ] = Field(None, description="Schema Format Type ID")
    Endian: EndianEnum = Field(
        ...,
        description="Endianness of binary value. Enumeration- \\BIG\\ \\LITTLE\\.  If absent applications will need to interpret from context indicators.",
    )
    Checksum: Optional[constr(pattern=r"^[0-9a-fA-F]32}$")] = Field(
        None, description="MD5 checksum of file bytes - a 32 byte hexadecimal number"
    )
    DatasetProperties: DatasetProperties1

    model_config = ConfigDict(use_enum_values=True)


class FileDetails(BaseModel):
    TargetKind: Optional[str] = Field(
        None,
        description="The target kind or schema ID which is to be used by the parser.",
        example="os:npd:wellbore:1:*.*",
        title="Target Schema ID",
    )
    FileType: Optional[str] = Field(
        None,
        description="Type of File to decide what kind of ingestion to be triggered",
        example="csv",
        title="File Type",
    )
    FrameOfReference: Optional[List[MetaItem]] = Field(
        None,
        description="The list metaItem definitions which maps a named frame of reference symbol or name to the self-contained persistableReference.",
        title="Frame of Reference for data present in file.",
    )
    ExtensionProperties: Optional[ExtensionProperties] = None
    ParentReference: Optional[str] = Field(
        None,
        description="The parent reference for this file.",
        example="CSBE0417",
        title="Parent Reference",
    )


class FileLocationRequest(BaseModel):
    FileID: Optional[FileID] = None


class FileLocationResponse(BaseModel):
    Driver: Optional[Driver] = None
    Location: Optional[str] = None


class FileListRequest(BaseModel):
    TimeFrom: Optional[DateTime] = None
    TimeTo: Optional[DateTime] = None
    PageNum: Optional[int] = None
    Items: Optional[int] = None
    UserID: Optional[str] = None


class FileListResponse(BaseModel):
    content: Optional[List[FileLocation]] = None
    number: Optional[int] = None
    numberOfElements: Optional[int] = None
    size: Optional[int] = None


class FileCollectionRecord(BaseModel):
    id: Optional[str] = Field(
        None,
        description="Unique identifier generated by the system for the directory metadata record.",
    )
    kind: str = Field(
        ...,
        description="Kind of data being ingested. Must follow the naming convention:data-Partition-Id}:dataset-name}:record-type}:version}.",
        example="osdu:wks:dataset--FileCollection.Generic:1.0.0",
    )
    acl: Acl
    legal: Legal
    data: FileCollections
    ancestry: Optional[LinkList] = None


class Relationships(BaseModel):
    parentEntity: Optional[ToOneRelationship] = None
    relatedItems: Optional[ToManyRelationship] = None


class ErrorModel(BaseModel):
    errors: Optional[List[Error]] = None
    code: Optional[int] = None
    message: Optional[str] = None


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


class ExtensionPropertiesModel(BaseModel):
    Name: Optional[str] = Field(
        None,
        description="The name of the file. Note- this is an additional property, which is not part of OSDU File.1.0.0",
        example="File",
        title="File Name",
    )
    Classification: Optional[str] = Field(
        None,
        description="The well-known entity classification code.",
        example="Raw File",
        title="File Classification",
    )
    Description: Optional[str] = Field(
        None,
        description="A text describing the entity.",
        example="An text further describing this file example.",
        title="Entity Description",
    )
    ExternalIds: Optional[List[str]] = Field(
        None,
        description="An array of identities (e.g. some kind if URL to be resolved in an external data store) which links to external realizations of the same entity.",
        title="Array of External IDs",
    )
    FileDateCreated: Optional[datetime] = Field(
        None,
        description="The UTC date time of the file creation",
        example="2013-03-22T11:16:03Z",
        title="Creation Date and Time",
    )
    FileDateModified: Optional[datetime] = Field(
        None,
        description="The UTC date time of the last file modification",
        example="2013-03-22T11:16:03Z",
        title="Last Modification Date and Time",
    )
    FileContentsDetails: Optional[FileDetails] = None
    relationships: Optional[Relationships] = None


class Files(BaseModel):
    Name: str = Field(
        ...,
        description="An optional name of the dataset, e.g. a user friendly file or file collection name.",
    )
    Description: Optional[str] = Field(
        None, description="An optional, textual description of the dataset."
    )
    TotalSize: Optional[constr(pattern=r"^[0-9]+$")] = Field(
        None,
        description="Total size of the dataset in bytes; for files it is the same as declared in FileSourceInfo.FileSize or the sum of all individual files. Implemented as string. The value must be convertible to a long integer (sizes can become very large).",
    )
    EncodingFormatTypeID: Optional[
        constr(
            pattern=r"^srn:<namespace>:reference-data\\/EncodingFormatType:[^:]+:[0-9]*$"
        )
    ] = Field(None, description="Encoding Format Type ID")
    SchemaFormatTypeID: Optional[
        constr(
            pattern=r"^srn:<namespace>:reference-data\\/SchemaFormatType:[^:]+:[0-9]*$"
        )
    ] = Field(None, description="Schema Format Type ID")
    Endian: EndianEnum = Field(
        ...,
        description="Endianness of binary value. Enumeration- \\BIG\\ \\LITTLE\\.  If absent applications will need to interpret from context indicators.",
    )
    Checksum: Optional[constr(pattern=r"^[0-9a-fA-F]32}$")] = Field(
        None, description="MD5 checksum of file bytes - a 32 byte hexadecimal number"
    )
    DatasetProperties: DatasetProperties
    ExtensionProperties: Optional[ExtensionPropertiesModel] = Field(
        None, title="File DMS Extension Properties"
    )


class Record(BaseModel):
    id: Optional[str] = Field(
        None,
        description="Unique identifier generated by the system for the file metadata record.",
    )
    kind: str = Field(
        ...,
        description="Kind of data being ingested. Must follow the naming convention:data-Partition-Id}:dataset-name}:record-type}:version}.",
        example="osdu:wks:dataset--File.Generic:1.0.0",
    )
    acl: Acl
    legal: Legal
    data: Files
    ancestry: Optional[LinkList] = None


class RecordVersion(BaseModel):
    id: Optional[str] = Field(
        None,
        description="Unique identifier generated by the system for the file metadata record.",
    )
    kind: Optional[str] = Field(
        None,
        description="Kind of data being ingested. Must follow the naming convention:data-Partition-Id}:dataset-name}:record-type}:version}.",
        example="osdu:wks:dataset--File.Generic:1.0.0",
    )
    acl: Optional[Acl] = None
    legal: Optional[Legal] = None
    data: Optional[Files] = None
    ancestry: Optional[LinkList] = None
    version: Optional[int] = Field(
        None,
        description="The version number of this OSDU resource; set by the framework.",
        example=1831253916104085,
        title="Version Number",
    )


class ApplicationError(BaseModel):
    error: Optional[ErrorModel] = None