"""Find components with iot_class: "cloud_polling" in their manifest."""

import asyncio
import json
import os


async def find_cloud_polling_components():
    """Find and print components with cloud_polling iot_class."""
    components_dir = os.path.join(
        os.path.dirname(__file__), "homeassistant", "components"
    )
    cloud_polling_components = []

    for component_dir in os.listdir(components_dir):
        component_path = os.path.join(components_dir, component_dir)
        if os.path.isdir(component_path):
            manifest_path = os.path.join(component_path, "manifest.json")
            try:
                with open(manifest_path) as f:
                    manifest = json.load(f)
                if manifest.get("iot_class") == "cloud_polling":
                    # Check if any file in the component directory contains 'auth'
                    has_auth = False
                    has_aiohttp = False
                    has_coordinator = False
                    for root, _, files in os.walk(component_path):
                        for file in files:
                            if file.endswith("coordinator.py"):
                                has_coordinator = True
                            if file.endswith(".py"):
                                file_path = os.path.join(root, file)
                                try:
                                    with open(
                                        file_path, encoding="utf-8"
                                    ) as file_content:
                                        content_lower = file_content.read().lower()
                                        if "authorization" in content_lower:
                                            has_auth = True
                                        if "aiohttp" in content_lower:
                                            has_aiohttp = True
                                except UnicodeDecodeError:
                                    # Skip files that can't be decoded as text
                                    pass

                    if has_auth and has_aiohttp and has_coordinator:
                        cloud_polling_components.append(component_dir)
            except (FileNotFoundError, json.JSONDecodeError):
                # Ignore missing or invalid manifest files
                pass

    print("Cloud Polling Components:")
    # Sort the components alphabetically
    cloud_polling_components.sort()
    for component in cloud_polling_components:
        print(component)


if __name__ == "__main__":
    asyncio.run(find_cloud_polling_components())
