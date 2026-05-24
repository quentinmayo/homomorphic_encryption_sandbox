$ErrorActionPreference = "Stop"

git config core.hooksPath .githooks
git update-index --add --chmod=+x .githooks/pre-commit .githooks/pre-push

Write-Host "Configured git hooks path to .githooks"
Write-Host "Enabled executable bit for pre-commit and pre-push hooks"
