"""
Contains service level configurations and metadata retrieval methods.
"""

from typing import ClassVar

from pydantic_settings import BaseSettings


class Metadata(BaseSettings):
    """
    Represents metadata for the application.
    """

    # Metadata properties
    title: ClassVar[str] = "dummy_users"
    description: ClassVar[str] = (
        "Service to fetch the list of dummy users from 3rd party downstream services"
    )
    version: ClassVar[str] = "1.1.6"
    contact: ClassVar[dict] = {
        "name": "Ashwin Hegde",
        "url": "https://github.com/hegdeashwin",
        "email": "ashwin.hegde3@gmail.com",
    }

    def get_service_title(self):
        """
        Retrieves the title of the service.
        """
        return self.title

    def get_service_description(self):
        """
        Retrieves the description of the service.
        """
        return self.description

    def get_service_release_version(self):
        """
        Retrieves the release version of the service.
        """
        return self.version

    def get_service_contact(self):
        """
        Retrieves the contact information of the service.
        """
        return self.contact

    def get_hostname(self):
        """
        Retrieves the machine hostname.
        """
        return "127.0.0.1"

    def get_port(self):
        """
        Retrieves the application server port.

        This port should be unique among all microservices existing for beaver.
        """
        return 3000

    def is_debug_mode(self):
        """
        Determines if the service is in debug mode.
        """
        return True

    def get_metadata(self):
        """
        Retrieves the metadata object of the service.
        """
        return {
            "title": self.title,
            "description": self.description,
            "version": self.version,
            "contact": self.contact,
            "hostname": self.get_hostname(),
            "port": self.get_port(),
        }
