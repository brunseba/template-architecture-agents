# Draw.io (.drawio) File Format Guide

This guide documents the draw.io XML file format for programmatic generation of diagrams, supporting both manual creation and MCP-based AI-assisted diagram generation.

## File Structure Overview

Draw.io files are XML documents with optional compression. The basic structure:

```xml
<mxfile host="app.diagrams.net" modified="2024-01-01T00:00:00.000Z" agent="..." version="...">
  <diagram id="unique-diagram-id" name="Diagram Name">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <!-- Your shapes and connections go here -->
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Core Components

### mxGraphModel Attributes

| Attribute | Description | Default |
|-----------|-------------|---------|
| `dx` | X-axis viewport offset | `1422` |
| `dy` | Y-axis viewport offset | `794` |
| `grid` | Show grid (0 or 1) | `1` |
| `gridSize` | Grid cell size | `10` |
| `guides` | Enable guides | `1` |
| `page` | Show page view | `1` |
| `pageWidth` | Page width in pixels | `827` (A4) |
| `pageHeight` | Page height in pixels | `1169` (A4) |

### Root Cells

Every diagram requires two root cells:

```xml
<mxCell id="0"/>
<mxCell id="1" parent="0"/>
```

- Cell `id="0"`: Root container
- Cell `id="1"`: Default layer (parent of all user elements)

## Shape Definition

### Basic Shape (Rectangle)

```xml
<mxCell id="shape-001" value="My Shape" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
</mxCell>
```

**Key Attributes**:
- `id`: Unique identifier
- `value`: Text displayed in shape
- `style`: Semicolon-separated style properties
- `vertex="1"`: Indicates this is a vertex (shape), not an edge
- `parent`: ID of parent cell (usually "1")

### Common Shape Styles

| Shape Type | Style String |
|------------|--------------|
| Rectangle | `rounded=0;whiteSpace=wrap;html=1;` |
| Rounded Rectangle | `rounded=1;whiteSpace=wrap;html=1;` |
| Ellipse | `ellipse;whiteSpace=wrap;html=1;` |
| Rhombus | `rhombus;whiteSpace=wrap;html=1;` |
| Hexagon | `shape=hexagon;perimeter=hexagonPerimeter2;whiteSpace=wrap;html=1;` |
| Cylinder | `shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;` |
| Cloud | `ellipse;shape=cloud;whiteSpace=wrap;html=1;` |

### AWS/Azure/GCP Shapes

Draw.io includes extensive cloud provider shape libraries. To use them:

```xml
<mxCell id="aws-ec2" value="EC2 Instance" 
       style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.instance;" 
       vertex="1" parent="1">
  <mxGeometry x="200" y="150" width="48" height="48" as="geometry"/>
</mxCell>
```

Key style properties for cloud shapes:
- `sketch=0`: Disable sketch mode
- `outlineConnect=0`: Disable outline connection points
- `shape=mxgraph.aws4.instance`: Specific shape from AWS library
- `aspect=fixed`: Maintain aspect ratio

### Container Shapes (Groups)

Create a container that holds other shapes:

```xml
<mxCell id="container-001" value="Container" style="swimlane;whiteSpace=wrap;html=1;" vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>

<mxCell id="child-001" value="Child Shape" style="rounded=0;whiteSpace=wrap;html=1;" vertex="1" parent="container-001">
  <mxGeometry x="20" y="40" width="120" height="60" as="geometry"/>
</mxCell>
```

**Swimlane styles**:
- `swimlane`: Creates a container with a header
- `startSize=23`: Header height
- `horizontal=1`: Horizontal orientation (0 for vertical)
- `collapsible=0`: Disable collapse functionality

## Connections (Edges)

### Basic Connection

```xml
<mxCell id="edge-001" value="Label" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" 
       edge="1" parent="1" source="shape-001" target="shape-002">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

**Key Attributes**:
- `edge="1"`: Indicates this is an edge (connection)
- `source`: ID of source shape
- `target`: ID of target shape
- `relative="1"`: Use relative geometry

### Edge Styles

| Style | Description |
|-------|-------------|
| `edgeStyle=orthogonalEdgeStyle` | Right-angle connections |
| `edgeStyle=elbowEdgeStyle` | Elbow-style connections |
| `edgeStyle=entityRelationEdgeStyle` | Entity-relationship style |
| `curved=1` | Curved connection |
| `dashed=1` | Dashed line |
| `startArrow=classic` | Arrow at start |
| `endArrow=classic` | Arrow at end |

### Connection with Waypoints

```xml
<mxCell id="edge-002" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" 
       edge="1" parent="1" source="shape-001" target="shape-002">
  <mxGeometry relative="1" as="geometry">
    <Array as="points">
      <mxPoint x="300" y="200"/>
      <mxPoint x="300" y="350"/>
    </Array>
  </mxGeometry>
</mxCell>
```

## Styling Properties

### Color Properties

```
fillColor=#dae8fc;      // Fill color
strokeColor=#6c8ebf;    // Border color
fontColor=#000000;      // Text color
```

Colors are hex values with `#` prefix.

### Text Properties

```
fontSize=12;            // Font size in points
fontStyle=1;            // 0=normal, 1=bold, 2=italic, 3=bold+italic
fontFamily=Helvetica;   // Font family
align=center;           // Horizontal: left, center, right
verticalAlign=middle;   // Vertical: top, middle, bottom
```

### Geometric Properties

```
rounded=1;              // Rounded corners (0 or 1)
strokeWidth=2;          // Border width
opacity=50;             // Opacity (0-100)
shadow=1;               // Drop shadow
```

## Layers

Organize elements into layers:

```xml
<root>
  <mxCell id="0"/>
  <mxCell id="1" parent="0"/>
  
  <!-- Second layer -->
  <mxCell id="layer-2" parent="0"/>
  
  <!-- Shape on layer 2 -->
  <mxCell id="shape-layer2" value="On Layer 2" style="rounded=0;whiteSpace=wrap;html=1;" 
         vertex="1" parent="layer-2">
    <mxGeometry x="100" y="100" width="120" height="60" as="geometry"/>
  </mxCell>
</root>
```

## Multiple Pages

Add multiple diagram pages:

```xml
<mxfile>
  <diagram id="page-1" name="Page 1">
    <mxGraphModel>
      <!-- Page 1 content -->
    </mxGraphModel>
  </diagram>
  
  <diagram id="page-2" name="Page 2">
    <mxGraphModel>
      <!-- Page 2 content -->
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Architecture Diagram Example

Complete example of a cloud architecture diagram:

```xml
<mxfile host="app.diagrams.net">
  <diagram id="cloud-arch" name="Cloud Architecture">
    <mxGraphModel dx="1422" dy="794" grid="1" gridSize="10" guides="1" page="1">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- VPC Container -->
        <mxCell id="vpc" value="VPC" 
               style="swimlane;whiteSpace=wrap;html=1;startSize=23;fillColor=#dae8fc;strokeColor=#6c8ebf;" 
               vertex="1" parent="1">
          <mxGeometry x="80" y="80" width="640" height="400" as="geometry"/>
        </mxCell>
        
        <!-- Load Balancer -->
        <mxCell id="lb" value="Load Balancer" 
               style="outlineConnect=0;fontColor=#232F3E;fillColor=#8C4FFF;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.elastic_load_balancing;" 
               vertex="1" parent="vpc">
          <mxGeometry x="296" y="40" width="48" height="48" as="geometry"/>
        </mxCell>
        
        <!-- Web Server 1 -->
        <mxCell id="web1" value="Web Server 1" 
               style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.instance;" 
               vertex="1" parent="vpc">
          <mxGeometry x="200" y="150" width="48" height="48" as="geometry"/>
        </mxCell>
        
        <!-- Web Server 2 -->
        <mxCell id="web2" value="Web Server 2" 
               style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#ED7100;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.instance;" 
               vertex="1" parent="vpc">
          <mxGeometry x="392" y="150" width="48" height="48" as="geometry"/>
        </mxCell>
        
        <!-- Database -->
        <mxCell id="db" value="Database" 
               style="sketch=0;outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=12;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.rds_instance;" 
               vertex="1" parent="vpc">
          <mxGeometry x="296" y="280" width="48" height="48" as="geometry"/>
        </mxCell>
        
        <!-- Connections -->
        <mxCell id="conn1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" 
               edge="1" parent="vpc" source="lb" target="web1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" 
               edge="1" parent="vpc" source="lb" target="web2">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" 
               edge="1" parent="vpc" source="web1" target="db">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
        <mxCell id="conn4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" 
               edge="1" parent="vpc" source="web2" target="db">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## MCP Integration for AI-Assisted Generation

When using Draw.io MCP Server (section 1.3), diagrams can be generated programmatically through the Model Context Protocol:

### Schema-to-Diagram Workflow

1. **Define Schema**: Provide structured data (JSON, YAML) describing components and relationships
2. **MCP Processing**: MCP server converts schema to draw.io XML structure
3. **Layout Generation**: Automatic positioning and connection routing
4. **Style Application**: Apply appropriate shapes and colors based on component types
5. **Export**: Generate .drawio file or export to PNG/SVG

### Programmatic Shape Selection

For cloud architecture diagrams, use provider-specific shape patterns:

| Provider | Shape Prefix | Example |
|----------|--------------|---------|
| AWS | `mxgraph.aws4.*` | `mxgraph.aws4.instance` |
| Azure | `mxgraph.azure.*` | `mxgraph.azure.compute.VM_Linux` |
| GCP | `mxgraph.gcp2.*` | `mxgraph.gcp2.compute_engine` |
| Kubernetes | `mxgraph.kubernetes.*` | `mxgraph.kubernetes.pod` |

### Auto-Layout Algorithms

For MCP-based generation, consider these layout patterns:

- **Hierarchical**: Top-down flow (load balancers → servers → databases)
- **Horizontal**: Left-to-right pipeline flow
- **Organic**: Force-directed layout for complex networks
- **Circular**: Radial layout for hub-and-spoke patterns
- **Grid**: Structured grid for microservices

## Common Patterns

### Network Diagram Pattern

```xml
<!-- Subnet container -->
<mxCell id="subnet" value="Private Subnet" 
       style="rounded=1;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;dashed=1;" 
       vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="300" height="200" as="geometry"/>
</mxCell>
```

### UML Class Diagram Pattern

```xml
<!-- Class shape with compartments -->
<mxCell id="class1" value="&lt;b&gt;ClassName&lt;/b&gt;&lt;hr&gt;- field1: Type&lt;br&gt;- field2: Type&lt;hr&gt;+ method1()&lt;br&gt;+ method2()" 
       style="rounded=0;whiteSpace=wrap;html=1;align=left;verticalAlign=top;" 
       vertex="1" parent="1">
  <mxGeometry x="100" y="100" width="160" height="120" as="geometry"/>
</mxCell>
```

### Flowchart Decision Pattern

```xml
<!-- Decision diamond -->
<mxCell id="decision" value="Condition?" 
       style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;" 
       vertex="1" parent="1">
  <mxGeometry x="250" y="150" width="100" height="80" as="geometry"/>
</mxCell>

<!-- True path -->
<mxCell id="edge-true" value="Yes" 
       style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" 
       edge="1" parent="1" source="decision" target="action-true">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>

<!-- False path -->
<mxCell id="edge-false" value="No" 
       style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;" 
       edge="1" parent="1" source="decision" target="action-false">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

## Best Practices for Programmatic Generation

1. **Unique IDs**: Always generate unique IDs for cells (e.g., UUID or sequential)
2. **Consistent Spacing**: Use grid-aligned coordinates (multiples of 10 or 20)
3. **Readable Styles**: Separate style properties with semicolons, no spaces
4. **Layer Organization**: Use layers to organize complex diagrams
5. **Shape Libraries**: Reference standard shape libraries (AWS, Azure, GCP) for consistency
6. **Connection Points**: Use `entryX`, `entryY`, `exitX`, `exitY` for precise connection anchoring
7. **Label Positioning**: Set `verticalLabelPosition` and `verticalAlign` for proper label placement
8. **Container Hierarchy**: Nest shapes properly in containers for logical grouping

## Common Mistakes to Avoid

1. **Missing Root Cells**: Always include cells with id="0" and id="1"
2. **Incorrect Parent References**: Ensure parent IDs exist and are valid
3. **Invalid Style Strings**: Check for typos in style properties
4. **Overlapping Geometries**: Plan layout to avoid shape overlap
5. **Wrong Edge Attributes**: Use `edge="1"` for connections, `vertex="1"` for shapes
6. **Missing Source/Target**: Edges must have valid source and target IDs
7. **Malformed HTML**: When using `html=1`, ensure value attribute contains valid HTML entities

## File Format Variants

### Uncompressed Format

Standard XML as shown in examples above. Use `.drawio` extension.

### Compressed Format

Draw.io can compress diagrams using deflate. The file contains base64-encoded, compressed XML.

### PNG with Embedded Diagram

Draw.io can embed XML data in PNG files for both image and editable diagram:
- PNG file with `mxGraphModel` in metadata
- Opens as editable diagram in draw.io
- Displays as image elsewhere

## References

- Draw.io GitHub Repository: https://github.com/jgraph/drawio
- Draw.io MCP Server: https://github.com/jgraph/drawio-mcp
- Shape Library Documentation: https://www.drawio.com/doc/
- MxGraph JavaScript Library: https://github.com/jgraph/mxgraph (underlying technology)
- diagrams.net Documentation: https://www.diagrams.net/doc/
