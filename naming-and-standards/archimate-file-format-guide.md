# ArchiMate Tool (.archimate) File Format Guide

This guide documents the native Archi Tool XML file format for programmatic generation of ArchiMate models.

## File Structure Overview

```xml
<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                 xmlns:archimate="http://www.archimatetool.com/archimate" 
                 name="Model Name" 
                 id="unique-model-id" 
                 version="5.0.0">
  <!-- Folders for elements -->
  <!-- Relations folder -->
  <!-- Views folder -->
  <purpose>Model description</purpose>
</archimate:model>
```

## Element Folders

Elements are organized in typed folders:

| Folder Type | type attribute | ArchiMate Layer |
|-------------|----------------|-----------------|
| Strategy | `strategy` | Capability, CourseOfAction, Resource, ValueStream |
| Business | `business` | BusinessActor, BusinessRole, BusinessService, BusinessProcess, etc. |
| Application | `application` | ApplicationComponent, ApplicationService, DataObject, etc. |
| Technology | `technology` | Node, Device, SystemSoftware, CommunicationNetwork, Facility, etc. |
| Motivation | `motivation` | Stakeholder, Driver, Goal, Principle, Requirement, Constraint |
| Implementation | `implementation_migration` | WorkPackage, Deliverable, ImplementationEvent, Plateau, Gap |
| Relations | `relations` | All relationship types |
| Views | `diagrams` | ArchimateDiagramModel elements |

### Element Definition

```xml
<folder name="Application" id="folder-app" type="application">
  <element xsi:type="archimate:ApplicationComponent" name="My App" id="elem-001"/>
  <element xsi:type="archimate:DataObject" name="Customer Data" id="elem-002">
    <documentation>Optional description</documentation>
  </element>
</folder>
```

## Relationships

All relationships go in the Relations folder:

```xml
<folder name="Relations" id="folder-relations" type="relations">
  <element xsi:type="archimate:ServingRelationship" id="rel-001" source="elem-001" target="elem-002"/>
  <element xsi:type="archimate:CompositionRelationship" id="rel-002" source="elem-001" target="elem-003"/>
  <element xsi:type="archimate:RealizationRelationship" id="rel-003" source="elem-004" target="elem-001"/>
</folder>
```

### Relationship Types

| Type | xsi:type |
|------|----------|
| Composition | `archimate:CompositionRelationship` |
| Aggregation | `archimate:AggregationRelationship` |
| Assignment | `archimate:AssignmentRelationship` |
| Realization | `archimate:RealizationRelationship` |
| Serving | `archimate:ServingRelationship` |
| Access | `archimate:AccessRelationship` |
| Influence | `archimate:InfluenceRelationship` |
| Triggering | `archimate:TriggeringRelationship` |
| Flow | `archimate:FlowRelationship` |
| Specialization | `archimate:SpecializationRelationship` |
| Association | `archimate:AssociationRelationship` |

## Views (Diagrams)

Views are defined in the diagrams folder using `ArchimateDiagramModel`:

```xml
<folder name="Views" id="folder-views" type="diagrams">
  <element xsi:type="archimate:ArchimateDiagramModel" name="View Name" id="view-001">
    <!-- Visual elements go here -->
  </element>
</folder>
```

### DiagramObject (Element on View)

To place an ArchiMate element on a view:

```xml
<child xsi:type="archimate:DiagramObject" id="do-001" archimateElement="elem-001">
  <bounds x="20" y="40" width="140" height="55"/>
</child>
```

- `archimateElement` references the element's ID
- `bounds` defines position (x, y) and size (width, height)
- Coordinates are relative to parent container

### Group (Visual Grouping Box)

Groups are visual containers (not ArchiMate elements):

```xml
<child xsi:type="archimate:Group" id="grp-001" name="Business Layer" fillColor="#ffffb5">
  <bounds x="20" y="20" width="760" height="120"/>
  <child xsi:type="archimate:DiagramObject" id="do-001" archimateElement="elem-001">
    <bounds x="20" y="40" width="140" height="55"/>
  </child>
</child>
```

- `fillColor` is hex color for background
- Child elements have coordinates relative to the group

### Nested Elements

Elements can be nested visually (containment):

```xml
<child xsi:type="archimate:DiagramObject" id="do-aks" archimateElement="node-aks">
  <bounds x="20" y="40" width="400" height="200"/>
  <child xsi:type="archimate:DiagramObject" id="do-pod" archimateElement="node-pod">
    <bounds x="20" y="40" width="140" height="55"/>
  </child>
</child>
```

### Connections (Visual Relationships)

To show a relationship line on a view:

```xml
<child xsi:type="archimate:DiagramObject" id="do-source" archimateElement="elem-001" 
       targetConnections="conn-001">
  <bounds x="20" y="120" width="160" height="80"/>
  <sourceConnection xsi:type="archimate:Connection" id="conn-002" 
                    source="do-source" target="do-target" relationship="rel-001"/>
</child>
<child xsi:type="archimate:DiagramObject" id="do-target" archimateElement="elem-002"
       targetConnections="conn-002">
  <bounds x="220" y="120" width="160" height="80"/>
</child>
```

Key attributes:
- `sourceConnection`: Defines outgoing connection from this element
- `targetConnections`: Space-separated list of incoming connection IDs
- `relationship`: References the relationship element ID
- `source`/`target`: Reference diagram object IDs (not element IDs)

## Complete Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<archimate:model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
                 xmlns:archimate="http://www.archimatetool.com/archimate" 
                 name="Example" id="model-001" version="5.0.0">
  
  <folder name="Application" id="f-app" type="application">
    <element xsi:type="archimate:ApplicationComponent" name="App A" id="app-a"/>
    <element xsi:type="archimate:ApplicationComponent" name="App B" id="app-b"/>
  </folder>
  
  <folder name="Relations" id="f-rel" type="relations">
    <element xsi:type="archimate:ServingRelationship" id="rel-01" source="app-a" target="app-b"/>
  </folder>
  
  <folder name="Views" id="f-views" type="diagrams">
    <element xsi:type="archimate:ArchimateDiagramModel" name="Application View" id="view-01">
      <child xsi:type="archimate:DiagramObject" id="do-a" archimateElement="app-a">
        <bounds x="20" y="60" width="140" height="55"/>
        <sourceConnection xsi:type="archimate:Connection" id="conn-01" 
                          source="do-a" target="do-b" relationship="rel-01"/>
      </child>
      <child xsi:type="archimate:DiagramObject" id="do-b" archimateElement="app-b" 
             targetConnections="conn-01">
        <bounds x="200" y="60" width="140" height="55"/>
      </child>
    </element>
  </folder>
  
  <purpose>Example model</purpose>
</archimate:model>
```

## Common Mistakes to Avoid

1. **Wrong type for groups**: Use `archimate:Group`, NOT `DiagramModelGroup`
2. **Wrong type for view elements**: Use `archimate:DiagramObject`, NOT `DiagramModelNote`
3. **Missing archimateElement**: DiagramObject must reference an element ID
4. **Connection target mismatch**: Connection source/target reference diagram object IDs, not element IDs
5. **Missing targetConnections**: Target elements need `targetConnections` attribute listing incoming connection IDs

## References

- Official Archi models: https://github.com/archimatetool/ArchiModels
- Archi source code: https://github.com/archimatetool/archi
- Open Group Exchange Format (different format): https://www.opengroup.org/xsd/archimate/
