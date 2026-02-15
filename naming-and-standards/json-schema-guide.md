# JSON Schema Specification Guide

This guide documents JSON Schema for programmatic validation, API contracts, and configuration management based on the JSON Schema specification.

## Schema Structure Overview

JSON Schema is a JSON document that defines the structure, constraints, and validation rules for JSON data.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/schemas/product.schema.json",
  "title": "Product",
  "description": "A product in the catalog",
  "type": "object",
  "properties": {
    "productId": {
      "type": "integer",
      "description": "Unique identifier for a product"
    },
    "productName": {
      "type": "string",
      "description": "Name of the product"
    }
  },
  "required": ["productId", "productName"]
}
```

## Core Keywords

### Meta-Schema Keywords

| Keyword | Purpose | Example |
|---------|---------|---------|
| `$schema` | Declares which JSON Schema version | `"https://json-schema.org/draft/2020-12/schema"` |
| `$id` | Unique identifier/base URI for schema | `"https://example.com/schemas/user.json"` |
| `title` | Human-readable title | `"User Schema"` |
| `description` | Detailed description | `"Schema for user registration"` |

### Type Definitions

JSON Schema supports seven primitive types:

```json
{
  "type": "string"      // String values
}
{
  "type": "number"      // Numeric values (integer or float)
}
{
  "type": "integer"     // Integer values only
}
{
  "type": "boolean"     // true or false
}
{
  "type": "null"        // null value
}
{
  "type": "array"       // Array of values
}
{
  "type": "object"      // Object with properties
}
```

Multiple types can be specified:

```json
{
  "type": ["string", "null"]  // String or null
}
```

## String Validation

### Length Constraints

```json
{
  "type": "string",
  "minLength": 3,
  "maxLength": 100
}
```

### Pattern Matching

Use regular expressions for pattern validation:

```json
{
  "type": "string",
  "pattern": "^[A-Z]{2}\\d{4}$"  // Two uppercase letters + 4 digits
}
```

### Format Validation

Built-in format validators:

```json
{
  "type": "string",
  "format": "email"      // Email address
}
{
  "type": "string",
  "format": "date"       // YYYY-MM-DD
}
{
  "type": "string",
  "format": "date-time"  // RFC 3339 date-time
}
{
  "type": "string",
  "format": "uri"        // URI reference
}
{
  "type": "string",
  "format": "uuid"       // UUID
}
{
  "type": "string",
  "format": "ipv4"       // IPv4 address
}
{
  "type": "string",
  "format": "ipv6"       // IPv6 address
}
```

### Enumeration

Restrict to specific values:

```json
{
  "type": "string",
  "enum": ["draft", "published", "archived"]
}
```

## Numeric Validation

### Range Constraints

```json
{
  "type": "integer",
  "minimum": 0,
  "maximum": 100,
  "exclusiveMinimum": 0,     // Greater than (not equal to) 0
  "exclusiveMaximum": 100    // Less than (not equal to) 100
}
```

### Multiple Constraints

```json
{
  "type": "number",
  "multipleOf": 0.01  // Must be multiple of 0.01 (e.g., for currency)
}
```

## Object Validation

### Basic Object Schema

```json
{
  "type": "object",
  "properties": {
    "firstName": {
      "type": "string",
      "minLength": 1
    },
    "lastName": {
      "type": "string",
      "minLength": 1
    },
    "age": {
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["firstName", "lastName"]
}
```

### Property Count

```json
{
  "type": "object",
  "minProperties": 1,
  "maxProperties": 10
}
```

### Additional Properties

Control whether additional properties are allowed:

```json
{
  "type": "object",
  "properties": {
    "name": { "type": "string" }
  },
  "additionalProperties": false  // No extra properties allowed
}
```

Allow additional properties with type constraints:

```json
{
  "type": "object",
  "properties": {
    "name": { "type": "string" }
  },
  "additionalProperties": {
    "type": "string"  // Additional properties must be strings
  }
}
```

### Pattern Properties

Define properties based on name patterns:

```json
{
  "type": "object",
  "patternProperties": {
    "^S_": { "type": "string" },      // Properties starting with S_
    "^I_": { "type": "integer" }      // Properties starting with I_
  }
}
```

### Property Dependencies

```json
{
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "creditCard": { "type": "string" },
    "billingAddress": { "type": "string" }
  },
  "dependencies": {
    "creditCard": ["billingAddress"]  // If creditCard exists, billingAddress required
  }
}
```

## Array Validation

### Basic Array Schema

```json
{
  "type": "array",
  "items": {
    "type": "string"  // All items must be strings
  }
}
```

### Array Length

```json
{
  "type": "array",
  "minItems": 1,
  "maxItems": 10
}
```

### Unique Items

```json
{
  "type": "array",
  "uniqueItems": true  // No duplicate values
}
```

### Tuple Validation

Fixed-length array with specific types per position:

```json
{
  "type": "array",
  "prefixItems": [
    { "type": "number" },   // First item: number
    { "type": "string" },   // Second item: string
    { "type": "boolean" }   // Third item: boolean
  ],
  "items": false  // No additional items allowed
}
```

### Contains Validation

At least one item must match schema:

```json
{
  "type": "array",
  "contains": {
    "type": "number",
    "minimum": 5
  },
  "minContains": 1,  // At least 1 match
  "maxContains": 3   // At most 3 matches
}
```

## Schema Composition

### allOf - Must Match All

```json
{
  "allOf": [
    { "type": "string" },
    { "minLength": 5 },
    { "maxLength": 10 }
  ]
}
```

### anyOf - Must Match At Least One

```json
{
  "anyOf": [
    { "type": "string", "maxLength": 5 },
    { "type": "number", "minimum": 0 }
  ]
}
```

### oneOf - Must Match Exactly One

```json
{
  "oneOf": [
    { "type": "number", "multipleOf": 5 },
    { "type": "number", "multipleOf": 3 }
  ]
}
```

### not - Must Not Match

```json
{
  "not": {
    "type": "string"  // Anything except string
  }
}
```

## Schema References ($ref)

### Internal References

Reference definitions within the same schema:

```json
{
  "$defs": {
    "address": {
      "type": "object",
      "properties": {
        "street": { "type": "string" },
        "city": { "type": "string" },
        "zipCode": { "type": "string" }
      },
      "required": ["street", "city", "zipCode"]
    }
  },
  "type": "object",
  "properties": {
    "billingAddress": { "$ref": "#/$defs/address" },
    "shippingAddress": { "$ref": "#/$defs/address" }
  }
}
```

### External References

Reference schemas from other files:

```json
{
  "$ref": "https://example.com/schemas/address.json"
}
```

```json
{
  "$ref": "./address.schema.json"
}
```

### Recursive References

Self-referential schemas for tree structures:

```json
{
  "$id": "https://example.com/tree.schema.json",
  "type": "object",
  "properties": {
    "value": { "type": "number" },
    "children": {
      "type": "array",
      "items": { "$ref": "#" }  // Reference to root schema
    }
  }
}
```

## Conditional Validation

### if/then/else

```json
{
  "type": "object",
  "properties": {
    "country": { "type": "string" },
    "postalCode": { "type": "string" }
  },
  "if": {
    "properties": { "country": { "const": "USA" } }
  },
  "then": {
    "properties": {
      "postalCode": { "pattern": "^\\d{5}(-\\d{4})?$" }
    }
  },
  "else": {
    "properties": {
      "postalCode": { "pattern": "^[A-Z0-9]+$" }
    }
  }
}
```

## Complete Examples

### User Registration Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/user.schema.json",
  "title": "User",
  "description": "User registration schema",
  "type": "object",
  "properties": {
    "username": {
      "type": "string",
      "minLength": 3,
      "maxLength": 20,
      "pattern": "^[a-zA-Z0-9_]+$",
      "description": "Unique username"
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "User email address"
    },
    "age": {
      "type": "integer",
      "minimum": 18,
      "maximum": 120,
      "description": "User age (must be 18+)"
    },
    "roles": {
      "type": "array",
      "items": {
        "type": "string",
        "enum": ["user", "admin", "moderator"]
      },
      "uniqueItems": true,
      "minItems": 1
    },
    "profile": {
      "type": "object",
      "properties": {
        "firstName": { "type": "string" },
        "lastName": { "type": "string" },
        "bio": { 
          "type": "string",
          "maxLength": 500
        }
      },
      "required": ["firstName", "lastName"]
    }
  },
  "required": ["username", "email", "roles"]
}
```

### API Response Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://api.example.com/response.schema.json",
  "title": "API Response",
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "enum": ["success", "error"]
    },
    "data": {
      "type": ["object", "array", "null"]
    },
    "error": {
      "type": "object",
      "properties": {
        "code": { "type": "string" },
        "message": { "type": "string" },
        "details": { "type": "object" }
      },
      "required": ["code", "message"]
    },
    "metadata": {
      "type": "object",
      "properties": {
        "timestamp": { "type": "string", "format": "date-time" },
        "requestId": { "type": "string", "format": "uuid" },
        "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+$" }
      }
    }
  },
  "required": ["status"],
  "allOf": [
    {
      "if": {
        "properties": { "status": { "const": "success" } }
      },
      "then": {
        "required": ["data"]
      }
    },
    {
      "if": {
        "properties": { "status": { "const": "error" } }
      },
      "then": {
        "required": ["error"]
      }
    }
  ]
}
```

### Configuration Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/config.schema.json",
  "title": "Application Configuration",
  "type": "object",
  "$defs": {
    "logLevel": {
      "type": "string",
      "enum": ["debug", "info", "warn", "error"]
    },
    "endpoint": {
      "type": "object",
      "properties": {
        "host": { "type": "string", "format": "hostname" },
        "port": { "type": "integer", "minimum": 1, "maximum": 65535 },
        "protocol": { "type": "string", "enum": ["http", "https"] }
      },
      "required": ["host", "port"]
    }
  },
  "properties": {
    "application": {
      "type": "object",
      "properties": {
        "name": { "type": "string" },
        "version": { "type": "string" },
        "logLevel": { "$ref": "#/$defs/logLevel" }
      },
      "required": ["name", "version"]
    },
    "server": {
      "$ref": "#/$defs/endpoint"
    },
    "database": {
      "type": "object",
      "properties": {
        "endpoint": { "$ref": "#/$defs/endpoint" },
        "credentials": {
          "type": "object",
          "properties": {
            "username": { "type": "string" },
            "password": { "type": "string" }
          },
          "required": ["username", "password"]
        },
        "maxConnections": {
          "type": "integer",
          "minimum": 1,
          "default": 10
        }
      },
      "required": ["endpoint", "credentials"]
    },
    "features": {
      "type": "object",
      "patternProperties": {
        "^feature_": { "type": "boolean" }
      },
      "additionalProperties": false
    }
  },
  "required": ["application", "server"]
}
```

## Common Patterns

### Polymorphic Objects (Discriminator)

```json
{
  "type": "object",
  "properties": {
    "type": { "type": "string" }
  },
  "required": ["type"],
  "oneOf": [
    {
      "properties": {
        "type": { "const": "circle" },
        "radius": { "type": "number" }
      },
      "required": ["radius"]
    },
    {
      "properties": {
        "type": { "const": "rectangle" },
        "width": { "type": "number" },
        "height": { "type": "number" }
      },
      "required": ["width", "height"]
    }
  ]
}
```

### Versioned Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://api.example.com/v2/resource.schema.json",
  "title": "Resource Schema v2",
  "type": "object",
  "properties": {
    "schemaVersion": {
      "type": "string",
      "const": "2.0.0"
    },
    "id": { "type": "string", "format": "uuid" },
    "name": { "type": "string" }
  },
  "required": ["schemaVersion", "id", "name"]
}
```

### Pagination Schema

```json
{
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": { "$ref": "#/$defs/item" }
    },
    "pagination": {
      "type": "object",
      "properties": {
        "page": { "type": "integer", "minimum": 1 },
        "pageSize": { "type": "integer", "minimum": 1, "maximum": 100 },
        "totalPages": { "type": "integer", "minimum": 0 },
        "totalItems": { "type": "integer", "minimum": 0 }
      },
      "required": ["page", "pageSize", "totalPages", "totalItems"]
    }
  },
  "required": ["items", "pagination"]
}
```

### Webhook Event Schema

```json
{
  "type": "object",
  "properties": {
    "eventId": { "type": "string", "format": "uuid" },
    "eventType": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "source": { "type": "string", "format": "uri" },
    "data": { "type": "object" }
  },
  "required": ["eventId", "eventType", "timestamp", "source", "data"]
}
```

## Best Practices

### 1. Use $id and $schema

Always specify schema version and identifier:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.com/schemas/my-schema.json"
}
```

### 2. Provide Documentation

Include `title` and `description` for schemas and properties:

```json
{
  "title": "User Profile",
  "description": "Schema for user profile data",
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "description": "User's primary email address"
    }
  }
}
```

### 3. Use Definitions for Reusability

Define common structures in `$defs`:

```json
{
  "$defs": {
    "timestamp": {
      "type": "string",
      "format": "date-time"
    }
  },
  "properties": {
    "createdAt": { "$ref": "#/$defs/timestamp" },
    "updatedAt": { "$ref": "#/$defs/timestamp" }
  }
}
```

### 4. Set Defaults

Provide sensible defaults where appropriate:

```json
{
  "properties": {
    "timeout": {
      "type": "integer",
      "minimum": 1,
      "default": 30
    }
  }
}
```

### 5. Use Examples

Include examples for clarity:

```json
{
  "properties": {
    "email": {
      "type": "string",
      "format": "email",
      "examples": ["user@example.com"]
    }
  }
}
```

### 6. Version Your Schemas

Include version information in schema IDs and consider backward compatibility:

```json
{
  "$id": "https://api.example.com/v1/user.schema.json",
  "properties": {
    "version": { "const": "1.0.0" }
  }
}
```

### 7. Use Appropriate Validation Levels

Balance strictness with flexibility:

- **Strict**: Use `additionalProperties: false` for known structures
- **Flexible**: Allow additional properties for extensibility
- **Typed**: Use `additionalProperties: { type: "..." }` for controlled flexibility

### 8. Leverage Format Validators

Use built-in formats instead of patterns when available:

```json
// Good
{ "type": "string", "format": "email" }

// Less maintainable
{ "type": "string", "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$" }
```

## Common Mistakes to Avoid

1. **Missing Required Fields**: Always specify `required` array for mandatory properties
2. **Overly Restrictive**: Don't use `additionalProperties: false` unless necessary
3. **Incorrect Pattern Escaping**: Remember to double-escape backslashes in regex patterns
4. **Type Mismatches**: Ensure default values match the specified type
5. **Circular References Without $id**: Use `$id` for recursive schemas
6. **Missing $schema Declaration**: Always declare which JSON Schema version you're using
7. **Ambiguous oneOf**: Ensure oneOf branches are mutually exclusive
8. **Format vs Pattern**: Use `format` for standard formats, `pattern` for custom validation

## Schema Validation Tools

### Command Line

```bash
# Using ajv-cli
npm install -g ajv-cli
ajv validate -s schema.json -d data.json

# Using check-jsonschema
pip install check-jsonschema
check-jsonschema --schemafile schema.json data.json
```

### Programmatic Validation (JavaScript)

```javascript
const Ajv = require("ajv");
const ajv = new Ajv();

const schema = {
  type: "object",
  properties: {
    name: { type: "string" },
    age: { type: "integer", minimum: 0 }
  },
  required: ["name", "age"]
};

const validate = ajv.compile(schema);
const valid = validate({ name: "John", age: 30 });

if (!valid) {
  console.log(validate.errors);
}
```

### Programmatic Validation (Python)

```python
import jsonschema

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer", "minimum": 0}
    },
    "required": ["name", "age"]
}

data = {"name": "John", "age": 30}

try:
    jsonschema.validate(instance=data, schema=schema)
    print("Valid!")
except jsonschema.exceptions.ValidationError as e:
    print(f"Validation error: {e.message}")
```

## Integration with OpenAPI

JSON Schema is used in OpenAPI specifications for request/response validation:

```yaml
openapi: 3.0.0
paths:
  /users:
    post:
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/User'
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
          format: uuid
        username:
          type: string
          minLength: 3
          maxLength: 20
      required:
        - username
```

## References

- JSON Schema Specification: https://json-schema.org/
- Understanding JSON Schema: https://json-schema.org/understanding-json-schema/
- JSON Schema Validator (ajv): https://ajv.js.org/
- JSON Schema Store: https://www.schemastore.org/
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- JSON Schema Bundler: https://github.com/json-schema-org/json-schema-bundler
