import assert from 'node:assert/strict';
import test from 'node:test';
import { readFile } from 'node:fs/promises';
import { resolveAll } from '../scripts/palette.mjs';
import { keys, hexColors, assertContrast } from './helpers.mjs';
const fixture = JSON.parse(await readFile(new URL('./fixtures/upstream.json', import.meta.url)));
const read = path => readFile(new URL('../' + path, import.meta.url), 'utf8');

for (const f of resolveAll()) test(f.name + ': documented custom JSON and diff contrast', async () => {
  const theme = JSON.parse(await read('themes/' + f.slug + '.json'));
  keys(theme, ['name', 'base', 'overrides']);
  assert.equal(theme.name, f.name);
  assert.equal(theme.base, f.light ? 'light' : 'dark');
  for (const key of Object.keys(theme.overrides)) assert.ok(fixture.allowed.includes(key), 'Unknown Claude token: ' + key);
  hexColors(theme.overrides);
  assert.equal(theme.overrides.claude, f.r('accent'));
  assert.equal(theme.overrides.text, f.r('fg'));
  assert.equal(theme.overrides.error, f.r('error'));
  assert.equal(theme.overrides.planMode, f.r('info'));
  assert.equal(theme.overrides.selectionBg, f.r('selection'));
  for (const key of ['claude', 'warning', 'permission', 'promptBorder', 'inactive', 'fastMode']) assert.ok(theme.overrides[key + 'Shimmer']);
  for (const color of ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'cyan']) assert.ok(theme.overrides[color + '_FOR_SUBAGENTS_ONLY']);
  assert.notEqual(theme.overrides.diffAdded, theme.overrides.diffAddedWord);
  assert.notEqual(theme.overrides.diffRemoved, theme.overrides.diffRemovedDimmed);
  for (const bg of ['userMessageBackground', 'diffAdded', 'diffRemoved', 'selectionBg']) assertContrast(theme.overrides.text, theme.overrides[bg]);
});
