<template>
  <div class="bg-white rounded-3xl p-8 sm:p-10 shadow-sm border border-stone-200/80 flex flex-col justify-between transition-all duration-300 hover:shadow-md">
    <!-- Zona Superior con la Ilustración del Perro Manchado -->
    <div class="flex flex-col items-center sm:items-start">
      <!-- Ilustración del perro blanco con manchas en estiramiento (downward dog) -->
      <div class="w-full flex justify-center py-4 sm:py-6">
        <svg
          class="w-48 h-32 sm:w-56 sm:h-36 text-[#0f382f]"
          viewBox="0 0 200 130"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <!-- Cuerpo del perro en pose de estiramiento juguetón -->
          <path
            d="M 50 115 
               C 50 85, 60 45, 95 45
               C 120 45, 145 75, 175 105
               L 185 105
               C 185 112, 175 115, 168 115
               C 155 115, 145 95, 135 85
               C 125 78, 105 75, 90 90
               C 78 102, 75 115, 70 115
               Z"
            fill="#ffffff"
            stroke="#0f382f"
            stroke-width="3"
            stroke-linejoin="round"
          />

          <!-- Pata trasera derecha -->
          <path
            d="M 68 85 L 60 115"
            stroke="#0f382f"
            stroke-width="3"
            stroke-linecap="round"
          />

          <!-- Cola levantada y contenta -->
          <path
            d="M 85 45 C 80 30, 85 15, 92 10 C 94 9, 97 12, 95 18 C 93 25, 95 38, 93 45"
            fill="#0f382f"
            stroke="#0f382f"
            stroke-width="2"
            stroke-linecap="round"
          />

          <!-- Cabeza inclinada mirando hacia adelante -->
          <path
            d="M 155 90
               C 165 80, 180 75, 188 85
               C 193 90, 195 98, 188 104
               C 180 108, 165 106, 155 102"
            fill="#ffffff"
            stroke="#0f382f"
            stroke-width="3"
            stroke-linejoin="round"
          />

          <!-- Oreja caída -->
          <path
            d="M 168 80 C 160 70, 150 75, 154 88 C 157 96, 165 92, 168 80 Z"
            fill="#0f382f"
          />

          <!-- Ojo alegre con brillo -->
          <ellipse cx="178" cy="88" rx="4.5" ry="5.5" fill="#0f382f" />
          <circle cx="177" cy="86" r="1.5" fill="#ffffff" />

          <!-- Nariz y sonrisa -->
          <circle cx="190" cy="92" r="3" fill="#0f382f" />
          <path
            d="M 188 95 C 185 98, 180 97, 178 95"
            stroke="#0f382f"
            stroke-width="2"
            stroke-linecap="round"
          />

          <!-- Bigotes divertidos -->
          <path d="M 183 93 L 178 92" stroke="#0f382f" stroke-width="1.5" stroke-linecap="round" />
          <path d="M 183 95 L 177 96" stroke="#0f382f" stroke-width="1.5" stroke-linecap="round" />

          <!-- Manchas negras en el cuerpo -->
          <ellipse cx="108" cy="62" rx="7" ry="9" fill="#0f382f" />
          <circle cx="128" cy="74" r="5" fill="#0f382f" />
          <ellipse cx="78" cy="68" rx="6" ry="8" fill="#0f382f" />
          <circle cx="148" cy="92" r="3.5" fill="#0f382f" />

          <!-- Patas delanteras estiradas en el piso -->
          <path
            d="M 160 105 L 180 115"
            stroke="#0f382f"
            stroke-width="3"
            stroke-linecap="round"
          />
          <path
            d="M 148 102 L 165 115"
            stroke="#0f382f"
            stroke-width="3"
            stroke-linecap="round"
          />

          <!-- Línea punteada de suelo -->
          <path
            d="M 45 116 C 85 116, 150 116, 190 116"
            stroke="#0f382f"
            stroke-width="2"
            stroke-dasharray="3 3"
            stroke-linecap="round"
            opacity="0.3"
          />
        </svg>
      </div>

      <!-- Título en Español -->
      <h3 class="text-xl sm:text-2xl font-extrabold text-[#0f382f] tracking-tight mt-2">
        Rescate y Rehabilitación
      </h3>

      <!-- Subtítulo en Español -->
      <span class="text-xs font-bold uppercase tracking-wider text-[#3b8754] mt-1">
        Nuestra Labor Diaria
      </span>

      <!-- Descripción en Español -->
      <p class="mt-4 text-stone-600 text-sm sm:text-base leading-relaxed">
        Rescatamos animales de situaciones de peligro, abandono o negligencia y les brindamos atención médica especializada, refugio seguro y nutrición de calidad.
      </p>

      <p class="mt-2 text-stone-500 text-xs sm:text-sm leading-relaxed">
        Cada mascota rescatada pasa por un protocolo veterinario integral: vacunación, desparasitación, esterilización y evaluación de comportamiento antes de ser entregada en adopción.
      </p>
    </div>

    <!-- Barra inferior -->
    <div class="mt-6 pt-4 border-t border-stone-100 flex items-center justify-between">
      <span class="inline-flex items-center gap-1.5 text-xs font-semibold text-[#0f382f]">
        <span class="w-2 h-2 rounded-full bg-[#a8dc8c]"></span>
        100% esterilizados y vacunados
      </span>
      <a href="#stats" class="text-xs font-bold text-[#0f382f] hover:text-[#3b8754] flex items-center gap-1">
        Conoce el protocolo →
      </a>
    </div>
  </div>
</template>
