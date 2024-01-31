import os
import errno
import logging

# import logging, create a new logger and then disable
# everything but passing up to the root logger
logger = logging.getLogger(__name__)


def safe_file_write(path, data):
    # Check if the folder exists, if not, create it
    folder_path = os.path.dirname(path)
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError as e:
            # Ignore the error if the folder exists
            if e.errno != errno.EEXIST:
                pass
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            pass

    # Try to open the file in write mode, creating it if it doesn't exist
    try:
        with open(path, "w") as file:
            file.write(data)
    except IOError as e:
        # Handle expected IO errors
        # (like file write permissions, disk full, etc.)
        logger.error(f"An IO error occurred: {e}")
        raise
    except Exception as e:
        # Handle any other unexpected errors
        logger.error(f"An unexpected error occurred: {e}")
        raise


# Example usage
# path = 'path/to/your/file.txt'
# data = 'Your data here'
# safe_file_write(path, data)
