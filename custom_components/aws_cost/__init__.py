"""The AWS Cost integration."""

from __future__ import annotations
import logging

from .const import DOMAIN
from homeassistant.const import   Platform
_LOGGER = logging.getLogger(__name__)


PLATFORMS: list[Platform] = [
    Platform.SENSOR
]

async def async_setup_entry(hass, config_entry):
    """Set up AWS Cost from a config entry."""
    
    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)

    return True

async def async_unload_entry(
    hass: HomeAssistant,
    entry: IntegrationBlueprintConfigEntry,
) -> bool:
    """Handle removal of an entry."""
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)


async def async_reload_entry(
    hass: HomeAssistant,
    entry: IntegrationBlueprintConfigEntry,
) -> None:
    """Reload config entry."""
    await hass.config_entries.async_reload(entry.entry_id)
