import pyautogui
import time
import pygetwindow as gw
import sys

def focus_gmail_window(window_title="Gmail"):
    """
    Finds and focuses the ARC window with Gmail open.
    """
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        print(f"No window found with title containing '{window_title}'. Please ensure ARC with Gmail is open.")
        sys.exit(1)

    window = windows[0]
    if not window.isActive:
        window.activate()
        time.sleep(1)  # Wait for the window to come into focus
    return

def archive_emails(n_iterations, select_pause=1, archive_pause=1):
    """
    Archives emails by selecting them and using the archive shortcut.

    Args:
        n_iterations (int): Number of times to perform the archive action.
        select_pause (float): Pause duration after selecting emails.
        archive_pause (float): Pause duration after archiving emails.
    """
    for i in range(n_iterations):
        print(f"Iteration {i+1}/{n_iterations}: Selecting emails...")
        # Press Shift + 8 then 'a' to select emails
        pyautogui.hotkey('shift', '8')  # This sends '*'
        time.sleep(0.1)  # Short pause between keystrokes
        pyautogui.press('a')          # This selects all
        time.sleep(select_pause)

        print(f"Iteration {i+1}/{n_iterations}: Archiving emails...")
        # Press 'e' to archive
        pyautogui.press('e')
        time.sleep(archive_pause)

    print("Archiving complete.")

def main():
    # Number of times to repeat the archiving process
    n = 10  # You can change this value as needed

    # Focus the Gmail window in ARC
    focus_gmail_window(window_title="Gmail")  # Adjust if necessary

    # Start archiving emails
    archive_emails(n_iterations=n)

if __name__ == "__main__":
    main()
