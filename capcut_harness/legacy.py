"""Private file/JSON adapter; no Codex dependency."""
import sys
from pathlib import Path

SCRIPTS=Path(__file__).parent/'cards_backend'
if str(SCRIPTS) not in sys.path:sys.path.insert(0,str(SCRIPTS))
import cards
