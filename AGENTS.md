# AGENTS.md - Blender CorteCloud Export Extension

## Build/Lint/Test Commands
- **Validate extension**: `blender --command extension validate`
- **Build extension**: `blender --command extension build`
- **Lint**: `ruff check .` (via VSCode extension)
- **Format**: `ruff format .`
- **Run single test**: No test framework; manually test in Blender by loading extension and running operators

## Code Style Guidelines

### Imports
- Multi-line imports on single line: `import bpy, os, re`
- Group standard library, then third-party, then local imports

### Formatting
- 4-space indentation
- No trailing whitespace
- Line length: flexible, no strict limit

### Types
- No type hints required (not used in codebase)

### Naming Conventions
- **Classes**: PascalCase (`EdgeTapes`, `WoodenPiece`)
- **Functions**: snake_case (`configure_environment`, `export_to_csv`)
- **Variables**: snake_case (`unit_settings`, `material_names`)
- **Constants**: UPPER_CASE (`func_options`)
- **Blender operators**: `OBJECT_OT_` prefix for IDs

### Error Handling
- Minimal error handling; assume operations succeed
- Use `try/except` only for critical operations

### Comments & Documentation
- Portuguese comments preferred (matches existing codebase)
- Docstrings: minimal, only for complex functions
- Inline comments for complex logic

### String Formatting
- Prefer f-strings: `f"{quantity};{width};{height}"`
- Use descriptive variable names in templates

### Blender-Specific Patterns
- Register/unregister classes in `register()`/`unregister()` functions
- Use `bpy.props` for custom properties
- Follow Blender naming conventions for operators and panels

## Code Principles
- **Conventional Commits**: Always use conventional commits as the standard for commit messages (e.g., `feat: add new feature`, `fix: resolve bug`).
- **DRY (Don't Repeat Yourself)**: Avoid code duplication; reuse code where possible.
- **KISS (Keep It Simple, Stupid)**: Keep code simple and straightforward.
- **YAGNI (You Aren't Gonna Need It)**: Do not add functionality until it is necessary.