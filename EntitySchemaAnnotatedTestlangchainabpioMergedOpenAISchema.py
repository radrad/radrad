from __future__ import annotations

from enum import Enum
from typing import List, Optional
import uuid

from pydantic import BaseModel, ConfigDict, Field, constr
from pydantic.json_schema import GenerateJsonSchema
from openai_function_call import OpenAISchema

class EntityGenerateJsonSchema(GenerateJsonSchema):
    def generate(self, schema, mode='validation'):
        json_schema = super().generate(schema, mode=mode)
        json_schema['$schema'] = self.schema_dialect
        json_schema['@id'] = 'http://blagomeni.com/schemas/entity.json'
        json_schema['title'] = 'Entity'        
        return json_schema
    
class BaseClassEnum(Enum):
    Entity = 'Entity'
    AggregateRoot = 'AggregateRoot'
    AuditedEntity = 'AuditedEntity'
    AuditedAggregateRoot = 'AuditedAggregateRoot'
    FullAuditedEntity = 'FullAuditedEntity'
    FullAuditedAggregateRoot = 'FullAuditedAggregateRoot'


class PrimaryKeyTypeEnum(Enum):
    Int = 'int'
    Long = 'long'
    Guid = 'Guid'
    String = 'string'

class TypeEnum(Enum):
    bool = 'bool'
    byte = 'byte'
    char = 'char'
    DateTime = 'DateTime'
    decimal = 'decimal'
    double = 'double'
    enum = 'enum'
    float = 'float'
    Guid = 'Guid'
    int = 'int'
    long = 'long'
    sbyte = 'sbyte'
    short = 'short'
    string = 'string'
    uint = 'uint'
    ulong = 'ulong'
    ushort = 'ushort'

class Property(OpenAISchema):
    model_config = ConfigDict(extra='forbid')
    Id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        description='The unique identifier for the property, represented as a UUID. This field should be generated by the client.',
        title='Id',
    )
    Name: constr(min_length=1) = Field(
        ...,
        description='The name of the property. This should be unique within the entity.',
        title='Name',
    )
    Type: TypeEnum = Field(
        ..., 
        description='The data type of the property', 
        title='Type'
    )
    EnumType: str = Field(
        '',
        description='The type of the enumeration, if the property is an enum. It should be empty for non-enum properties.',
        title='EnumType',
    )
    EnumNamespace: str = Field(
        '',
        description='The namespace where the enumeration is defined, if applicable. Do not use C# reserved keywords.',
        title='EnumNamespace',
    )
    EnumAngularImport: str = Field(
        'shared/enums',
        description='The Angular import path for the enumeration, if the property is an enum.',
        title='EnumAngularImport',
    )
    EnumFilePath: str = Field(
        None,
        description='The file path to the enumeration definition, if the property is an enum.',
        title='EnumFilePath',
    )
    DefaultValue: str = Field(
        None,
        description='The default value of the property if not otherwise set.',
        title='DefaultValue',
    )
    IsNullable: bool = Field(
        False,
        description='Indicates whether the property can be null.',
        title='IsNullable',
    )
    IsRequired: bool = Field(
        False,
        description='Indicates whether the property is required for the entity.',
        title='IsRequired',
    )
    AllowEmptyStrings: bool = Field(
        False,
        description='Determines if empty strings are allowed for string type properties.',
        title='AllowEmptyStrings',
    )
    IsTextArea: bool = Field(
        False,
        description='Indicates if the property should be represented as a text area in the UI, typically used for longer text strings.',
        title='IsTextArea',
    )
    MinLength: int = Field(
        None,
        description='The minimum length for the property value, applicable to string types.',
        title='MinLength',
    )
    MaxLength: int = Field(
        None,
        description='The maximum length for the property value, applicable to string types.',
        title='MaxLength',
    )
    SortOrder: int = Field(
        0,
        description='Specifies the default sort order of the property when listed.',
        title='SortOrder',
    )
    SortType: int = Field(
        0,
        description='Determines how the property is sorted. A value of 0 typically represents default or no sorting.',
        title='SortType',
    )
    Regex: str = Field(
        '',
        description='A regular expression pattern that the property value must match.',
        title='Regex',
    )
    EmailValidation: bool = Field(
        False,
        description='Indicates if the property value should be validated as an email address.',
        title='EmailValidation',
    )
    ShowOnList: bool = Field(
        True,
        description='Indicates if the property should be displayed in list views.',
        title='ShowOnList',
    )
    ShowOnCreateModal: bool = Field(
        True,
        description='Indicates if the property should be included in create modals/forms.',
        title='ShowOnCreateModal',
    )
    ShowOnEditModal: bool = Field(
        True,
        description='Indicates if the property should be included in edit modals/forms.',
        title='ShowOnEditModal',
    )
    ReadonlyOnEditModal: bool = Field(
        False,
        description='Indicates if the property should be read-only in edit modals/forms.',
        title='ReadonlyOnEditModal',
    )
    EnumValues: str = Field(
        None,
        description='An object representing the possible values of an enumeration, if the property is an enum.',
        title='EnumValues',
    )
    IsSelected: bool = Field(
        True,
        description='Indicates whether the property is selected by default in the UI.',
        title='IsSelected',
    )
    OrdinalIndex: int = Field(
        0,
        description='The index that can be used for ordering properties ordinally.',
        title='OrdinalIndex',
    )


class UiPickTypeEnum(Enum):
    Modal = 'Modal'
    Dropdown = 'Dropdown'
    Typeahead = 'Typeahead'


class RelatedTypeEnum(Enum):
    Int = 'int'
    Long = 'long'
    Guid = 'Guid'
    String = 'string'


class NavigationProperty(OpenAISchema):
    model_config = ConfigDict(extra='forbid')
    EntityNameWithDuplicationNumber: constr(min_length=1) = Field(
        ...,
        description='The name of the related entity, with a number appended if there is more than one relationship with the same entity.',
        title='EntityNameWithDuplicationNumber',
    )
    EntitySetNameWithDuplicationNumber: constr(min_length=1) = Field(
        ...,
        description='The name of the set containing multiple instances of the related entity.',
        title='EntitySetNameWithDuplicationNumber',
    )
    ReferencePropertyName: constr(min_length=1) = Field(
        ...,
        description='The name of the property in this entity that holds the reference to the related entity.',
        title='ReferencePropertyName',
    )
    UiPickType: UiPickTypeEnum = Field(
        'Modal',
        description='The type of UI control that should be used to pick the related entity.',
        title='UiPickType',
    )
    IsRequired: bool = Field(
        False,
        description='Indicates whether a relationship to the related entity is required.',
        title='IsRequired',
    )
    Name: constr(min_length=1) = Field(
        ...,
        description='The name of the identifier property for this navigation property.',
        title='Name',
    )
    DisplayProperty: constr(min_length=1) = Field(
        ...,
        description='The name of the property of the related entity that should be displayed in the UI.',
        title='DisplayProperty',
    )
    Namespace: constr(min_length=1) = Field(
        ..., description='The namespace of the related entity. Do not use C# reserved keywords.', title='Namespace'
    )
    EntityName: constr(min_length=1) = Field(
        ..., description='The name of the related entity. Do not use C# reserved keywords.', title='EntityName'
    )
    EntitySetName: constr(min_length=1) = Field(
        ...,
        description='The name of the set that contains multiple instances of the related entity.',
        title='EntitySetName',
    )
    DtoNamespace: constr(min_length=1) = Field(
        ...,
        description='The namespace of the Data Transfer Object (DTO) for the related entity. Do not use C# reserved keywords.',
        title='DtoNamespace',
    )
    DtoEntityName: constr(min_length=1) = Field(
        ...,
        description='The name of the DTO for the related entity.',
        title='DtoEntityName',
    )
    Type: RelatedTypeEnum = Field(
        'String',
        description='The type of the identifier for the related entity.',
        title='Type',
    )


class NavigationConnection(OpenAISchema):
    model_config = ConfigDict(extra='forbid')
    Name: constr(min_length=1) = Field(
        ...,
        description='The name of the connection, which typically represents the relationship.',
        title='Name',
    )
    DisplayProperty: constr(min_length=1) = Field(
        ...,
        description='The name of the property that should be displayed for the connection in the UI.',
        title='DisplayProperty',
    )
    Namespace: constr(min_length=1) = Field(
        ..., description='The namespace of the connected entity. Do not use C# reserved keywords.', title='Namespace'
    )
    EntityName: constr(min_length=1) = Field(
        ..., description='The name of the connected entity.', title='EntityName'
    )
    EntitySetName: constr(min_length=1) = Field(
        ...,
        description='The name of the set that contains multiple instances of the connected entity.',
        title='EntitySetName',
    )
    DtoNamespace: constr(min_length=1) = Field(
        ...,
        description='The namespace of the DTO for the connected entity. Do not use C# reserved keywords.',
        title='DtoNamespace',
    )
    DtoEntityName: constr(min_length=1) = Field(
        ...,
        description='The name of the DTO for the connected entity.',
        title='DtoEntityName',
    )
    Type: RelatedTypeEnum = Field(
        'String',
        description='The type of the identifier for the related entity.',
        title='Type',
    )


class Entity(OpenAISchema):
    """
    This is the Entity info
    """    
    class Config:
        extra = 'forbid'
    Id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        description='The unique identifier for the property, represented as a UUID. This field should be generated by the client.',
        title='Id',
    )
    Name: constr(min_length=1) = Field(
        ...,
        description='Entity name will be used as class name of your entity. Do not use C# reserved keywords.',
        title='Name',
    )
    OriginalName: constr(min_length=1) = Field(
        ...,
        description='Original Entity name will be used as class name of your entity.',
        title='OriginalName',
    )
    NamePlural: constr(min_length=1) = Field(
        ...,
        description='Plural name will be used as collection names and folder names. Do not use C# reserved keywords.',
        title='NamePlural',
    )
    DatabaseTableName: constr(min_length=1) = Field(
        ...,
        description='For relational databases it will be used as database table name. For NoSQL databases it will be used as collection name. Do not use C# reserved keywords.',
        title='DatabaseTableName',
    )
    Namespace: constr(min_length=1) = Field(
        ...,
        description="Will be used as namespace - e.g., Book entity's namespace will be Acme.Bookstore.Books. Do not use C# reserved keywords.",
        title='Namespace',
    )
    BaseClass: BaseClassEnum = Field(
        'FullAuditedAggregateRoot',
        description="ABP Framework's base class to derive this entity.",
        title='BaseClass',
    )
    MenuIcon: constr(min_length=1) = Field(
        'file-alt',
        description="Menu icon will be the entity's font awesome icon.",
        title='MenuIcon',
    )
    PrimaryKeyType: PrimaryKeyTypeEnum = Field(
        'String',
        description="Will be used as the entity's primary key data type. Guid is recommended.",
        title='PrimaryKeyType',
    )
    PreserveCustomCode: bool = Field(
        True,
        description='If selected, it will not override the custom code blocks in your entity during regeneration.',
        title='PreserveCustomCode',
    )
    IsMultiTenant: bool = Field(
        False,
        description='If selected, the entity will be multi-tenant, isolating data between tenants.',
        title='IsMultiTenant',
    )
    CheckConcurrency: bool = Field(
        True,
        description='If selected, concurrency check will be enabled for this entity.',
        title='CheckConcurrency',
    )
    ShouldCreateUserInterface: bool = Field(
        True,
        description='If selected, a user interface will be generated for managing this entity.',
        title='ShouldCreateUserInterface',
    )
    ShouldCreateBackend: bool = Field(
        True,
        description='If selected, the backend services will be generated for this entity.',
        title='ShouldCreateBackend',
    )
    ShouldExportExcel: bool = Field(
        True,
        description='If selected, functionality for exporting entity data to Excel will be generated.',
        title='ShouldExportExcel',
    )
    ShouldAddMigration: bool = Field(
        True,
        description='If selected, a new database migration will be added for this entity.',
        title='ShouldAddMigration',
    )
    ShouldUpdateDatabase: bool = Field(
        True,
        description='If selected, the database schema will be updated to include this entity.',
        title='ShouldUpdateDatabase',
    )
    CreateTests: bool = Field(
        True,
        description='If selected, unit and integration tests will be created for this entity.',
        title='CreateTests',
    )
    Properties: Optional[List[Property]] = Field(
        [],
        description='An array of Property objects, each representing a property of the entity.',
        title='Properties',
    )
    NavigationProperties: Optional[List[NavigationProperty]] = Field(
        [],
        description='An array of objects that define the navigation properties for the entity. Navigation properties represent relationships between different entities.',
        title='NavigationProperties',
    )
    NavigationConnections: Optional[List[NavigationConnection]] = Field(
        [],
        description='An array of objects that define the connections for many-to-many relationships between entities.',
        title='NavigationConnections',
    )
    PhysicalFileName: constr(min_length=1) = Field(
        ...,
        description='File name of the JSON serialization of an entity.',
        title='PhysicalFileName',
    )       
