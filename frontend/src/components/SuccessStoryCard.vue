<template>
  <div class="bg-[#a8dc8c] text-[#0f382f] rounded-3xl p-8 sm:p-10 shadow-sm border border-[#0f382f]/10 flex flex-col justify-between transition-all duration-300 hover:shadow-md">
    <div>
      <!-- Categoría e Insignia -->
      <div class="flex items-center justify-between">
        <span class="text-xs font-bold uppercase tracking-wider bg-[#0f382f]/10 px-3 py-1 rounded-full text-[#0f382f]">
          Historia de Éxito
        </span>
        <span class="text-xs font-medium text-[#0f382f]/70">
          Adopción responsable
        </span>
      </div>

      <!-- Título en Español -->
      <h3 class="text-2xl sm:text-3xl font-extrabold tracking-tight text-[#0f382f] mt-4">
        Una Segunda Oportunidad
      </h3>

      <!-- Fotos destacadas del rescate y nuevo hogar -->
      <div class="grid grid-cols-2 gap-3 my-5">
        <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-inner border border-[#0f382f]/10">
          <img
            src="https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=600&q=80"
            alt="Voluntaria con perro rescatado"
            class="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
          />
        </div>
        <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-inner border border-[#0f382f]/10">
          <img
            src="https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80"
            alt="Perro feliz en su nuevo hogar"
            class="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
          />
        </div>
      </div>

      <!-- Cita y Relato en Español -->
      <p class="text-sm sm:text-base font-medium text-[#0f382f]/90 leading-relaxed italic">
        "Llegó a nosotros siendo un perro adulto, con un pasado que hablaba por sí solo. Pasó por momentos difíciles, pero con paciencia y cariño descubrió lo que es sentirse seguro en una familia para siempre."
      </p>

      <p class="mt-3 text-xs sm:text-sm text-[#0f382f]/80 leading-relaxed">
        Llegó con miedo y desconfianza, pero tras semanas de rehabilitación emocional y cuidados veterinarios, hoy comparte una vida plena y llena de juegos junto a sus adoptantes.
      </p>
    </div>

    <!-- Pie de tarjeta con adoptantes -->
    <div class="mt-6 pt-4 border-t border-[#0f382f]/15 flex items-center justify-between">
      <div class="flex items-center gap-2.5">
        <div class="w-8 h-8 rounded-full bg-[#0f382f] text-[#a8dc8c] flex items-center justify-center font-bold text-xs">
          ♥
        </div>
        <div>
          <p class="text-xs font-bold text-[#0f382f] leading-none">Familia Martínez</p>
          <p class="text-[11px] text-[#0f382f]/70">Adoptantes de Max</p>
        </div>
      </div>

      <a href="#find-a-friend" class="text-xs font-bold text-[#0f382f] hover:underline">
        Adoptar ahora →
      </a>
    </div>
  </div>
</template>
