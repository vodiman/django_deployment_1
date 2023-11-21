from django import template

register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts all occurrences of arg from input value string.
    """
    return value.replace(arg,'')

# register with desired template filter name string and name 
# of function as 2nd parm: 
# register.filter('cut',cut)
#
# Or use decorator above(much cleaner)
#