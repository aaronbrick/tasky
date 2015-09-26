# master definition of task class, which is a dict and has no methods.
# "infrastructural" attributes such as can be identified will start with an underscore.

class Task (dict):

 # adopt specified parameters
 # ID is specified by the space, kwargs are passed through
 def __init__(self,id,**kwargs):
  self.update(kwargs)
  self['id'] = id 

  # add dummy entries if base terms are unspecified
  if 'subject' not in self:
   self['subject'] = 'you'
  if 'verb' not in self:
   self['verb'] = 'do'
  if 'object' not in self:
   self['object'] = 'something'

  # at least the stub for some dependencies
  if not 'dependencies' in self:
   self['dependencies'] = set()


