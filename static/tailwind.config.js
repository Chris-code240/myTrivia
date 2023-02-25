/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.html"],
  theme: {
    extend: {
      colors:{
        darkBlue: "rgb(1, 1, 27)",
        purple: "rgb(55, 1, 105)",
        lightRed: "rgba(248, 8, 8, 0.363)",
        veryLightRed: "rgba(248, 8, 8, 0.263)"
      }
    },
  },
  plugins: [],
}
