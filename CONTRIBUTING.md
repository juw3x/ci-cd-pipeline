# Contributing to CI/CD Pipeline

Thank you for your interest in contributing to this CI/CD Pipeline project! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)

## 🤝 Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

## 🚀 How to Contribute

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Description**: A clear and concise description of the problem
- **Python Version**: `python --version`
- **Docker Version**: `docker --version`
- **Steps to Reproduce**: Detailed steps to reproduce the behavior
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Error Messages**: Full error output
- **Logs**: Relevant logs from Docker or CI/CD

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:

- **Use Case**: Describe the use case for the enhancement
- **Proposed Solution**: Describe how you envision the solution
- **Alternatives**: Describe any alternative solutions you've considered
- **Additional Context**: Any other context, diagrams, or examples

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes locally
5. Commit your changes (`git commit -m 'feat: add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 🛠️ Development Setup

### Prerequisites

- Python 3.11+
- Docker 20.10+
- Docker Compose 2.0+
- Git
- GitHub account
- Docker Hub account (for CI/CD)

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/juw3x/ci-cd-pipeline.git
cd ci-cd-pipeline
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

5. Run tests:
```bash
pytest tests/ -v
```

### Docker Development

1. Build and run with Docker Compose:
```bash
docker-compose up api
```

2. Run tests with Docker:
```bash
docker-compose up api-test
```

3. Stop containers:
```bash
docker-compose down
```

### Making Changes

- Make your changes in the appropriate files
- Test your changes locally
- Run linter: `flake8 app/`
- Run tests: `pytest tests/ -v`
- Update documentation if needed
- Commit with a clear message

## 📝 Pull Request Process

### PR Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guide
- [ ] `flake8` passes without errors
- [ ] `pytest` passes with all tests
- [ ] Code coverage is maintained or improved
- [ ] Documentation is updated
- [ ] Commit messages are clear and descriptive
- [ ] PR description explains the changes
- [ ] No sensitive information is included

### PR Title Format

Use clear and descriptive titles:

- `feat: add OAuth2 authentication`
- `fix: resolve Docker build cache issue`
- `docs: update CI/CD pipeline documentation`
- `refactor: improve API response structure`

### Commit Message Format

Follow conventional commits:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes

Example:
```
feat(api): add rate limiting middleware

- Implement rate limiting with slowapi
- Add configurable rate limits
- Include documentation for configuration
```

## 🎨 Coding Standards

### Python Code

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Write testable code
- Use type hints where appropriate

### FastAPI Best Practices

- Use Pydantic models for request/response validation
- Implement proper error handling
- Use async/await for I/O operations
- Add API documentation with docstrings
- Implement proper HTTP status codes

### Docker Best Practices

- Use minimal base images (python:3.11-slim)
- Run as non-root user
- Use multi-stage builds
- Optimize layer caching
- Health checks for containers
- Do not run as root

### GitHub Actions

- Use descriptive job names
- Cache dependencies for faster builds
- Use matrix strategy for testing across versions
- Fail fast on critical errors
- Use environment variables for configuration

## 🧪 Testing

### Running Tests Locally

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=app --cov-report=html

# Run specific test
pytest tests/test_main.py::test_read_root

# Run with verbose output
pytest tests/ -vv
```

### Code Quality

```bash
# Lint code
flake8 app/

# Format code (if using black)
black app/

# Type checking (if using mypy)
mypy app/
```

### Docker Testing

```bash
# Build image
docker build -t devops-api:latest .

# Run container
docker run -d -p 8000:8000 devops-api:latest

# Test health endpoint
curl http://localhost:8000/health

# Run tests in container
docker-compose up api-test
```

### Manual Testing Checklist

- [ ] Application starts successfully
- [ ] All API endpoints work correctly
- [ ] Error handling works as expected
- [ ] Health check endpoint responds
- [ ] Docker image builds successfully
- [ ] Tests pass locally
- [ ] Linter passes without errors
- [ ] Code coverage is maintained

## 📚 Documentation

### README Updates

- Update feature lists when adding new features
- Update installation instructions for new dependencies
- Update CI/CD pipeline configuration
- Keep architecture diagrams current

### Code Comments

- Add comments for complex logic
- Explain why (not just what)
- Keep comments up to date with code changes
- Use inline comments for tricky sections

### API Documentation

If adding API endpoints:
- Document endpoint URL and method
- Document request/response format
- Include example requests
- Document error responses
- Add examples to Swagger UI

## 🐛 Bug Fix Template

```markdown
**Issue**: [Link to issue]

**Changes**:
- Description of changes made
- Files modified
- Python version used

**Testing**:
- How the fix was tested
- Test results
- Coverage impact

**Screenshots** (if applicable):
- API response examples
- CI/CD pipeline logs
```

## ✨ Feature Template

```markdown
**Feature**: [Brief description]

**Motivation**:
- Why this feature is needed
- What problem it solves
- Use cases

**Implementation**:
- How it was implemented
- Technical decisions made
- Dependencies added

**Testing**:
- How the feature was tested
- Test coverage
- CI/CD impact

**Documentation**:
- Links to updated documentation
- API examples
```

## 📧 Getting Help

If you need help contributing:

- Open an issue with the `question` label
- Check existing issues for similar questions
- Refer to the project documentation
- Check FastAPI documentation
- Check GitHub Actions documentation

## 🎉 Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project README

Thank you for contributing to CI/CD Pipeline! 🙌
