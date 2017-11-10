import getpass
from jira import JIRA

username = raw_input('Username:')
password = getpass.getpass('Password:')
jira_site = raw_input('')
basic_auth = (username, password)
options = {'server': jira_site, 'verify': False}
jira_client = JIRA(basic_auth=basic_auth, options=options)

# Search issues with JQL
issues = jira_client.search_issues("assignee=%s and status=NEW and project=RFS and text ~ 'Position – Consultant'" % username, maxResults=100000)
for i in issues:
    # Get an issue.
    issue = jira_client.issue(i)
    # Add a comment to the issue.
    jira_client.add_comment(issue, 'Safe, it can be closed.')
    # Resolve the issue and assign it to 'samz' in one step
    jira_client.transition_issue(issue, '2', assignee={'name': 'samz'}, resolution={'name': 'Done'})
