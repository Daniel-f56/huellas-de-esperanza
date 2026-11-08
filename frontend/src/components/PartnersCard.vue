<template>
  <div class="bg-[#faf8f5] rounded-3xl p-8 sm:p-10 shadow-sm border border-stone-200/80 transition-all duration-300 hover:shadow-md">
    <!-- Encabezado en Español -->
    <div class="mb-6">
      <span class="text-xs font-bold tracking-[0.2em] uppercase text-stone-500 block">
        NUESTROS ALIADOS
      </span>
      <h3 class="text-2xl sm:text-3xl font-extrabold text-[#0f382f] tracking-tight mt-1">
        Nuestros Maravillosos Aliados
      </h3>
      <p class="mt-2 text-xs sm:text-sm text-stone-600">
        Empresas y organizaciones que hacen posible la alimentación, rescate y atención médica diaria.
      </p>
    </div>

    <!-- Cuadrícula de Aliados -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 pt-2">
      <!-- Aliado 1: Silpo -->
      <div class="p-5 sm:p-6 rounded-2xl bg-white border border-stone-200/70 shadow-xs flex flex-col justify-between">
        <div>
          <!-- Logo Silpo en Español -->
          <div class="h-10 flex items-center mb-4">
            <span class="text-xl font-black italic tracking-wide text-[#0f382f] border-2 border-[#0f382f] px-3.5 py-0.5 rounded-full inline-block">
              Silpo
            </span>
          </div>

          <div class="w-full h-px bg-stone-200 my-3"></div>

          <h4 class="text-sm font-bold text-[#0f382f]">
            Cadena de Supermercados Silpo
          </h4>
          <p class="mt-2 text-xs text-stone-600 leading-relaxed">
            Su dedicación al bienestar animal ha brindado toneladas de alimento balanceado y suministros vitales para apoyar el sostenimiento de nuestros refugios de emergencia.
          </p>
        </div>

        <div class="mt-4 pt-3 border-t border-stone-100 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-[#a8dc8c]"></span>
          <span class="text-[11px] font-semibold text-stone-500">Alimentación asegurada</span>
        </div>
      </div>

      <!-- Aliado 2: Purina -->
      <div class="p-5 sm:p-6 rounded-2xl bg-white border border-stone-200/70 shadow-xs flex flex-col justify-between">
        <div>
          <!-- Logo Purina -->
          <div class="h-10 flex items-center mb-4">
            <div class="flex items-center gap-1.5 bg-[#0f382f] text-white px-3.5 py-1 rounded-lg">
              <span class="text-xs font-mono font-bold tracking-widest">PURINA</span>
              <span class="w-2 h-2 bg-[#d97736] rounded-full"></span>
            </div>
          </div>

          <div class="w-full h-px bg-stone-200 my-3"></div>

          <h4 class="text-sm font-bold text-[#0f382f]">
            Compañía Purina
          </h4>
          <p class="mt-2 text-xs text-stone-600 leading-relaxed">
            Su inquebrantable compromiso con el bienestar animal y la nutrición ha tenido un impacto profundo y positivo en la salud y recuperación de nuestros amigos peludos.
          </p>
        </div>

        <div class="mt-4 pt-3 border-t border-stone-100 flex items-center gap-2">
          <span class="w-2 h-2 rounded-full bg-[#a8dc8c]"></span>
          <span class="text-[11px] font-semibold text-stone-500">Nutrición y Salud Digestiva</span>
        </div>
      </div>
    </div>
  </div>
</template>
