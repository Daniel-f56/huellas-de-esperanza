<template>
  <header class="sticky top-0 z-40 bg-[#f6f3eb]/95 backdrop-blur-md border-b border-[#0f382f]/10 transition-all duration-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20 gap-4">
        <!-- Logo de Huellas de Esperanza -->
        <a href="#" class="flex items-center gap-3 shrink-0 group focus:outline-none select-none">
          <div class="w-11 h-11 rounded-2xl bg-[#0f382f] flex items-center justify-center text-[#a8dc8c] shadow-md group-hover:scale-105 transition-transform duration-200 shrink-0">
            <!-- Icono de Huella -->
            <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24">
              <path d="M12 13.5c-1.38 0-2.5 1.12-2.5 2.5 0 .8.4 1.5 1 1.95v.05c.4.3.9.5 1.5.5s1.1-.2 1.5-.5v-.05c.6-.45 1-1.15 1-1.95 0-1.38-1.12-2.5-2.5-2.5zm-4.5-3c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm9 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm-6.5-4c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm4 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2z" />
            </svg>
          </div>
          <div class="flex flex-col whitespace-nowrap">
            <span class="text-lg sm:text-xl font-extrabold tracking-tight text-[#0f382f] leading-tight">
              Huellas<span class="text-[#3b8754]"> de Esperanza</span>
            </span>
            <span class="text-[10px] font-bold tracking-wider text-[#0f382f]/60 uppercase">
              Adopción Responsable
            </span>
          </div>
        </a>

        <!-- Enlaces de Navegación en Escritorio (lg: y superior) -->
        <nav class="hidden lg:flex items-center gap-4 xl:gap-7 text-[14px] xl:text-[15px] font-medium text-[#0f382f]/80">
          <a
            href="#find-a-friend"
            class="hover:text-[#0f382f] transition-colors flex items-center gap-2 py-1 whitespace-nowrap shrink-0 group"
          >
          </a>

          <a
            href="#adoption-steps"
            class="hover:text-[#0f382f] transition-colors py-1 whitespace-nowrap shrink-0"
          >
            Cómo Adoptar
          </a>

          <a
            href="#stats"
            class="hover:text-[#0f382f] transition-colors py-1 whitespace-nowrap shrink-0"
          >
            Impacto
          </a>

          <a
            href="#rescue-rehab"
            class="hover:text-[#0f382f] transition-colors py-1 whitespace-nowrap shrink-0"
          >
            Nuestra Labor
          </a>

          <a
            href="#second-chance"
            class="hover:text-[#0f382f] transition-colors py-1 whitespace-nowrap shrink-0"
          >
            Historias
          </a>

          <a
            href="#partners"
            class="hover:text-[#0f382f] transition-colors py-1 whitespace-nowrap shrink-0"
          >
            Aliados
          </a>

          <a
            href="#contact"
            class="hover:text-[#0f382f] transition-colors py-1 whitespace-nowrap shrink-0"
          >
            Contacto
          </a>
        </nav>

        <!-- Botón de Acción Principal (Derecha) -->
        <div class="hidden sm:flex items-center gap-2.5 shrink-0">
          <!-- Botón de Acceso al Panel Admin -->
          <button
            @click="$emit('open-admin')"
            type="button"
            class="whitespace-nowrap px-4 py-2.5 rounded-full bg-white hover:bg-stone-100 text-[#0f382f] border border-stone-300 text-xs font-bold shadow-2xs hover:shadow-xs transition-all flex items-center gap-1.5 cursor-pointer"
            title="Ingresar al Panel de Gestión"
          >
            <span>⚙️ Panel Admin</span>
          </button>

          <a
            href="#find-a-friend"
            class="whitespace-nowrap px-5 py-2.5 rounded-full bg-[#0f382f] text-[#f6f3eb] hover:bg-[#164d40] text-sm font-bold shadow-sm hover:shadow transition-all duration-200 flex items-center gap-2 group cursor-pointer"
          >
            <span>Quiero Adoptar</span>
            <svg class="w-4 h-4 text-[#a8dc8c] transform group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
            </svg>
          </a>
        </div>

        <!-- Botón Menú Móvil (para pantallas menores a lg: 1024px) -->
        <div class="flex lg:hidden items-center">
          <button
            @click="isMobileMenuOpen = !isMobileMenuOpen"
            type="button"
            class="p-2 rounded-xl text-[#0f382f] hover:bg-[#0f382f]/10 focus:outline-none cursor-pointer"
            aria-label="Abrir menú"
          >
            <svg v-if="!isMobileMenuOpen" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
            <svg v-else class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </div>

      <!-- Menú Desplegable Móvil y Tablet (< 1024px) -->
      <div v-show="isMobileMenuOpen" class="lg:hidden py-4 border-t border-[#0f382f]/10 space-y-1.5 animate-fadeIn">
        <a
          href="#find-a-friend"
          @click="isMobileMenuOpen = false"
          class="flex items-center justify-between px-3.5 py-2.5 rounded-xl font-semibold text-[#0f382f] hover:bg-[#a8dc8c]/30"
        >
          <span>🐾 Encuentra un Amigo</span>
          <span class="text-xs font-bold bg-[#a8dc8c]/50 px-2 py-0.5 rounded-full">8 disponibles</span>
        </a>

        <a
          href="#adoption-steps"
          @click="isMobileMenuOpen = false"
          class="block px-3.5 py-2.5 rounded-xl font-medium text-[#0f382f]/85 hover:bg-[#a8dc8c]/20"
        >
          Cómo Funciona la Adopción
        </a>

        <a
          href="#stats"
          @click="isMobileMenuOpen = false"
          class="block px-3.5 py-2.5 rounded-xl font-medium text-[#0f382f]/85 hover:bg-[#a8dc8c]/20"
        >
          Impacto & Estadísticas
        </a>

        <a
          href="#rescue-rehab"
          @click="isMobileMenuOpen = false"
          class="block px-3.5 py-2.5 rounded-xl font-medium text-[#0f382f]/85 hover:bg-[#a8dc8c]/20"
        >
          Rescate y Rehabilitación
        </a>

        <a
          href="#second-chance"
          @click="isMobileMenuOpen = false"
          class="block px-3.5 py-2.5 rounded-xl font-medium text-[#0f382f]/85 hover:bg-[#a8dc8c]/20"
        >
          Historias de Éxito
        </a>

        <a
          href="#partners"
          @click="isMobileMenuOpen = false"
          class="block px-3.5 py-2.5 rounded-xl font-medium text-[#0f382f]/85 hover:bg-[#a8dc8c]/20"
        >
          Nuestros Aliados
        </a>

        <a
          href="#contact"
          @click="isMobileMenuOpen = false"
          class="block px-3.5 py-2.5 rounded-xl font-medium text-[#0f382f]/85 hover:bg-[#a8dc8c]/20"
        >
          Contacto & Formulario
        </a>

        <div class="pt-2 px-1 space-y-2">
          <button
            @click="$emit('open-admin'); isMobileMenuOpen = false"
            type="button"
            class="block w-full text-center px-4 py-2.5 rounded-full bg-stone-100 border border-stone-300 text-[#0f382f] font-bold text-xs shadow-2xs"
          >
            ⚙️ Abrir Panel de Administrador
          </button>
          <a
            href="#find-a-friend"
            @click="isMobileMenuOpen = false"
            class="block w-full text-center px-4 py-3 rounded-full bg-[#0f382f] text-[#f6f3eb] font-bold text-sm shadow-sm"
          >
            Quiero Adoptar
          </a>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'

defineEmits(['open-admin'])

const isMobileMenuOpen = ref(false)
</script>
