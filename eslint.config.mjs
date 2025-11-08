/**
 * @author gye hyun james kim <pnuskgh@gmail.com>
 * @copyright 2017~2025, BlueStone Inc.
 * @license BlueStone License 1.0
 */

import fs from 'fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import globals from 'globals';
import { defineConfig } from 'eslint/config';
import eslint from '@eslint/js';
import tseslint from 'typescript-eslint';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ignorePath = path.resolve(__dirname, '.prettierignore');

const ignores = fs
    .readFileSync(ignorePath, 'utf8')
    .split('\n')
    .filter((line) => line.startsWith('#') == false && line.trim() != '')
    .map((ignore) => ignore.replace('\r', ''));

export default defineConfig([
    eslint.configs.recommended,
    ...tseslint.configs.recommended,

    {
        files: ['**/*.ts'],
        ignores: ignores,
        languageOptions: {
            globals: globals.browser,
        },
        rules: {
            'no-unused-vars': 'off',
            '@typescript-eslint/no-unused-vars': [
                'error',
                {
                    args: 'all',
                    argsIgnorePattern: '^_',
                    caughtErrors: 'all',
                    caughtErrorsIgnorePattern: '^_',
                    destructuredArrayIgnorePattern: '^_',
                    varsIgnorePattern: '^_',
                    ignoreRestSiblings: true,
                },
            ],
        },
    },
]);
