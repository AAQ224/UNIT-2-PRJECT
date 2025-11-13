# history/context_processors.py
from .data import ERAS

def eras_nav(request):
    return {"ERAS_NAV": ERAS}
