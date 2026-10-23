"""Resume a labeled, port-owned demo in Claude Code's real conversation UI."""
import json
import re


SESSION = 'a40d1e4c-1150-4000-8000-000000000001'


def prepare(c):
    c.git_fixture()
    c.copy(f'themes/{c.slug}.json', f'.claude/themes/{c.slug}.json')
    key = 'sk-ant-api03-living-code-capture-not-a-real-key'
    c.write('.claude.json', json.dumps({
        'hasCompletedOnboarding': True, 'theme': 'custom:' + c.slug,
        'hasSeenAutoModeAnnouncement': True,
        'apiKeyApprovals': {'approved': [key[-20:]], 'rejected': []},
        'projects': {str(c.work): {'hasTrustDialogAccepted': True, 'hasCompletedProjectOnboarding': True}},
    }))
    c.env.update(ANTHROPIC_API_KEY=key, ANTHROPIC_BASE_URL='http://127.0.0.1:9',
                 CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC='1', DISABLE_AUTOUPDATER='1', DISABLE_TELEMETRY='1')
    common = {'sessionId': SESSION, 'cwd': str(c.work), 'version': '2.1.296',
              'timestamp': '2026-01-01T12:00:00.000Z', 'isSidechain': False, 'userType': 'external'}
    entries = [
        {**common, 'type': 'user', 'uuid': 'a40d1e4c-1150-4000-8000-000000000002', 'parentUuid': None,
         'message': {'role': 'user', 'content': 'Review the glyph render loop and suggest a safer implementation. (Local demo)'}},
        {**common, 'type': 'assistant', 'uuid': 'a40d1e4c-1150-4000-8000-000000000003',
         'parentUuid': 'a40d1e4c-1150-4000-8000-000000000002',
         'message': {'id': 'msg_local_demo', 'type': 'message', 'role': 'assistant', 'model': 'claude-sonnet-4-5',
                     'content': [{'type': 'text', 'text': (c.root / 'capture/review.md').read_text()}],
                     'stop_reason': 'end_turn', 'stop_sequence': None, 'usage': {'input_tokens': 0, 'output_tokens': 0}}},
    ]
    project = re.sub(r'[^a-zA-Z0-9-]', '-', str(c.work))
    c.write(f'.claude/projects/{project}/{SESSION}.jsonl', '\n'.join(json.dumps(x) for x in entries) + '\n')
    return ['claude', '--resume', SESSION, '--strict-mcp-config', '--mcp-config', '{"mcpServers":{}}',
            '--setting-sources', 'user', '--permission-mode', 'manual', '--model', 'sonnet']


def drive(c):
    c.wait_text(r'A safer render loop|trust|API key')
    screen = c.text()
    if 'API key' in screen and ('Yes' in screen or 'use' in screen):
        c.key('enter')
    if 'trust' in c.text().lower():
        c.key('enter')
    c.wait_text(r'add boundary tests next')
