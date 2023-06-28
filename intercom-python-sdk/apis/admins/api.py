from uplink import Consumer, get, returns

# Self-imports
from .schemas import AdminSchema, TeamPriorityLevelSchema

class AdminsAPI(Consumer):
    URI = "/admins"

    @returns(AdminSchema(many=False)) # type: ignore
    @get(f"{URI}/me")
    def me(self):
        """ Get the current admin user. """
        

