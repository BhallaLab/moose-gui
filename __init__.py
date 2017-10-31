all = [ "plugins", 'suds' ]

# Fixes for QString.
try:
    from PyQt4.QtCore import QString 
except ImportError as e:
    QString = str
