from django import template

register = template.Library()

@register.simple_tag
def urlencodedurl(*args, **kwargs):
    # url_tag:URLNode = url(parser, token)
    #
    # url_tag.render = lambda context: "xxx"
    return "xxxx"