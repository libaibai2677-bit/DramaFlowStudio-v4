# DramaFlow Studio v4 - Pexels Provider

import requests
from typing import List, Dict, Any

PEXELS_API_URL = "https://api.pexels.com/v1/search"


class PexelsProvider:
    """
    Simple Pexels image provider.
    MVP version for Image Search Engine v4.
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.api_key = self._get_api_key()

    def _get_api_key(self) -> str:
        # Try config first
        key = (
            self.config.get("providers", {})
            .get("pexels", {})
            .get("api_key", "")
        )
        return key

    def search(self, query: str, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Search images from Pexels API.
        """

        if not self.api_key:
            return [
                {
                    "title": "Missing API Key",
                    "url": "",
                    "thumbnail": "",
                    "source": "pexels",
                    "error": "No API key provided in config.providers.pexels.api_key"
                }
            ]

        headers = {
            "Authorization": self.api_key
        }

        params = {
            "query": query,
            "per_page": limit
        }

        try:
            response = requests.get(PEXELS_API_URL, headers=headers, params=params, timeout=10)
            data = response.json()

            results = []

            for item in data.get("photos", []):
                results.append({
                    "title": item.get("alt", ""),
                    "url": item.get("src", {}).get("original", ""),
                    "thumbnail": item.get("src", {}).get("medium", ""),
                    "source": "pexels"
                })

            return results

        except Exception as e:
            return [
                {
                    "title": "Request Failed",
                    "url": "",
                    "thumbnail": "",
                    "source": "pexels",
                    "error": str(e)
                }
            ]
