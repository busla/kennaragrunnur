from selectable.base import ModelLookup
from selectable.registry import registry
from teachers.models import JobTitle, Marriage, Teacher


class JobTitleLookup(ModelLookup):
    model = JobTitle
    search_fields = 'name__icontains'

    def get_item_value(self, item):
        # Display for currently selected item
        return item.name
    def get_item_label(self, item): # Display for choice listings 
        return u"%s (%s)" % (item.name, item.id)

class MarriageLookup(ModelLookup):
    model = Marriage
    search_fields = 'marriage_status__icontains'

    def get_item_value(self, item):
        # Display for currently selected item
        return item.marriage_status
    def get_item_label(self, item): # Display for choice listings 
        return u"%s (%s)" % (item.marriage_status, item.id)

class GenderLookup(ModelLookup):
    model = Teacher
    search_fields = 'gender__icontains'

    def get_item_value(self, item):
        # Display for currently selected item
        return item.gender
    def get_item_label(self, item): # Display for choice listings 
        return u"%s (%s)" % (item.gender, item.id)
            
registry.register(JobTitleLookup)
registry.register(MarriageLookup)
registry.register(GenderLookup)