import unittest
from unittest.mock import patch
from io import StringIO

class TestFetchData(unittest.TestCase):
    @patch('builtins.print', side_effect=lambda *args, **kwargs: None)
    def test_fetch_data(self, mock_print):
        # Mock the get_teams function
        mock_teams = [
            {'id': 1, 'full_name': 'Team A'},
            {'id': 2, 'full_name': 'Team B'},
            {'id': 3, 'full_name': 'Team C'}
        ]
        with patch('teams.get_teams', return_value=mock_teams):
            # Mock the LeagueStandings class
            mock_standings = {
                'resultSets': [
                    {
                        'rowSet': [
                            [1, 'Team A', 'Division A', 10, 5],
                            [2, 'Team B', 'Division B', 8, 7],
                            [3, 'Team C', 'Division C', 6, 9]
                        ]
                    }
                ]
            }
            with patch('leaguestandings.LeagueStandings.get_dict', return_value=mock_standings):
                # Redirect stdout to capture the output
                captured_output = StringIO()
                import sys
                sys.stdout = captured_output

                # Call the fetch_data function
                fetch_data()

                # Restore stdout
                sys.stdout = sys.__stdout__

                # Check the output
                expected_output = "Team: Team A\nWins: 10\nLosses: 5\n\n" \
                                  "Team: Team B\nWins: 8\nLosses: 7\n\n" \
                                  "Team: Team C\nWins: 6\nLosses: 9\n\n"
                self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()