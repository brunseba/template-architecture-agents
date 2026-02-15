# Conventional Commits Specification Guide

This guide documents Conventional Commits for standardized commit messages, automated changelog generation, and semantic versioning integration based on the Conventional Commits 1.0.0 specification.

## Commit Message Format

Conventional Commits follow a structured format:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Basic Example

```
feat: add user authentication module
```

### Complete Example

```
feat(auth): add OAuth2 integration

Integrate OAuth2 provider support for Google and GitHub authentication.
This enables users to sign in using their social accounts.

Closes #123
BREAKING CHANGE: Authentication endpoints have changed from /login to /auth/login
```

## Commit Types

### Standard Types

| Type | Description | Semantic Version Impact |
|------|-------------|------------------------|
| `feat` | New feature | MINOR version bump |
| `fix` | Bug fix | PATCH version bump |
| `docs` | Documentation only | No version bump |
| `style` | Code style changes (formatting, whitespace) | No version bump |
| `refactor` | Code refactoring (no functional changes) | No version bump |
| `perf` | Performance improvement | PATCH version bump |
| `test` | Adding or updating tests | No version bump |
| `build` | Build system or dependencies | No version bump |
| `ci` | CI/CD configuration changes | No version bump |
| `chore` | Other changes (tooling, etc.) | No version bump |
| `revert` | Revert a previous commit | Depends on reverted commit |

### Type Examples

#### feat (Feature)

```
feat: add dark mode support
feat(ui): add user profile page
feat(api): implement GraphQL endpoint
```

#### fix (Bug Fix)

```
fix: resolve memory leak in cache
fix(auth): correct token expiration handling
fix(db): prevent SQL injection vulnerability
```

#### docs (Documentation)

```
docs: update API documentation
docs(readme): add installation instructions
docs: fix typo in contributing guide
```

#### style (Code Style)

```
style: format code with prettier
style: remove trailing whitespace
style(components): organize imports alphabetically
```

#### refactor (Code Refactoring)

```
refactor: simplify user validation logic
refactor(auth): extract authentication middleware
refactor: migrate to TypeScript
```

#### perf (Performance)

```
perf: optimize database query performance
perf(images): implement lazy loading
perf: reduce bundle size by 20%
```

#### test (Tests)

```
test: add unit tests for user service
test(integration): add API endpoint tests
test: increase code coverage to 85%
```

#### build (Build System)

```
build: upgrade webpack to v5
build(deps): update dependencies
build: configure production build optimization
```

#### ci (CI/CD)

```
ci: add GitHub Actions workflow
ci(deploy): configure automatic deployments
ci: enable code coverage reporting
```

#### chore (Maintenance)

```
chore: update .gitignore
chore(deps): bump lodash from 4.17.20 to 4.17.21
chore: release version 2.0.0
```

## Scope

Scope provides additional context about the affected part of the codebase:

```
feat(parser): add JSON parsing support
fix(api/users): correct email validation
docs(contributing): update PR guidelines
```

### Common Scopes by Project Type

**Web Application**:
```
feat(auth): ...
fix(ui): ...
perf(api): ...
```

**Library**:
```
feat(core): ...
fix(utils): ...
docs(api): ...
```

**Microservices**:
```
feat(user-service): ...
fix(payment-service): ...
ci(gateway): ...
```

**Monorepo**:
```
feat(frontend/components): ...
fix(backend/api): ...
test(shared/utils): ...
```

## Description

The description is a brief summary of the change:

### Guidelines

- Use imperative, present tense: "add" not "added" or "adds"
- Don't capitalize the first letter
- No period (.) at the end
- Keep it under 50 characters if possible

### Good Examples

```
✓ feat: add password reset functionality
✓ fix: prevent race condition in cache
✓ docs: clarify installation steps
✓ refactor: simplify error handling logic
```

### Bad Examples

```
✗ feat: Added password reset functionality  // Past tense
✗ fix: Prevent race condition in cache     // Capitalized
✗ docs: clarify installation steps.        // Period at end
✗ refactor: Simplified the error handling  // Past tense
```

## Body

The body provides detailed explanation of the change:

```
feat(api): implement pagination for user list

Add pagination support to the user listing API endpoint.
This improves performance when dealing with large user datasets.

The implementation uses cursor-based pagination with the following
query parameters:
- limit: number of items per page (default: 20, max: 100)
- cursor: pagination cursor for next/previous page

API response includes pagination metadata in headers:
- X-Total-Count: total number of items
- X-Next-Cursor: cursor for next page
- X-Prev-Cursor: cursor for previous page
```

### Body Guidelines

- Separate from description with a blank line
- Use to explain "what" and "why", not "how"
- Wrap at 72 characters per line
- Can include multiple paragraphs
- Use bullet points for lists

## Footer

Footers contain metadata about the commit:

### Breaking Changes

Breaking changes must be indicated in the footer (or as `!` after type/scope):

```
BREAKING CHANGE: The authentication API endpoints have changed.

The /login endpoint has been removed. Use /auth/login instead.
All authentication requests now require API version header.

Migration guide: https://docs.example.com/migration/v2
```

Or using the `!` notation:

```
feat!: remove support for Node.js 12

Drop support for Node.js 12 as it has reached end-of-life.
Minimum required version is now Node.js 16.
```

### Issue References

```
Closes #123
Fixes #456
Resolves #789
```

Multiple issues:

```
Closes #123, #456, #789
```

Or separate lines:

```
Closes #123
Closes #456
Relates to #789
```

### Multiple Footers

```
feat(api): add webhook support

Implements webhook delivery system for real-time notifications.

Closes #234
Reviewed-by: Jane Doe <jane@example.com>
Refs: #456
```

## Breaking Changes

Breaking changes trigger a MAJOR version bump:

### Method 1: Footer with BREAKING CHANGE

```
feat(api): change response format

BREAKING CHANGE: API responses now use camelCase instead of snake_case.

Before: { "user_name": "john" }
After:  { "userName": "john" }
```

### Method 2: ! after Type/Scope

```
refactor!: rename configuration file

Configuration file renamed from config.yaml to app.config.yaml
```

### Method 3: Both (Recommended)

```
feat(auth)!: update authentication flow

BREAKING CHANGE: Authentication tokens are no longer stored in localStorage.
Tokens are now stored in httpOnly cookies for improved security.

Migration: Clear existing tokens and require users to re-authenticate.
```

## Complete Examples

### Feature Addition

```
feat(shopping-cart): add item quantity adjustment

Allow users to adjust item quantities directly from the shopping cart
without removing and re-adding items.

Closes #456
```

### Bug Fix

```
fix(payments): prevent duplicate charge processing

Add idempotency key to payment processing to prevent duplicate charges
when users click the submit button multiple times.

The fix implements a request deduplication mechanism using Redis with
a 5-minute expiration window.

Closes #789
Fixes #790
```

### Breaking Change

```
feat(database)!: migrate to PostgreSQL

BREAKING CHANGE: MongoDB support has been removed.

The application now exclusively uses PostgreSQL for data storage.
This change improves query performance and adds support for complex
transactions.

Migration steps:
1. Export data from MongoDB using the provided script
2. Run database migrations: npm run migrate
3. Import data to PostgreSQL: npm run import

See docs/migration-postgres.md for detailed instructions.

Closes #123
```

### Performance Improvement

```
perf(images): implement progressive loading

Implement progressive JPEG loading and WebP format support.
This reduces initial page load time by approximately 40%.

Performance measurements:
- Initial load: 2.1s → 1.2s (-43%)
- First contentful paint: 1.8s → 1.0s (-44%)

Closes #567
```

### Documentation Update

```
docs(api): add authentication examples

Add code examples for OAuth2 and JWT authentication flows.
Includes examples in JavaScript, Python, and Go.

Closes #345
```

### Refactoring

```
refactor(user-service): extract validation logic

Extract user validation logic into separate validator classes
to improve code organization and testability.

No functional changes. Test coverage increased from 72% to 89%.
```

### Revert

```
revert: feat(api): add webhook support

This reverts commit a1b2c3d4e5f6g7h8i9j0.

Reverting due to performance issues in production. Will reintroduce
with optimizations in a future release.

Refs: #678
```

## Integration with Tools

### Commitizen

Interactive CLI for creating commits:

```bash
npm install -g commitizen cz-conventional-changelog

# Initialize in project
commitizen init cz-conventional-changelog --save-dev --save-exact

# Create commit interactively
git cz
```

### Commitlint

Validate commit messages:

```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional

# commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      ['feat', 'fix', 'docs', 'style', 'refactor', 'perf', 'test', 'build', 'ci', 'chore', 'revert']
    ],
    'subject-case': [2, 'never', ['upper-case', 'pascal-case', 'start-case']],
    'subject-max-length': [2, 'always', 50]
  }
};
```

### Husky

Enforce commit message format with git hooks:

```bash
npm install --save-dev husky

# .husky/commit-msg
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npx --no-install commitlint --edit $1
```

### Standard Version

Automate versioning and changelog generation:

```bash
npm install --save-dev standard-version

# package.json
{
  "scripts": {
    "release": "standard-version",
    "release:minor": "standard-version --release-as minor",
    "release:major": "standard-version --release-as major"
  }
}
```

### Semantic Release

Fully automated version management:

```bash
npm install --save-dev semantic-release

# .releaserc.json
{
  "branches": ["main"],
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/changelog",
    "@semantic-release/npm",
    "@semantic-release/git",
    "@semantic-release/github"
  ]
}
```

## Changelog Generation

Conventional Commits enable automatic changelog generation:

### Example CHANGELOG.md

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2023-06-15

### ⚠ BREAKING CHANGES

* **auth:** Authentication endpoints have changed
* Minimum Node.js version is now 16

### Features

* **api:** add webhook support ([a1b2c3d](https://github.com/user/repo/commit/a1b2c3d))
* **auth:** implement OAuth2 authentication ([b2c3d4e](https://github.com/user/repo/commit/b2c3d4e))
* add dark mode support ([c3d4e5f](https://github.com/user/repo/commit/c3d4e5f))

### Bug Fixes

* **payments:** prevent duplicate charges ([d4e5f6g](https://github.com/user/repo/commit/d4e5f6g))
* resolve memory leak in cache ([e5f6g7h](https://github.com/user/repo/commit/e5f6g7h))

### Performance Improvements

* **images:** implement progressive loading ([f6g7h8i](https://github.com/user/repo/commit/f6g7h8i))

## [1.2.1] - 2023-06-01

### Bug Fixes

* **api:** correct response status codes ([g7h8i9j](https://github.com/user/repo/commit/g7h8i9j))
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Validate Commits

on: [pull_request]

jobs:
  commitlint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm install @commitlint/cli @commitlint/config-conventional
      
      - name: Validate commit messages
        run: npx commitlint --from ${{ github.event.pull_request.base.sha }} --to ${{ github.event.pull_request.head.sha }} --verbose
```

### Automated Releases

```yaml
name: Release

on:
  push:
    branches: [main]

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
        run: npx semantic-release
```

## Best Practices

### 1. Atomic Commits

Each commit should represent one logical change:

```
✓ Good:
  feat: add user profile page
  fix: correct email validation

✗ Bad:
  feat: add user profile page and fix email validation
```

### 2. Present Tense

Use imperative mood in descriptions:

```
✓ Good: feat: add support for WebP images
✗ Bad:  feat: added support for WebP images
```

### 3. Lowercase Descriptions

Don't capitalize the first letter:

```
✓ Good: feat: add user authentication
✗ Bad:  feat: Add user authentication
```

### 4. No Periods

Don't end descriptions with a period:

```
✓ Good: feat: add pagination support
✗ Bad:  feat: add pagination support.
```

### 5. Meaningful Scopes

Use clear, consistent scopes:

```
✓ Good: feat(auth): add OAuth2 support
✗ Bad:  feat(stuff): add OAuth2 support
```

### 6. Breaking Changes

Always document breaking changes clearly:

```
✓ Good:
  feat(api)!: change response format
  
  BREAKING CHANGE: API responses now use camelCase.
  Migration guide: https://...

✗ Bad:
  feat(api): change response format
```

### 7. Reference Issues

Link to relevant issues:

```
✓ Good:
  fix(auth): prevent token expiration race condition
  
  Closes #456

✗ Bad:
  fix(auth): prevent token expiration race condition
```

## Common Patterns

### Multi-Repository Changes

When changes span multiple repositories:

```
feat(frontend): add new dashboard widgets

Requires backend changes in user-service repository.
See: https://github.com/org/user-service/pull/789

Closes #456
Related: org/user-service#789
```

### Security Fixes

For security-related fixes:

```
fix(auth): patch authentication bypass vulnerability

Security fix for CVE-2023-12345.
Updated authentication middleware to properly validate
session tokens.

Closes #567
Security: HIGH
```

### Dependency Updates

For dependency updates:

```
build(deps): bump express from 4.17.1 to 4.18.2

Updates Express framework to address security vulnerabilities
and improve performance.

Changelog: https://github.com/expressjs/express/releases/tag/4.18.2
```

### Feature Flags

For feature flag changes:

```
feat(feature-flags): enable dark mode for all users

Remove beta flag for dark mode feature after successful
rollout to 25% of users.

Relates to #345
```

## Common Mistakes

### 1. ❌ Wrong Type

```
✗ feat: fix bug in user service    // Should be "fix"
✓ fix: correct user service error
```

### 2. ❌ Vague Description

```
✗ fix: update code                  // Too vague
✓ fix(auth): prevent null pointer exception in token validation
```

### 3. ❌ Multiple Changes

```
✗ feat: add login page, fix header bug, update docs
✓ Separate into three commits:
  feat(auth): add login page
  fix(ui): correct header alignment
  docs: update authentication guide
```

### 4. ❌ Missing Breaking Change Flag

```
✗ feat(api): change endpoint URLs   // Breaking change not indicated
✓ feat(api)!: change endpoint URLs
  
  BREAKING CHANGE: All API endpoints now use /v2 prefix
```

### 5. ❌ Unclear Scope

```
✗ feat(stuff): add new feature
✓ feat(payments): add PayPal integration
```

## References

- Conventional Commits Specification: https://www.conventionalcommits.org/
- Commitizen: https://github.com/commitizen/cz-cli
- Commitlint: https://github.com/conventional-changelog/commitlint
- Standard Version: https://github.com/conventional-changelog/standard-version
- Semantic Release: https://github.com/semantic-release/semantic-release
- Angular Commit Guidelines: https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit
