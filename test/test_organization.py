from src.core.models.organization_model import OrganizationModel

from src.core.services.settings_manager import SettingsManager

test_dict = {
    "inn": "123456789012",
    "account": "40702810123",
    "correspondent_account": "38104000000",
    "bic": "044525225",
    "name": "Hello world",
    "type_of_ownership": "hello"
}


def test_organization_creation_from_settings():
    settings_manager = SettingsManager(settings_dict=test_dict)
    settings = settings_manager.settings
    organization = OrganizationModel(settings)

    assert organization.inn == settings.inn
    assert organization.bic == settings.bic
    assert organization.account == settings.account
    assert organization.org_type == settings.type_of_ownership
