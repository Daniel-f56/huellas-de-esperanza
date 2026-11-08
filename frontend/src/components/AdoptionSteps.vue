<template>
  <section id="adoption-steps" class="py-12 sm:py-16 bg-[#efe9dd]/50 border-y border-[#0f382f]/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Encabezado de la Sección -->
      <div class="text-center max-w-2xl mx-auto mb-12 sm:mb-16">
        <span class="text-xs font-bold tracking-[0.2em] uppercase text-[#3b8754] block mb-2">
          PROCESO TRANSPARENTE
        </span>
        <h2 class="text-3xl sm:text-4xl font-extrabold text-[#0f382f] tracking-tight">
          ¿Cómo funciona la adopción responsable?
        </h2>
        <p class="mt-3 text-sm sm:text-base text-stone-600">
          Un proceso guiado, seguro y sin costos ocultos, enfocado siempre en el bienestar tanto de la mascota como de tu familia.
        </p>
      </div>

      <!-- Cuadrícula de 4 Pasos -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 relative">
        <div
          v-for="step in steps"
          :key="step.number"
          class="bg-white rounded-3xl p-6 sm:p-7 border border-stone-200/80 shadow-xs hover:shadow-md transition-all duration-300 flex flex-col justify-between group hover:-translate-y-1"
        >
          <div>
            <!-- Número de paso y badge -->
            <div class="flex items-center justify-between mb-5">
              <span class="text-2xl font-black text-[#a8dc8c] group-hover:text-[#3b8754] transition-colors">
                {{ step.number }}
              </span>
              <div class="w-10 h-10 rounded-2xl bg-[#f6f3eb] group-hover:bg-[#a8dc8c]/30 text-[#0f382f] flex items-center justify-center transition-colors">
                <!-- Icono de Búsqueda -->
                <svg v-if="step.icon === 'search'" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
                <!-- Icono de Formulario -->
                <svg v-else-if="step.icon === 'form'" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2-2z" />
                </svg>
                <!-- Icono de Corazón -->
                <svg v-else-if="step.icon === 'heart'" class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
                <!-- Icono de Hogar -->
                <svg v-else class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
              </div>
            </div>

            <h3 class="text-base sm:text-lg font-bold text-[#0f382f] tracking-tight">
              {{ step.title }}
            </h3>
            <p class="text-xs font-semibold text-[#3b8754] mt-0.5 mb-3">
              {{ step.subtitle }}
            </p>
            <p class="text-xs sm:text-sm text-stone-600 leading-relaxed">
              {{ step.description }}
            </p>
          </div>

          <div class="mt-6 pt-3 border-t border-stone-100 flex items-center justify-between text-[11px] font-semibold text-stone-400">
            <span>Paso {{ step.number }} de 04</span>
            <span class="text-[#a8dc8c] font-black group-hover:translate-x-1 transition-transform">→</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ADOPTION_STEPS } from '../data/pets.js'

const steps = ADOPTION_STEPS
</script>

