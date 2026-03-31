from settings import Settings


def test_settings_load_correct_values():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "mlops-lab1-test"
    assert settings.SECRET_API_KEY == "6345246357345"
