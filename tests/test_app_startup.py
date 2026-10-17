import runpy
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from TheQuantQuotes.quotes_generator import (
    CATEGORY_ALIASES,
    QUOTES_BY_CATEGORY,
    TRADING_QUOTES,
)


class SessionState(SimpleNamespace):
    def __contains__(self, key):
        return hasattr(self, key)


class AppStartupTests(unittest.TestCase):
    def test_startup_initializes_generator_with_categories_and_aliases(self):
        app_dir = Path(__file__).resolve().parents[1] / "TheQuantQuotes"
        streamlit = MagicMock()
        streamlit.session_state = SessionState()
        streamlit.columns.side_effect = lambda spec: [
            MagicMock() for _ in range(spec if isinstance(spec, int) else len(spec))
        ]
        streamlit.button.return_value = False
        integrations = {
            "streamlit": streamlit,
            "streamlit_autorefresh": MagicMock(),
            "arrow": MagicMock(),
            "analytics": MagicMock(),
            "export_quote": MagicMock(),
        }

        with patch.dict(sys.modules, integrations), patch.object(
            sys, "path", [str(app_dir), *sys.path]
        ):
            runpy.run_path(str(app_dir / "main.py"), run_name="__main__")

        generator = streamlit.session_state.generator
        self.assertEqual(generator.categories, sorted(QUOTES_BY_CATEGORY))
        self.assertEqual(generator.quotes, TRADING_QUOTES)
        self.assertIn(streamlit.session_state.current_quote, generator.quotes)
        for alias, category in CATEGORY_ALIASES.items():
            with self.subTest(alias=alias):
                self.assertEqual(
                    generator.get_category_quote(alias, seed=0),
                    generator.get_category_quote(category, seed=0),
                )


if __name__ == "__main__":
    unittest.main()
