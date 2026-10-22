"""Use Claude Code's own custom-theme picker/preview, without submitting a prompt."""
import json
import time


def prepare(c):
    c.git_fixture()
    c.copy(f'themes/{c.slug}.json', f'.claude/themes/{c.slug}.json')
    key = 'sk-ant-api03-living-code-capture-not-a-real-key'
    c.write('.claude.json', json.dumps({'hasCompletedOnboarding': True, 'theme': 'custom:' + c.slug,
                                      'apiKeyApprovals': {'approved': [key[-20:]], 'rejected': []},
                                      'projects': {str(c.work): {'hasTrustDialogAccepted': True, 'hasCompletedProjectOnboarding': True}}}))
    c.env.update(ANTHROPIC_API_KEY=key, ANTHROPIC_BASE_URL='http://127.0.0.1:9',
                 CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC='1', DISABLE_AUTOUPDATER='1', DISABLE_TELEMETRY='1')
    return ['claude', '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}', '--setting-sources', 'user']


def drive(c):
    c.wait_text(r'Claude|trust|API key')
    screen = c.text()
    if 'API key' in screen and ('Yes' in screen or 'use' in screen):
        c.key('enter')
    if 'trust' in c.text().lower():
        c.key('enter')
    c.wait_text(r'shift\+tab')
    time.sleep(1)
    window = c.run(['xdotool', 'search', '--onlyvisible', '--class', 'kitty']).split()[-1]
    c.run(['xdotool', 'windowfocus', window])
    c.run(['xdotool', 'type', '--clearmodifiers', '--delay', '100', '/theme'])
    time.sleep(0.5)
    c.run(['xdotool', 'key', '--clearmodifiers', 'Return'])
    c.wait_text(r'Select theme|Choose.*theme|custom theme|Living Code')
