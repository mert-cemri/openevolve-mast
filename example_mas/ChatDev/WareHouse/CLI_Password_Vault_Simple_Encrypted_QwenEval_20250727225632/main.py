'''
Main entry point for the Password Vault application.
This file initializes the PasswordVault and VaultCLI classes and starts the application.
'''
from password_vault import PasswordVault
from vault_cli import VaultCLI
def main():
    vault = PasswordVault()
    cli = VaultCLI(vault)
    cli.start()
if __name__ == "__main__":
    main()