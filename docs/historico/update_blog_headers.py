#!/usr/bin/env python3
"""
Script to update all blog articles with premium header structure.
This script will systematically replace basic headers with premium ones.
"""

import os
import glob
import re

# Premium header template
PREMIUM_HEADER = '''    <!-- Premium Header -->
    <header class="sticky top-0 z-50 transition-all duration-300" id="main-header">
      <!-- Nivel 1: Logo + Credenciales + CTAs Premium -->
      <div class="bg-gradient-to-r from-white via-primary/5 to-secondary/5 backdrop-blur-sm">
        <div class="max-w-7xl mx-auto px-6 py-6">
          <div class="flex justify-between items-center">

            <!-- Logo Simplificado -->
            <a href="/" class="flex items-center group">
              <div class="relative">
                <img src="../../images/logo.png" alt="CertiAlmería" class="h-16 md:h-18 lg:h-20 w-auto object-contain transform group-hover:scale-105 transition-all duration-500">
                <!-- Glow effect sutil -->
                <div class="absolute inset-0 bg-gradient-to-br from-primary/20 to-secondary/20 rounded-lg blur-lg opacity-0 group-hover:opacity-100 transition-opacity duration-500 -z-10"></div>
              </div>
            </a>

            <!-- Stats + CTAs Redistributed -->
            <div class="hidden lg:flex items-center gap-10">

              <!-- COAAT Badge visible on medium screens -->
              <div class="hidden md:block lg:hidden">
                <span class="text-sm bg-primary/10 text-primary font-bold px-4 py-2 rounded-full border border-primary/20">COAAT 1.440</span>
              </div>

              <!-- Stats Premium - Más prominentes -->
              <div class="flex items-center gap-8">
                <div class="text-center group">
                  <div class="text-3xl font-black text-primary group-hover:scale-110 transition-transform duration-300">1800+</div>
                  <div class="text-sm text-neutral-600 font-bold">Certificados</div>
                </div>
                <div class="w-px h-16 bg-gradient-to-b from-transparent via-neutral-300 to-transparent"></div>
                <div class="text-center group">
                  <div class="text-3xl font-black text-secondary group-hover:scale-110 transition-transform duration-300">24h</div>
                  <div class="text-sm text-neutral-600 font-bold">Entrega</div>
                </div>
                <div class="w-px h-16 bg-gradient-to-b from-transparent via-neutral-300 to-transparent"></div>
                <div class="text-center group">
                  <div class="text-3xl font-black text-accent group-hover:scale-110 transition-transform duration-300">75€</div>
                  <div class="text-sm text-neutral-600 font-bold">Precio fijo</div>
                </div>
              </div>

              <!-- CTAs Premium - Más destacados -->
              <div class="flex items-center gap-5">
                <!-- Teléfono Premium -->
                <a href="tel:+34667451538" class="group relative overflow-hidden">
                  <div class="relative bg-white border-2 border-primary/20 rounded-2xl px-6 py-4 shadow-lg hover:shadow-2xl transition-all duration-300 backdrop-blur-sm">
                    <!-- Hover effect background -->
                    <div class="absolute inset-0 bg-gradient-to-r from-primary/5 to-secondary/5 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>

                    <div class="relative flex items-center gap-3">
                      <div class="w-12 h-12 bg-gradient-to-br from-primary to-secondary rounded-xl flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                        <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                        </svg>
                      </div>
                      <div>
                        <div class="text-sm text-neutral-500 font-bold">Llama gratis</div>
                        <div class="text-xl font-black text-neutral-800">667 45 15 38</div>
                      </div>
                    </div>
                  </div>
                </a>

                <!-- WhatsApp Ultra Premium -->
                <a href="https://wa.me/34667451538" class="group relative overflow-hidden">
                  <div class="relative bg-gradient-to-r from-whatsapp via-green-500 to-green-600 rounded-2xl px-8 py-5 shadow-2xl hover:shadow-green-500/25 hover:shadow-2xl transition-all duration-300 transform hover:scale-105">
                    <!-- Shine effect -->
                    <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 -skew-x-12 transform translate-x-full group-hover:translate-x-[-200%] transition-transform duration-1000"></div>

                    <div class="relative flex items-center gap-4">
                      <svg class="w-7 h-7 text-white group-hover:scale-110 transition-transform duration-300" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.56-.01-.188 0-.495.074-.754.371-.26.297-.99.968-.99 2.36 0 1.393 1.015 2.74 1.156 2.93.14.19 2.001 3.055 4.851 4.283.677.292 1.206.465 1.619.594.68.21 1.299.18 1.789.109.546-.082 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>
                      </svg>
                      <div class="text-white">
                        <div class="text-lg font-bold">WhatsApp</div>
                        <div class="text-sm opacity-90">Respuesta inmediata</div>
                      </div>
                    </div>
                  </div>
                </a>
              </div>
            </div>

            <!-- Botón hamburguesa visible solo en móvil -->
            <button class="lg:hidden relative z-50 p-2" id="mobile-menu-button" aria-label="Abrir menú de navegación">
              <div class="w-6 h-0.5 bg-gray-600 mb-1.5 transition-all duration-300" id="line1"></div>
              <div class="w-6 h-0.5 bg-gray-600 mb-1.5 transition-all duration-300" id="line2"></div>
              <div class="w-6 h-0.5 bg-gray-600 transition-all duration-300" id="line3"></div>
            </button>
          </div>
        </div>
      </div>

      <!-- Nivel 2: Navegación Premium con Glassmorphism -->
      <div class="bg-white/80 backdrop-blur-md border-t border-white/20 shadow-sm">
        <div class="max-w-7xl mx-auto px-6">
          <nav class="hidden lg:block py-6">
            <ul class="flex justify-center items-center gap-12">

              <!-- Navigation Items Premium -->
              <li>
                <a href="/" class="nav-item-premium group">
                  <span class="relative z-10">Inicio</span>
                  <div class="nav-glow"></div>
                </a>
              </li>

              <li>
                <a href="/certificado-energetico/" class="nav-item-premium group">
                  <span class="relative z-10">Certificado Energético</span>
                  <div class="nav-glow"></div>
                </a>
              </li>

              <li>
                <a href="/certificado-energetico-barato/" class="nav-item-premium group relative">
                  <span class="relative z-10">Precios</span>
                  <div class="absolute -top-2 -right-2 bg-gradient-to-r from-red-500 to-orange-500 text-white text-xs font-bold px-2 py-1 rounded-full shadow-lg animate-pulse">HOT</div>
                  <div class="nav-glow"></div>
                </a>
              </li>

              <li>
                <a href="/municipios/" class="nav-item-premium group">
                  <span class="relative z-10">Municipios</span>
                  <div class="nav-glow"></div>
                </a>
              </li>

              <!-- Dropdown Premium -->
              <li class="relative group">
                <button class="nav-item-premium group flex items-center">
                  <span class="relative z-10">Comparativas</span>
                  <svg class="w-4 h-4 ml-2 transform group-hover:rotate-180 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                  <div class="nav-glow"></div>
                </button>

                <!-- Dropdown Menu Ultra Premium -->
                <div class="absolute top-full left-1/2 transform -translate-x-1/2 mt-4 w-72 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300 z-50">
                  <div class="bg-white/90 backdrop-blur-xl rounded-3xl shadow-2xl border border-white/20 overflow-hidden">
                    <!-- Dropdown Header -->
                    <div class="bg-gradient-to-r from-primary/10 to-secondary/10 px-6 py-4 border-b border-white/20">
                      <h3 class="font-bold text-neutral-800">Comparativas Honestas</h3>
                      <p class="text-xs text-neutral-600">Ve las diferencias reales</p>
                    </div>

                    <!-- Dropdown Items -->
                    <div class="p-2">
                      <a href="/vs-certicalia/" class="block p-4 rounded-2xl hover:bg-primary/5 transition-all duration-200 group/item">
                        <div class="flex items-center gap-3">
                          <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center">
                            <span class="text-white font-bold text-sm">C</span>
                          </div>
                          <div>
                            <div class="font-semibold text-neutral-800 group-hover/item:text-primary transition-colors">vs Certicalia</div>
                            <div class="text-xs text-neutral-500">75€ vs 90€+</div>
                          </div>
                        </div>
                      </a>

                      <a href="/vs-tinsa/" class="block p-4 rounded-2xl hover:bg-primary/5 transition-all duration-200 group/item">
                        <div class="flex items-center gap-3">
                          <div class="w-10 h-10 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center">
                            <span class="text-white font-bold text-sm">T</span>
                          </div>
                          <div>
                            <div class="font-semibold text-neutral-800 group-hover/item:text-primary transition-colors">vs Tinsa</div>
                            <div class="text-xs text-neutral-500">Ahorra 45€</div>
                          </div>
                        </div>
                      </a>

                      <a href="/vs-diego-certificacia/" class="block p-4 rounded-2xl hover:bg-primary/5 transition-all duration-200 group/item">
                        <div class="flex items-center gap-3">
                          <div class="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-600 rounded-xl flex items-center justify-center">
                            <span class="text-white font-bold text-sm">D</span>
                          </div>
                          <div>
                            <div class="font-semibold text-neutral-800 group-hover/item:text-primary transition-colors">vs Competencia Local</div>
                            <div class="text-xs text-neutral-500">Disponibilidad garantizada</div>
                          </div>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
              </li>

              <li>
                <a href="/blog/" class="nav-item-premium group">
                  <span class="relative z-10">Blog</span>
                  <div class="nav-glow"></div>
                </a>
              </li>

              <li>
                <a href="/contacto/" class="nav-item-premium group">
                  <span class="relative z-10">Contacto</span>
                  <div class="nav-glow"></div>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>

      <!-- Menú móvil overlay completo -->
      <div class="lg:hidden fixed inset-0 bg-white z-40 transform translate-x-full transition-transform duration-300" id="mobile-menu">
        <div class="pt-24 pb-8 px-6">
          <nav role="navigation" aria-label="Navegación móvil">
            <ul class="space-y-0">
              <li class="border-b border-neutral-100">
                <a href="/" class="block py-4 text-lg text-neutral-700 hover:text-primary transition-colors duration-300">Inicio</a>
              </li>
              <li class="border-b border-neutral-100">
                <a href="/certificado-energetico/" class="block py-4 text-lg text-neutral-700 hover:text-primary transition-colors duration-300">Certificado Energético</a>
              </li>
              <li class="border-b border-neutral-100">
                <a href="/certificado-energetico-barato/" class="block py-4 text-lg text-neutral-700 hover:text-primary transition-colors duration-300">Precios</a>
              </li>
              <li class="border-b border-neutral-100">
                <a href="/municipios/" class="block py-4 text-lg text-neutral-700 hover:text-primary transition-colors duration-300">Municipios</a>
              </li>
              <!-- Comparativas expandidas en móvil -->
              <li class="border-b border-neutral-100">
                <button class="w-full text-left py-4 text-lg text-neutral-700 hover:text-primary transition-colors duration-300" onclick="toggleMobileSubmenu(this)">
                  Comparativas
                  <svg class="w-4 h-4 inline-block ml-2 transform transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                  </svg>
                </button>
                <div class="hidden pl-6 pb-2 bg-neutral-50">
                  <a href="/vs-certicalia/" class="block py-2 text-base text-neutral-600 hover:text-primary transition-colors">vs Certicalia</a>
                  <a href="/vs-tinsa/" class="block py-2 text-base text-neutral-600 hover:text-primary transition-colors">vs Tinsa</a>
                  <a href="/vs-diego-certificacia/" class="block py-2 text-base text-neutral-600 hover:text-primary transition-colors">vs Competencia Local</a>
                </div>
              </li>
              <li class="border-b border-neutral-100">
                <a href="/blog/" class="block py-4 text-lg text-neutral-700 hover:text-primary transition-colors duration-300">Blog</a>
              </li>
              <li class="border-b border-neutral-100">
                <a href="/contacto/" class="block py-4 text-lg text-neutral-700 hover:text-primary transition-colors duration-300">Contacto</a>
              </li>
            </ul>
          </nav>

          <!-- CTAs móvil -->
          <div class="mt-8 space-y-4">
            <a href="tel:+34667451538" class="block text-center bg-gradient-to-r from-primary to-secondary text-white py-3 px-6 rounded-full font-semibold hover:from-secondary hover:to-primary transition-colors duration-300">
              📞 667 45 15 38
            </a>
            <a href="https://wa.me/34667451538?text=Hola,%20necesito%20un%20certificado%20energético%20en%20Almería" class="block text-center bg-whatsapp text-white py-3 px-6 rounded-full font-semibold hover:bg-green-600 transition-colors duration-300">
              💬 WhatsApp
            </a>
          </div>
        </div>
      </div>
    </header>'''

# Premium CSS additions
PREMIUM_CSS = '''
        /* Premium Navigation Styles */
        .nav-item-premium {
          @apply relative px-6 py-3 text-lg font-semibold text-neutral-700 transition-all duration-300 rounded-2xl overflow-hidden;
        }

        .nav-item-premium:hover {
          @apply text-primary transform scale-105;
        }

        .nav-glow {
          @apply absolute inset-0 bg-gradient-to-r from-primary/0 via-primary/10 to-secondary/0 opacity-0 group-hover:opacity-100 transition-all duration-300 rounded-2xl;
        }

        /* Responsive magic */
        @media (max-width: 1024px) {
          .nav-item-premium {
            @apply px-4 py-2 text-base;
          }
        }

        /* Scroll effect */
        .header-scrolled {
          @apply shadow-2xl;
          background: rgba(255, 255, 255, 0.95);
          backdrop-filter: blur(20px);
        }'''

# Premium JavaScript
PREMIUM_JS = '''    <!-- Premium Header JavaScript -->
    <script>
        // Mobile menu functionality
        const mobileMenuButton = document.getElementById('mobile-menu-button');
        const mobileMenu = document.getElementById('mobile-menu');
        const line1 = document.getElementById('line1');
        const line2 = document.getElementById('line2');
        const line3 = document.getElementById('line3');

        if (mobileMenuButton && mobileMenu) {
          mobileMenuButton.addEventListener('click', () => {
            mobileMenu.classList.toggle('translate-x-full');

            // Animate hamburger to X
            line1.classList.toggle('rotate-45');
            line1.classList.toggle('translate-y-2');
            line2.classList.toggle('opacity-0');
            line3.classList.toggle('-rotate-45');
            line3.classList.toggle('-translate-y-2');
          });

          // Close menu on link clicks
          const mobileMenuLinks = mobileMenu.querySelectorAll('a');
          mobileMenuLinks.forEach(link => {
            link.addEventListener('click', () => {
              mobileMenu.classList.add('translate-x-full');
              // Reset hamburger
              line1.classList.remove('rotate-45', 'translate-y-2');
              line2.classList.remove('opacity-0');
              line3.classList.remove('-rotate-45', '-translate-y-2');
            });
          });
        }

        // Mobile submenu toggle
        function toggleMobileSubmenu(button) {
          const submenu = button.nextElementSibling;
          const icon = button.querySelector('svg');

          if (submenu && icon) {
            submenu.classList.toggle('hidden');
            icon.classList.toggle('rotate-180');
          }
        }

        // Make function global for onclick
        window.toggleMobileSubmenu = toggleMobileSubmenu;

        // Header scroll effects
        window.addEventListener('scroll', () => {
          const header = document.getElementById('main-header');
          if (window.scrollY > 100) {
            header.classList.add('header-scrolled');
          } else {
            header.classList.remove('header-scrolled');
          }
        });
    </script>'''

def update_blog_article(file_path):
    """Update a single blog article with premium header."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Pattern to match basic header section
        header_pattern = r'    <!-- Header -->\s*<header class="bg-white shadow-lg sticky top-0 z-50[^>]*">.*?</header>'

        # Check if header needs updating
        if '<!-- Premium Header -->' in content:
            print(f"Already updated: {file_path}")
            return True

        # Replace basic header with premium header
        updated_content = re.sub(header_pattern, PREMIUM_HEADER, content, flags=re.DOTALL)

        # Add premium CSS if not present
        if '.nav-item-premium' not in content:
            # Find the closing </style> tag and add premium CSS before it
            style_pattern = r'(\s*)(</style>)'
            updated_content = re.sub(style_pattern, r'\1' + PREMIUM_CSS + r'\1\2', updated_content)

        # Add premium JavaScript before closing </body>
        if 'mobile-menu-button' not in content or 'Premium Header JavaScript' not in content:
            js_pattern = r'</body>\s*</html>'
            updated_content = re.sub(js_pattern, PREMIUM_JS + '\n</body>\n</html>', updated_content)

        # Write updated content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Updated: {file_path}")
        return True

    except Exception as e:
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update all blog articles."""
    # Get blog directory
    blog_dir = "C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA/blog"

    # Find all blog HTML files (excluding main blog index)
    blog_files = []
    for root, dirs, files in os.walk(blog_dir):
        for file in files:
            if file == 'index.html' and root != blog_dir:  # Exclude main blog index
                blog_files.append(os.path.join(root, file))

    print(f"Found {len(blog_files)} blog articles to update:")

    updated_count = 0
    for file_path in blog_files:
        if update_blog_article(file_path):
            updated_count += 1

    print(f"\nSuccessfully updated {updated_count} out of {len(blog_files)} blog articles.")

if __name__ == "__main__":
    main()