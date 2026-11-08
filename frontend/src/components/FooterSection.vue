<template>
  <footer class="bg-[#0f382f] text-white pt-16 pb-12 border-t border-[#164e41] mt-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Main Footer Grid -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-10 pb-12 border-b border-white/10">
        <!-- Col 1: Brand -->
        <div class="space-y-4 md:col-span-1">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-2xl bg-white/10 flex items-center justify-center text-[#a8dc8c]">
              <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24">
                <path d="M12 13.5c-1.38 0-2.5 1.12-2.5 2.5 0 .8.4 1.5 1 1.95v.05c.4.3.9.5 1.5.5s1.1-.2 1.5-.5v-.05c.6-.45 1-1.15 1-1.95 0-1.38-1.12-2.5-2.5-2.5zm-4.5-3c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm9 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm-6.5-4c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm4 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2z" />
              </svg>
            </div>
            <div>
              <span class="text-xl font-extrabold text-white block leading-tight">
                Huellas de Esperanza
              </span>
              <span class="text-[11px] text-[#a8dc8c] uppercase tracking-wider font-semibold">
                Adopción Responsable
              </span>
            </div>
          </div>
          <p class="text-xs sm:text-sm text-white/70 leading-relaxed">
            Plataforma dedicada a rescatar, recuperar y reubicar animales en hogares llenos de amor y respeto.
          </p>
          <div class="pt-2 text-xs text-[#a8dc8c] flex items-center gap-2">
            <span class="w-2 h-2 rounded-full bg-[#a8dc8c] animate-pulse"></span>
            Línea de rescate y emergencias disponible
          </div>
        </div>

        <!-- Col 2: Navigation Links -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-[#a8dc8c] mb-4">
            Explorar
          </h4>
          <ul class="space-y-2.5 text-sm text-white/75">
            <li>
              <a href="#find-a-friend" class="hover:text-white transition-colors">Encuentra un Amigo</a>
            </li>
            <li>
              <a href="#stats" class="hover:text-white transition-colors">Impacto y Estadísticas</a>
            </li>
            <li>
              <a href="#rescue-rehab" class="hover:text-white transition-colors">Rescate y Rehabilitación</a>
            </li>
            <li>
              <a href="#second-chance" class="hover:text-white transition-colors">Historias de Éxito</a>
            </li>
            <li>
              <a href="#partners" class="hover:text-white transition-colors">Nuestros Aliados</a>
            </li>
          </ul>
        </div>

        <!-- Col 3: Adoption Info -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-[#a8dc8c] mb-4">
            Proceso de Adopción
          </h4>
          <ul class="space-y-2.5 text-sm text-white/75">
            <li>✓ 1. Selecciona a tu compañero</li>
            <li>✓ 2. Llena la solicitud en línea</li>
            <li>✓ 3. Entrevista y visita guiada</li>
            <li>✓ 4. Firma de acuerdo responsable</li>
            <li>✓ 5. Seguimiento y acompañamiento</li>
          </ul>
        </div>

        <!-- Col 4: Newsletter / Support -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-[#a8dc8c] mb-4">
            Únete a la Causa
          </h4>
          <p class="text-xs text-white/70 leading-relaxed mb-3">
            Suscríbete para recibir noticias de jornadas de adopción y casos de rescate.
          </p>
          <div class="flex items-center gap-2">
            <input
              type="email"
              placeholder="Tu correo electrónico"
              class="bg-white/10 text-white placeholder-white/40 text-xs px-3.5 py-2.5 rounded-xl border border-white/15 focus:outline-none focus:ring-1 focus:ring-[#a8dc8c] w-full"
            />
            <button
              type="button"
              class="px-4 py-2.5 rounded-xl bg-[#a8dc8c] text-[#0f382f] text-xs font-bold hover:bg-[#b8e89f] transition-colors cursor-pointer shrink-0"
            >
              Unirme
            </button>
          </div>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="mt-8 flex flex-col sm:flex-row items-center justify-between text-xs text-white/50 gap-4">
        <p>© 2026 Huellas de Esperanza. Todos los derechos reservados.</p>
        <p class="flex items-center gap-1">
          Hecho con <span class="text-[#d97736]">♥</span> para los animales que merecen una vida digna.
        </p>
      </div>
    </div>
  </footer>
</template>

