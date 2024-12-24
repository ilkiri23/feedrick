import path from 'node:path'
import resolve from '@rollup/plugin-node-resolve'
import commonjs from '@rollup/plugin-commonjs'
import alias from '@rollup/plugin-alias'
import json from '@rollup/plugin-json'
import terser from '@rollup/plugin-terser'
import postcss from 'rollup-plugin-postcss'
import atImport from 'postcss-import'
import cssnano from 'cssnano'

const production = !process.env.ROLLUP_WATCH

export default {
	input: 'app/static/src/js/main.js',
	output: {
		file: 'app/static/dist/bundle.js',
		format: 'iife',
		// sourcemap: !production || 'inline'
	},
	watch: {
		include: [
			'app/static/src/js/**/*.js',
			'app/static/src/css/**/*.css'
		]
	},
	plugins: [
		postcss({
			extract: 'styles.css',
			plugins: [
				atImport(),
				production && cssnano({
					preset: ['default', {
						colormin: false,
						convertValues: false
					}]
				})
			]
		}),
		// alias({
		// 	entries: {
		// 		htmx: 'htmx.org/dist/htmx.js'
		// 	}
		// }),
		resolve(),
		commonjs(),
		// json(),
		production && terser()
	]
};
