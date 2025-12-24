# Changelog

All notable changes will be documented in this file following [Keep a Changelog](https://keepachangelog.com/) and [SemVer](https://semver.org/).

## [0.6.0] - 2025-12-24
### Added
- `token_type` configuration for authz clients to send `id_token` or `session_token` payloads.
- README guidance on token type selection and remote authz configuration.

### Changed
- Authz client requests now POST JSON payloads to `/authz` and `/authz/check` to match the server API.
- FastAPI flow documentation clarifies ID token usage and response codes.

## [0.5.0] - 2024-05-01
### Added
- FastAPI, Flask, and Django helpers built on the shared HTTP client.
- Token discovery utilities plus permission decorators.
- Initial test suite and FastAPI sample application.

## [0.4.0] - 2024-04-15
### Added
- Async + sync GoogleAuthz clients for service-to-service calls.
- Config class that loads environment variables and builds clients.

## [0.3.0] - 2024-03-10
### Added
- Foundational HTTP client and EffectiveAuth models used across frameworks.

[0.6.0]: https://github.com/example/google-authz-client/releases/tag/v0.6.0
[0.5.0]: https://github.com/example/google-authz-client/releases/tag/v0.5.0
[0.4.0]: https://github.com/example/google-authz-client/releases/tag/v0.4.0
[0.3.0]: https://github.com/example/google-authz-client/releases/tag/v0.3.0
