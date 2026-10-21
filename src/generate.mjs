// Public Claude Code theme tokens. Unspecified tokens inherit the matching built-in preset.
const roles = {
  claude: 'accent', text: 'fg', inverseText: 'bg', inactive: 'fgMuted', subtle: 'fgSubtle',
  suggestion: 'accent', permission: 'info', remember: 'decorator', success: 'success', error: 'error',
  warning: 'warning', merged: 'decorator', promptBorder: 'borderActive', planMode: 'info',
  autoAccept: 'success', bashBorder: 'warning', ide: 'hint', fastMode: 'warning', effortUltra: 'decorator',
  userMessageBackground: 'bgAlt', userMessageBackgroundHover: 'lineHighlight', bashMessageBackgroundColor: 'bgAlt',
  memoryBackgroundColor: 'bgAlt', selectionBg: 'selection', composerSidebarBackground: 'bgDeep',
  rate_limit_fill: 'accent', rate_limit_empty: 'border', briefLabelYou: 'fgMuted', briefLabelClaude: 'accent',
};
export function generate(flavors) {
  return flavors.map(f => {
    const overrides = Object.fromEntries(Object.entries(roles).map(([key, role]) => [key, f.r(role)]));
    for (const [key, role] of Object.entries({ diffAdded: 'added', diffRemoved: 'removed' })) {
      overrides[key] = f.mix('bg', role, 0.12);
      overrides[`${key}Dimmed`] = f.mix('bg', role, 0.06);
      overrides[`${key}Word`] = f.mix('bg', role, 0.24);
    }
    for (const key of ['claude', 'warning', 'permission', 'promptBorder', 'inactive', 'fastMode']) {
      overrides[`${key}Shimmer`] = f.mix(roles[key], 'fg', 0.25);
    }
    for (const [key, color] of Object.entries({ red: 'flare', blue: 'steel', green: 'moss', yellow: 'amber', purple: 'orchid', orange: 'copper', pink: 'rose', cyan: 'aqua' })) {
      overrides[`${key}_FOR_SUBAGENTS_ONLY`] = f.c(color);
    }
    return { path: `themes/${f.slug}.json`, content: JSON.stringify({ name: f.name, base: f.light ? 'light' : 'dark', overrides }, null, 2) + '\n' };
  });
}
