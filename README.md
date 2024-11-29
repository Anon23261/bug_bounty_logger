# Bug Bounty Tool

This Python tool allows you to log bugs, track their status, and generate reports.

## Features
- Log bugs with a title and description
- Update the status of bugs
- Generate a report of all logged bugs

## Usage

1. **Log a Bug**: Use the `log_bug` method to add a new bug.
2. **Update Bug Status**: Use the `update_bug_status` method to change the status of a bug.
3. **Generate Report**: Use the `generate_report` method to print a report of all bugs.

## Example

```python
# Example usage
if __name__ == "__main__":
    tool = BugBountyTool()
    tool.log_bug("Sample Bug", "This is a sample bug description.")
    tool.update_bug_status("Sample Bug", "closed")
    tool.generate_report()
```

## Setup

Ensure you have Python installed. Run the tool using:

```bash
python bug_bounty_tool.py
```
