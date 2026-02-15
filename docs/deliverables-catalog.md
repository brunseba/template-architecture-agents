# Deliverables Catalog

**Version**: 1.0.0  
**Last Updated**: 2026-02-15  
**Status**: Active

## Overview

This catalog documents all deliverables generated or maintained by the architecture template system. Each deliverable is linked to source inputs and categorized by purpose.

---

## 1. Architecture Templates

### 1.1 Draw.io OpenGroup Template
**ID**: `drawio-opengroup`  
**Format**: `.drawio`  
**Source**: [OpenGroup Standards](uri.csv#opengroup)

A comprehensive Draw.io template with multiple sheets designed for enterprise architecture design based on OpenGroup architecture standards. Includes pre-configured layers for business, application, data, and technology architecture views.

**Sheets Included**:
- Context Diagram
- Business Architecture Canvas
- Application Portfolio View
- Data Flow Diagrams
- Technology Reference Model
- Integration Architecture

### 1.2 Excel OpenGroup Template
**ID**: `xlsx-opengroup`  
**Format**: `.xlsx`  
**Source**: [OpenGroup Standards](uri.csv#opengroup)

An Excel workbook with multiple sheets facilitating requirements management and architecture documentation aligned with OpenGroup architecture standards.

**Sheets Included**:
- Use Cases
- Functionnal Requirements
- Non Functional Requirements
- Requirements Traceability Matrix
- Stakeholder Analysis
- Capability Assessment
- Risk Register
- Architecture Decision Log

### 1.3 Mermaid Templates
**ID**: `mermaid-templates`  
**Format**: `.mmd`  
**Source**: [Mermaid](uri.csv#mermaid)

Architecture diagram templates in Mermaid syntax for creating version-controlled diagrams. Supports flowcharts, sequence diagrams, and C4 model representations.

**Template Types**:
- System Context Diagram (C4)
- Container Diagram (C4)
- Component Diagram (C4)
- Sequence Diagrams
- State Machines
- Entity Relationship Diagrams

### 1.4 ArchiMate Templates
**ID**: `archi-templates`  
**Format**: `.archimate`  
**Source**: [Archi](uri.csv#archi)

ArchiMate model templates for enterprise architecture modeling following the ArchiMate 3.2 specification.

**Viewpoints Included**:
- Organization Viewpoint
- Business Process Viewpoint
- Application Usage Viewpoint
- Technology Viewpoint
- Layered Viewpoint

### 1.5 AWS Diagrams as Code
**ID**: `aws-diagrams`  
**Format**: `.yaml`  
**Source**: [AWS Diagram as Code](uri.csv#aws-diagram-as-code)

AWS architecture diagrams defined in YAML for programmatic generation. Enables infrastructure documentation as code with official AWS icons.

**Diagram Types**:
- VPC Architecture
- Serverless Patterns
- Container Orchestration
- Data Pipeline Architecture
- Multi-Region Deployment

---

## 2. Testing & BDD

### 2.1 Gherkin Templates
**ID**: `gherkin-templates`  
**Format**: `.feature`  
**Source**: [Gherkin Docs](uri.csv#gherkin)

Gherkin feature file templates for behavior-driven development testing scenarios. Provides structured templates for writing executable specifications.

**Template Categories**:
- User Authentication Scenarios
- API Endpoint Testing
- Data Validation Rules
- Integration Test Scenarios
- Performance Acceptance Criteria

### 2.2 Test Scenarios Catalog
**ID**: `test-scenarios`  
**Format**: `.md`  
**Source**: [Spec Kit](uri.csv#spec-kit)

Product test scenarios catalog based on GitHub's Spec Kit methodology. Documents acceptance criteria and test cases for product features.

**Sections**:
- Feature Specifications
- User Story Acceptance Criteria
- Edge Case Documentation
- Regression Test Inventory

---

## 3. Documentation

### 3.1 Tools Catalog
**ID**: `tools-catalog`  
**Format**: `.md`  
**Source**: [uri.csv](uri.csv)

Generated tools catalog documentation compiled from URI references. Provides comprehensive descriptions of all tools, frameworks, and standards used in the architecture template system.

**Output**: `docs/tools-catalog.md`

### 3.2 API Schemas
**ID**: `api-schemas`  
**Format**: `.json`  
**Source**: [JSON Schema](uri.csv#json-schema)

JSON Schema definitions for API validation and documentation. Provides reusable schema components for common data structures.

**Schema Types**:
- Request/Response Schemas
- Configuration File Schemas
- Event Payload Schemas
- Metadata Schemas

---

## 4. Data Management

### 4.1 DataHub Configuration
**ID**: `datahub-config`  
**Format**: `.yaml`  
**Source**: [DataHub](uri.csv#datahub)

DataHub metadata configuration templates for setting up data catalog and lineage tracking.

**Configuration Files**:
- Ingestion Recipes
- Metadata Policies
- Access Control Rules
- Lineage Configuration

### 4.2 OpenMetadata Configuration
**ID**: `openmetadata-config`  
**Format**: `.yaml`  
**Source**: [OpenMetadata](uri.csv#openmetadata)

OpenMetadata setup templates for metadata management and data discovery.

**Configuration Files**:
- Connector Configurations
- Quality Rules
- Glossary Templates
- Tag Taxonomies

---

## 5. DevOps & Kubernetes

### 5.1 Kubernetes Operator Templates
**ID**: `k8s-operator-templates`  
**Format**: `.yaml`  
**Source**: [Kubernetes Operator](uri.csv#k8s-operator)

Kubernetes operator scaffolding with Custom Resource Definitions (CRDs) for extending Kubernetes capabilities.

**Templates Include**:
- CRD Definitions
- Controller Scaffolding
- RBAC Configuration
- OLM Catalog Entries
- Helm Chart Templates

### 5.2 Conventional Commit Configuration
**ID**: `conventional-commit-config`  
**Format**: `.yaml`  
**Source**: [Conventional Commits](uri.csv#conventional-commits)

Pre-commit hooks and changelog configuration for maintaining conventional commit standards.

**Configuration Files**:
- `.pre-commit-config.yaml`
- `commitlint.config.js`
- Changelog generation rules
- GitHub Actions workflow

---

## Usage

### Generating Deliverables

```bash
# Track a deliverable generation
track track inputs/deliverables.csv docs/deliverables-catalog.md -d "Deliverables catalog"

# Validate tracking
track validate

# Check synchronization
track sync
```

### Deliverable Categories Summary

| Category | Count | Formats |
|----------|-------|---------|
| Architecture | 5 | drawio, xlsx, mmd, archimate, yaml |
| Testing | 2 | feature, md |
| Documentation | 2 | md, json |
| Data Management | 2 | yaml |
| DevOps | 2 | yaml |

---

## Version History

- **1.0.0** (2026-02-15): Initial catalog with 13 deliverables
