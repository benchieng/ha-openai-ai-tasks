"""Constants for the Custom OpenAI AI Tasks integration."""

DOMAIN = "custom_openai_ai_tasks"

# The config entry schema version this release understands. Bump it alongside
# ConfigFlow.VERSION whenever the stored entry shape changes, and give
# async_migrate_entry a branch for the previous version.
CONFIG_ENTRY_VERSION = 2

# Repair issue IDs (suffixed with the entry ID, so two entries can each raise
# their own issue).
ISSUE_MIGRATION_DOWNGRADE = "migrate_downgrade"
ISSUE_MIGRATION_INCOMPLETE = "migrate_incomplete_config"
# Same problem as ISSUE_MIGRATION_INCOMPLETE, but raised on Home Assistant
# versions without config_entries.async_retry_migration, where we cannot offer
# a Fix button - an entry in the migration_error state is non-recoverable, so
# async_reload refuses to touch it and only a restart re-runs the migration.
ISSUE_MIGRATION_INCOMPLETE_RESTART = "migrate_incomplete_config_restart"

# Configuration keys
CONF_ENDPOINT = "endpoint"
CONF_API_KEY = "api_key"
CONF_CHAT_MODEL = "chat_model"
CONF_IMAGE_MODEL = "image_model"

# This integration talks to any OpenAI-compatible /v1 server (OpenAI itself,
# local engines such as llama.cpp/Ollama-family servers, proxies, ...). The
# user provides the server URL (with or without a trailing /v1); the model is
# always carried in the request body and auth is a Bearer token.

# Default values
DEFAULT_NAME = "Custom OpenAI AI Tasks"
DEFAULT_CHAT_MODEL = "gpt-4o"
DEFAULT_IMAGE_MODEL = "dall-e-3"

# Available models (free-text in the config flow; this list is only a hint)
CHAT_MODELS = [
    "gpt-4",
    "gpt-4-32k", 
    "gpt-4-turbo",
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-5",
    "gpt-5-mini"
]

# Available image generation models
IMAGE_MODELS = [
    "dall-e-2",
    "dall-e-3",
    "gpt-image-1"
]