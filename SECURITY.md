# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅        |
| < 1.0   | ❌        |

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please report it responsibly.

### How to Report

**Do NOT** open a public issue for security vulnerabilities.

Instead, please send an email to: gribanov.0812@gmail.com

The email should include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if available)

### What to Expect

- You will receive an acknowledgment within 48 hours
- We will assess the severity and determine a timeline
- We will work with you to understand and fix the issue
- A fix will be released as soon as possible
- Credit will be given in the release notes

## Security Best Practices

### For Users

1. **Never commit secrets**: Do not commit credentials, API keys, or sensitive data to the repository
2. **Use environment variables**: Store sensitive data in environment variables or GitHub Secrets
3. **Rotate credentials regularly**: Regularly rotate Docker Hub tokens and API keys
4. **Enable MFA**: Enable Multi-Factor Authentication for your GitHub and Docker Hub accounts
5. **Review dependencies**: Regularly review and update dependencies for security patches
6. **Monitor pipeline runs**: Review CI/CD pipeline runs for suspicious activity
7. **Keep updated**: Regularly update Python, Docker, and dependencies

### For Deployment

1. **Use GitHub Secrets**: Store sensitive data in GitHub Secrets, not in code
2. **Enable branch protection**: Protect main branch and require PR reviews
4. **Scan images**: Always scan Docker images before deployment
5. **Use non-root containers**: Run containers as non-root user
6. **Minimal base images**: Use minimal base images to reduce attack surface
7. **Limit permissions**: Grant minimum necessary permissions to CI/CD tokens

### For CI/CD Pipeline

1. **Secrets management**: Use GitHub Secrets for sensitive data
2. **Branch protection**: Require PR reviews before merging to main
3. **Security scanning**: Scan for vulnerabilities in every build
4. **Dependency scanning**: Check for vulnerable dependencies
5. **Code signing**: Sign Docker images with Docker Content Trust
6. **Audit logging**: Enable audit logging for CI/CD actions
7. **Access control**: Limit who can trigger deployments

## Dependency Management

### Python Dependencies

This project uses pinned dependencies in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Updates

Regularly update dependencies for security patches:

```bash
pip list --outdated
pip install --upgrade <package>
```

### Dependency Scanning

Use tools to scan for vulnerable dependencies:

```bash
# Safety
pip install safety
safety check

# Pip-audit
pip install pip-audit
pip-audit
```

## Known Security Considerations

### Current Limitations

1. **No authentication**: The current version does not implement authentication. Anyone can access the API.
2. **No rate limiting**: API endpoints are not rate-limited, making them vulnerable to abuse.
3. **No input sanitization**: While Pydantic provides validation, additional sanitization may be needed.
4. **No database**: No database integration, data is stored in memory only.
5. **No encryption**: No TLS/SSL encryption for API communications.
6. **No audit logging**: No logging of API access or modifications.

### Recommendations for Production

1. **Add authentication**: Implement OAuth2, JWT, or API key authentication
2. **Add rate limiting**: Implement rate limiting to prevent abuse
3. **Enable HTTPS**: Use TLS/SSL encryption for all API communications
4. **Add database**: Implement persistent storage with PostgreSQL or similar
5. **Add audit logging**: Log all API access and modifications
6. **Implement CORS**: Configure CORS properly for production
7. **Add monitoring**: Implement APM and monitoring (Datadog, New Relic, etc.)
8. **Add WAF**: Use Web Application Firewall for protection
9. **Secrets management**: Use AWS Secrets Manager or HashiCorp Vault
10. **Enable content trust**: Use Docker Content Trust for image verification

## Security Features

### Implemented

- ✅ Non-root Docker user
- ✅ Minimal Docker base image (python:3.11-slim)
- ✅ Security scanning with Trivy
- ✅ Dependency pinning
- ✅ Health checks
- ✅ GitHub Secrets for sensitive data
- ✅ Code quality checks with flake8
- ✅ Automated testing
- ✅ Code coverage reporting

### Planned

- ⏳ OAuth2 authentication
- ⏳ JWT token authentication
- ⏳ API rate limiting
- ⏳ Input validation and sanitization
- ⏳ HTTPS/TLS support
- ⏳ PostgreSQL integration
- ⏳ Audit logging
- ⏳ API key authentication
- ⏳ Security headers middleware
- ⏳ CORS configuration
- ⏳ OWASP Top 10 compliance
- ⏳ Secret rotation
- ⏳ Dependency scanning in CI/CD
- ⏳ Docker Content Trust
- ⏳ Kubernetes network policies

## Docker Security Best Practices

### Image Security

1. **Use minimal base images**: Use `python:3.11-slim` instead of full images
2. **Run as non-root**: Run containers as non-root user
3. **Scan images**: Scan images for vulnerabilities before deployment
4. **Update regularly**: Regularly update base images and dependencies
5. **Don't run as root**: Never run containers as root user
6. **Use specific tags**: Use specific image tags instead of `latest`

### Container Security

1. **Read-only filesystem**: Mount filesystem as read-only where possible
2. **Drop capabilities**: Drop unnecessary Linux capabilities
3. **Resource limits**: Set CPU and memory limits
4. **Network isolation**: Use Docker networks for isolation
5. **No privileged mode**: Never run in privileged mode
6. **User namespaces**: Use user namespaces for isolation

### Docker Compose Security

1. **Use secrets**: Use Docker secrets for sensitive data
2. **Network isolation**: Use separate networks for different services
3. **Volume permissions**: Set proper permissions on volumes
4. **Environment variables**: Use environment variables for configuration
5. **Health checks**: Implement health checks for all services

## CI/CD Security Best Practices

### GitHub Actions Security

1. **Use GitHub Secrets**: Never hardcode secrets in workflows
2. **Branch protection**: Protect main branch and require reviews
3. **Required checks**: Require status checks before merging
4. **Token permissions**: Use minimum necessary token permissions
5. **Third-party actions**: Review and pin third-party actions
6. **Self-hosted runners**: Use self-hosted runners for sensitive operations
7. **Audit logging**: Enable audit logging for GitHub Actions

### Pipeline Security

1. **Security scanning**: Scan for vulnerabilities in every build
2. **Dependency scanning**: Check for vulnerable dependencies
3. **SAST**: Static Application Security Testing
4. **DAST**: Dynamic Application Security Testing
5. **Image signing**: Sign Docker images with Docker Content Trust
6. **Environment separation**: Separate staging and production environments
7. **Manual approval**: Require manual approval for production deployments

## API Security Best Practices

### Authentication & Authorization

1. **Implement authentication**: Use OAuth2, JWT, or API keys
2. **Authorization**: Implement proper authorization checks
3. **Session management**: Manage sessions securely
4. **Token expiration**: Set appropriate token expiration times
5. **Refresh tokens**: Implement token refresh mechanism
6. **Multi-factor**: Consider MFA for sensitive operations

### Input Validation

1. **Validate all inputs**: Validate all user inputs
2. **Sanitize data**: Sanitize data to prevent injection attacks
3. **Type checking**: Use type hints and Pydantic for validation
4. **Length limits**: Set appropriate length limits on inputs
5. **Whitelist validation**: Use whitelist validation where possible
6. **Error messages**: Don't expose sensitive information in error messages

### API Security

1. **HTTPS only**: Enforce HTTPS in production
2. **CORS**: Configure CORS properly
3. **Rate limiting**: Implement rate limiting
4. **Security headers**: Add security headers (HSTS, X-Frame-Options, etc.)
5. **API versioning**: Implement API versioning
6. **Documentation**: Document security requirements

## Security Scanning

### Recommended Tools

- **Trivy**: Security scanner for containers and filesystems
  ```bash
  trivy image devops-api:latest
  ```

- **Safety**: Python dependency vulnerability scanner
  ```bash
  safety check
  ```

- **Pip-audit**: Python package vulnerability scanner
  ```bash
  pip-audit
  ```

- **Bandit**: Python security linter
  ```bash
  bandit -r app/
  ```

- **Snyk**: Vulnerability scanner for dependencies and containers
  ```bash
  snyk test
  ```

### Pre-commit Hooks

Consider adding pre-commit hooks for security scanning:

```yaml
repos:
  - repo: https://github.com/PyCQA/bandit
    hooks:
      - id: bandit
        args: ['-r', 'app/']
  - repo: https://github.com/psf/bugbear
    hooks:
      - id: flake8-bugbear
```

## Compliance

### OWASP Top 10

Consider implementing OWASP Top 10 controls:

- **A01:2021 - Broken Access Control**: Implement proper authentication and authorization
- **A02:2021 - Cryptographic Failures**: Use encryption for sensitive data
- **A03:2021 - Injection**: Implement input validation and sanitization
- **A04:2021 - Insecure Design**: Implement secure design patterns
- **A05:2021 - Security Misconfiguration**: Review and harden configurations
- **A06:2021 - Vulnerable Components**: Regularly update dependencies
- **A07:2021 - Authentication Failures**: Implement proper authentication
- **A08:2021 - Software and Data Integrity**: Use code signing and verification
- **A09:2021 - Security Logging**: Implement audit logging
- **A10:2021 - Server-Side Request Forgery**: Validate and sanitize all URLs

## Contact

For security-related questions or concerns:
- Email: gribanov.0812@gmail.com
- GitHub: https://github.com/juw3x/ci-cd-pipeline

## References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [GitHub Actions Security](https://docs.github.com/en/actions/security-guides)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [Python Security](https://docs.python.org/3/library/security_warnings.html)
