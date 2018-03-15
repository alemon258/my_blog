import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

#自定义filter时必须加上
register = template.Library()

#注册template filter
@register.filter(is_safe=True)

#希望字符串作为参数
@stringfilter
def custom_markdown(value):
	return mark_safe(markdown.markdown(value, 
		extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'], 
		safe_mode=True,
		enable_attributes=False))
