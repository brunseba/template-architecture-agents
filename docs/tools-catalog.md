# Tools Catalog

**Version**: 1.1.0  
**Last Updated**: 2026-02-15  
**Git Commit**: ad4712a  
**Status**: Active

## 1. Diagram and Visualization Tools

### 1.1 Mermaid
**Repository**: [mermaid-js/mermaid](https://github.com/mermaid-js/mermaid.git)  
**Extension**: `.mmd`  
**Scope**: Diagram generation

Mermaid is a JavaScript-based diagramming and charting tool that renders Markdown-inspired text definitions to create and modify diagrams dynamically. It enables developers to create flowcharts, sequence diagrams, Gantt charts, class diagrams, state diagrams, and more using simple text-based syntax. This tool is particularly valuable for architecture documentation as diagrams are version-controlled as code, making them easy to maintain and review alongside other project artifacts.

**Key Features**:
- Text-to-diagram conversion
- Wide range of diagram types (flowcharts, sequence, ER, Gantt, etc.)
- Integration with documentation platforms (MkDocs, GitBook, Confluence)
- Live preview and rendering in modern browsers
- Extensive theming and styling options

### 1.2 Draw.io (diagrams.net)
**Repository**: [jgraph/drawio](https://github.com/jgraph/drawio.git)  
**Extension**: `.drawio`  
**Scope**: Diagram creation

Draw.io is a free, open-source diagramming application that provides a rich visual editor for creating professional diagrams. It supports a comprehensive library of shapes for network diagrams, UML, BPMN, cloud architecture, and more. The tool can be used online or as a desktop application, with files stored locally or in cloud storage services.

**Key Features**:
- Extensive shape libraries (AWS, Azure, GCP, Kubernetes, etc.)
- Vector graphics export (SVG, PDF, PNG)
- Real-time collaboration capabilities
- Integration with cloud storage (Google Drive, OneDrive, Dropbox)
- Custom shape and template creation

### 1.3 AWS Diagram as Code
**Repository**: [awslabs/diagram-as-code](https://github.com/awslabs/diagram-as-code.git)  
**Extension**: `.yaml`  
**Scope**: AWS architecture diagrams

AWS Diagram as Code is a tool from AWS Labs that enables creating AWS architecture diagrams using YAML definitions. It provides a declarative approach to generating professional AWS architecture diagrams programmatically, making it easy to version control, review, and automate diagram generation as part of CI/CD pipelines.

**Key Features**:
- YAML-based diagram definitions
- Official AWS architecture icons
- Programmatic diagram generation
- CI/CD integration capabilities
- Consistent diagram styling
- Infrastructure documentation as code

### 1.4 Draw.io MCP Server
**Repository**: [jgraph/drawio-mcp](https://github.com/jgraph/drawio-mcp.git)  
**Extension**: `.drawio`  
**Scope**: Schema design, Model Context Protocol

The Draw.io MCP server extends Draw.io functionality to support the Model Context Protocol, enabling AI-assisted diagram creation and manipulation. This tool bridges the gap between AI language models and visual diagram creation, allowing for programmatic diagram generation based on natural language descriptions or structured data schemas.

**Key Features**:
- MCP protocol integration
- AI-driven diagram generation
- Schema-to-diagram conversion
- Automated layout and positioning
- API-based diagram manipulation

## 2. Architecture Modeling Tools

### 2.1 Archi - ArchiMate Modeling Tool
**Repository**: [archimatetool/archi](https://github.com/archimatetool/archi.git)  
**Extension**: `.archimate`  
**Scope**: Enterprise architecture modeling

Archi is an open-source modeling toolkit for creating ArchiMate models and sketches. ArchiMate is an open and independent enterprise architecture modeling language that supports the description, analysis, and visualization of architecture across business domains. Archi provides a user-friendly interface for modeling complex enterprise architectures with support for multiple viewpoints and stakeholder concerns.

**Key Features**:
- Full ArchiMate 3.2 specification support
- Multiple views and perspectives
- HTML report generation
- Model exchange format support
- Extensible through plugins
- Collaboration features via model repository

### 2.2 The Open Group Standards
**Repository**: [The Open Group Publications](https://publications.opengroup.org/standards)  
**Scope**: Architecture modeling standards

The Open Group maintains and publishes industry standards including TOGAF (The Open Group Architecture Framework) and ArchiMate. These standards provide frameworks, methodologies, and best practices for enterprise architecture. The standards define common vocabulary, principles, and guidelines that enable consistent architecture development and communication across organizations.

**Key Standards**:
- TOGAF: Comprehensive EA framework
- ArchiMate: EA modeling language
- IT4IT: IT management framework
- O-PAS: Process automation standard
- Open Agile Architecture: Agile EA approach

## 3. Requirements and Product Definition

### 3.1 GitHub Spec Kit
**Repository**: [github/spec-kit](https://github.com/github/spec-kit.git)  
**Scope**: Product scenarios and specifications

Spec Kit is GitHub's internal framework for writing product specifications and user scenarios. It provides templates, guidelines, and best practices for documenting product requirements, user stories, and technical specifications. This toolkit helps teams create clear, consistent, and actionable product documentation that bridges the gap between product management, design, and engineering.

**Key Features**:
- Structured specification templates
- User scenario frameworks
- Acceptance criteria guidelines
- Collaboration workflows
- Version-controlled documentation approach

## 4. Methodology and Frameworks

### 4.1 BMAD Method
**Repository**: [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD.git)  
**Scope**: AI-driven development methodology

The BMAD Method (Business Model AI-Driven) represents a modern approach to software development that integrates AI capabilities into the development lifecycle. This methodology provides frameworks and practices for leveraging AI tools in architecture design, code generation, testing, and deployment processes while maintaining control, quality, and architectural integrity.

**Key Components**:
- AI-assisted architecture design
- Agent-driven development workflows
- Quality assurance frameworks
- Human-AI collaboration patterns
- Governance and control mechanisms

### 4.2 Azure Well-Architected Reliability Assessment
**Repository**: [Azure/Well-Architected-Reliability-Assessment](https://github.com/Azure/Well-Architected-Reliability-Assessment.git)  
**Scope**: Reliability assessment framework

Microsoft's Well-Architected Framework provides a reliability assessment tool for evaluating cloud architectures against best practices. This assessment framework helps teams identify reliability risks, gaps, and improvement opportunities in their Azure deployments. It covers availability, resilience, disaster recovery, and operational excellence dimensions.

**Key Areas**:
- Availability and uptime analysis
- Disaster recovery planning
- Resilience patterns evaluation
- Monitoring and alerting assessment
- Operational procedures review

## 5. Model Context Protocol (MCP) Tools

### 5.1 AWS Labs MCP
**Repository**: [awslabs/mcp](https://github.com/awslabs/mcp.git)  
**Scope**: MCP implementation for AWS services

AWS Labs' MCP implementation provides Model Context Protocol integration for AWS services. This enables AI agents to interact with AWS infrastructure, query service states, and perform operations through a standardized protocol. It bridges AI language models with AWS APIs, CloudFormation, and infrastructure management tools.

**Key Features**:
- AWS service integration
- Infrastructure-as-code support
- CloudFormation template generation
- Resource discovery and querying
- Cost optimization insights

### 5.2 CucumberStudio MCP
**Repository**: [HeroSizy/cucumberstudio-mcp](https://github.com/HeroSizy/cucumberstudio-mcp.git)  
**Scope**: MCP for testing and BDD

CucumberStudio MCP server connects AI agents with behavior-driven development (BDD) testing workflows. It enables AI-assisted test scenario generation, Gherkin syntax validation, and test case management. This tool streamlines the creation of executable specifications and automated tests using natural language descriptions.

**Key Features**:
- Gherkin scenario generation
- Test case management integration
- BDD workflow automation
- Natural language to test conversion
- Test coverage analysis

## 6. Testing and Quality Assurance

### 6.1 Gherkin Documentation
**Reference**: [Cucumber Gherkin Docs](https://cucumber.io/docs/gherkin/)  
**Scope**: Testing syntax and BDD

Gherkin is a domain-specific language for writing executable specifications in a human-readable format. It uses a structured syntax (Given-When-Then) to describe software behavior without detailing implementation. Gherkin scenarios serve as both documentation and automated tests, ensuring that software behavior matches business requirements.

**Key Concepts**:
- Feature files and scenarios
- Given-When-Then syntax
- Scenario outlines and examples
- Tags and organization
- Step definition binding
- Living documentation approach

## 7. Research and Discovery

### 7.1 Semantic Scholar
**Platform**: [Semantic Scholar](https://www.semanticscholar.org/)  
**Scope**: AI-powered academic search

Semantic Scholar is a free, AI-powered research tool for scientific literature developed by the Allen Institute for AI. It uses machine learning to understand the semantics of research papers, helping users discover relevant publications, track citations, and explore research trends. This tool is particularly valuable for staying current with academic research in AI, architecture patterns, and emerging technologies.

**Key Features**:
- Semantic paper search
- Citation graph exploration
- Research trend analysis
- Paper recommendations
- PDF access and reading tools
- Research feed customization

## 8. Development Tools and Extensions

### 8.1 VS Code Extension Samples
**Repository**: [microsoft/vscode-extension-samples](https://github.com/microsoft/vscode-extension-samples.git)  
**Scope**: VS Code plugin development

Microsoft's official collection of sample extensions for Visual Studio Code provides working examples of various extension capabilities. These samples demonstrate API usage, best practices, and patterns for extending VS Code functionality. This resource is essential for developing custom tooling, language support, or workflow automation within the VS Code ecosystem.

**Sample Categories**:
- Language features (IntelliSense, diagnostics)
- Debugging and task providers
- Webview and UI extensions
- Source control integration
- Custom commands and menus
- Settings and configuration

## 9. Kubernetes and Container Orchestration

### 9.1 Kubernetes Operator Pattern
**Documentation**: [Kubernetes Operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)  
**Scope**: Kubernetes extension pattern

The Operator pattern is a Kubernetes extension mechanism that uses custom controllers to automate the management of complex, stateful applications. Operators encode operational knowledge about an application's lifecycle, including deployment, scaling, backup, recovery, and upgrades. This pattern extends Kubernetes' declarative API to manage custom resources beyond standard workloads.

**Key Concepts**:
- Custom Resource Definitions (CRDs)
- Controller reconciliation loops
- Operator SDK frameworks
- Operator Lifecycle Manager (OLM)
- Best practices and patterns
- State management and observability

### 9.2 Kubernetes API
**Repository**: [kubernetes/api](https://github.com/kubernetes/api.git)  
**Scope**: Kubernetes API definitions

The Kubernetes API repository contains the canonical definitions of Kubernetes API objects. These definitions include all resource types (Pods, Deployments, Services, etc.) and their schemas. Understanding the API structure is essential for developing controllers, operators, custom tooling, and infrastructure automation that interacts with Kubernetes clusters.

**Key Components**:
- Core API definitions
- API versioning and evolution
- OpenAPI specifications
- Go type definitions
- API conventions and patterns
- Backward compatibility guarantees

## 10. Data Standards and Schemas

### 10.1 JSON Schema
**Specification**: [JSON Schema](https://json-schema.org/)  
**Scope**: JSON data validation

JSON Schema is a vocabulary that allows you to annotate and validate JSON documents. It provides a contract for JSON data, describing the structure, constraints, and validation rules. JSON Schema is widely used for API documentation, configuration validation, and data exchange formats, ensuring data integrity and providing clear documentation of expected data structures.

**Key Features**:
- Schema validation
- Type definitions and constraints
- Schema composition ($ref, allOf, anyOf)
- Documentation and examples
- Format validation
- Extensibility and custom keywords

## 11. Data Management and Governance

### 11.1 DataHub
**Platform**: [DataHub](https://datahub.com/)  
**Scope**: Data catalog and management

DataHub is an open-source metadata platform that provides data discovery, governance, and observability capabilities. It creates a comprehensive catalog of data assets across an organization, enabling teams to discover, understand, and trust their data. DataHub supports lineage tracking, quality monitoring, and access control for data assets.

**Key Features**:
- Metadata ingestion from multiple sources
- Data lineage visualization
- Search and discovery
- Data governance workflows
- Schema evolution tracking
- Data quality monitoring

### 11.2 OpenMetadata
**Platform**: [OpenMetadata](https://open-metadata.org/)  
**Scope**: Metadata management

OpenMetadata is an open-source metadata platform for data discovery, governance, and collaboration. It provides a centralized repository for metadata across databases, data warehouses, dashboards, pipelines, and ML models. OpenMetadata emphasizes data quality, lineage, and collaboration features to build trust in data assets.

**Key Features**:
- Unified metadata repository
- Automated metadata extraction
- Data lineage and impact analysis
- Collaborative annotations and documentation
- Data quality rules and monitoring
- Role-based access control

## 12. Versioning and Release Management

### 12.1 Semantic Versioning (SemVer)
**Specification**: [SemVer](https://semver.org/)  
**Scope**: Version numbering standard

Semantic Versioning is a versioning scheme that uses a three-part version number (MAJOR.MINOR.PATCH) to communicate the nature of changes in software releases. This standard helps developers and users understand the impact of upgrading to a new version and ensures backward compatibility expectations are clearly communicated.

**Version Format**:
- MAJOR: Incompatible API changes
- MINOR: Backward-compatible functionality additions
- PATCH: Backward-compatible bug fixes
- Pre-release and build metadata tags
- Version precedence rules

### 12.2 Conventional Commits
**Specification**: [Conventional Commits](https://www.conventionalcommits.org/)  
**Scope**: Commit message standard

Conventional Commits is a specification for commit messages that provides a standardized format for describing changes. This convention enables automated changelog generation, semantic versioning, and clear communication of change intent. It structures commit messages with types (feat, fix, docs, etc.), optional scopes, and breaking change indicators.

**Commit Format**:
- Type: feat, fix, docs, style, refactor, test, chore
- Scope: Optional context identifier
- Description: Brief change summary
- Body: Detailed explanation
- Footer: Breaking changes and issue references
- Automated tooling integration

---

## Usage and Integration

These tools collectively support a comprehensive architecture and development workflow:

1. **Design Phase**: Use Mermaid, Draw.io, and Archi for creating architecture diagrams and models
2. **Requirements**: Apply Spec Kit and Gherkin for defining product scenarios and acceptance criteria
3. **Development**: Leverage MCP tools, VS Code extensions, and Kubernetes APIs for implementation
4. **Quality**: Employ testing frameworks, JSON Schema validation, and BDD approaches
5. **Data Management**: Utilize DataHub and OpenMetadata for data governance
6. **Release**: Follow SemVer and Conventional Commits for version control and changelog generation
7. **Research**: Use Semantic Scholar for staying current with industry developments

## Recommended Tool Combinations

- **Cloud Architecture Documentation**: Mermaid + Draw.io + AWS Diagram as Code + Azure Well-Architected Framework
- **Enterprise Architecture**: Archi + The Open Group Standards + OpenMetadata
- **AI-Driven Development**: BMAD Method + MCP tools + VS Code Extensions
- **Testing Strategy**: Gherkin + CucumberStudio MCP + Conventional Commits
- **Kubernetes Platform Engineering**: Kubernetes Operator + Kubernetes API + DataHub
- **API Development**: JSON Schema + OpenMetadata + Semantic Versioning
