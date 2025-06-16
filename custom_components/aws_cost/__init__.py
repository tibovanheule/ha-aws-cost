"""The AWS Cost integration."""

from __future__ import annotations
import logging

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass, config):
    """Set up the AWS Cost component."""
    hass.data[DOMAIN] = {}
    return True


async def async_setup_entry(hass, config_entry):
    """Set up AWS Cost from a config entry."""

    await hass.config_entries.async_forward_entry_setups(config_entry, [DOMAIN])

    return True


async def async_unload_entry(hass, config_entry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(config_entry, "sensor")

    return True
