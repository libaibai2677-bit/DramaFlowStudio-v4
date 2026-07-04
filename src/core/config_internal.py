# ⚙️ Core Configuration (Stabilized Internal System)

class Config:
    """
    Minimal configuration for internal AI platform.
    No SaaS, no billing, no multi-tenant complexity.
    """

    APP_NAME = "DramaFlow Studio v4"
    ENV = "internal"

    # AI settings
    DEFAULT_INTENT = "general"

    # Database
    DB_PATH = "dramaflow.db"

    # Logging
    LOG_LEVEL = "INFO"

    # Feature flags (internal control only)
    ENABLE_LEGACY_FALLBACK = False
