module.exports = {
  content: [
    './templates/**/*.html',
    './news/templates/**/*.html',
    './users/templates/**/*.html'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
