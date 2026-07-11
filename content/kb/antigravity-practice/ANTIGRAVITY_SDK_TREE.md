# 📄 google.antigravity 模組架構拓撲樹

> 本文件由 `dump_module_tree.py` 自動探測生成。

---

## 📦 模組: `google.antigravity`
  *   *實體檔案: [__init__.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/__init__.py)*

### 類別 (Classes)
*   **`class Agent(config: google.antigravity.connections.connection.AgentConfig)`**
    *   *描述: High-level Agent API for simplified interaction.*
    *   **方法列表 (Methods):**
        - `def chat(prompt: str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand | collections.abc.Sequence[str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand])` — *Sends a prompt and returns the final response.*
*   **`class AgentConfig(**data: 'Any')`**
    *   *描述: Abstract base class for agent configuration.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def create_strategy(tool_runner: Any, hook_runner: Any)` — *Creates the ConnectionStrategy for this config.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: Optional[Mapping[str, Any]] = None, deep: bool = False)`
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Audio(**data: 'Any')`**
    *   *描述: Audio content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class BuiltinTools(*args, **kwds)`**
    *   *描述: Identifiers for common connection-provided builtin tools.*
*   **`class CapabilitiesConfig(**data: 'Any')`**
    *   *描述: General agent capability configuration.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class CustomSystemInstructions(**data: 'Any')`**
    *   *描述: Use this to completely replace the system instructions.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Document(**data: 'Any')`**
    *   *描述: Document content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class GeminiAPIEndpoint(**data: 'Any')`**
    *   *描述: Endpoint for the Gemini Developer API.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
        - `def validate_endpoint(None)`
*   **`class GeminiModelOptions(**data: 'Any')`**
    *   *描述: Gemini-specific model options.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Image(**data: 'Any')`**
    *   *描述: Image content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class LocalAgentConfig(system_instructions: str | google.antigravity.types.CustomSystemInstructions | google.antigravity.types.TemplatedSystemInstructions | None = None, capabilities: google.antigravity.types.CapabilitiesConfig | None = None, tools: list[typing.Callable[..., typing.Any]] | None = None, policies: Optional[Sequence[Union[google.antigravity.hooks.policy.Policy, Sequence[google.antigravity.hooks.policy.Policy]]]] = None, hooks: list[google.antigravity.hooks.hooks.InspectHook | google.antigravity.hooks.hooks.DecideHook | google.antigravity.hooks.hooks.TransformHook] | None = None, triggers: list[typing.Callable[[google.antigravity.triggers.triggers.TriggerContext], typing.Awaitable[NoneType]]] | None = None, mcp_servers: list[google.antigravity.types.McpStdioServer | google.antigravity.types.McpStreamableHttpServer] | None = None, workspaces: list[str] | None = None, conversation_id: str | None = None, save_dir: str | None = None, app_data_dir: str | None = None, response_schema: dict[str, typing.Any] | type[pydantic.main.BaseModel] | str | None = None, skills_paths: list[str] | None = None, model: str | google.antigravity.models.ModelTarget | None = None, models: list[google.antigravity.models.ModelTarget] | None = None, api_key: str | None = None, vertex: bool | None = None, project: str | None = None, location: str | None = None, **kwargs: Any)`**
    *   *描述: Configuration for the local harness backend.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def create_strategy(tool_runner: Any, hook_runner: Any)`
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: Optional[Mapping[str, Any]] = None, deep: bool = False)`
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ModelEndpoint(**data: 'Any')`**
    *   *描述: Base class for model endpoint authentication & routing.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
        - `def validate_endpoint(None)` — *Validates the configuration of the endpoint.*
*   **`class ModelTarget(**data: 'Any')`**
    *   *描述: Configuration for a single model.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ModelType(*args, **kwds)`**
    *   *描述: Discriminator for model purpose.*
*   **`class SystemInstructionSection(**data: 'Any')`**
    *   *描述: A named section to append to the system instructions.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class TemplatedSystemInstructions(**data: 'Any')`**
    *   *描述: Use this to override the agent's identity and append sections to the default system instructions.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ThinkingLevel(*args, **kwds)`**
    *   *描述: Thinking level for Gemini models that support extended thinking.*
*   **`class ToolContext(conversation: google.antigravity.conversation.conversation.Conversation)`**
    *   *描述: Conversation-aware context injected into tools that request it.*
    *   **方法列表 (Methods):**
        - `def get_state(key: str, default: Any = None)` — *Retrieves a value from the per-conversation state store.*
        - `def set_state(key: str, value: Any)` — *Stores a value in the per-conversation state store.*
*   **`class UsageMetadata(**data: 'Any')`**
    *   *描述: Token usage metadata from the model API.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class VertexEndpoint(**data: 'Any')`**
    *   *描述: Endpoint for the Vertex AI backend.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
        - `def validate_endpoint(None)`
*   **`class Video(**data: 'Any')`**
    *   *描述: Video content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`

### 📦 模組: `google.antigravity.agent`
  *   *實體檔案: [agent.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/agent.py)*

### 類別 (Classes)
*   **`class Agent(config: google.antigravity.connections.connection.AgentConfig)`**
    *   *描述: High-level Agent API for simplified interaction.*
    *   **方法列表 (Methods):**
        - `def chat(prompt: str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand | collections.abc.Sequence[str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand])` — *Sends a prompt and returns the final response.*

### 📦 模組: `google.antigravity.agent_test`
  *   *實體檔案: [agent_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/agent_test.py)*

### 類別 (Classes)
*   **`class AgentConfigTest(methodName='runTest')`**
    *   *描述: Tests for AgentConfig sugar, conflict guards, and defensive copy.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_agent_with_response_schema(mock_conv_create, mock_strategy_class)`
        - `def test_conversation_id_returns_none_before_session(None)` — *Verifies conversation_id is None before the session starts.*
        - `def test_conversation_id_returns_value_after_session(None)` — *Verifies conversation_id returns the runtime-assigned ID.*
        - `def test_defaults(None)` — *Verifies AgentConfig defaults: safe policies, default model.*
        - `def test_model_sugar_does_not_clobber_image_generation(None)` — *Verifies model sugar only sets default slot, not image_generation.*
        - `def test_sugar_api_key_flows_to_models(None)` — *Verifies api_key sugar flows to config.models.*
        - `def test_sugar_model_flows_to_models(None)` — *Verifies model sugar flows to config.models.*
*   **`class AgentTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_agent_aexit_passes_exceptions(None)`
        - `def test_agent_aexit_returns_suppression_status(None)`
        - `def test_agent_api_key_env(mock_conv_create, mock_strategy_class)`
        - `def test_agent_chat(mock_conv_create, mock_strategy_class)`
        - `def test_agent_chat_before_start(None)`
        - `def test_agent_chat_multimodal_input(mock_conv_create, mock_strategy_class)` — *Verifies that the Agent public API method accepts multimodal Content payloads.*
        - `def test_agent_conversation_after_start(mock_conv_create, mock_strategy_class)` — *Verifies conversation returns the Conversation instance after start.*
        - `def test_agent_conversation_before_start(None)` — *Verifies conversation raises RuntimeError before session starts.*
        - `def test_agent_default_capabilities(mock_conv_create, mock_strategy_class)` — *Default LocalAgentConfig enables all tools (permissive).*
        - `def test_agent_is_started_after_start(mock_conv_create, mock_strategy_class)` — *Verifies is_started returns True inside async with.*
        - `def test_agent_is_started_before_start(None)` — *Verifies is_started returns False before session starts.*
        - `def test_agent_lifecycle(mock_conv_create, mock_strategy_class)`
        - `def test_agent_mcp_server_unknown_type(mock_conv_create, mock_strategy_class)`
        - `def test_agent_model_sugar_flows_to_strategy(mock_conv_create, mock_strategy_class)`
        - `def test_agent_register_hook(mock_conv_create, mock_strategy_class)`
        - `def test_agent_register_trigger(mock_trigger_runner_class, mock_conv_create, mock_strategy_class)`
        - `def test_agent_requires_policies_in_write_mode(mock_conv_create, mock_strategy_class)`
        - `def test_agent_with_policies(mock_conv_create, mock_strategy_class)`
        - `def test_agent_with_session_config(mock_conv_create, mock_strategy_class)`
        - `def test_agent_with_skills_paths(mock_conv_create, mock_strategy_class)`
        - `def test_agent_with_system_instructions_object(mock_conv_create, mock_strategy_class)`
        - `def test_agent_write_mode_with_policies(mock_conv_create, mock_strategy_class)`
        - `def test_policy_guard_empty_disabled_tools(mock_conv_create, mock_strategy_class)` — *Guard fires when disabled_tools=[] (= all tools enabled).*
        - `def test_policy_guard_explicit_all_tools(mock_conv_create, mock_strategy_class)` — *Guard fires when all tools are listed explicitly.*
        - `def test_policy_guard_explicit_write_tool(mock_conv_create, mock_strategy_class)` — *Guard fires when enabled_tools includes a non-read-only tool.*
        - `def test_policy_guard_mcp_server_requires_policies_or_hook(mock_conv_create, mock_strategy_class)` — *Guard fires when MCP servers are present but no policies or hooks.*
        - `def test_policy_guard_mcp_server_with_hook_passes(mock_conv_create, mock_strategy_class)` — *No guard when MCP servers are present AND a decide hook is provided.*
        - `def test_policy_guard_mcp_server_with_policy_passes(mock_conv_create, mock_strategy_class)` — *No guard when MCP servers are present AND policies are provided.*
        - `def test_policy_guard_read_only_explicit_passes(mock_conv_create, mock_strategy_class)` — *No guard when only read-only tools are explicitly enabled.*
        - `def test_policy_guard_write_tools_with_policy_passes(mock_conv_create, mock_strategy_class)` — *No guard when write tools are enabled AND policies are provided.*

### 📦 模組: `google.antigravity.connections`
  *   *實體檔案: [__init__.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/__init__.py)*

#### 📦 模組: `google.antigravity.connections.connection`
  *   *實體檔案: [connection.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/connection.py)*

### 類別 (Classes)
*   **`class AgentConfig(**data: 'Any')`**
    *   *描述: Abstract base class for agent configuration.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def create_strategy(tool_runner: Any, hook_runner: Any)` — *Creates the ConnectionStrategy for this config.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: Optional[Mapping[str, Any]] = None, deep: bool = False)`
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Connection(*args, **kwargs)`**
    *   *描述: A live session with an agent backend.*
    *   **方法列表 (Methods):**
        - `def cancel(None)` — *Cancels the current turn in progress.*
        - `def disconnect(None)` — *Disconnects the session and releases resources.*
        - `def receive_steps(None)` — *Receives steps as they complete from the agent.*
        - `def send(prompt: str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand | collections.abc.Sequence[str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand] | None, **kwargs: Any)` — *Sends a prompt to the agent.*
        - `def send_trigger_notification(content: str)` — *Sends a trigger message to the agent.*
        - `def wait_for_idle(None)` — *Blocks until the connection becomes idle.*
        - `def wait_for_wakeup(timeout: float = 300.0)` — *Blocks until the connection wakes up or the timeout is reached.*
*   **`class ConnectionStrategy(*args, **kwargs)`**
    *   *描述: Strategy for establishing a Connection to an agent backend.*
    *   **方法列表 (Methods):**
        - `def connect(None)` — *Returns the established Connection.*

#### 📦 模組: `google.antigravity.connections.connection_test`
  *   *實體檔案: [connection_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/connection_test.py)*

### 類別 (Classes)
*   **`class AgentConfigTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_cannot_instantiate_abc(None)`
        - `def test_concrete_subclass_works(None)`
        - `def test_model_copy_deep_preserves_executable_references(None)`
        - `def test_policies_validation(None)`
        - `def test_response_schema_invalid_json_raises(None)`
        - `def test_response_schema_unsupported_type_raises(None)`
        - `def test_response_schema_valid_json_string(None)`
        - `def test_subclass_must_implement_create_strategy(None)`
*   **`class ConnectionTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_default_implementations(None)`
*   **`class DummyConnection(*args, **kwargs)`**
    *   **方法列表 (Methods):**
        - `def cancel(None)` — *Cancels the current turn in progress.*
        - `def disconnect(None)`
        - `def receive_steps(None)`
        - `def send(prompt: str, **kwargs)`
        - `def send_trigger_notification(content: str)`
        - `def wait_for_idle(None)` — *Blocks until the connection becomes idle.*
        - `def wait_for_wakeup(timeout: float = 300.0)` — *Blocks until the connection wakes up or the timeout is reached.*

#### 📦 模組: `google.antigravity.connections.local`
  *   *實體檔案: [__init__.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/__init__.py)*

### 類別 (Classes)
*   **`class EditFileResult(**data: 'Any')`**
    *   *描述: Structured result from an edit_file tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class FindFileResult(**data: 'Any')`**
    *   *描述: Structured result from a find_file tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class GenerateImageResult(**data: 'Any')`**
    *   *描述: Structured result from a generate_image tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ListDirectoryEntry(**data: 'Any')`**
    *   *描述: Single entry in a directory listing.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ListDirectoryResult(**data: 'Any')`**
    *   *描述: Structured result from a list_directory tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class LocalAgentConfig(system_instructions: str | google.antigravity.types.CustomSystemInstructions | google.antigravity.types.TemplatedSystemInstructions | None = None, capabilities: google.antigravity.types.CapabilitiesConfig | None = None, tools: list[typing.Callable[..., typing.Any]] | None = None, policies: Optional[Sequence[Union[google.antigravity.hooks.policy.Policy, Sequence[google.antigravity.hooks.policy.Policy]]]] = None, hooks: list[google.antigravity.hooks.hooks.InspectHook | google.antigravity.hooks.hooks.DecideHook | google.antigravity.hooks.hooks.TransformHook] | None = None, triggers: list[typing.Callable[[google.antigravity.triggers.triggers.TriggerContext], typing.Awaitable[NoneType]]] | None = None, mcp_servers: list[google.antigravity.types.McpStdioServer | google.antigravity.types.McpStreamableHttpServer] | None = None, workspaces: list[str] | None = None, conversation_id: str | None = None, save_dir: str | None = None, app_data_dir: str | None = None, response_schema: dict[str, typing.Any] | type[pydantic.main.BaseModel] | str | None = None, skills_paths: list[str] | None = None, model: str | google.antigravity.models.ModelTarget | None = None, models: list[google.antigravity.models.ModelTarget] | None = None, api_key: str | None = None, vertex: bool | None = None, project: str | None = None, location: str | None = None, **kwargs: Any)`**
    *   *描述: Configuration for the local harness backend.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def create_strategy(tool_runner: Any, hook_runner: Any)`
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: Optional[Mapping[str, Any]] = None, deep: bool = False)`
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class LocalConnection(process: subprocess.Popen[bytes] | None, ws: Any, tool_runner: google.antigravity.tools.tool_runner.ToolRunner | None = None, hook_runner: google.antigravity.hooks.hook_runner.HookRunner | None = None, initial_history: Optional[Sequence[google.antigravity.types.Step]] = None)`**
    *   *描述: Connection to the Go-based local harness.*
    *   **方法列表 (Methods):**
        - `def cancel(None)` — *Cancels the current turn.*
        - `def disconnect(None)` — *Tears down the harness connection in a careful order.*
        - `def receive_steps(None)` — *Receives steps as they complete from the agent.*
        - `def send(prompt: str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand | collections.abc.Sequence[str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand] | None, **kwargs: Any)` — *Sends a prompt to the agent.*
        - `def send_trigger_notification(content: str)` — *Sends a trigger message to the agent.*
        - `def wait_for_idle(None)` — *Blocks until the connection becomes idle.*
        - `def wait_for_wakeup(timeout: float = 300.0)` — *Blocks until the connection wakes up or the timeout is reached.*
*   **`class LocalConnectionStep(**data: 'Any')`**
    *   *描述: Connection-specific step for LocalConnection.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_dict(step_dict: dict[str, typing.Any])` — *Creates a LocalConnectionStep from a dictionary representation of StepUpdate.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class LocalConnectionStrategy(tool_runner: google.antigravity.tools.tool_runner.ToolRunner | None = None, hook_runner: google.antigravity.hooks.hook_runner.HookRunner | None = None, models: list[google.antigravity.models.ModelTarget] | None = None, skills_paths: list[str] | None = None, system_instructions: str | google.antigravity.types.CustomSystemInstructions | google.antigravity.types.TemplatedSystemInstructions | None = None, capabilities_config: google.antigravity.types.CapabilitiesConfig | None = None, conversation_id: str | None = None, save_dir: str | None = None, workspaces: list[str] | None = None, app_data_dir: str | None = None, mcp_servers: Optional[Sequence[google.antigravity.types.McpStdioServer | google.antigravity.types.McpStreamableHttpServer]] = None, subagents: list[google.antigravity.types.SubagentConfig] | None = None)`**
    *   *描述: Strategy for establishing a LocalConnection.*
    *   **方法列表 (Methods):**
        - `def connect(None)` — *Returns the established Connection.*
*   **`class RunCommandResult(**data: 'Any')`**
    *   *描述: Structured result from a run_command tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SearchDirectoryResult(**data: 'Any')`**
    *   *描述: Structured result from a search_directory tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class TextResult(**data: 'Any')`**
    *   *描述: Generic fallback for tools without structured output (e.g. view_file).*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`

##### 📦 模組: `google.antigravity.connections.local.hook_router`
  *   *實體檔案: [hook_router.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/hook_router.py)*

### 類別 (Classes)
*   **`class HookRouter(hook_runner: google.antigravity.hooks.hook_runner.HookRunner, event_sender: Callable[[localharness_pb2.InputEvent], Coroutine[Any, Any, NoneType]])`**
    *   *描述: Routes and dispatches CallHookRequest messages from the local harness to the active HookRunner.*
    *   **方法列表 (Methods):**
        - `def handle(req: localharness_pb2.CallHookRequest)` — *Handles an incoming CallHookRequest and sends a CallHookResponse back to the harness.*

##### 📦 模組: `google.antigravity.connections.local.hook_router_test`
  *   *實體檔案: [hook_router_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/hook_router_test.py)*

### 類別 (Classes)
*   **`class HookRouterTest(*args, **kwargs)`**
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_handle_on_session_end(None)`
        - `def test_handle_on_session_start(None)`
        - `def test_handle_post_turn(None)`
        - `def test_handle_pre_turn_allow(None)`
        - `def test_handle_pre_turn_multipart_content(None)`
        - `def test_handle_unknown_hook(None)`

##### 📦 模組: `google.antigravity.connections.local.local_connection`
  *   *實體檔案: [local_connection.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/local_connection.py)*

### 類別 (Classes)
*   **`class LocalConnection(process: subprocess.Popen[bytes] | None, ws: Any, tool_runner: google.antigravity.tools.tool_runner.ToolRunner | None = None, hook_runner: google.antigravity.hooks.hook_runner.HookRunner | None = None, initial_history: Optional[Sequence[google.antigravity.types.Step]] = None)`**
    *   *描述: Connection to the Go-based local harness.*
    *   **方法列表 (Methods):**
        - `def cancel(None)` — *Cancels the current turn.*
        - `def disconnect(None)` — *Tears down the harness connection in a careful order.*
        - `def receive_steps(None)` — *Receives steps as they complete from the agent.*
        - `def send(prompt: str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand | collections.abc.Sequence[str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand] | None, **kwargs: Any)` — *Sends a prompt to the agent.*
        - `def send_trigger_notification(content: str)` — *Sends a trigger message to the agent.*
        - `def wait_for_idle(None)` — *Blocks until the connection becomes idle.*
        - `def wait_for_wakeup(timeout: float = 300.0)` — *Blocks until the connection wakes up or the timeout is reached.*
*   **`class LocalConnectionStep(**data: 'Any')`**
    *   *描述: Connection-specific step for LocalConnection.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_dict(step_dict: dict[str, typing.Any])` — *Creates a LocalConnectionStep from a dictionary representation of StepUpdate.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class LocalConnectionStrategy(tool_runner: google.antigravity.tools.tool_runner.ToolRunner | None = None, hook_runner: google.antigravity.hooks.hook_runner.HookRunner | None = None, models: list[google.antigravity.models.ModelTarget] | None = None, skills_paths: list[str] | None = None, system_instructions: str | google.antigravity.types.CustomSystemInstructions | google.antigravity.types.TemplatedSystemInstructions | None = None, capabilities_config: google.antigravity.types.CapabilitiesConfig | None = None, conversation_id: str | None = None, save_dir: str | None = None, workspaces: list[str] | None = None, app_data_dir: str | None = None, mcp_servers: Optional[Sequence[google.antigravity.types.McpStdioServer | google.antigravity.types.McpStreamableHttpServer]] = None, subagents: list[google.antigravity.types.SubagentConfig] | None = None)`**
    *   *描述: Strategy for establishing a LocalConnection.*
    *   **方法列表 (Methods):**
        - `def connect(None)` — *Returns the established Connection.*
*   **`class _PendingCallKey(*args, **kwargs)`**
    *   *描述: Key for tracking approved built-in tool calls.*
*   **`class _PendingCallValue(*args, **kwargs)`**
    *   *描述: Value for tracking approved built-in tool calls.*
*   **`class _StepTracker(state: int = 0, handled_requests: set[str] = <factory>, pre_step_dispatched: bool = False, post_step_dispatched: bool = False)`**
    *   *描述: Tracks state and handled requests for a trajectory step to prevent non-linearity bugs.*
    *   **方法列表 (Methods):**
        - `def mark_handled(request_type: str)` — *Marks a request as handled to prevent duplicate processing.*
        - `def update_state(new_state: int)` — *Updates state and clears handled requests if transitioning out of waiting.*

##### 📦 模組: `google.antigravity.connections.local.local_connection_config`
  *   *實體檔案: [local_connection_config.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/local_connection_config.py)*

### 類別 (Classes)
*   **`class LocalAgentConfig(system_instructions: str | google.antigravity.types.CustomSystemInstructions | google.antigravity.types.TemplatedSystemInstructions | None = None, capabilities: google.antigravity.types.CapabilitiesConfig | None = None, tools: list[typing.Callable[..., typing.Any]] | None = None, policies: Optional[Sequence[Union[google.antigravity.hooks.policy.Policy, Sequence[google.antigravity.hooks.policy.Policy]]]] = None, hooks: list[google.antigravity.hooks.hooks.InspectHook | google.antigravity.hooks.hooks.DecideHook | google.antigravity.hooks.hooks.TransformHook] | None = None, triggers: list[typing.Callable[[google.antigravity.triggers.triggers.TriggerContext], typing.Awaitable[NoneType]]] | None = None, mcp_servers: list[google.antigravity.types.McpStdioServer | google.antigravity.types.McpStreamableHttpServer] | None = None, workspaces: list[str] | None = None, conversation_id: str | None = None, save_dir: str | None = None, app_data_dir: str | None = None, response_schema: dict[str, typing.Any] | type[pydantic.main.BaseModel] | str | None = None, skills_paths: list[str] | None = None, model: str | google.antigravity.models.ModelTarget | None = None, models: list[google.antigravity.models.ModelTarget] | None = None, api_key: str | None = None, vertex: bool | None = None, project: str | None = None, location: str | None = None, **kwargs: Any)`**
    *   *描述: Configuration for the local harness backend.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def create_strategy(tool_runner: Any, hook_runner: Any)`
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: Optional[Mapping[str, Any]] = None, deep: bool = False)`
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`

##### 📦 模組: `google.antigravity.connections.local.local_connection_test`
  *   *實體檔案: [local_connection_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/local_connection_test.py)*

### 類別 (Classes)
*   **`class GetDefaultBinaryPathTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_raises_when_not_found(mock_which, mock_files, mock_dist)`
        - `def test_returns_env_path(None)`
        - `def test_returns_external_wheel_path(mock_exists, mock_files, mock_dist)`
        - `def test_returns_internal_pyglib_resource_path(mock_dist)`
        - `def test_returns_metadata_distribution_path(mock_exists, mock_dist)`
        - `def test_returns_system_path(mock_which, mock_files, mock_dist)`
*   **`class LocalAgentConfigTest(*args, **kwargs)`**
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_app_data_dir_relative_path_raises(None)`
        - `def test_constructor_parameters_fully_typed(None)` — *Verifies all subclass fields are accepted by the constructor under pytype.*
        - `def test_create_strategy(None)`
        - `def test_create_strategy_app_data_dir(None)`
        - `def test_create_strategy_with_mcp_servers(None)`
        - `def test_explicit_allow_all_overrides_default(None)` — *Explicit allow_all() replaces the confirm_run_command default.*
        - `def test_merge_models_explicit_and_shorthand(None)`
        - `def test_merge_models_explicit_only(None)`
        - `def test_merge_models_only_defaults(None)`
        - `def test_merge_models_shorthand_only(None)`
        - `def test_safe_defaults(None)` — *LocalAgentConfig defaults to confirm_run_command() — deny run_command.*
        - `def test_safe_defaults_with_default_workspace(None)` — *LocalAgentConfig defaults to CWD workspace when not specified.*
        - `def test_workspace_policies_auto_prepended(None)` — *workspace_only() policies are auto-prepended when workspaces are set.*
*   **`class LocalAgentConfigWorkspaceTest(*args, **kwargs)`**
    *   *描述: Tests for workspace scoping policy with app_data_dir inclusion.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)` — *Returns the descriptive ID of the test.*
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_workspace_policy_denies_symlink_traversal(None)` — *Tests that the workspace scoping policy correctly blocks symlinks pointing outside.*
        - `def test_workspace_policy_scenarios_allowed_in_custom_app_data_dir(app_data_dir_factory, path_factory, expected_allowed: bool, msg: str)` — *test_workspace_policy_scenarios_allowed_in_custom_app_data_dir(app_data_dir_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076fc040>, path_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076fc0e0>, expected_allowed=True, msg='Target inside custom app_data_dir should be allowed')*
        - `def test_workspace_policy_scenarios_allowed_in_default_app_data_dir(app_data_dir_factory, path_factory, expected_allowed: bool, msg: str)` — *test_workspace_policy_scenarios_allowed_in_default_app_data_dir(app_data_dir_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076fc180>, path_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076fc220>, expected_allowed=True, msg='Target inside default app_data_dir should be allowed when config is None')*
        - `def test_workspace_policy_scenarios_allowed_in_workspace(app_data_dir_factory, path_factory, expected_allowed: bool, msg: str)` — *test_workspace_policy_scenarios_allowed_in_workspace(app_data_dir_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076f3ec0>, path_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076f3f60>, expected_allowed=True, msg='Target inside workspace should be allowed')*
        - `def test_workspace_policy_scenarios_denied_outside_both(app_data_dir_factory, path_factory, expected_allowed: bool, msg: str)` — *test_workspace_policy_scenarios_denied_outside_both(app_data_dir_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076fc2c0>, path_factory=<function LocalAgentConfigWorkspaceTest.<lambda> at 0x1076fc360>, expected_allowed=False, msg='Target outside both workspace and app_data_dir should be denied')*
*   **`class LocalConnectionBuiltinDecideHookTest(methodName='runTest')`**
    *   *描述: Verifies Decide hooks run for built-in tool confirmations.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_decide_hooks_run_for_builtin_tools(None)` — *Verifies PreToolCallDecideHook runs and can deny builtin tools.*
*   **`class LocalConnectionBuiltinToolHooksTest(methodName='runTest')`**
    *   *描述: Tests for PostToolCallHook / OnToolErrorHook dispatch for built-in tools.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_denied_builtin_not_tracked(None)` — *Verifies denied builtin tools are not tracked for post-tool dispatch.*
        - `def test_no_spurious_hook_for_non_builtin_step(None)` — *Verifies post-tool hooks don't fire for normal model response steps.*
        - `def test_on_tool_error_dispatched_for_builtin_error(None)` — *Verifies OnToolErrorHook fires when a builtin tool transitions to STATE_ERROR.*
        - `def test_tool_result_fallback_for_view_file(None)` — *Verifies PostToolCallHook falls back to step text for view_file.*
        - `def test_tool_result_for_edit_file(None)` — *Verifies PostToolCallHook receives EditFileResult for edit_file.*
        - `def test_tool_result_for_find_file(None)` — *Verifies PostToolCallHook receives FindFileResult for find_file.*
        - `def test_tool_result_for_generate_image(None)` — *Verifies PostToolCallHook receives GenerateImageResult for generate_image.*
        - `def test_tool_result_for_list_directory(None)` — *Verifies PostToolCallHook receives ListDirectoryResult for list_dir.*
        - `def test_tool_result_for_run_command(None)` — *Verifies PostToolCallHook receives RunCommandResult for run_command.*
        - `def test_tool_result_for_search_directory(None)` — *Verifies PostToolCallHook receives SearchDirectoryResult for grep_search.*
        - `def test_tool_result_for_search_web(None)` — *Verifies PostToolCallHook receives SearchWebResult for search_web.*
*   **`class LocalConnectionCompactionHookTest(methodName='runTest')`**
    *   *描述: Tests for compaction hook dispatch.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_compaction_step_dispatches_hook(None)` — *Verifies OnCompactionHook fires when a compaction step is received.*
*   **`class LocalConnectionDisconnectTest(methodName='runTest')`**
    *   *描述: Tests for the disconnect shutdown sequence.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_disconnect_closes_stdin(None)` — *Verifies stdin is closed during disconnect to trigger harness save.*
        - `def test_disconnect_closes_ws_before_stdin(None)` — *Verifies the WebSocket is closed before stdin.*
        - `def test_disconnect_kills_on_double_timeout(None)` — *Verifies SIGKILL is sent when SIGTERM also fails.*
        - `def test_disconnect_sets_disconnecting_flag(None)` — *Verifies _disconnecting is set before any cleanup runs.*
        - `def test_disconnect_terminates_on_timeout(None)` — *Verifies SIGTERM is sent when the process doesn't exit in time.*
        - `def test_disconnect_waits_for_process(None)` — *Verifies disconnect waits for the harness process to exit.*
*   **`class LocalConnectionExceptionSafetyTest(methodName='runTest')`**
    *   *描述: Tests verifying that handler exceptions don't deadlock the harness.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_question_handler_crash_sends_error(None)` — *Verifies a crashing interaction hook sends the error message.*
        - `def test_tool_call_crash_sends_error_result(None)` — *Verifies a crashing pre-tool hook sends error in ToolResponse.*
        - `def test_tool_confirmation_crash_sends_rejection(None)` — *Verifies a crashing pre-tool hook sends accepted=False.*
*   **`class LocalConnectionHookAcceptanceTest(methodName='runTest')`**
    *   *描述: Verifies that previously-unsupported hooks are now accepted.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_compaction_hooks_no_longer_raise(None)` — *Compaction hooks should be accepted now.*
        - `def test_subagent_tool_hooks_accepted(None)` — *Subagent lifecycle is handled by tool hooks; no special subagent lists.*
*   **`class LocalConnectionPostTurnHookTest(methodName='runTest')`**
    *   *描述: Tests for post-turn hook dispatch.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_post_turn_hook_dispatched_on_final_step(None)` — *Verifies PostTurnHook fires when a terminal model step is received.*
        - `def test_post_turn_hook_not_fired_for_environment_step(None)` — *Verifies PostTurnHook does NOT fire for TARGET_ENVIRONMENT steps.*
        - `def test_receive_steps_includes_target_environment(None)` — *Verifies TARGET_ENVIRONMENT steps are yielded by receive_steps().*
*   **`class LocalConnectionSendTest(methodName='runTest')`**
    *   *描述: Validates multi-modal coercion and InputEvent serialization inside LocalConnection.send().*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_concurrent_receive_steps_raises(None)` — *Verifies that a second concurrent receive_steps() call raises RuntimeError.*
        - `def test_send_flat_string_populates_user_input(None)` — *Verifies that a standard string prompt maps to the user_input proto field.*
        - `def test_send_mixed_list_populates_multiple_complex_content(None)` — *Verifies that a list containing both strings and rich Content primitives compiles correctly to spec.*
        - `def test_send_none_prompt_populates_blank_string(None)` — *Verifies that passing a prompt of None maps to a blank userInput string frame.*
        - `def test_send_single_media_content_populates_complex_user_input(None)` — *Verifies that a single rich Content primitive maps to the complex_user_input parts list.*
        - `def test_send_slash_command_populates_complex_user_input(None)` — *Verifies that a SlashCommand primitive maps to complex_user_input slash_command field.*
        - `def test_trigger_notification_succeeds_while_busy(None)` — *Verifies send_trigger_notification() and send() work during an active turn.*
*   **`class LocalConnectionSerializationTest(methodName='runTest')`**
    *   *描述: Tests verifying Pydantic-based normalization in _tool_result_to_dict.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_normalizes_bytes_to_string(None)` — *Verifies _tool_result_to_dict normalizes bytes into UTF-8 strings.*
        - `def test_normalizes_datetime_to_iso_string(None)` — *Verifies _tool_result_to_dict normalizes datetimes into ISO strings.*
        - `def test_normalizes_set_to_list(None)` — *Verifies _tool_result_to_dict normalizes sets into JSON lists.*
        - `def test_preserves_pydantic_custom_serializer(None)` — *Verifies _tool_result_to_dict respects custom @field_serializer.*
*   **`class LocalConnectionSessionHooksTest(methodName='runTest')`**
    *   *描述: Tests for session start/end hook dispatch.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_session_end_hook_dispatched_on_disconnect(None)` — *Verifies OnSessionEndHook fires via LSP handshake when disconnect() is called.*
        - `def test_strategy_dispatches_session_start(None)` — *Verifies the connection correctly delegates OnSessionStart hook execution to the HookRunner whenever requested by the harness engine.*
*   **`class LocalConnectionStderrReaderTest(methodName='runTest')`**
    *   *描述: Tests for the background stderr reader thread.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_start_stderr_reader_drains_lines(None)` — *Verifies that _start_stderr_reader captures stderr lines.*
        - `def test_stderr_reader_handles_closed_stream(None)` — *Verifies the reader thread exits cleanly when the stream closes.*
        - `def test_stderr_reader_respects_maxlen(None)` — *Verifies the deque drops old lines when it exceeds maxlen.*
        - `def test_stderr_reader_thread_is_daemon(None)` — *Verifies the stderr reader thread is a daemon thread.*
*   **`class LocalConnectionStepFromDictTest(methodName='runTest')`**
    *   *描述: Tests for LocalConnectionStep.from_dict derivation logic.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_is_complete_response_false_when_error_state(None)` — *Verifies is_complete_response is False when state is ERROR.*
        - `def test_is_complete_response_false_when_no_text(None)` — *Verifies is_complete_response is False when text is empty.*
        - `def test_is_complete_response_false_when_not_done(None)` — *Verifies is_complete_response is False when state is not DONE.*
        - `def test_is_complete_response_false_when_source_not_model(None)` — *Verifies is_complete_response is False when source is not MODEL.*
        - `def test_is_complete_response_false_when_target_environment(None)` — *Verifies is_complete_response is False for TARGET_ENVIRONMENT steps.*
        - `def test_is_complete_response_true(None)` — *Verifies is_complete_response is True when source=MODEL, state=DONE, target=TARGET_USER, and text is present.*
        - `def test_step_from_dict_normalizes_cns_uri_arguments(None)` — *Verifies that LocalConnectionStep.from_dict normalizes cns:// URIs.*
        - `def test_step_from_dict_normalizes_file_uri_arguments(None)` — *Verifies that LocalConnectionStep.from_dict normalizes file:// URIs.*
        - `def test_step_type_tool_call_with_builtin(None)` — *Verifies that a step with a builtin tool proto field is typed TOOL_CALL and parses details.*
        - `def test_structured_output_extracted_from_finish(None)` — *Verifies that structured output is extracted when finish payload is present.*
        - `def test_structured_output_extracted_from_finish_handles_invalid_json(None)` — *Verifies that invalid JSON in finish payload defaults to None.*
*   **`class LocalConnectionStrategyApiKeyTest(methodName='runTest')`**
    *   *描述: Tests for API key validation in LocalConnectionStrategy.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_accepts_env_var_api_key(mock_popen)` — *Verifies entry does not raise when GEMINI_API_KEY env var is set.*
        - `def test_accepts_models_api_key(mock_popen)` — *Verifies entry does not raise when model endpoint api_key is set.*
        - `def test_accepts_vertex_config_with_project_location(mock_popen)` — *Verifies entry does not raise when Vertex is enabled and project/location are provided.*
        - `def test_raises_with_empty_endpoint_api_key(None)` — *Verifies entry raises when GeminiAPIEndpoint has no api_key and env is unset.*
        - `def test_raises_without_api_key(None)` — *Verifies entry raises when no API key is available.*
        - `def test_raises_without_auth_in_vertex_mode(None)` — *Verifies strategy raises validation error when Vertex is set but no project/location or api_key provided.*
*   **`class LocalConnectionStrategyConfigTest(*args, **kwargs)`**
    *   *描述: Tests for config-to-proto translation in LocalConnectionStrategy.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)` — *Returns the descriptive ID of the test.*
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_app_data_dir_default_empty(None)`
        - `def test_app_data_dir_specified(None)`
        - `def test_capabilities_config_compaction_threshold(None)` — *Verifies compaction_threshold maps to HarnessConfig.compaction_threshold.*
        - `def test_capabilities_config_disabled_tools(None)` — *Verifies that disabling tools produces the correct proto.*
        - `def test_capabilities_config_enabled_tools(None)` — *Verifies that enabled_tools allowlist excludes non-listed tools.*
        - `def test_capabilities_config_finish_tool_schema_json_to_proto(None)` — *Verifies capabilities config propagates finish tool schema to the proto config.*
        - `def test_capabilities_config_none_uses_defaults(None)` — *Verifies that capabilities_config=None produces default-enabled tools.*
        - `def test_capabilities_config_subagents_disabled_via_disabled_tools(capabilities_config)` — *test_capabilities_config_subagents_disabled_via_disabled_tools(capabilities_config=CapabilitiesConfig(enable_subagents=True, enabled_tools=None, disabled_tools=[<BuiltinTools.START_SUBAGENT: 'start_subagent'>], compaction_threshold=None, finish_tool_schema_json=None))*
        - `def test_capabilities_config_subagents_disabled_via_enable_subagents_false(capabilities_config)` — *test_capabilities_config_subagents_disabled_via_enable_subagents_false(capabilities_config=CapabilitiesConfig(enable_subagents=False, enabled_tools=None, disabled_tools=None, compaction_threshold=None, finish_tool_schema_json=None))*
        - `def test_cascade_id_default_empty(None)` — *Verifies that cascade_id defaults to empty string when no conversation_id set.*
        - `def test_cascade_id_passed_through(None)` — *Verifies that session_config.conversation_id maps to HarnessConfig.cascade_id.*
        - `def test_default_config_produces_valid_harness_config(None)` — *Verifies that a strategy with all defaults produces a well-formed proto.*
        - `def test_empty_workspaces_list(None)` — *Verifies that an empty list produces an empty repeated field.*
        - `def test_full_session_config_to_proto(None)` — *Verifies that a full session_config produces correct proto fields.*
        - `def test_gemini_config_none_fields_omitted(None)` — *Verifies that None fields on ModelConfig are not set on the proto.*
        - `def test_gemini_config_to_proto(None)` — *Verifies GeminiConfig fields translate to the correct proto fields.*
        - `def test_legacy_shorthands_api_key_produces_valid_proto(None)` — *Verifies that the legacy api_key shorthand translates to the models proto.*
        - `def test_legacy_shorthands_vertex_produces_valid_proto(None)` — *Verifies that the legacy vertex shorthands translate to the models proto.*
        - `def test_models_default_model_name(None)` — *Verifies the default model name propagates correctly.*
        - `def test_models_list_custom_endpoints_propagate(None)` — *Verifies that custom endpoints in the models list propagate to proto.*
        - `def test_models_list_propagates(None)` — *Verifies that the new models list propagates to HarnessConfig.*
        - `def test_models_stored_directly_on_strategy(None)` — *Verifies that the models list is stored as self._models.*
        - `def test_models_thinking_level_all_values(None)` — *Verifies all ThinkingLevel enum values produce correct proto strings.*
        - `def test_models_thinking_level_none_omitted(None)` — *Verifies that thinking_level=None leaves the proto field at its default.*
        - `def test_models_thinking_level_set(None)` — *Verifies that thinking_level on ModelTarget maps to the proto field.*
        - `def test_session_config_save_dir_default_none(None)` — *Verifies that save_dir defaults to None when not provided.*
        - `def test_session_config_save_dir_stored(None)` — *Verifies that session_config.save_dir is preserved on the strategy.*
        - `def test_skills_paths_to_proto(None)` — *Verifies skills_paths translate directly to the proto repeated field.*
        - `def test_storage_directory_defaults_to_none(None)` — *Verifies save_dir is None when not specified.*
        - `def test_storage_directory_from_save_dir(None)` — *Verifies save_dir maps to InputConfig.storage_directory.*
        - `def test_strategy_normalizes_configured_workspaces(None)` — *Verifies that workspace configurations using file:// URIs are canonicalized.*
        - `def test_system_instructions_model_custom(None)` — *Verifies that CustomSystemInstructions sets custom on the proto.*
        - `def test_system_instructions_model_templated(None)` — *Verifies that TemplatedSystemInstructions sets appended on the proto.*
        - `def test_system_instructions_model_templated_only_identity(None)` — *Verifies that TemplatedSystemInstructions with only identity maps correctly.*
        - `def test_system_instructions_model_templated_only_sections(None)` — *Verifies that TemplatedSystemInstructions with only sections maps correctly.*
        - `def test_system_instructions_none(None)` — *Verifies that no system_instructions field is set when not provided.*
        - `def test_system_instructions_string_shorthand(None)` — *Verifies that a plain string normalizes to AppendedSystemInstructions.*
        - `def test_vertex_config_propagates(None)` — *Verifies that Vertex configuration fields propagate to proto.*
        - `def test_workspaces_default_empty(None)` — *Verifies no workspace protos when session_config has no workspaces.*
        - `def test_workspaces_none(None)` — *Verifies that no workspaces are set when not provided.*
        - `def test_workspaces_to_proto(None)` — *Verifies workspace paths translate to Workspace protos correctly.*
*   **`class LocalConnectionSubagentHookTest(methodName='runTest')`**
    *   *描述: Tests for subagent hook dispatch via tool hooks.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_connection_waits_for_subagents_before_idle(None)` — *Verifies receive_steps blocks until subagents complete.*
        - `def test_invoke_subagent_step_classified_as_tool_call(None)` — *Verifies invoke_subagent steps are classified as TOOL_CALL.*
        - `def test_post_tool_hook_on_subagent_trajectory_idle(None)` — *Verifies post-tool-call hook fires when a non-main trajectory goes idle.*
        - `def test_send_resets_subagent_tracking(None)` — *Verifies send() clears subagent tracking state.*
        - `def test_subagent_running_tracked(None)` — *Verifies STATE_RUNNING adds subagent to active set.*
        - `def test_ws_reader_parses_usage_metadata(None)` — *Verifies that _ws_reader_loop parses and attaches usage_metadata to steps.*
*   **`class LocalConnectionSubagentsTest(methodName='runTest')`**
    *   *描述: Tests verifying that static subagent configs are built into HarnessConfig.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_builds_subagents_proto_correctly(None)`
        - `def test_builds_subagents_proto_with_sections(None)`
        - `def test_subagent_harness_tools_as_strings_raise_if_not_registered(None)`
        - `def test_subagent_tool_not_registered_raises(None)`
        - `def test_subagent_tools_stripped_and_warned(None)`
*   **`class LocalConnectionTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_async_non_blocking_dispatch(None)` — *Verifies that wait handlers run concurrently without blocking loop.*
        - `def test_cancel_e2e_raises_cancelled_error(None)` — *Verifies programmatic cancel raises AntigravityCancelledError.*
        - `def test_concurrent_receive_steps_raises_runtime_error(None)` — *Verifies that concurrent receive_steps() calls raise RuntimeError.*
        - `def test_connection_normalizes_file_uri_arguments(None)` — *Verifies that file:// URIs in tool confirmations are normalized before hooks.*
        - `def test_deduplication_of_wait_requests(None)` — *Verifies that multiple updates for the same wait state don't duplicate.*
        - `def test_handle_tool_call_queues_step(None)` — *Tests ensuring _handle_tool_call manually queues the ToolCall step in _step_queue.*
        - `def test_initial_handshake_synchronization(None)` — *Verifies that L2 connections receive restored historical steps synchronously during initialization and start fully idle.*
        - `def test_local_connection_step_from_dict(None)` — *Tests that LocalConnectionStep maps fields correctly.*
        - `def test_local_connection_step_from_dict_content_delta(None)` — *Tests that content_delta is correctly parsed from text_delta.*
        - `def test_local_connection_step_from_dict_deltas_default_empty(None)` — *Tests that delta fields default to empty when not present.*
        - `def test_local_connection_step_from_dict_thinking(None)` — *Tests that thinking field is correctly populated from step dict.*
        - `def test_local_connection_step_from_dict_thinking_delta(None)` — *Tests that thinking_delta is correctly parsed.*
        - `def test_local_connection_step_from_dict_thinking_empty_by_default(None)` — *Tests that thinking defaults to empty string when not present.*
        - `def test_mcp_tool_confirmation_request_allowed(None)`
        - `def test_mcp_tool_confirmation_request_denied(None)`
        - `def test_question_hook_integration(None)`
        - `def test_question_hook_integration_empty_questions(None)`
        - `def test_question_hook_integration_unhandled_question(None)`
        - `def test_receive_steps_basic(None)`
        - `def test_receive_steps_system_error(None)`
        - `def test_receive_steps_system_error_401(None)`
        - `def test_receive_steps_system_error_429(None)`
        - `def test_receive_steps_thinking_and_text_independent(None)` — *Tests that thinking and text are independent, non-exclusive fields.*
        - `def test_receive_steps_thinking_populated(None)` — *Tests that thinking field flows from proto through to SDK Step.*
        - `def test_receive_steps_trajectory_error(None)`
        - `def test_send_none_dispatches_turn_hook_with_empty_string(None)`
        - `def test_state_transition_clears_handled_requests(None)` — *Verifies WAITING -> ACTIVE -> WAITING transitions re-trigger handlers.*
        - `def test_thinking_only_step_is_target_user_not_complete(None)` — *Tests that thinking-only steps are TARGET_USER but not is_complete_response.*
        - `def test_tool_confirmation_request_has_id(None)`
        - `def test_tool_confirmation_request_integration(None)`
        - `def test_tool_confirmation_uses_enum_value_for_find_file(None)` — *Verifies that a find_file step update is correctly recognized.*
        - `def test_tool_confirmation_uses_enum_value_for_view_file(None)` — *Verifies that hooks receive the BuiltinTools enum value as the tool name.*
        - `def test_tool_hook_deny(None)`
        - `def test_turn_hook_deny(None)`
        - `def test_wait_for_idle_does_not_deadlock(None)` — *Verifies that wait_for_idle completes when the connection goes idle.*
        - `def test_yielding_wait_state_to_queue(None)` — *Verifies that wait states are correctly yielded to the step queue for the UI to render.*
*   **`class LocalConnectionToolCallHooksTest(methodName='runTest')`**
    *   *描述: Tests for post-tool-call and on-tool-error hooks.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_on_tool_error_hook_receives_original_exception_type(None)` — *Verifies OnToolErrorHook receives the original exception, not wrapped.*
        - `def test_on_tool_error_hook_with_recovery(None)` — *Verifies OnToolErrorHook can provide recovery values on tool failure.*
        - `def test_post_tool_call_hook_dispatched(None)` — *Verifies PostToolCallHook fires after successful tool execution.*
*   **`class LocalConnectionToolCallNoRunnerTest(methodName='runTest')`**
    *   *描述: Tests for tool call handling when no ToolRunner is configured.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_tool_call_without_runner_yields_step(None)` — *Verifies that a tool call with no ToolRunner queues a step for the user.*
*   **`class LocalConnectionUnexpectedCloseTest(methodName='runTest')`**
    *   *描述: Tests for error surfacing when the harness crashes mid-session.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_expected_ws_close_does_not_surface_error(None)` — *Verifies no error is queued when disconnect() initiated the close.*
        - `def test_unexpected_ws_close_surfaces_stderr(None)` — *Verifies harness stderr is surfaced when the WS closes unexpectedly.*

##### 📦 模組: `google.antigravity.connections.local.test_utils`
  *   *實體檔案: [test_utils.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/test_utils.py)*

### 類別 (Classes)
*   **`class TestLocalHarness(test_case: unittest.case.TestCase, process: unittest.mock.MagicMock, ws: google.antigravity.connections.local.test_utils.TestWebSocket | None = None, tool_runner: google.antigravity.tools.tool_runner.ToolRunner | None = None, hook_runner: google.antigravity.hooks.hook_runner.HookRunner | None = None, initial_history: list[google.antigravity.types.Step] | None = None)`**
    *   *描述: Helper to test LocalConnection by simulating the Go harness side of the WebSocket.*
    *   **方法列表 (Methods):**
        - `def close_from_harness_side(None)` — *Simulates the Go harness closing the WebSocket connection.*
        - `def disconnect_sdk(None)` — *Simulates the SDK initiating a disconnect.*
        - `def send_event(event: localharness_pb2.OutputEvent)` — *Simulates the harness transmitting an OutputEvent to the SDK.*
        - `def send_tool_call(id: str, name: str, arguments_json: str)` — *Simulates the harness transmitting a ToolCall event to the SDK.*
        - `def send_tool_confirmation_request(trajectory_id: str, step_index: int, **kwargs)` — *Simulates the harness transmitting a ToolConfirmationRequest event.*
        - `def wait_for_event(event: asyncio.locks.Event, timeout=10.0)` — *Awaits a test event to be fired with a given timeout.*
        - `def wait_for_response(timeout=10.0)` — *Awaits the next response from the SDK and returns the parsed JSON.*
*   **`class TestWebSocket(None)`**
    *   *描述: Mock WebSocket allowing async injection and inspection of messages.*
    *   **方法列表 (Methods):**
        - `def close(None)`
        - `def put_event(event)`
        - `def send(message)`

##### 📦 模組: `google.antigravity.connections.local.test_utils_test`
  *   *實體檔案: [test_utils_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/test_utils_test.py)*

### 類別 (Classes)
*   **`class TestLocalHarnessTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_harness_creates_default_ws(None)`
        - `def test_send_event_puts_to_socket(None)`
        - `def test_send_tool_call(None)`
        - `def test_send_tool_confirmation_request(None)`
        - `def test_wait_for_response_succeeds(None)`
        - `def test_wait_for_response_times_out(None)`
*   **`class TestWebSocketTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_close_ends_iteration(None)`
        - `def test_put_event_enqueues_json(None)`
        - `def test_send_adds_to_sent_messages(None)`
        - `def test_send_puts_to_sent_queue(None)`

##### 📦 模組: `google.antigravity.connections.local.types`
  *   *實體檔案: [types.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/connections/local/types.py)*

### 類別 (Classes)
*   **`class EditFileResult(**data: 'Any')`**
    *   *描述: Structured result from an edit_file tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class FindFileResult(**data: 'Any')`**
    *   *描述: Structured result from a find_file tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class GenerateImageResult(**data: 'Any')`**
    *   *描述: Structured result from a generate_image tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ListDirectoryEntry(**data: 'Any')`**
    *   *描述: Single entry in a directory listing.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ListDirectoryResult(**data: 'Any')`**
    *   *描述: Structured result from a list_directory tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class RunCommandResult(**data: 'Any')`**
    *   *描述: Structured result from a run_command tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SearchDirectoryResult(**data: 'Any')`**
    *   *描述: Structured result from a search_directory tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SearchWebResult(**data: 'Any')`**
    *   *描述: Structured result from a search_web tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class TextResult(**data: 'Any')`**
    *   *描述: Generic fallback for tools without structured output (e.g. view_file).*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`

### 📦 模組: `google.antigravity.hooks`
  *   *實體檔案: [__init__.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/hooks/__init__.py)*

### 類別 (Classes)
*   **`class DecideHook(*args, **kwargs)`**
    *   *描述: Read-only, blocking hook for policy decisions.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the decision hook.*
*   **`class HookContext(parent: "'HookContext | None'" = None)`**
    *   *描述: Base context for hooks to share state.*
    *   **方法列表 (Methods):**
        - `def get_state(key: 'str', default: 'Any' = None)` — *Gets a value from the context or its parents.*
        - `def set_state(key: 'str', value: 'Any')` — *Sets a value in the local context.*
*   **`class InspectHook(*args, **kwargs)`**
    *   *描述: Read-only, non-blocking hook for observability.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnCompactionHook(*args, **kwargs)`**
    *   *描述: Invoked when a context compaction event occurs.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnInteractionHook(*args, **kwargs)`**
    *   *描述: Hook invoked when the agent needs user interaction.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the transformation hook.*
*   **`class OnSessionEndHook(*args, **kwargs)`**
    *   *描述: Invoked when the session ends.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnSessionStartHook(*args, **kwargs)`**
    *   *描述: Invoked when the session starts.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnToolErrorHook(*args, **kwargs)`**
    *   *描述: Invoked when a tool fails, allowing for recovery or modification.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the transformation hook.*
*   **`class PostToolCallHook(*args, **kwargs)`**
    *   *描述: Invoked after a tool call completes.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class PostTurnHook(*args, **kwargs)`**
    *   *描述: Invoked after a turn ends.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class PreToolCallDecideHook(*args, **kwargs)`**
    *   *描述: Invoked before a tool call to decide if it should proceed.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the decision hook.*
*   **`class PreTurnHook(*args, **kwargs)`**
    *   *描述: Invoked before a turn starts.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the decision hook.*
*   **`class TransformHook(*args, **kwargs)`**
    *   *描述: Modifying, blocking hook for data transformation.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the transformation hook.*

#### 📦 模組: `google.antigravity.hooks.hook_runner`
  *   *實體檔案: [hook_runner.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/hooks/hook_runner.py)*

### 類別 (Classes)
*   **`class HookRunner(on_session_start_hooks: list[google.antigravity.hooks.hooks.OnSessionStartHook] | None = None, on_session_end_hooks: list[google.antigravity.hooks.hooks.OnSessionEndHook] | None = None, pre_turn_hooks: list[google.antigravity.hooks.hooks.PreTurnHook] | None = None, post_turn_hooks: list[google.antigravity.hooks.hooks.PostTurnHook] | None = None, pre_tool_call_decide_hooks: list[google.antigravity.hooks.hooks.PreToolCallDecideHook] | None = None, post_tool_call_hooks: list[google.antigravity.hooks.hooks.PostToolCallHook] | None = None, on_tool_error_hooks: list[google.antigravity.hooks.hooks.OnToolErrorHook] | None = None, on_interaction_hooks: list[google.antigravity.hooks.hooks.OnInteractionHook] | None = None, on_compaction_hooks: list[google.antigravity.hooks.hooks.OnCompactionHook] | None = None, _pre_step_hooks: list[google.antigravity.hooks.hooks._PreStepHook] | None = None, _post_step_hooks: list[google.antigravity.hooks.hooks._PostStepHook] | None = None)`**
    *   *描述: Manages collections of specific hook types and dispatches events.*
    *   **方法列表 (Methods):**
        - `def dispatch_compaction(turn_context: google.antigravity.hooks.hooks.TurnContext, data: Any)` — *Dispatches compaction events.*
        - `def dispatch_interaction(turn_context: google.antigravity.hooks.hooks.TurnContext, interaction_spec: Any)` — *Dispatches interaction events.*
        - `def dispatch_on_tool_error(op_context: google.antigravity.hooks.hooks.OperationContext, error: Exception)` — *Dispatches tool error events.*
        - `def dispatch_post_step(turn_context: google.antigravity.hooks.hooks.TurnContext, step: google.antigravity.types.Step)` — *Dispatches internal post-step observability events.*
        - `def dispatch_post_tool_call(op_context: google.antigravity.hooks.hooks.OperationContext, result: Any)` — *Dispatches post-tool call events.*
        - `def dispatch_post_turn(turn_context: google.antigravity.hooks.hooks.TurnContext, response: str)` — *Dispatches post-turn events.*
        - `def dispatch_pre_step(turn_context: google.antigravity.hooks.hooks.TurnContext, step: google.antigravity.types.Step)` — *Dispatches internal pre-step observability events.*
        - `def dispatch_pre_tool_call(turn_context: google.antigravity.hooks.hooks.TurnContext, tool_call: google.antigravity.types.ToolCall)` — *Dispatches pre-tool call events.*
        - `def dispatch_pre_turn(prompt: str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand | collections.abc.Sequence[str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand] | None)` — *Dispatches pre-turn events.*
        - `def dispatch_session_end(None)` — *Dispatches session end events to all registered hooks.*
        - `def dispatch_session_start(None)` — *Dispatches session start events to all registered hooks.*
        - `def register_hook(hook: Any)` — *Registers a hook by inferring its type.*

#### 📦 模組: `google.antigravity.hooks.hook_runner_test`
  *   *實體檔案: [hook_runner_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/hooks/hook_runner_test.py)*

### 類別 (Classes)
*   **`class DecoratorTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_on_interaction_decorator(None)`
        - `def test_on_tool_error_decorator(None)`
        - `def test_post_turn_decorator(None)`
        - `def test_pre_tool_call_decide_decorator(None)`
        - `def test_pre_turn_decorator(None)`
*   **`class HookRunnerTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_base_class_calls(None)` — *Verifies default pass implementations in base hook classes.*
        - `def test_context_scoping(None)`
        - `def test_dispatch_compaction(None)`
        - `def test_dispatch_interaction(None)`
        - `def test_dispatch_on_tool_error_exception(None)`
        - `def test_dispatch_on_tool_error_fall_through(None)`
        - `def test_dispatch_on_tool_error_recovery(None)`
        - `def test_dispatch_post_tool_call(None)`
        - `def test_dispatch_post_turn(None)`
        - `def test_dispatch_pre_model_call_exception(None)` — *Verifies that unknown hook types raise ValueError.*
        - `def test_dispatch_pre_tool_call_decide(None)`
        - `def test_dispatch_pre_tool_call_deny(None)`
        - `def test_dispatch_pre_turn_allow(None)`
        - `def test_dispatch_pre_turn_deny(None)`
        - `def test_dispatch_pre_turn_multimodal_list(None)`
        - `def test_dispatch_pre_turn_none_normalizes_to_empty_string(None)`
        - `def test_dispatch_session_end(None)`
        - `def test_dispatch_session_start(None)`
        - `def test_has_hooks_includes_compaction(None)`
        - `def test_register_hook(None)`

#### 📦 模組: `google.antigravity.hooks.hooks`
  *   *實體檔案: [hooks.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/hooks/hooks.py)*

### 類別 (Classes)
*   **`class DecideHook(*args, **kwargs)`**
    *   *描述: Read-only, blocking hook for policy decisions.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the decision hook.*
*   **`class HookContext(parent: "'HookContext | None'" = None)`**
    *   *描述: Base context for hooks to share state.*
    *   **方法列表 (Methods):**
        - `def get_state(key: 'str', default: 'Any' = None)` — *Gets a value from the context or its parents.*
        - `def set_state(key: 'str', value: 'Any')` — *Sets a value in the local context.*
*   **`class InspectHook(*args, **kwargs)`**
    *   *描述: Read-only, non-blocking hook for observability.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnCompactionHook(*args, **kwargs)`**
    *   *描述: Invoked when a context compaction event occurs.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnInteractionHook(*args, **kwargs)`**
    *   *描述: Hook invoked when the agent needs user interaction.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the transformation hook.*
*   **`class OnSessionEndHook(*args, **kwargs)`**
    *   *描述: Invoked when the session ends.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnSessionStartHook(*args, **kwargs)`**
    *   *描述: Invoked when the session starts.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class OnToolErrorHook(*args, **kwargs)`**
    *   *描述: Invoked when a tool fails, allowing for recovery or modification.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the transformation hook.*
*   **`class OperationContext(turn_context: 'TurnContext')`**
    *   *描述: Context scoped to a specific operation (e.g. tool call).*
    *   **方法列表 (Methods):**
        - `def get_state(key: 'str', default: 'Any' = None)` — *Gets a value from the context or its parents.*
        - `def set_state(key: 'str', value: 'Any')` — *Sets a value in the local context.*
*   **`class PostToolCallHook(*args, **kwargs)`**
    *   *描述: Invoked after a tool call completes.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class PostTurnHook(*args, **kwargs)`**
    *   *描述: Invoked after a turn ends.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class PreToolCallDecideHook(*args, **kwargs)`**
    *   *描述: Invoked before a tool call to decide if it should proceed.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the decision hook.*
*   **`class PreTurnHook(*args, **kwargs)`**
    *   *描述: Invoked before a turn starts.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the decision hook.*
*   **`class SessionContext(None)`**
    *   *描述: Context scoped to an entire session.*
    *   **方法列表 (Methods):**
        - `def get_state(key: 'str', default: 'Any' = None)` — *Gets a value from the context or its parents.*
        - `def set_state(key: 'str', value: 'Any')` — *Sets a value in the local context.*
*   **`class TransformHook(*args, **kwargs)`**
    *   *描述: Modifying, blocking hook for data transformation.*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the transformation hook.*
*   **`class TurnContext(session_context: 'SessionContext')`**
    *   *描述: Context scoped to a single turn.*
    *   **方法列表 (Methods):**
        - `def get_state(key: 'str', default: 'Any' = None)` — *Gets a value from the context or its parents.*
        - `def set_state(key: 'str', value: 'Any')` — *Sets a value in the local context.*
*   **`class _PostStepHook(*args, **kwargs)`**
    *   *描述: Invoked when a step completes (internal).*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*
*   **`class _PreStepHook(*args, **kwargs)`**
    *   *描述: Invoked when a step is first seen in the stream (internal).*
    *   **方法列表 (Methods):**
        - `def run(context: 'HookContext', data: 'T')` — *Runs the inspection hook.*

#### 📦 模組: `google.antigravity.hooks.hooks_test`
  *   *實體檔案: [hooks_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/hooks/hooks_test.py)*

### 類別 (Classes)
*   **`class BaseHookTest(methodName='runTest')`**
    *   *描述: Tests default behavior of specific Hook classes and result types.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_decide_hook(None)` — *Verifies DecideHook can be executed and returns HookResult.*
        - `def test_hook_result_defaults(None)` — *Verifies the default attributes of HookResult.*
        - `def test_inspect_hook(None)` — *Verifies InspectHook can be executed.*
        - `def test_on_compaction_hook(None)` — *Verifies OnCompactionHook can be instantiated and executed.*
        - `def test_pre_turn_hook(None)` — *Verifies PreTurnHook accepts types.Content and returns HookResult.*
        - `def test_transform_hook(None)` — *Verifies TransformHook can be executed and modifies data.*

#### 📦 模組: `google.antigravity.hooks.policy`
  *   *實體檔案: [policy.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/hooks/policy.py)*

### 類別 (Classes)
*   **`class Decision(*args, **kwds)`**
    *   *描述: Outcome a policy can produce.*
*   **`class Policy(tool: 'str', decision: 'Decision', when: 'Predicate | None' = None, ask_user: 'AskUserHandler | None' = None, name: 'str' = '')`**
    *   *描述: A single tool call policy rule.*
*   **`class _PolicyDecideHook(buckets: 'Sequence[Sequence[Policy]]', server_names: 'Sequence[str] | None' = None)`**
    *   *描述: PreToolCallDecideHook that enforces a set of policies.*
    *   **方法列表 (Methods):**
        - `def run(context: 'hooks.HookContext', data: 'types.ToolCall')` — *Evaluates policies against the tool call.*

#### 📦 模組: `google.antigravity.hooks.policy_test`
  *   *實體檔案: [policy_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/hooks/policy_test.py)*

### 類別 (Classes)
*   **`class AskUserTest(methodName='runTest')`**
    *   *描述: Verifies ASK_USER handler invocation.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_handler_approve(None)` — *Handler returning True → tool is allowed.*
        - `def test_handler_async(None)` — *Async handler is awaited correctly.*
        - `def test_handler_deny(None)` — *Handler returning False → tool is denied.*
        - `def test_handler_exception_denies(None)` — *Handler exception is caught and denies the tool call.*
        - `def test_handler_receives_tool_call(None)` — *Handler receives the full ToolCall object, not just args.*
*   **`class BuilderTest(methodName='runTest')`**
    *   *描述: Verifies that builder functions construct Policy objects correctly.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_allow_all_creates_wildcard_approve(None)` — *allow_all() must produce a wildcard APPROVE policy.*
        - `def test_allow_creates_approve_policy(None)` — *allow() must produce a Policy with decision=APPROVE.*
        - `def test_ask_user_creates_ask_user_policy(None)` — *ask_user() must produce a Policy with decision=ASK_USER and handler.*
        - `def test_deny_all_creates_wildcard_deny(None)` — *deny_all() must produce a wildcard DENY policy.*
        - `def test_deny_creates_deny_policy(None)` — *deny() must produce a Policy with decision=DENY.*
        - `def test_deny_with_predicate(None)` — *deny() with a when clause stores the predicate.*
*   **`class ConfirmCommandsTest(methodName='runTest')`**
    *   *描述: Verifies the confirm_run_command() preset — the default for LocalAgentConfig.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_allows_other_tools_by_default(None)` — *Without a handler, all non-run_command tools are allowed.*
        - `def test_denies_run_command_by_default(None)` — *Without a handler, run_command is denied with a clear message.*
        - `def test_returns_list_of_policies(None)` — *confirm_run_command() always returns a list of Policy objects.*
        - `def test_with_handler_allows_other_tools(None)` — *With a handler, non-run_command tools are still auto-allowed.*
        - `def test_with_handler_asks_user_for_run_command(None)` — *With a handler, run_command triggers ASK_USER instead of DENY.*
        - `def test_with_handler_deny_propagates(None)` — *Handler returning False denies the tool call.*
*   **`class ConvenienceBuilderTest(methodName='runTest')`**
    *   *描述: Verifies allow_all() and deny_all() evaluate correctly through enforce.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_allow_all_approves_any_tool(None)` — *allow_all() approves arbitrary tool calls.*
        - `def test_deny_all_denies_any_tool(None)` — *deny_all() denies arbitrary tool calls.*
        - `def test_deny_all_with_specific_allow_override(None)` — *deny_all() + allow(tool) creates deny-by-default with exceptions.*
*   **`class DefaultBehaviorTest(methodName='runTest')`**
    *   *描述: Verifies behavior when no policies match.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_empty_policies_allows_all(None)` — *An empty policy list allows everything.*
        - `def test_no_matching_policy_allows(None)` — *When no policy matches, the tool call is allowed (open system).*
*   **`class DenyReasonTest(methodName='runTest')`**
    *   *描述: Verifies that deny reasons include useful context.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_named_policy_in_deny_reason(None)` — *Policy name appears in the deny reason message.*
        - `def test_unnamed_policy_uses_tool_name(None)` — *When a policy has no name, the tool name is used in the reason.*
*   **`class IntegrationWithHookRunnerTest(methodName='runTest')`**
    *   *描述: Verifies the policy hook integrates with HookRunner dispatch.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_policy_hook_in_hook_runner(None)` — *Policy hook works when dispatched through HookRunner.*
*   **`class McpPolicyTest(methodName='runTest')`**
    *   *描述: Unit tests for overloaded MCP policy methods and structured target alignment.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_9_level_priority_specific_allow_beats_prefix_deny(None)` — *Specific Allow (level 2) must beat Prefix Deny (level 3).*
        - `def test_allow_mcp_builder_specific_tools(None)` — *allow(mcp_config, tools) must produce policies in 'server/tool' format.*
        - `def test_allow_mcp_builder_wildcard(None)` — *allow(mcp_config) must produce a single wildcard policy in structured target format.*
        - `def test_ask_user_mcp_builder_specific_tools(None)` — *ask_user(mcp_config, tools) must produce policies in 'server/tool' format with handler.*
        - `def test_builder_custom_name_unique(None)` — *Builders must append tool suffix to custom name for unique logging.*
        - `def test_builder_rejects_string_with_mcp_tools(None)` — *Builders must raise ValueError if mcp_tools is provided for a string tool name.*
        - `def test_deny_mcp_builder_specific_tools(None)` — *deny(mcp_config, tools) must produce policies in 'server/tool' format.*
        - `def test_enforce_fails_closed_on_missing_servers(None)` — *enforce() must raise ValueError if MCP policies exist but mcp_servers is missing.*
        - `def test_enforce_flattens_nested_policies(None)` — *enforce() must successfully flatten mixed nested lists of policies.*
        - `def test_enforce_rejects_invalid_policy_type(None)` — *enforce() must raise ValueError if a direct invalid type is passed.*
        - `def test_enforce_rejects_non_policy_in_sequence(None)` — *enforce() must raise ValueError if a non-Policy is found in a nested sequence.*
        - `def test_matches_target_unknown_server_prefix(None)` — *Prefixed calls with unknown server name must be treated as standard tools.*
        - `def test_mcp_tools_string_type_guard(None)` — *Builders must raise ValueError if mcp_tools is passed as a raw string.*
        - `def test_secure_longest_match_matching(None)` — *math prefix must not eagerly match math_advanced tools.*
*   **`class PolicyPathScopingDirectTest(*args, **kwargs)`**
    *   *描述: Direct unit tests for path normalization and workspace scoping.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_is_case_insensitive_prober(None)` — *_is_case_insensitive must dynamically check OS filesystem case sensitivity.*
        - `def test_is_path_in_workspace_case_folding(None)` — *is_path_in_workspace must fold casing symmetrically on case-insensitive drives.*
        - `def test_is_path_in_workspace_structural_containment(None)` — *is_path_in_workspace must securely check path containment component-wise.*
        - `def test_secure_normalize_path_resolves_existing_symlinks(None)` — *_secure_normalize_path must follow and resolve existing symlinks.*
*   **`class PredicateTest(methodName='runTest')`**
    *   *描述: Verifies sync, async, and failing predicates.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_allow_predicate_exception_denies(None)` — *Exception in allow policy predicate must deny (fail-closed).*
        - `def test_async_predicate_false(None)` — *Async predicate returning False skips the policy.*
        - `def test_async_predicate_true(None)` — *Async predicate returning True causes the policy to match.*
        - `def test_parameterless_predicate(None)` — *Predicate with no arguments should be called without arguments.*
        - `def test_parameterless_predicate_allow(None)` — *Parameterless predicate in ALLOW policy works and allows/denies correctly.*
        - `def test_predicate_exception_matches_fail_closed(None)` — *Exception in predicate → policy matches (fail-closed).*
        - `def test_sync_predicate_false(None)` — *Sync predicate returning False skips the policy.*
        - `def test_sync_predicate_true(None)` — *Sync predicate returning True causes the policy to match.*
        - `def test_typed_predicate(None)` — *Predicate expecting a Pydantic model receives the parsed object.*
*   **`class PriorityEvaluationTest(methodName='runTest')`**
    *   *描述: Verifies the 6-level priority evaluation model.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_specific_allow_overrides_wildcard_deny(None)` — *Level 3 (specific allow) beats Level 4 (wildcard deny).*
        - `def test_specific_ask_overrides_wildcard_deny(None)` — *Level 2 (specific ask) beats Level 4 (wildcard deny).*
        - `def test_specific_deny_overrides_specific_allow(None)` — *Level 1 (specific deny) beats Level 3 (specific allow).*
        - `def test_specific_deny_overrides_wildcard_allow(None)` — *Level 1 (specific deny) beats Level 6 (wildcard allow).*
        - `def test_wildcard_allow(None)` — *Level 6 (wildcard allow) allows all tools.*
        - `def test_wildcard_ask_user(None)` — *Level 5 (wildcard ask) applies to all tools.*
        - `def test_wildcard_deny_blocks_unmatched_tools(None)` — *Level 4 (wildcard deny) blocks tools with no specific policy.*
*   **`class RunCommandArgs(**data: 'Any')`**
    *   *描述: Arguments for run_command tool.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SafeDefaultsTest(methodName='runTest')`**
    *   *描述: Verifies safe_defaults() preset.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_safe_defaults_allows_read_only_tools(None)` — *safe_defaults() must allow read-only tools.*
        - `def test_safe_defaults_asks_for_other_tools(None)` — *safe_defaults() must ask for non-read-only tools.*
*   **`class ShortCircuitTest(methodName='runTest')`**
    *   *描述: Verifies first-match-wins within a priority group.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_first_match_wins_within_allow_group(None)` — *When two specific allow policies match, only the first is evaluated.*
        - `def test_first_match_wins_within_deny_group(None)` — *When two specific deny policies match, only the first is evaluated.*
        - `def test_skips_non_matching_predicate(None)` — *A policy whose predicate returns False is skipped; next one wins.*
*   **`class ValidationTest(methodName='runTest')`**
    *   *描述: Verifies startup validation in enforce().*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_enforce_rejects_ask_user_without_handler(None)` — *enforce() must raise ValueError when ASK_USER has no handler.*
        - `def test_enforce_rejects_ask_user_without_handler_unnamed(None)` — *enforce() error message includes tool name when policy has no name.*
*   **`class WorkspaceOnlyTest(methodName='runTest')`**
    *   *描述: Verifies workspace_only() — restricts file tools to workspace dirs.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_allows_files_inside_workspace(None)` — *File tool with path inside workspace is allowed.*
        - `def test_allows_non_file_tools(None)` — *Non-file tools are unaffected — no matching policy, default allows.*
        - `def test_allows_when_no_path_arg(None)` — *File tool with no path argument is allowed (don't break edge cases).*
        - `def test_denies_create_outside_workspace(None)` — *create_file outside workspace is denied.*
        - `def test_denies_edit_outside_workspace(None)` — *edit_file outside workspace is denied.*
        - `def test_denies_files_outside_workspace(None)` — *File tool with path outside workspace is denied.*
        - `def test_exact_workspace_path_allowed(None)` — *A path that is exactly the workspace directory itself is allowed.*
        - `def test_multiple_workspaces(None)` — *Paths in any configured workspace are allowed.*
        - `def test_prevents_path_prefix_attack(None)` — *Path /workspace-evil/file.txt must NOT match workspace /workspace.*

### 📦 模組: `google.antigravity.models`
  *   *實體檔案: [models.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/models.py)*

### 類別 (Classes)
*   **`class GeminiAPIEndpoint(**data: 'Any')`**
    *   *描述: Endpoint for the Gemini Developer API.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
        - `def validate_endpoint(None)`
*   **`class GeminiModelOptions(**data: 'Any')`**
    *   *描述: Gemini-specific model options.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ModelEndpoint(**data: 'Any')`**
    *   *描述: Base class for model endpoint authentication & routing.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
        - `def validate_endpoint(None)` — *Validates the configuration of the endpoint.*
*   **`class ModelTarget(**data: 'Any')`**
    *   *描述: Configuration for a single model.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ModelType(*args, **kwds)`**
    *   *描述: Discriminator for model purpose.*
*   **`class ThinkingLevel(*args, **kwds)`**
    *   *描述: Thinking level for Gemini models that support extended thinking.*
*   **`class VertexEndpoint(**data: 'Any')`**
    *   *描述: Endpoint for the Vertex AI backend.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
        - `def validate_endpoint(None)`

### 📦 模組: `google.antigravity.triggers`
  *   *實體檔案: [__init__.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/triggers/__init__.py)*

### 類別 (Classes)
*   **`class FileChange(**data: 'Any')`**
    *   *描述: A single filesystem change detected by a file-watching trigger.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class FileChangeKind(*args, **kwds)`**
    *   *描述: Kind of filesystem change detected by a file-watching trigger.*
*   **`class TriggerContext(connection: 'TriggerConnection')`**
    *   *描述: Handle provided to every trigger at startup.*
    *   **方法列表 (Methods):**
        - `def send(content: 'str')` — *Sends a message to the agent.*

#### 📦 模組: `google.antigravity.triggers.helpers_test`
  *   *實體檔案: [helpers_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/triggers/helpers_test.py)*

### 類別 (Classes)
*   **`class EveryTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_every_calls_callback_on_interval(None)`
        - `def test_every_rejects_non_positive_interval(None)`
        - `def test_every_sets_name(None)`
*   **`class OnFileChangeTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_on_file_change_import_error(None)` — *Verify helpful error when watchfiles is missing.*
        - `def test_on_file_change_sets_name(None)`
        - `def test_on_file_change_success(None)` — *Verify callback is called with mapped changes.*

#### 📦 模組: `google.antigravity.triggers.trigger_runner`
  *   *實體檔案: [trigger_runner.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/triggers/trigger_runner.py)*

### 類別 (Classes)
*   **`class TriggerRunner(triggers: Sequence[Callable[[google.antigravity.triggers.triggers.TriggerContext], Awaitable[NoneType]]], connection: google.antigravity.connections.connection.Connection)`**
    *   *描述: Manages registration, startup, and shutdown of triggers.*
    *   **方法列表 (Methods):**
        - `def start(None)` — *Start all triggers as concurrent asyncio tasks.*
        - `def stop(None)` — *Cancel all trigger tasks and wait for them to finish.*

#### 📦 模組: `google.antigravity.triggers.trigger_runner_test`
  *   *實體檔案: [trigger_runner_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/triggers/trigger_runner_test.py)*

### 類別 (Classes)
*   **`class TriggerRunnerTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_context_manager_starts_and_stops(None)`
        - `def test_empty_triggers_list(None)`
        - `def test_exception_in_trigger_does_not_crash_others(None)`
        - `def test_restart_after_stop(None)`
        - `def test_start_runs_triggers(None)`
        - `def test_start_twice_raises(None)`
        - `def test_stop_cancels_all_triggers(None)`
        - `def test_stop_when_not_started_is_noop(None)`
        - `def test_trigger_receives_context_with_connection(None)`

#### 📦 模組: `google.antigravity.triggers.triggers`
  *   *實體檔案: [triggers.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/triggers/triggers.py)*

### 類別 (Classes)
*   **`class FileChange(**data: 'Any')`**
    *   *描述: A single filesystem change detected by a file-watching trigger.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class FileChangeKind(*args, **kwds)`**
    *   *描述: Kind of filesystem change detected by a file-watching trigger.*
*   **`class TriggerConnection(*args, **kwargs)`**
    *   **方法列表 (Methods):**
        - `def send_trigger_notification(content: 'str')`
*   **`class TriggerContext(connection: 'TriggerConnection')`**
    *   *描述: Handle provided to every trigger at startup.*
    *   **方法列表 (Methods):**
        - `def send(content: 'str')` — *Sends a message to the agent.*

#### 📦 模組: `google.antigravity.triggers.triggers_test`
  *   *實體檔案: [triggers_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/triggers/triggers_test.py)*

### 類別 (Classes)
*   **`class FileChangeTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_file_change_is_immutable(None)`
*   **`class TriggerContextTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_send_calls_connection_send_trigger_notification(None)`
*   **`class TriggerDecoratorTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_not_async_raises_value_error(None)`
        - `def test_valid_trigger_accepted(None)`
        - `def test_wrong_signature_raises_value_error(None)`
*   **`class TriggerTypeTest(methodName='runTest')`**
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_trigger_is_callable_type(None)` — *Verify that an async def is a valid Trigger.*

### 📦 模組: `google.antigravity.types`
  *   *實體檔案: [types.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/types.py)*

### 類別 (Classes)
*   **`class AntigravityCancelledError(message: 'str' = 'The request was cancelled by the client.')`**
    *   *描述: Raised when an active turn is cancelled programmatically.*
*   **`class AntigravityConnectionError(*args, **kwargs)`**
    *   *描述: Base class for connection errors in the Google Antigravity SDK.*
*   **`class AntigravityExecutionError(*args, **kwargs)`**
    *   *描述: Raised when the agent execution encounters a terminal error.*
*   **`class AntigravityValidationError(message: 'str', errors: 'list[dict[str, Any]] | None' = None)`**
    *   *描述: Wraps Pydantic ValidationError at the SDK boundary.*
*   **`class AskQuestionEntry(**data: 'Any')`**
    *   *描述: A single question with predefined options.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class AskQuestionInteractionSpec(**data: 'Any')`**
    *   *描述: Interaction spec for ask_question dialog.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class AskQuestionOption(**data: 'Any')`**
    *   *描述: Option for an AskQuestion entry.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Audio(**data: 'Any')`**
    *   *描述: Audio content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class BaseMcpServerConfig(**data: 'Any')`**
    *   *描述: Base configuration for all Model Context Protocol (MCP) servers.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class BuiltinSlashCommandName(*args, **kwds)`**
    *   *描述: Supported system slash commands.*
*   **`class BuiltinTools(*args, **kwds)`**
    *   *描述: Identifiers for common connection-provided builtin tools.*
*   **`class CapabilitiesConfig(**data: 'Any')`**
    *   *描述: General agent capability configuration.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ChatResponse(chunk_stream: 'AsyncIterator[StreamChunk | ToolCall | ToolResult]', conversation: 'Any')`**
    *   *描述: The turn response from Agent.chat().*
    *   **方法列表 (Methods):**
        - `def cancel(None)` — *Cancels the active execution turn and halts generation.*
        - `def resolve(None)` — *Drains the underlying stream completely and returns all chunks as a flat list.*
        - `def structured_output(None)` — *Drains the stream and extracts the parsed structured output payload, if one exists.*
        - `def text(None)` — *Drains the stream and returns the fully aggregated conversational response text.*
*   **`class CustomSystemInstructions(**data: 'Any')`**
    *   *描述: Use this to completely replace the system instructions.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Document(**data: 'Any')`**
    *   *描述: Document content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class HookResult(**data: 'Any')`**
    *   *描述: Result of a decision hook execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Image(**data: 'Any')`**
    *   *描述: Image content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class McpStdioServer(**data: 'Any')`**
    *   *描述: Configuration for an MCP server connected via stdio.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class McpStreamableHttpServer(**data: 'Any')`**
    *   *描述: Configuration for an MCP server connected via Streamable HTTP.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class QuestionHookResult(**data: 'Any')`**
    *   *描述: Result of an interaction containing a list of responses.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class QuestionResponse(**data: 'Any')`**
    *   *描述: Individual response for an AskQuestion entry.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SlashCommand(**data: 'Any')`**
    *   *描述: Slash command context primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Step(**data: 'Any')`**
    *   *描述: Structure representing one action in the agent trajectory.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class StepSource(*args, **kwds)`**
    *   *描述: Source of a step.*
*   **`class StepStatus(*args, **kwds)`**
    *   *描述: Status of a step.*
*   **`class StepTarget(*args, **kwds)`**
    *   *描述: Target of a step interaction.*
*   **`class StepType(*args, **kwds)`**
    *   *描述: High-level type of a step.*
*   **`class StreamChunk(**data: 'Any')`**
    *   *描述: Base class for all real-time semantic chunks yielded during agent.chat() streaming.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SubagentCapabilities(**data: 'Any')`**
    *   *描述: Capabilities configuration for subagents.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SubagentConfig(**data: 'Any')`**
    *   *描述: Configuration for a static subagent.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class SystemInstructionSection(**data: 'Any')`**
    *   *描述: A named section to append to the system instructions.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class TemplatedSystemInstructions(**data: 'Any')`**
    *   *描述: Use this to override the agent's identity and append sections to the default system instructions.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Text(**data: 'Any')`**
    *   *描述: A delta chunk representing a piece of the model's text output.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Thought(**data: 'Any')`**
    *   *描述: A delta chunk representing a piece of the model's internal reasoning/thinking.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ToolCall(**data: 'Any')`**
    *   *描述: A tool call to inject into the conversation.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class ToolResult(**data: 'Any')`**
    *   *描述: Result of a single tool execution.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class TriggerDelivery(*args, **kwds)`**
    *   *描述: Controls how trigger messages are delivered to the agent.*
*   **`class UsageMetadata(**data: 'Any')`**
    *   *描述: Token usage metadata from the model API.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class Video(**data: 'Any')`**
    *   *描述: Video content attachment primitive.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class _BaseMedia(**data: 'Any')`**
    *   *描述: Base class for all rich multimedia content attachment primitives.*
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_file(path: 'str | pathlib.Path', description: 'str | None' = None)` — *Instantiates a media content primitive from a local file path.*
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`

### 📦 模組: `google.antigravity.types_test`
  *   *實體檔案: [types_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/types_test.py)*

### 類別 (Classes)
*   **`class AntigravityConnectionErrorTest(methodName='runTest')`**
    *   *描述: Validates the AntigravityConnectionError hierarchy.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_is_exception(None)` — *Verifies that AntigravityConnectionError is a proper Exception.*
        - `def test_message(None)` — *Verifies that the message is stored and retrievable.*
*   **`class AntigravityValidationErrorTest(methodName='runTest')`**
    *   *描述: Validates the AntigravityValidationError wrapper.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)` — *Verifies direct construction with a message.*
        - `def test_from_pydantic(None)` — *Verifies construction from a real Pydantic ValidationError.*
        - `def test_is_exception(None)` — *Verifies that AntigravityValidationError is a proper Exception.*
        - `def test_step_pydantic(None)` — *Tests that Step can be instantiated as a Pydantic model.*
        - `def test_step_with_tool_calls(None)` — *Tests that Step can hold multiple tool calls.*
        - `def test_tool_call_pydantic(None)` — *Tests that ToolCall can be instantiated as a Pydantic model.*
        - `def test_with_errors_list(None)` — *Verifies construction with an explicit errors list.*
*   **`class AskQuestionModelsTest(methodName='runTest')`**
    *   *描述: Tests for AskQuestion related models.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_ask_question_entry(None)`
        - `def test_ask_question_interaction_spec(None)`
        - `def test_ask_question_option(None)`
*   **`class AudioTest(methodName='runTest')`**
    *   *描述: Validates the Audio content attachment primitive and its validators.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)` — *Verifies that an Audio can be successfully constructed with valid arguments.*
        - `def test_unsupported_mime_type_raises(None)` — *Verifies that an unsupported Audio MIME type triggers ValidationError.*
*   **`class BuiltinToolsTest(*args, **kwargs)`**
    *   *描述: Tests for the BuiltinTools enum.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)` — *Returns the descriptive ID of the test.*
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_all_tools_returns_every_member(None)` — *Verifies that all_tools() returns every enum member.*
        - `def test_enum_values_ask_question(enum_member, expected_value)` — *test_enum_values_ask_question(<BuiltinTools.ASK_QUESTION: 'ask_question'>, 'ask_question')*
        - `def test_enum_values_create_file(enum_member, expected_value)` — *test_enum_values_create_file(<BuiltinTools.CREATE_FILE: 'create_file'>, 'create_file')*
        - `def test_enum_values_edit_file(enum_member, expected_value)` — *test_enum_values_edit_file(<BuiltinTools.EDIT_FILE: 'edit_file'>, 'edit_file')*
        - `def test_enum_values_generate_image(enum_member, expected_value)` — *test_enum_values_generate_image(<BuiltinTools.GENERATE_IMAGE: 'generate_image'>, 'generate_image')*
        - `def test_enum_values_list_dir(enum_member, expected_value)` — *test_enum_values_list_dir(<BuiltinTools.LIST_DIR: 'list_directory'>, 'list_directory')*
        - `def test_enum_values_run_command(enum_member, expected_value)` — *test_enum_values_run_command(<BuiltinTools.RUN_COMMAND: 'run_command'>, 'run_command')*
        - `def test_enum_values_search_dir(enum_member, expected_value)` — *test_enum_values_search_dir(<BuiltinTools.SEARCH_DIR: 'search_directory'>, 'search_directory')*
        - `def test_enum_values_search_web(enum_member, expected_value)` — *test_enum_values_search_web(<BuiltinTools.SEARCH_WEB: 'search_web'>, 'search_web')*
        - `def test_enum_values_start_subagent(enum_member, expected_value)` — *test_enum_values_start_subagent(<BuiltinTools.START_SUBAGENT: 'start_subagent'>, 'start_subagent')*
        - `def test_enum_values_view_file(enum_member, expected_value)` — *test_enum_values_view_file(<BuiltinTools.VIEW_FILE: 'view_file'>, 'view_file')*
        - `def test_nondestructive_covers_all_tools(None)` — *Verifies nondestructive + destructive tools = full enum.*
        - `def test_none_returns_empty_list(None)` — *Verifies that none() returns an empty list.*
        - `def test_read_only_covers_all_tools(None)` — *Verifies read_only + write tools = full enum.*
*   **`class CapabilitiesConfigTest(methodName='runTest')`**
    *   *描述: Tests for the CapabilitiesConfig Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_compaction_threshold_explicit(None)` — *Verifies that compaction_threshold accepts an explicit integer.*
        - `def test_default_construction(None)` — *Verifies defaults: subagents enabled, no tool lists, no threshold.*
        - `def test_disabled_tools(None)` — *Verifies that disabled_tools accepts a list of BuiltinTools.*
        - `def test_enabled_tools(None)` — *Verifies that enabled_tools accepts a list of BuiltinTools.*
        - `def test_mutually_exclusive_raises(None)` — *Verifies that setting both enabled_tools and disabled_tools raises.*
*   **`class ChatResponseStreamTest(methodName='runTest')`**
    *   *描述: Tests for ChatResponse async stream and caching properties.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_all_three_sequential(None)` — *Cache replay: thoughts → tool_calls → text from one response.*
        - `def test_cancel_completed_stream_is_noop(None)` — *Verifies that cancel() is a safe no-op on a completed stream.*
        - `def test_cancel_delegates_to_conversation(None)` — *Verifies that cancel() delegates to conversation.cancel() if not done.*
        - `def test_concurrent_cursors_via_gather(None)` — *Lock safety: two cursors via asyncio.gather don't crash.*
        - `def test_empty_stream_all_iterators(None)` — *All iterators return empty on an empty stream.*
        - `def test_empty_stream_text(None)` — *Verifies that an empty stream resolves text to an empty string.*
        - `def test_error_propagation_to_all_cursors(None)` — *Error storage: stream error re-raised to every cursor.*
        - `def test_explicit_lock_contention_double_check(None)` — *Explicitly tests the double-check condition under lock contention.*
        - `def test_interleaved_chunk_types(None)` — *Thought-Text-Thought-Text-ToolCall pattern streams correctly.*
        - `def test_lazy_caching_and_re_iteration(None)` — *Verifies that stream tokens are cached in memory and replayed for re-iteration.*
        - `def test_resolve_then_text_then_aiter(None)` — *resolve(), text(), and __aiter__ all work on the same response.*
        - `def test_sequential_text_then_thoughts(None)` — *Cache replay: text first, then thoughts sees all Thought chunks.*
        - `def test_sequential_thoughts_then_text(None)` — *Cache replay: thoughts first, then text sees all Text chunks.*
        - `def test_sequential_tool_calls_then_text(None)` — *Cache replay: tool_calls first, then text.*
        - `def test_stream_cancellation_sets_is_done(None)` — *Verifies that if stream raises CancelledError, _is_done becomes True.*
        - `def test_structured_output_lazy_accessor(None)` — *Verifies structured_output resolves the stream and fetches parsed payload from conversation.*
        - `def test_text_chunk_validation(None)` — *Verifies that the Text subclass validates Pydantic schemas correctly.*
        - `def test_text_concatenation(None)` — *Verifies that text() aggregates and concatenates all Text chunks.*
        - `def test_thought_chunk_validation(None)` — *Verifies that the Thought subclass validates Pydantic schemas correctly.*
        - `def test_thoughts_sugared_stream(None)` — *Verifies thoughts property yields only Thought delta strings.*
        - `def test_tool_calls_sugared_stream(None)` — *Verifies tool_calls property yields only ToolCall objects.*
        - `def test_two_chunks_cursors_independent(None)` — *Two raw .chunks cursors both see identical output.*
        - `def test_usage_metadata_lazy_accessor(None)` — *Verifies usage_metadata resolves the stream and fetches payload from conversation.*
*   **`class ContentFromFileResolverTest(*args, **kwargs)`**
    *   *描述: Validates the global from_file content resolver helper function.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)` — *Returns the descriptive ID of the test.*
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_directory_path_raises_error(None)` — *Verifies that passing a path targeting a directory triggers IsADirectoryError.*
        - `def test_inference_failure_raises_clear_value_error(None)` — *Verifies that an extensionless path failure raises a descriptive ValueError.*
        - `def test_non_existent_path_raises_error(None)` — *Verifies that passing a non-existent path triggers FileNotFoundError.*
        - `def test_os_error_wrapping(None)` — *Verifies that OS-level read errors are caught and wrapped appropriately.*
        - `def test_permission_error_wrapping(None)` — *Verifies that permission errors are caught and wrapped appropriately.*
        - `def test_resolves_from_file_audio(filename, expected_class, expected_mime)` — *test_resolves_from_file_audio('clip.mp3', <class 'google.antigravity.types.Audio'>, 'audio/mpeg')*
        - `def test_resolves_from_file_document(filename, expected_class, expected_mime)` — *test_resolves_from_file_document('report.pdf', <class 'google.antigravity.types.Document'>, 'application/pdf')*
        - `def test_resolves_from_file_image(filename, expected_class, expected_mime)` — *test_resolves_from_file_image('diagram.png', <class 'google.antigravity.types.Image'>, 'image/png')*
        - `def test_resolves_from_file_video(filename, expected_class, expected_mime)` — *test_resolves_from_file_video('movie.mp4', <class 'google.antigravity.types.Video'>, 'video/mp4')*
*   **`class HookResultTest(methodName='runTest')`**
    *   *描述: Validates the HookResult Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_defaults(None)` — *Verifies that HookResult defaults to allow=True.*
        - `def test_deny(None)` — *Verifies construction of a deny HookResult.*
        - `def test_mutable(None)` — *Verifies that HookResult is mutable.*
*   **`class ImageTest(methodName='runTest')`**
    *   *描述: Tests for the Image content attachment primitive and its validators.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)` — *Verifies that an Image can be successfully constructed with valid arguments.*
        - `def test_from_file_success(None)` — *Verifies that from_file loader loads bytes and guesses MIME correctly.*
        - `def test_unsupported_mime_type_raises(None)` — *Verifies that an unsupported Image MIME type triggers ValidationError.*
*   **`class McpServerConfigTest(*args, **kwargs)`**
    *   *描述: Validates the McpServerConfig Pydantic models and required fields.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertBetween(value, minv, maxv, msg=None)` — *Asserts that value is between minv and maxv (inclusive).*
        - `def assertCommandFails(command, regexes, env=None, close_fds=True, msg=None)` — *Asserts a shell command fails and the error matches a regex in a list.*
        - `def assertCommandSucceeds(command, regexes=(b'',), env=None, close_fds=True, msg=None)` — *Asserts that a shell command succeeds (i.e. exits with code 0).*
        - `def assertContainsExactSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as an exact subsequence.*
        - `def assertContainsInOrder(strings, target, msg=None)` — *Asserts that the strings provided are found in the target in order.*
        - `def assertContainsSubsequence(container, subsequence, msg=None)` — *Asserts that "container" contains "subsequence" as a subsequence.*
        - `def assertContainsSubset(expected_subset, actual_set, msg=None)` — *Checks whether actual iterable is a superset of expected iterable.*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDataclassEqual(first, second, msg=None)` — *Asserts two dataclasses are equal with more informative errors.*
        - `def assertDictAlmostEqual(a, b, places=None, msg=None, delta=None)` — *Raises AssertionError if a and b are not equal or almost equal dicts.*
        - `def assertDictContainsSubset(subset: Mapping[Any, Any], dictionary: Mapping[Any, Any], msg=None)` — *Raises AssertionError if "dictionary" is not a superset of "subset".*
        - `def assertDictEqual(a, b, msg=None)` — *Raises AssertionError if a and b are not equal dictionaries.*
        - `def assertEmpty(container, msg=None)` — *Asserts that an object has zero length.*
        - `def assertEndsWith(actual, expected_end, msg=None)` — *Asserts that actual.endswith(expected_end) is True.*
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertItemsEqual(expected_seq, actual_seq, msg=None)` — *Deprecated, please use assertCountEqual instead.*
        - `def assertJsonEqual(first, second, msg=None)` — *Asserts that the JSON objects defined in two strings are equal.*
        - `def assertLen(container, expected_len, msg=None)` — *Asserts that an object has the expected length.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMappingEqual(a, b, msg=None, mapping_type=<class 'collections.abc.Mapping'>, check_values_equality=<function TestCase.<lambda> at 0x1076674c0>)` — *Raises AssertionError if a and b differ in keys or values.*
        - `def assertMultiLineEqual(first, second, msg=None, **kwargs)` — *Asserts that two multi-line strings are equal.*
        - `def assertNoCommonElements(expected_seq, actual_seq, msg=None)` — *Checks whether actual iterable and expected iterable are disjoint.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEmpty(container, msg=None)` — *Asserts that an object has non-zero length.*
        - `def assertNotEndsWith(actual, unexpected_end, msg=None)` — *Asserts that actual.endswith(unexpected_end) is False.*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertNotStartsWith(actual, unexpected_start, msg=None)` — *Asserts that actual.startswith(unexpected_start) is False.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRaisesWithLiteralMatch(expected_exception, expected_exception_message, callable_obj=None, *args, **kwargs)` — *Asserts that the message in a raised exception equals the given string.*
        - `def assertRaisesWithPredicateMatch(expected_exception, predicate, callable_obj=None, *args, **kwargs)` — *Asserts that exception is thrown and predicate(exception) is true.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertRegexMatch(actual_str, regexes, message=None)` — *Asserts that at least one regex in regexes matches str.*
        - `def assertSameElements(expected_seq, actual_seq, msg=None)` — *Asserts that two sequences have the same elements (in any order).*
        - `def assertSameStructure(a, b, aname='a', bname='b', msg=None)` — *Asserts that two values contain the same structural content.*
        - `def assertSequenceAlmostEqual(expected_seq, actual_seq, places=None, msg=None, delta=None)` — *An approximate equality assertion for ordered sequences.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSequenceStartsWith(prefix, whole, msg=None)` — *An equality assertion for the beginning of ordered sequences.*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertStartsWith(actual, expected_start, msg=None)` — *Asserts that actual.startswith(expected_start) is True.*
        - `def assertTotallyOrdered(*groups, **kwargs)` — *Asserts that total ordering has been implemented correctly.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertUrlEqual(a, b, msg=None)` — *Asserts that urls are equal, ignoring ordering of query params.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def create_tempdir(name: Optional[str] = None, cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary directory specific to the test.*
        - `def create_tempfile(file_path: Optional[str] = None, content: Optional[~AnyStr] = None, mode: str = 'w', encoding: str = 'utf8', errors: str = 'strict', cleanup: Optional[absl.testing.absltest.TempFileCleanup] = None)` — *Create a temporary file specific to the test.*
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def enter_context(manager: ContextManager[~_T])`
        - `def fail(msg=None, user_msg=None)` — *Fail immediately with the given standard message and user message.*
        - `def id(None)` — *Returns the descriptive ID of the test.*
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)`
        - `def shortDescription(None)` — *Formats both the test method name and the first line of its docstring.*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_server_construction_success_http(server_cls, init_kwargs, expected_attrs)` — *test_server_construction_success_http(<class 'google.antigravity.types.McpStreamableHttpServer'>, {'name': 'http_server', 'url': 'http://localhost/http'}, {'name': 'http_server', 'url': 'http://localhost/http'})*
        - `def test_server_construction_success_stdio(server_cls, init_kwargs, expected_attrs)` — *test_server_construction_success_stdio(<class 'google.antigravity.types.McpStdioServer'>, {'name': 'stdio_server', 'command': 'node', 'args': ['index.js']}, {'name': 'stdio_server', 'command': 'node', 'args': ['index.js']})*
        - `def test_server_construction_success_stdio_with_env(server_cls, init_kwargs, expected_attrs)` — *test_server_construction_success_stdio_with_env(<class 'google.antigravity.types.McpStdioServer'>, {'name': 'stdio_server', 'command': 'node', 'args': ['index.js'], 'env': {'FOO': 'bar'}}, {'name': 'stdio_server', 'command': 'node', 'args': ['index.js'], 'env': {'FOO': 'bar'}})*
        - `def test_server_construction_with_filtering_stdio_disabled(server_cls, init_kwargs, expected_attr, expected_val)` — *test_server_construction_with_filtering_stdio_disabled(<class 'google.antigravity.types.McpStdioServer'>, {'name': 'stdio_server', 'command': 'node', 'disabled_tools': ['tool2']}, 'disabled_tools', ['tool2'])*
        - `def test_server_construction_with_filtering_stdio_enabled(server_cls, init_kwargs, expected_attr, expected_val)` — *test_server_construction_with_filtering_stdio_enabled(<class 'google.antigravity.types.McpStdioServer'>, {'name': 'stdio_server', 'command': 'node', 'enabled_tools': ['tool1']}, 'enabled_tools', ['tool1'])*
        - `def test_server_exclusive_filtering_raises_stdio_different_tools(server_cls, init_kwargs)` — *test_server_exclusive_filtering_raises_stdio_different_tools(<class 'google.antigravity.types.McpStdioServer'>, {'name': 'stdio_server', 'command': 'node', 'enabled_tools': ['tool1'], 'disabled_tools': ['tool2']})*
        - `def test_server_exclusive_filtering_raises_stdio_same_tool(server_cls, init_kwargs)` — *test_server_exclusive_filtering_raises_stdio_same_tool(<class 'google.antigravity.types.McpStdioServer'>, {'name': 'stdio_server', 'command': 'node', 'enabled_tools': ['tool1'], 'disabled_tools': ['tool1']})*
        - `def test_server_invalid_names_raise0(name)` — *test_server_invalid_names_raise('invalid name')*
        - `def test_server_invalid_names_raise1(name)` — *test_server_invalid_names_raise('invalid.name')*
        - `def test_server_invalid_names_raise2(name)` — *test_server_invalid_names_raise('invalid/name')*
        - `def test_server_invalid_names_raise3(name)` — *test_server_invalid_names_raise('invalid@name')*
        - `def test_server_invalid_names_raise4(name)` — *test_server_invalid_names_raise('invalidName!')*
        - `def test_server_missing_name_raises_http(server_cls, init_kwargs)` — *test_server_missing_name_raises_http(<class 'google.antigravity.types.McpStreamableHttpServer'>, {'url': 'http://localhost/http'})*
        - `def test_server_missing_name_raises_stdio(server_cls, init_kwargs)` — *test_server_missing_name_raises_stdio(<class 'google.antigravity.types.McpStdioServer'>, {'command': 'node'})*
        - `def test_server_valid_names0(name)` — *test_server_valid_names('validName')*
        - `def test_server_valid_names1(name)` — *test_server_valid_names('valid-name')*
        - `def test_server_valid_names2(name)` — *test_server_valid_names('valid_name')*
        - `def test_server_valid_names3(name)` — *test_server_valid_names('valid_name-123')*
        - `def test_union_deserialization(None)` — *Verifies that TypeAdapter parses McpServerConfig union variants with name correctly.*
*   **`class ModelTargetTest(methodName='runTest')`**
    *   *描述: Tests for the polymorphic ModelTarget hierarchy.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_text_construction(None)`
        - `def test_image_model_construction(None)`
        - `def test_vertex_endpoint_construction(None)`
*   **`class QuestionHookResultTest(methodName='runTest')`**
    *   *描述: Validates the QuestionHookResult Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)` — *Verifies construction with a list of responses.*
        - `def test_cancelled(None)` — *Verifies cancelled interaction.*
        - `def test_missing_responses_raises(None)` — *Verifies that omitting required 'responses' raises.*
*   **`class QuestionResponseTest(methodName='runTest')`**
    *   *描述: Validates the QuestionResponse Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_defaults(None)` — *Verifies QuestionResponse defaults.*
        - `def test_selected_options(None)` — *Verifies construction with selected option IDs.*
        - `def test_skipped(None)` — *Verifies construction of a skipped response.*
        - `def test_write_in(None)` — *Verifies construction with a write-in response.*
*   **`class StepTest(methodName='runTest')`**
    *   *描述: Validates the Step Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)` — *Verifies that a Step can be constructed with all fields.*
        - `def test_defaults(None)` — *Verifies that all Step fields have sensible defaults.*
        - `def test_extra_fields_allowed(None)` — *Verifies extra='allow' on Step as per Karmel's model.*
        - `def test_mutable(None)` — *Verifies that Step is mutable as per Karmel's model.*
        - `def test_nested_tool_call(None)` — *Verifies that a Step can contain a nested ToolCall.*
*   **`class SubagentCapabilitiesTest(methodName='runTest')`**
    *   *描述: Validates the SubagentCapabilities Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_defaults(None)`
        - `def test_mutually_exclusive_ok_disabled(None)`
        - `def test_mutually_exclusive_ok_enabled(None)`
        - `def test_mutually_exclusive_raises(None)`
*   **`class SubagentConfigTest(methodName='runTest')`**
    *   *描述: Validates the SubagentConfig Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)`
        - `def test_required_fields(None)`
*   **`class SystemInstructionsTest(methodName='runTest')`**
    *   *描述: Tests for the SystemInstructions Pydantic model union.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_custom_construction(None)` — *Verifies construction of CustomSystemInstructions.*
        - `def test_custom_text_is_required(None)` — *Verifies that CustomSystemInstructions raises when text is missing.*
        - `def test_templated_construction(None)` — *Verifies construction of TemplatedSystemInstructions.*
        - `def test_templated_empty_construction(None)` — *Verifies that TemplatedSystemInstructions can be constructed empty.*
        - `def test_union_parsing_custom(None)` — *Verifies that Pydantic parses CustomSystemInstructions from dict.*
        - `def test_union_parsing_empty_dict(None)` — *Verifies that Pydantic parses empty dict as TemplatedSystemInstructions.*
        - `def test_union_parsing_templated(None)` — *Verifies that Pydantic parses TemplatedSystemInstructions from dict.*
*   **`class ThinkingLevelTest(methodName='runTest')`**
    *   *描述: Tests for the ThinkingLevel enum.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_enum_values(None)` — *Verifies each enum member has the expected string value.*
        - `def test_string_comparison(None)` — *Verifies ThinkingLevel members compare equal to their string values.*
*   **`class ToolCallTest(methodName='runTest')`**
    *   *描述: Validates the ToolCall Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)` — *Verifies that a ToolCall can be constructed with name and args.*
        - `def test_canonical_path_default_none(None)` — *Verifies that canonical_path defaults to None.*
        - `def test_canonical_path_explicit(None)` — *Verifies that canonical_path can be explicitly set.*
        - `def test_default_args(None)` — *Verifies that args defaults to empty dict when omitted.*
        - `def test_extra_fields_ignored(None)` — *Verifies that unknown fields are silently dropped.*
        - `def test_id_defaults_to_none(None)` — *Verifies that id defaults to None when omitted.*
        - `def test_id_explicitly_set(None)` — *Verifies that id can be explicitly set.*
        - `def test_missing_name_raises(None)` — *Verifies that omitting required field 'name' raises.*
*   **`class ToolResultTest(methodName='runTest')`**
    *   *描述: Validates the ToolResult Pydantic model.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_error_result(None)` — *Verifies construction of an error ToolResult.*
        - `def test_extra_fields_ignored(None)` — *Verifies extra='ignore' on ToolResult.*
        - `def test_id_defaults_to_none(None)` — *Verifies that id defaults to None when omitted.*
        - `def test_id_explicitly_set(None)` — *Verifies that id can be explicitly set for call correlation.*
        - `def test_id_mutable(None)` — *Verifies that id can be set after construction.*
        - `def test_mutable(None)` — *Verifies that ToolResult is mutable (not frozen).*
        - `def test_success_result(None)` — *Verifies construction of a successful ToolResult.*
*   **`class VideoTest(methodName='runTest')`**
    *   *描述: Validates the Video content attachment primitive and its validators.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_basic_construction(None)` — *Verifies that a Video can be successfully constructed with valid arguments.*
        - `def test_unsupported_mime_type_raises(None)` — *Verifies that an unsupported Video MIME type triggers ValidationError.*

### 📦 模組: `google.antigravity.utils`
  *   *實體檔案: [__init__.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/utils/__init__.py)*

#### 📦 模組: `google.antigravity.utils.interactive`
  *   *實體檔案: [interactive.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/utils/interactive.py)*

### 類別 (Classes)
*   **`class AskQuestionHook(*args, **kwargs)`**
    *   *描述: Hook that prompts the user to answer questions asked by the agent.*
    *   **方法列表 (Methods):**
        - `def run(context: 'hooks.HookContext', data: 'types.AskQuestionInteractionSpec')` — *Asks the user for answers to each question via standard input.*
*   **`class Spinner(message: 'str' = 'Thinking...')`**
    *   *描述: A lightweight terminal spinner for async processing feedback.*
    *   **方法列表 (Methods):**
        - `def update(message: 'str')` — *Updates the spinner display message.*
*   **`class ToolConfirmationHook(*args, **kwargs)`**
    *   *描述: Hook that prompts the user for confirmation before executing a tool.*
    *   **方法列表 (Methods):**
        - `def run(context: 'hooks.HookContext', data: 'types.ToolCall')` — *Asks the user for confirmation via standard input.*

#### 📦 模組: `google.antigravity.utils.interactive_test`
  *   *實體檔案: [interactive_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/utils/interactive_test.py)*

### 類別 (Classes)
*   **`class AskQuestionHookTest(methodName='runTest')`**
    *   *描述: Tests for AskQuestionHook.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)`
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_ask_question_hook_eof(mock_input)` — *Verifies that EOFError results in a cancelled response.*
        - `def test_ask_question_hook_option_number(mock_input)` — *Verifies that the user can select an option by its index.*
        - `def test_ask_question_hook_option_text(mock_input)` — *Verifies that the user can select an option by its exact text.*
        - `def test_ask_question_hook_skip(mock_input)` — *Verifies that the user can skip a question by providing empty input.*
        - `def test_ask_question_hook_write_in(mock_input)` — *Verifies that the user can provide a write-in response.*
*   **`class AskUserHandlerTest(methodName='runTest')`**
    *   *描述: Tests for ask_user_handler.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)`
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_ask_user_handler_allow(mock_input)` — *Verifies that the handler returns True when the user confirms.*
        - `def test_ask_user_handler_deny(mock_input)` — *Verifies that the handler returns False when the user declines.*
        - `def test_ask_user_handler_eof(mock_input)` — *Verifies that the handler returns False on EOFError.*
*   **`class AsyncInputTest(methodName='runTest')`**
    *   *描述: Tests for async_input.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_cancellation(mock_input)` — *Verifies that cancelling the future does not crash the thread.*
        - `def test_default_prompt(mock_input)` — *Verifies that async_input passes an empty prompt by default.*
        - `def test_propagates_eof_error(mock_input)` — *Verifies that EOFError from input() is propagated.*
        - `def test_returns_user_input(mock_input)` — *Verifies that async_input returns the value from input().*
*   **`class RunInteractiveLoopTest(methodName='runTest')`**
    *   *描述: Tests for run_interactive_loop.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_run_interactive_loop(mock_async_input, mock_conv_create, mock_strategy_class)` — *Verifies the basic interactive loop flow.*
        - `def test_run_interactive_loop_appends_ask_question_hook_when_missing(mock_async_input, mock_conv_create, mock_strategy_class)` — *Verifies that AskQuestionHook is added when not present.*
        - `def test_run_interactive_loop_does_not_duplicate_ask_question_hook_when_present(mock_async_input, mock_conv_create, mock_strategy_class)` — *Verifies that AskQuestionHook is not duplicated if already present.*
        - `def test_run_interactive_loop_interrupt(mock_async_input, mock_conv_create, mock_strategy_class)` — *Verifies clean exit on KeyboardInterrupt.*
*   **`class ToolConfirmationHookTest(methodName='runTest')`**
    *   *描述: Tests for ToolConfirmationHook.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)`
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_tool_confirmation_hook_allow(mock_input)` — *Verifies that the hook allows execution when the user confirms.*
        - `def test_tool_confirmation_hook_deny(mock_input)` — *Verifies that the hook denies execution when the user declines.*
        - `def test_tool_confirmation_hook_eof(mock_input)` — *Verifies that the hook denies execution on EOFError.*
*   **`class UpgradePoliciesListTest(methodName='runTest')`**
    *   *描述: Tests for _upgrade_policies_list.*
    *   **方法列表 (Methods):**
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def countTestCases(None)`
        - `def debug(None)` — *Run the test without collecting errors in a TestResult*
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)` — *Hook method for setting up the test fixture before exercising it.*
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)` — *Hook method for deconstructing the test fixture after testing it.*
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_upgrade_policies_list(None)` — *Verifies that deny policies on run_command are converted to ask_user.*

#### 📦 模組: `google.antigravity.utils.otel`
  *   *實體檔案: [otel.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/utils/otel.py)*

### 類別 (Classes)
*   **`class OTelOnToolErrorHook(*args, **kwargs)`**
    *   *描述: Records exceptions and ends a tool span on error.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: Exception)`
*   **`class OTelPostStepHook(*args, **kwargs)`**
    *   *描述: Ends a step span.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: google.antigravity.types.Step)`
*   **`class OTelPostToolCallHook(*args, **kwargs)`**
    *   *描述: Ends a tool span.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: google.antigravity.types.ToolResult)`
*   **`class OTelPostTurnHook(*args, **kwargs)`**
    *   *描述: Ends the Turn span.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: str)`
*   **`class OTelPreStepHook(*args, **kwargs)`**
    *   *描述: Starts a step span.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: google.antigravity.types.Step)`
*   **`class OTelPreToolCallHook(*args, **kwargs)`**
    *   *描述: Starts a tool span.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: google.antigravity.types.ToolCall)`
*   **`class OTelPreTurnHook(agent_name: str = 'Antigravity')`**
    *   *描述: Starts the Turn span under Session.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand | collections.abc.Sequence[str | google.antigravity.types.Image | google.antigravity.types.Document | google.antigravity.types.Audio | google.antigravity.types.Video | google.antigravity.types.SlashCommand])`
*   **`class OTelSessionEndHook(*args, **kwargs)`**
    *   *描述: Closes the root session span.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: None)`
*   **`class OTelSessionStartHook(*args, **kwargs)`**
    *   *描述: Starts the root session span.*
    *   **方法列表 (Methods):**
        - `def run(context: google.antigravity.hooks.hooks.HookContext, data: None)`

#### 📦 模組: `google.antigravity.utils.otel_test`
  *   *實體檔案: [otel_test.py](file:///Users/wuulong/opt/anaconda3/envs/m2504/lib/python3.12/site-packages/google/antigravity/utils/otel_test.py)*

### 類別 (Classes)
*   **`class DummyStep(**data: 'Any')`**
    *   **方法列表 (Methods):**
        - `def construct(_fields_set: 'set[str] | None' = None, **values: 'Any')`
        - `def copy(include: 'AbstractSetIntStr | MappingIntStrAny | None' = None, exclude: 'AbstractSetIntStr | MappingIntStrAny | None' = None, update: 'Dict[str, Any] | None' = None, deep: 'bool' = False)` — *Returns a copy of the model.*
        - `def dict(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False)`
        - `def from_orm(obj: 'Any')`
        - `def json(include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, by_alias: 'bool' = False, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, encoder: 'Callable[[Any], Any] | None' = PydanticUndefined, models_as_dict: 'bool' = PydanticUndefined, **dumps_kwargs: 'Any')`
        - `def model_construct(_fields_set: 'set[str] | None' = None, **values: 'Any')` — *Creates a new instance of the `Model` class with validated data.*
        - `def model_copy(update: 'Mapping[str, Any] | None' = None, deep: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump(mode: "Literal['json', 'python'] | str" = 'python', include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_dump_json(indent: 'int | None' = None, include: 'IncEx | None' = None, exclude: 'IncEx | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, exclude_unset: 'bool' = False, exclude_defaults: 'bool' = False, exclude_none: 'bool' = False, round_trip: 'bool' = False, warnings: "bool | Literal['none', 'warn', 'error']" = True, fallback: 'Callable[[Any], Any] | None' = None, serialize_as_any: 'bool' = False)` — *!!! abstract "Usage Documentation"*
        - `def model_json_schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', schema_generator: 'type[GenerateJsonSchema]' = <class 'pydantic.json_schema.GenerateJsonSchema'>, mode: 'JsonSchemaMode' = 'validation')` — *Generates a JSON schema for a model class.*
        - `def model_parametrized_name(params: 'tuple[type[Any], ...]')` — *Compute the class name for parametrizations of generic classes.*
        - `def model_post_init(context: 'Any')` — *Override this method to perform additional initialization after `__init__` and `model_construct`.*
        - `def model_rebuild(force: 'bool' = False, raise_errors: 'bool' = True, _parent_namespace_depth: 'int' = 2, _types_namespace: 'MappingNamespace | None' = None)` — *Try to rebuild the pydantic-core schema for the model.*
        - `def model_validate(obj: 'Any', strict: 'bool | None' = None, from_attributes: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate a pydantic model instance.*
        - `def model_validate_json(json_data: 'str | bytes | bytearray', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *!!! abstract "Usage Documentation"*
        - `def model_validate_strings(obj: 'Any', strict: 'bool | None' = None, context: 'Any | None' = None, by_alias: 'bool | None' = None, by_name: 'bool | None' = None)` — *Validate the given object with string data against the Pydantic model.*
        - `def parse_file(path: 'str | Path', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def parse_obj(obj: 'Any')`
        - `def parse_raw(b: 'str | bytes', content_type: 'str | None' = None, encoding: 'str' = 'utf8', proto: 'DeprecatedParseProtocol | None' = None, allow_pickle: 'bool' = False)`
        - `def schema(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}')`
        - `def schema_json(by_alias: 'bool' = True, ref_template: 'str' = '#/$defs/{model}', **dumps_kwargs: 'Any')`
        - `def update_forward_refs(**localns: 'Any')`
        - `def validate(value: 'Any')`
*   **`class OtelHooksTest(methodName='runTest')`**
    *   *描述: Tests tracing context propagation across turns and interleaved steps.*
    *   **方法列表 (Methods):**
        - `def addAsyncCleanup(func, *args, **kwargs)`
        - `def addClassCleanup(function, *args, **kwargs)` — *Same as addCleanup, except the cleanup items are called even if*
        - `def addCleanup(function, *args, **kwargs)` — *Add a function, with arguments, to be called when the test is*
        - `def addTypeEqualityFunc(typeobj, function)` — *Add a type specific assertEqual style function to compare a type.*
        - `def assertAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are unequal as determined by their*
        - `def assertCountEqual(first, second, msg=None)` — *Asserts that two iterables have the same elements, the same number of*
        - `def assertDictEqual(d1, d2, msg=None)`
        - `def assertEqual(first, second, msg=None)` — *Fail if the two objects are unequal as determined by the '=='*
        - `def assertFalse(expr, msg=None)` — *Check that the expression is false.*
        - `def assertGreater(a, b, msg=None)` — *Just like self.assertTrue(a > b), but with a nicer default message.*
        - `def assertGreaterEqual(a, b, msg=None)` — *Just like self.assertTrue(a >= b), but with a nicer default message.*
        - `def assertIn(member, container, msg=None)` — *Just like self.assertTrue(a in b), but with a nicer default message.*
        - `def assertIs(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is b), but with a nicer default message.*
        - `def assertIsInstance(obj, cls, msg=None)` — *Same as self.assertTrue(isinstance(obj, cls)), with a nicer*
        - `def assertIsNone(obj, msg=None)` — *Same as self.assertTrue(obj is None), with a nicer default message.*
        - `def assertIsNot(expr1, expr2, msg=None)` — *Just like self.assertTrue(a is not b), but with a nicer default message.*
        - `def assertIsNotNone(obj, msg=None)` — *Included for symmetry with assertIsNone.*
        - `def assertLess(a, b, msg=None)` — *Just like self.assertTrue(a < b), but with a nicer default message.*
        - `def assertLessEqual(a, b, msg=None)` — *Just like self.assertTrue(a <= b), but with a nicer default message.*
        - `def assertListEqual(list1, list2, msg=None)` — *A list-specific equality assertion.*
        - `def assertLogs(logger=None, level=None)` — *Fail unless a log message of level *level* or higher is emitted*
        - `def assertMultiLineEqual(first, second, msg=None)` — *Assert that two multi-line strings are equal.*
        - `def assertNoLogs(logger=None, level=None)` — *Fail unless no log messages of level *level* or higher are emitted*
        - `def assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)` — *Fail if the two objects are equal as determined by their*
        - `def assertNotEqual(first, second, msg=None)` — *Fail if the two objects are equal as determined by the '!='*
        - `def assertNotIn(member, container, msg=None)` — *Just like self.assertTrue(a not in b), but with a nicer default message.*
        - `def assertNotIsInstance(obj, cls, msg=None)` — *Included for symmetry with assertIsInstance.*
        - `def assertNotRegex(text, unexpected_regex, msg=None)` — *Fail the test if the text matches the regular expression.*
        - `def assertRaises(expected_exception, *args, **kwargs)` — *Fail unless an exception of class expected_exception is raised*
        - `def assertRaisesRegex(expected_exception, expected_regex, *args, **kwargs)` — *Asserts that the message in a raised exception matches a regex.*
        - `def assertRegex(text, expected_regex, msg=None)` — *Fail the test unless the text matches the regular expression.*
        - `def assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)` — *An equality assertion for ordered sequences (like lists and tuples).*
        - `def assertSetEqual(set1, set2, msg=None)` — *A set-specific equality assertion.*
        - `def assertTrue(expr, msg=None)` — *Check that the expression is true.*
        - `def assertTupleEqual(tuple1, tuple2, msg=None)` — *A tuple-specific equality assertion.*
        - `def assertWarns(expected_warning, *args, **kwargs)` — *Fail unless a warning of class warnClass is triggered*
        - `def assertWarnsRegex(expected_warning, expected_regex, *args, **kwargs)` — *Asserts that the message in a triggered warning matches a regexp.*
        - `def asyncSetUp(None)`
        - `def asyncTearDown(None)`
        - `def countTestCases(None)`
        - `def debug(None)`
        - `def defaultTestResult(None)`
        - `def doClassCleanups(None)` — *Execute all class cleanup functions. Normally called for you after*
        - `def doCleanups(None)` — *Execute all cleanup functions. Normally called for you after*
        - `def enterAsyncContext(cm)` — *Enters the supplied asynchronous context manager.*
        - `def enterClassContext(cm)` — *Same as enterContext, but class-wide.*
        - `def enterContext(cm)` — *Enters the supplied context manager.*
        - `def fail(msg=None)` — *Fail immediately, with the given message.*
        - `def id(None)`
        - `def run(result=None)`
        - `def setUp(None)`
        - `def setUpClass(None)` — *Hook method for setting up class fixture before running tests in the class.*
        - `def shortDescription(None)` — *Returns a one-line description of the test, or None if no*
        - `def skipTest(reason)` — *Skip this test.*
        - `def subTest(msg=<object object at 0x10332f6f0>, **params)` — *Return a context manager that will return the enclosed block*
        - `def tearDown(None)`
        - `def tearDownClass(None)` — *Hook method for deconstructing the class fixture after running all tests in the class.*
        - `def test_active_tool_span_propagation(None)` — *Verifies that nested spans started during tool execution are parented under the tool span.*
        - `def test_auto_cleanup_remaining_spans(None)` — *Verifies that hooks clean up spans left open due to missing lifecycle calls.*
        - `def test_get_otel_hooks(None)`
        - `def test_interleaved_steps_tracing(None)` — *Verifies steps and tools are correctly parented under concurrent execution.*
        - `def test_session_and_turn_hierarchy(None)` — *Verifies that turn spans are nested under session spans.*
        - `def test_step_failure_tracing(None)` — *Verifies that failed steps record error status on the span.*
        - `def test_tool_failure_tracing(None)` — *Verifies OTelOnToolErrorHook records exception and ends tool span.*
        - `def test_tool_span_context_exit_different_task(None)` — *Verifies that exiting tool span context in a different task does not fail.*
        - `def test_trajectory_id_fallbacks(None)`
