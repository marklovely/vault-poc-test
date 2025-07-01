# Vault POC Test Repository

This repository tests HashiCorp Vault integration with GitHub Actions using OIDC JWT authentication.

## Setup

1. Configure Vault JWT authentication for this repository
2. Update the `VAULT_ADDR` in the GitHub Actions workflow
3. Push changes or manually trigger the workflow

## Test Secrets

- `secret/github/database` - Contains database password
- `secret/github/api` - Contains API key

## Workflow Features

- ✅ OIDC JWT token generation
- ✅ Vault authentication
- ✅ Secret retrieval
- ✅ Error handling and debugging