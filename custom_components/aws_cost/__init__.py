"""The AWS Cost integration."""
from __future__ import annotations
import logging

from homeassistant.helpers.discovery import load_platform
from .aws_cost import AWSCostExplorer

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    """Set up the AWS Cost component."""
    hass.data[DOMAIN] = {}
    ## conferir
    #hass.data.setdefault(DOMAIN, {})
    return True

async def async_setup_entry(hass, config_entry):
    """Set up AWS Cost from a config entry."""
    
    aws_access_key_id = config_entry.data["aws_access_key_id"]
    aws_secret_key = config_entry.data["aws_secret_access_key"]
    region_name = config_entry.data["region_name"]
    
    client = AWSCostExplorer(aws_access_key_id, aws_secret_key, region_name)

    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(config_entry, "sensor")
    )

    return True

async def async_unload_entry(hass, config_entry):
    """Unload a config entry."""
    await hass.config_entries.async_forward_entry_unload(
        config_entry, "sensor"
    )

    return True