/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './index.html',
    './404.html',
    './arquitecto-tecnico-coaat-1440/**/*.html',
    './aviso-legal/**/*.html',
    './blog/**/*.html',
    './calculadora-precio-certificado-energetico/**/*.html',
    './certificado-energetico/**/*.html',
    './certificado-energetico-24-horas/**/*.html',
    './certificado-energetico-75-euros/**/*.html',
    './certificado-energetico-barato/**/*.html',
    './certificado-energetico-rapido/**/*.html',
    './certificado-local-comercial/**/*.html',
    './certificado-oficina/**/*.html',
    './certificado-vivienda/**/*.html',
    './consultoria-energetica/**/*.html',
    './contacto/**/*.html',
    './cookies/**/*.html',
    './municipios/**/*.html',
    './politica-privacidad/**/*.html',
    './registro-junta-andalucia/**/*.html',
    './vs-certicalia/**/*.html',
    './vs-tinsa/**/*.html',
  ],
  safelist: [
    // Critical classes that must always be included
    'hero-bg',
    'container-custom',
    'text-shadow',
    'card-depth',
    'form-depth',
    'section-padding',
    'hero-wave',
    'wave-divider',
    'animate-fade-in-up',
    'gradient-text',
    'bg-gradient-primary',
    'bg-gradient-secondary',
    'bg-gradient-accent',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#8BC34A',
        secondary: '#7CB342',
        accent: '#689F38',
        success: '#8BC34A',
        whatsapp: '#25d366',
        neutral: {
          50: '#fafafa',
          100: '#f5f5f5',
          200: '#e5e5e5',
          300: '#d4d4d4',
          400: '#a3a3a3',
          500: '#737373',
          600: '#525252',
          700: '#404040',
          800: '#262626',
          900: '#171717'
        }
      },
      fontFamily: {
        'sans': ['"Montserrat"', 'system-ui', 'sans-serif'],
        'display': ['"Montserrat"', 'system-ui', 'sans-serif']
      },
      animation: {
        'fade-in-up': 'fadeInUp 0.8s ease-out',
        'pulse-slow': 'pulse 3s infinite',
        'bounce-slow': 'bounce 2s infinite'
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
        '128': '32rem'
      }
    }
  },
  plugins: [],
}
