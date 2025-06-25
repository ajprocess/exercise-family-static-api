"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_number": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_number": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_number": [1]
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    

    def add_member(self, member):
        # fill this method and update the return
        if member["id"] == None:
            member["id"] = self._generateId()

        member["last_name"] = self.last_name
        self._members.append(member)
        
        return member


    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return member
            return None

    def get_member(self, id):
        # fill this method and update the return
        member = list(filter(lambda member: member["id"] == id, self._members))
        if len(member) > 0:
            return member[0]
        return None

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members