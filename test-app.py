#!/usr/bin/env python3
import os
import hvac

def main():
    # In a real application, you'd get these from Vault
    vault_url = os.environ.get('VAULT_ADDR')
    vault_token = os.environ.get('VAULT_TOKEN')

    if not vault_url or not vault_token:
        print("Missing Vault configuration")
        return

    client = hvac.Client(url=vault_url, token=vault_token)

    # Read secrets
    try:
        db_secret = client.secrets.kv.v2.read_secret_version(path='github/database')
        api_secret = client.secrets.kv.v2.read_secret_version(path='github/api')

        print("✅ Successfully connected to database")
        print("✅ Successfully authenticated with API")

    except Exception as e:
        print(f"❌ Error accessing secrets: {e}")

if __name__ == "__main__":
    main()