<template>
  <section id="stats" class="py-8 sm:py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Encabezado de la Sección -->
      <div class="flex flex-col md:flex-row md:items-end justify-between mb-8 gap-4">
        <div>
          <span class="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-widest text-[#0f382f]/70 bg-[#a8dc8c]/40 px-3 py-1 rounded-full whitespace-nowrap">
            <span class="w-2 h-2 rounded-full bg-[#0f382f]"></span>
            Nuestro Compromiso Real
          </span>
          <h2 class="mt-2.5 text-2xl sm:text-3xl lg:text-4xl font-extrabold text-[#0f382f] tracking-tight">
            Transformando vidas, una huella a la vez
          </h2>
        </div>
        <p class="text-sm text-[#0f382f]/70 max-w-md">
          Cada cifra representa un animal rescatado de la soledad y la incertidumbre, recibiendo atención de calidad y un nuevo comienzo.
        </p>
      </div>

      <!-- Cuadrícula de Estadísticas con Alturas Equilibradas -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative">
        <!-- Tarjeta 1: Adopciones Exitosas (Tarjeta Verde Lima) -->
        <div class="relative bg-[#a8dc8c] text-[#0f382f] rounded-3xl p-7 sm:p-9 shadow-sm border border-[#0f382f]/10 overflow-hidden flex flex-col justify-between transition-transform duration-200 hover:-translate-y-1 min-h-[250px] sm:min-h-[270px]">
          <div>
            <div class="flex items-center justify-between gap-3">
              <span class="text-base sm:text-lg font-bold tracking-tight text-[#0f382f] whitespace-nowrap">
                Adopciones Exitosas
              </span>
              <span class="text-xs font-bold uppercase tracking-wider bg-[#0f382f]/10 px-2.5 py-1 rounded-full whitespace-nowrap shrink-0">
                Hogares Felices
              </span>
            </div>
            <!-- Línea divisoria delgada del diseño -->
            <div class="w-full h-px bg-[#0f382f]/20 my-4 sm:my-5"></div>
          </div>

          <div class="flex items-end justify-between mt-2">
            <div class="flex flex-col">
              <span class="text-5xl sm:text-6xl lg:text-7xl font-extrabold tracking-tighter text-[#0f382f] leading-none">
                48
              </span>
              <p class="mt-3 text-xs sm:text-sm font-medium text-[#0f382f]/85 max-w-xs leading-snug">
                animales felizmente integrados en hogares llenos de amor y respeto.
              </p>
            </div>
            
            <div class="hidden sm:flex w-14 h-14 rounded-2xl bg-[#0f382f]/10 items-center justify-center text-[#0f382f] shrink-0">
              <!-- Icono de hogar con huella -->
              <svg class="w-7 h-7 fill-current" viewBox="0 0 24 24">
                <path d="M12 3L2 12h3v8h6v-6h2v6h6v-8h3L12 3zm0 4.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5z" />
              </svg>
            </div>
          </div>

          <!-- Garabato / Doodle decorativo curvo -->
          <div class="absolute -right-4 -bottom-6 pointer-events-none opacity-40">
            <svg class="w-36 h-36 text-[#0f382f]" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M10 60 C 30 20, 50 90, 70 30 C 80 10, 95 40, 75 70 C 60 90, 45 40, 85 25" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>
        </div>

        <!-- Tarjeta 2: Tratamientos Médicos (Tarjeta Verde Bosque Profundo) -->
        <div class="relative bg-[#0f382f] text-white rounded-3xl p-7 sm:p-9 shadow-lg border border-[#0f382f] overflow-hidden flex flex-col justify-between transition-transform duration-200 hover:-translate-y-1 min-h-[250px] sm:min-h-[270px]">
          <div>
            <div class="flex items-center justify-between gap-3">
              <span class="text-base sm:text-lg font-bold tracking-tight text-white whitespace-nowrap">
                Tratamientos Médicos
              </span>
              <span class="text-xs font-bold uppercase tracking-wider bg-white/10 text-[#a8dc8c] px-2.5 py-1 rounded-full whitespace-nowrap shrink-0">
                Salud y Bienestar
              </span>
            </div>
            <!-- Línea divisoria delgada del diseño -->
            <div class="w-full h-px bg-white/20 my-4 sm:my-5"></div>
          </div>

          <div class="flex items-end justify-between mt-2">
            <div class="flex flex-col">
              <span class="text-5xl sm:text-6xl lg:text-7xl font-extrabold tracking-tighter text-white leading-none">
                208
              </span>
              <p class="mt-3 text-xs sm:text-sm font-normal text-white/80 max-w-xs leading-snug">
                animales con atención médica especializada, vacunas completas y cuidado preventivo.
              </p>
            </div>

            <div class="hidden sm:flex w-14 h-14 rounded-2xl bg-white/10 items-center justify-center text-[#a8dc8c] shrink-0">
              <!-- Cruz médica con círculo -->
              <svg class="w-7 h-7 fill-none stroke-current" viewBox="0 0 24 24" stroke-width="2.2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 4v16m8-8H4" />
                <circle cx="12" cy="12" r="9" stroke-width="1.5" />
              </svg>
            </div>
          </div>

          <!-- Luz ambiental sutil decorativa -->
          <div class="absolute -left-10 -bottom-10 w-44 h-44 rounded-full bg-[#a8dc8c]/10 blur-3xl pointer-events-none"></div>
        </div>
      </div>
    </div>
  </section>
</template>
