"""
Holds all service level configurations
"""
from pydantic import BaseSettings


class Metadata(BaseSettings):
    """
    Return the application's metadata info
    """

    title = "dummy_users"
    description = (
        "Service to fetch the list of dummy users from 3rd party downstream services"
    )
    version = "1.1.3"
    contact = {
        "name": "Ashwin Hegde",
        "url": "https://github.com/hegdeashwin",
        "email": "ashwin.hegde3@gmail.com",
    }

    def get_service_title(self):
        """
        Return title
        """
        return self.title

    def get_service_description(self):
        """
        Return description
        """
        return self.description

    def get_service_release_version(self):
        """
        Return version
        """
        return self.version

    def get_service_contact(self):
        """
        Return contact
        """
        return self.contact

    def get_hostname(self):
        """
        Return machine hostname
        """
        return "127.0.0.1"

    def get_port(self):
        """
        Return application server port. This should be unique
        amoung all the microservice exist for beaver.
        """
        return 8000

    def is_debug_mode(self):
        """
        Return debug model
        """
        return True

    def get_metadata(self):
        """
        Return metadata object
        """
        return {
            "title": self.title,
            "description": self.description,
            "version": self.version,
            "contact": self.contact,
            "hostname": self.get_hostname(),
            "port": self.get_port(),
        }
