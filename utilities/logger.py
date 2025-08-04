"""Logger utility for setting up file and console logging handlers."""

import logging
import os

def setup_logger():
    """Set up and return a logger with file and console handlers."""
    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.INFO)
    
    # Create logs directory if not exists
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # File handler
    file_handler = logging.FileHandler(os.path.join(log_dir, 'test.log'))
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
    
    _logger.addHandler(file_handler)
    _logger.addHandler(console_handler)
    return _logger

logger = setup_logger()