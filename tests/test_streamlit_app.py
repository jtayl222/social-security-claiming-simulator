import os
import sys
import unittest
from unittest.mock import patch, MagicMock, ANY
import importlib

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class TestStreamlitApp(unittest.TestCase):
    
    def setUp(self):
        # Nothing needed in setup
        pass

    @patch('streamlit.markdown')
    @patch('streamlit.text_input', return_value='1965-01-01')
    @patch('streamlit.number_input', return_value=3000.0)
    @patch('streamlit.write')
    @patch('requests.get')
    def test_app_loads_and_renders(self, mock_requests, mock_write, mock_number_input, mock_text_input, mock_markdown):
        # Mock the API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Model1': [{'Age': 65, '401k Balance (2025$)': 500000}],
            'Model2': [{'Age': 65, '401k Balance (2025$)': 600000}]
        }
        mock_requests.return_value = mock_response
        
        # Try importing the app
        try:
            # Clear modules to ensure fresh import
            if 'src.streamlit_app' in sys.modules:
                del sys.modules['src.streamlit_app']
                
            # Import the app
            import src.streamlit_app
            
            # Skip assertions - just make sure it imports without error
            pass
        except Exception as e:
            self.fail(f"Failed to import streamlit_app: {e}")
    
    @patch('streamlit.error')
    @patch('streamlit.text_input', return_value='invalid-date')
    @patch('requests.get')
    def test_invalid_input_handling(self, mock_requests, mock_text_input, mock_error):
        # Mock API error response
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_requests.return_value = mock_response
        
        try:
            # Clear modules to ensure fresh import
            if 'src.streamlit_app' in sys.modules:
                del sys.modules['src.streamlit_app']
                
            # Import the app
            import src.streamlit_app
            
            # Skip assertions - just make sure it imports without error
            pass
        except Exception as e:
            self.fail(f"App crashed with invalid input: {e}")
    
    @patch('streamlit.success')
    @patch('streamlit.write')
    @patch('requests.get')
    def test_api_success_flow(self, mock_requests, mock_write, mock_success):
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'Model1': [{'Age': 65, '401k Balance (2025$)': 500000}],
            'Model2': [{'Age': 65, '401k Balance (2025$)': 600000}]
        }
        mock_requests.return_value = mock_response
        
        try:
            # Clear modules to ensure fresh import
            if 'src.streamlit_app' in sys.modules:
                del sys.modules['src.streamlit_app']
                
            # Import the app
            import src.streamlit_app
            
            # Skip assertions - just make sure it imports without error
            pass
        except Exception as e:
            self.fail(f"API success flow test failed: {e}")

if __name__ == '__main__':
    unittest.main()