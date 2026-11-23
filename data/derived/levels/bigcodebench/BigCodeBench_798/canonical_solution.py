import os
import shutil

# Constants
BACKUP_DIR = '/tmp/backup'

def task_func(directory):
    """
    Rollback the update of a directory by restoring it from a backup.
    
    Parameters:
    - directory (str): The directory path to rollback.
    
    Returns:
    - directory (str): The restored directory path if successful, otherwise an error message.
    
    Requirements:
    - os
    - shutil
    
    Constants:
    - BACKUP_DIR: The directory where backups are stored. Default is '/tmp/backup'.
    
    Examples:
    >>> task_func('/tmp/my_data')
    '/tmp/my_data'
    
    >>> task_func('/tmp/nonexistent')
    'Backup directory /tmp/backup does not exist. Cannot rollback update.'
    
    Note: 
    - This function will return the restored directory path on successful rollback, or an error message otherwise.
    """
    # Check if the backup directory exists
    if not os.path.exists(BACKUP_DIR):
        return f'Backup directory {BACKUP_DIR} does not exist. Cannot rollback update.'

    backups = sorted(os.listdir(BACKUP_DIR))
    latest_backup = backups[-1] if backups else None

    if not latest_backup:
        return f'No backups found in {BACKUP_DIR}. Cannot rollback update.'

    if os.path.exists(directory):
        shutil.rmtree(directory)

    shutil.copytree(os.path.join(BACKUP_DIR, latest_backup), directory)
    return directory
