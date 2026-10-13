from unittest.mock import MagicMock, patch

from django.core.management import call_command
from psycopg2 import OperationalError


class TestWaitForDb:
    """Test cases for the wait_for_db management command."""

    @patch("psycopg2.connect")
    def test_wait_for_db_ready(self, mock_connect: MagicMock) -> None:
        """Calls the wait_for_db command when DB is ready."""
        call_command("wait_for_db")
        assert mock_connect.called is True

    @patch("time.sleep", return_value=None)
    @patch("psycopg2.connect")
    def test_wait_for_db_delay(
        self,
        mock_connect: MagicMock,
        mock_sleep: MagicMock,
    ) -> None:
        """Retries connection if DB is initially unavailable."""
        mock_connect.side_effect = [OperationalError] * 5 + [MagicMock()]
        call_command("wait_for_db")
        calls = 6
        assert mock_connect.call_count == calls
