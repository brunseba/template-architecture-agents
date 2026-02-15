# Semantic Versioning (SemVer) Specification Guide

This guide documents Semantic Versioning for version numbering, release management, and dependency management based on the SemVer 2.0.0 specification.

## Version Format Overview

Semantic Versioning uses a three-part version number format:

```
MAJOR.MINOR.PATCH
```

Example: `2.4.7`

- **MAJOR** version (`2`): Incompatible API changes
- **MINOR** version (`4`): Backward-compatible functionality additions
- **PATCH** version (`7`): Backward-compatible bug fixes

## Core Principles

### Version Number Structure

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]
```

Components:
1. **MAJOR**: Breaking changes that require consumer updates
2. **MINOR**: New features that maintain backward compatibility
3. **PATCH**: Bug fixes that maintain backward compatibility
4. **PRERELEASE** (optional): Pre-release version identifier
5. **BUILD** (optional): Build metadata

### Version `0.y.z` - Initial Development

```
0.1.0  // Initial development
0.2.0  // Added features during development
0.2.1  // Bug fixes during development
```

- Version `0.y.z` indicates initial development
- Anything may change at any time
- Public API should not be considered stable
- Version `1.0.0` defines the first stable public API

### Version `1.0.0` and Beyond

```
1.0.0  // First stable release
1.0.1  // Patch: bug fixes only
1.1.0  // Minor: new features added
2.0.0  // Major: breaking changes
```

Once you release `1.0.0`, version increments follow strict rules.

## Incrementing Rules

### PATCH Version (Z in x.y.Z)

Increment when you make backward-compatible bug fixes:

```
1.2.3 → 1.2.4  // Fixed null pointer exception
1.2.4 → 1.2.5  // Fixed calculation error
```

**Examples**:
- Internal bug fixes
- Performance improvements that don't change behavior
- Documentation corrections
- Security patches (non-breaking)

### MINOR Version (Y in x.Y.z)

Increment when you add backward-compatible functionality:

```
1.2.5 → 1.3.0  // Added new API endpoint
1.3.0 → 1.4.0  // Added optional configuration parameter
```

**Must reset PATCH to 0**

**Examples**:
- New features or capabilities
- New public API methods
- Substantial new functionality in private code
- Deprecating functionality (but not removing it)
- Optional new parameters with defaults

### MAJOR Version (X in X.y.z)

Increment when you make incompatible API changes:

```
1.4.0 → 2.0.0  // Removed deprecated API
2.0.0 → 3.0.0  // Changed function signature
```

**Must reset MINOR and PATCH to 0**

**Examples**:
- Removing public APIs
- Changing method signatures
- Renaming public classes or methods
- Changing behavior of existing features
- Removing deprecated features
- Major refactoring affecting public API

## Pre-release Versions

Pre-release versions are denoted by appending a hyphen and identifiers:

```
1.0.0-alpha
1.0.0-alpha.1
1.0.0-beta
1.0.0-beta.2
1.0.0-rc.1
1.0.0
```

### Pre-release Format

```
MAJOR.MINOR.PATCH-PRERELEASE
```

**Rules**:
- Pre-release identifiers are separated by dots
- Identifiers must comprise only ASCII alphanumerics and hyphens `[0-9A-Za-z-]`
- Numeric identifiers must not include leading zeroes
- Pre-release versions have lower precedence than normal versions

### Common Pre-release Identifiers

| Identifier | Meaning | Example |
|------------|---------|---------|
| `alpha` | Alpha release (feature incomplete) | `1.0.0-alpha` |
| `alpha.N` | Alpha release number N | `1.0.0-alpha.1` |
| `beta` | Beta release (feature complete, unstable) | `1.0.0-beta` |
| `beta.N` | Beta release number N | `1.0.0-beta.2` |
| `rc` | Release candidate | `1.0.0-rc.1` |
| `rc.N` | Release candidate number N | `1.0.0-rc.2` |

### Pre-release Progression

Typical progression toward a release:

```
1.0.0-alpha.1
1.0.0-alpha.2
1.0.0-beta.1
1.0.0-beta.2
1.0.0-rc.1
1.0.0-rc.2
1.0.0
```

## Build Metadata

Build metadata is denoted by appending a plus sign and identifiers:

```
1.0.0+20230615
1.0.0+sha.5114f85
1.0.0-beta.1+exp.sha.5114f85
```

### Build Metadata Format

```
MAJOR.MINOR.PATCH[+BUILD]
MAJOR.MINOR.PATCH-PRERELEASE[+BUILD]
```

**Rules**:
- Build metadata identifiers are separated by dots
- Identifiers must comprise only ASCII alphanumerics and hyphens `[0-9A-Za-z-]`
- Build metadata should be ignored when determining version precedence
- Two versions that differ only in build metadata have the same precedence

**Examples**:
```
1.0.0+20230615142530
1.0.0+build.123
1.0.0+sha.abc123
1.0.0+20230615.sha.abc123
```

## Version Precedence

Versions are compared from left to right:

1. Compare MAJOR, MINOR, PATCH numerically
2. Pre-release version has lower precedence than normal version
3. Compare pre-release identifiers from left to right
4. Numeric identifiers are compared numerically
5. Alphanumeric identifiers are compared lexically
6. Larger set of pre-release fields has higher precedence

### Precedence Examples

```
1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0
```

Detailed comparison:
```
1.0.0 < 2.0.0 < 2.1.0 < 2.1.1
1.0.0-alpha < 1.0.0
1.0.0-alpha < 1.0.0-alpha.1
1.0.0-alpha.1 < 1.0.0-alpha.beta
1.0.0-alpha.beta < 1.0.0-beta
1.0.0-beta.2 < 1.0.0-beta.11
1.0.0-rc.1 < 1.0.0
```

## Practical Examples

### Library Development Lifecycle

```
0.1.0   Initial development
0.2.0   Added authentication module
0.2.1   Fixed bug in authentication
0.3.0   Added logging functionality
1.0.0   First stable release
1.0.1   Fixed memory leak
1.1.0   Added caching feature
1.1.1   Fixed cache invalidation bug
1.2.0   Added metrics collection
2.0.0   Removed deprecated authentication methods
2.0.1   Fixed metrics reporting bug
2.1.0   Added OAuth2 support
```

### API Versioning Example

```
// Version 1.0.0
public class UserService {
    public User getUser(int id) { ... }
    public void createUser(User user) { ... }
}

// Version 1.1.0 - Added feature (backward compatible)
public class UserService {
    public User getUser(int id) { ... }
    public void createUser(User user) { ... }
    public List<User> searchUsers(String query) { ... }  // NEW
}

// Version 1.2.0 - Added optional parameter (backward compatible)
public class UserService {
    public User getUser(int id) { ... }
    public User getUser(int id, boolean includeDeleted) { ... }  // NEW overload
    public void createUser(User user) { ... }
    public List<User> searchUsers(String query) { ... }
}

// Version 2.0.0 - Breaking change
public class UserService {
    public User getUser(String uuid) { ... }  // CHANGED: int → String
    public void createUser(User user) { ... }
    public List<User> searchUsers(String query) { ... }
}
```

### NPM Package Example

```json
{
  "name": "my-library",
  "version": "1.2.3",
  "dependencies": {
    "express": "^4.18.0",      // Compatible with 4.18.0, < 5.0.0
    "lodash": "~4.17.21",      // Compatible with 4.17.x
    "moment": "2.29.4"         // Exactly 2.29.4
  }
}
```

### Python Package Example

```python
# setup.py
setup(
    name="my-package",
    version="2.1.0",
    install_requires=[
        "requests>=2.28.0,<3.0.0",  # SemVer range
        "click~=8.1.0",              # Compatible release
        "pydantic>=2.0.0",           # Minimum version
    ],
)
```

## Version Range Specifications

### NPM/JavaScript Syntax

| Range | Matches | Description |
|-------|---------|-------------|
| `1.2.3` | `1.2.3` | Exact version |
| `^1.2.3` | `>=1.2.3 <2.0.0` | Compatible with version |
| `~1.2.3` | `>=1.2.3 <1.3.0` | Approximately equivalent |
| `>1.2.3` | `>1.2.3` | Greater than |
| `>=1.2.3` | `>=1.2.3` | Greater than or equal |
| `<2.0.0` | `<2.0.0` | Less than |
| `1.2.x` | `>=1.2.0 <1.3.0` | Wildcard |
| `*` | `>=0.0.0` | Any version |

### Python Syntax

| Range | Matches | Description |
|-------|---------|-------------|
| `==1.2.3` | `1.2.3` | Exact version |
| `>=1.2.3` | `>=1.2.3` | Greater than or equal |
| `~=1.2.3` | `>=1.2.3 <1.3.0` | Compatible release |
| `>=1.2.0,<2.0.0` | `>=1.2.0 <2.0.0` | Range |

### Maven/Gradle Syntax

```xml
<!-- Exact version -->
<version>1.2.3</version>

<!-- Version range -->
<version>[1.2.0,2.0.0)</version>

<!-- Minimum version -->
<version>[1.2.0,)</version>
```

## Best Practices

### 1. Start with 0.1.0

```
0.1.0  // First development version, not 0.0.1
```

### 2. Release 1.0.0 When API is Stable

Only release `1.0.0` when:
- Public API is defined and documented
- API is being used in production
- You commit to maintaining backward compatibility

### 3. Document Breaking Changes

```
# CHANGELOG.md

## [2.0.0] - 2023-06-15
### BREAKING CHANGES
- Removed deprecated `getUser()` method
- Changed `User.id` from integer to string (UUID)
- Minimum Node.js version is now 18.x
```

### 4. Use Pre-release for Unstable Versions

```
2.0.0-alpha.1  // Testing new features
2.0.0-beta.1   // Feature complete, testing
2.0.0-rc.1     // Release candidate
2.0.0          // Stable release
```

### 5. Deprecate Before Removing

```
// Version 1.5.0 - Deprecate
@Deprecated("Use getUser(String uuid) instead")
public User getUser(int id) { ... }

public User getUser(String uuid) { ... }  // New method

// Version 2.0.0 - Remove deprecated
public User getUser(String uuid) { ... }  // Only new method
```

### 6. Maintain Changelog

Keep a `CHANGELOG.md` file following these principles:
- Guiding Principles: Changelogs are for humans, not machines
- Types of changes: Added, Changed, Deprecated, Removed, Fixed, Security
- Link to version comparison

### 7. Tag Releases in Git

```bash
# Tag release
git tag -a v1.2.3 -m "Release version 1.2.3"
git push origin v1.2.3

# Tag pre-release
git tag -a v2.0.0-rc.1 -m "Release candidate 1 for version 2.0.0"
git push origin v2.0.0-rc.1
```

### 8. Automate Version Bumping

```bash
# Using npm
npm version patch  # 1.2.3 → 1.2.4
npm version minor  # 1.2.4 → 1.3.0
npm version major  # 1.3.0 → 2.0.0

# Using Python semantic-release
semantic-release version
```

## Common Mistakes to Avoid

### 1. ❌ Incrementing Multiple Version Parts

```
❌ 1.2.3 → 1.3.4  // Wrong: incremented both minor and patch
✓  1.2.3 → 1.3.0  // Correct: reset patch to 0
```

### 2. ❌ Using Leading Zeros

```
❌ 1.02.3         // Wrong: leading zero in minor
❌ 1.2.03         // Wrong: leading zero in patch
✓  1.2.3          // Correct
```

### 3. ❌ Breaking Changes in Minor/Patch

```
❌ 1.2.3 → 1.2.4  // Changed method signature (breaking!)
✓  1.2.3 → 2.0.0  // Breaking change requires major bump
```

### 4. ❌ Adding Features in Patch

```
❌ 1.2.3 → 1.2.4  // Added new API endpoint
✓  1.2.3 → 1.3.0  // New features require minor bump
```

### 5. ❌ Mixing Pre-release Formats

```
❌ 1.0.0-alpha → 1.0.0-BETA  // Inconsistent capitalization
✓  1.0.0-alpha → 1.0.0-beta  // Consistent lowercase
```

### 6. ❌ Skipping 1.0.0

```
❌ 0.9.9 → 2.0.0  // Skipped 1.0.0
✓  0.9.9 → 1.0.0  // First stable release
```

## Integration with CI/CD

### GitHub Actions Example

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Extract version from tag
        id: version
        run: echo "VERSION=${GITHUB_REF#refs/tags/v}" >> $GITHUB_OUTPUT
      
      - name: Validate SemVer
        run: |
          if [[ ! "${{ steps.version.outputs.VERSION }}" =~ ^[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?$ ]]; then
            echo "Invalid SemVer format"
            exit 1
          fi
      
      - name: Create Release
        uses: actions/create-release@v1
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ steps.version.outputs.VERSION }}
```

### Automated Version Bumping

```yaml
- name: Bump version
  id: bump
  run: |
    if [[ "${{ github.event.head_commit.message }}" == *"BREAKING CHANGE"* ]]; then
      npm version major
    elif [[ "${{ github.event.head_commit.message }}" == feat:* ]]; then
      npm version minor
    else
      npm version patch
    fi
```

## Tools and Libraries

### Version Validation

**JavaScript**
```javascript
const semver = require('semver');

semver.valid('1.2.3');          // '1.2.3'
semver.valid('a.b.c');          // null
semver.gt('1.2.3', '1.2.2');    // true
semver.satisfies('1.2.3', '^1.2.0'); // true
```

**Python**
```python
from packaging import version

v1 = version.parse("1.2.3")
v2 = version.parse("1.2.4")
v1 < v2  # True
```

**Go**
```go
import "github.com/Masterminds/semver/v3"

v, err := semver.NewVersion("1.2.3")
constraint, _ := semver.NewConstraint(">= 1.2.0, < 2.0.0")
constraint.Check(v) // true
```

### Version Management Tools

| Tool | Language | Purpose |
|------|----------|---------|
| `npm version` | JavaScript | Bump package version |
| `semantic-release` | Multiple | Automated versioning |
| `standard-version` | JavaScript | Changelog and version management |
| `bump2version` | Python | Version bumping utility |
| `commitizen` | Multiple | Commit message formatter |

## FAQ

### When should I release 1.0.0?

When your software is being used in production and you're ready to commit to a stable public API.

### What if I accidentally release a breaking change as a minor version?

Release a new version that restores compatibility and reverts the breaking change, then release the breaking change as a new major version.

### How do I handle security fixes?

- Non-breaking security fixes: PATCH version
- Breaking security fixes: MAJOR version (with clear communication)

### Can I use four-part version numbers?

No, SemVer strictly defines three parts plus optional pre-release and build metadata. Use build metadata for additional versioning needs: `1.2.3+build.4`

### Should I version my internal services?

Yes, even internal services benefit from semantic versioning for tracking changes and managing dependencies.

## References

- Semantic Versioning Specification: https://semver.org/
- Keep a Changelog: https://keepachangelog.com/
- Conventional Commits: https://www.conventionalcommits.org/
- npm semver Calculator: https://semver.npmjs.com/
- Semantic Versioning Cheatsheet: https://devhints.io/semver
