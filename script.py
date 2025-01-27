import pyautogui
import time
import pygetwindow as gw
import sys
import argparse

def focus_gmail_window(window_title_substring="Gmail"):
    """
    Finds and focuses the ARC window with Gmail open using available pygetwindow functions.

    Args:
        window_title_substring (str): Substring to match in the window title.

    Raises:
        SystemExit: If no matching window is found.
    """
    # Retrieve all window titles
    all_titles = gw.getAllTitles()
    print("Available window titles:")
    for title in all_titles:
        print(f" - {title}")

    # Find titles that contain the specified substring (case-insensitive)
    matching_titles = [title for title in all_titles if window_title_substring.lower() in title.lower()]

    if not matching_titles:
        print(f"No window found with title containing '{window_title_substring}'. Please ensure ARC with Gmail is open.")
        sys.exit(1)

    # Activate the first matching window
    window_title = matching_titles[0]
    try:
        gw.activate(window_title)
        time.sleep(1)  # Wait for the window to come into focus
        print(f"Focused window: {window_title}")
    except Exception as e:
        print(f"Failed to activate window '{window_title}'. Error: {e}")
        sys.exit(1)

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
        pyautogui.hotkey('shift', '8', 'a')  # This sends '*'
        time.sleep(select_pause)

        print(f"Iteration {i+1}/{n_iterations}: Archiving emails...")
        # Press 'e' to archive
        pyautogui.press('e')
        time.sleep(archive_pause)

    print("Archiving complete.")

def parse_arguments():
    """
    Parses command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments with 'iterations' attribute.
    """
    parser = argparse.ArgumentParser(description="Automate archiving of Gmail emails in ARC.")
    parser.add_argument(
        '-n', '--iterations',
        type=int,
        default=1,
        help='Number of times to perform the archive action (default: 1)'
    )
    return parser.parse_args()

def main():
    # Parse command-line arguments
    args = parse_arguments()
    n = args.iterations

    time.sleep(5)  # Wait for the user to switch to the Gmail window

    if n < 1:
        print("Number of iterations must be at least 1.")
        sys.exit(1)

    # Focus the ARC window
    # focus_gmail_window(window_title_substring="Arc")  # Adjust if necessary

    # Start archiving emails
    archive_emails(n_iterations=n, select_pause=2, archive_pause=2)

if __name__ == "__main__":
    main()
