from dynaconf import Dynaconf

# Initialize Dynaconf settings
settings = Dynaconf(
    # Define where to look for the settings files
    settings_files=["settings.toml", ".secrets.toml"],
    # Define the environments, default is 'development'
    environments=True,
    envvar_prefix="SPT",  # Environment variables prefix SPT_FOO=bar
    # Custom settings can be defined here as well
    # Example: default values if not provided in files or env vars
    defaults={"default_value": "This is a default value"},
    # Optionally, you can set the environment explicitly
    # environment='production'
)


# Custom function to validate or manipulate settings if needed
def configure_settings():
    # Example: Validate certain settings
    # if not settings.get('IMPORTANT_KEY'):
    #     raise ValueError("IMPORTANT_KEY is not set in the settings")

    # Perform other custom configuration or checks
    pass


# Call the configure function to perform any additional setup
configure_settings()

# Now, settings can be imported from this config module elsewhere in your project
