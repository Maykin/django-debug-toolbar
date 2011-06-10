import warnings

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from debug_toolbar.panels import DebugPanel
from django.utils import simplejson

class HeaderDebugPanel(DebugPanel):
    """
    A panel to display HTTP headers.
    """
    name = 'Header'
    title = _('HTTP Headers')
    template = 'debug_toolbar/panels/headers.html'
    has_content = True

    # List of headers we want to display
    header_filter = (
        'CONTENT_TYPE',
        'HTTP_ACCEPT',
        'HTTP_ACCEPT_CHARSET',
        'HTTP_ACCEPT_ENCODING',
        'HTTP_ACCEPT_LANGUAGE',
        'HTTP_CACHE_CONTROL',
        'HTTP_CONNECTION',
        'HTTP_HOST',
        'HTTP_KEEP_ALIVE',
        'HTTP_REFERER',
        'HTTP_USER_AGENT',
        'QUERY_STRING',
        'REMOTE_ADDR',
        'REMOTE_HOST',
        'REQUEST_METHOD',
        'SCRIPT_NAME',
        'SERVER_NAME',
        'SERVER_PORT',
        'SERVER_PROTOCOL',
        'SERVER_SOFTWARE',
    )

    def nav_title(self):
        warnings.warn('Old style use of nav_title method.', DeprecationWarning)
        return _('HTTP Headers')

    def title(self):
        warnings.warn('Old style use of title method.', DeprecationWarning)
        return _('HTTP Headers')

    def url(self):
        warnings.warn('Old style use of url method.', DeprecationWarning)
        return ''

    def process_request(self, request):
        self.headers = dict(
            [(k, request.META[k]) for k in self.header_filter if k in request.META]
        )

    def content(self):
        warnings.warn('Old style use of content method.', DeprecationWarning)
        context = self.context.copy()
        context.update({
            'headers': self.headers
        })
        return render_to_string('debug_toolbar/panels/headers.html', context)        
        
    def get_data(self):
        return self.headers
    