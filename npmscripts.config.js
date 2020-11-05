const CHECK_AND_FIX_GLOBS = [
	'**/*.{md,yml}',
	'/docs/**/*.{css,json}',
	'/site/**/*.scss',
	'/site/**/*.js',
];

module.exports = {
	check: CHECK_AND_FIX_GLOBS,
	fix: CHECK_AND_FIX_GLOBS,
	preset: '@liferay/npm-scripts/src/presets/standard',
};
