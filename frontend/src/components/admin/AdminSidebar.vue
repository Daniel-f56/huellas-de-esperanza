<template>
  <aside class="w-64 bg-white border-r border-stone-200/80 flex flex-col justify-between shrink-0 select-none min-h-screen">
    <div>
      <!-- Cabecera de la Barra Lateral con Logo -->
      <div class="h-20 flex items-center px-6 border-b border-stone-100 gap-3">
        <div class="w-10 h-10 rounded-2xl bg-[#0f382f] flex items-center justify-center text-[#a8dc8c] shadow-sm shrink-0">
          <!-- Icono de Huella -->
          <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24">
            <path d="M12 13.5c-1.38 0-2.5 1.12-2.5 2.5 0 .8.4 1.5 1 1.95v.05c.4.3.9.5 1.5.5s1.1-.2 1.5-.5v-.05c.6-.45 1-1.15 1-1.95 0-1.38-1.12-2.5-2.5-2.5zm-4.5-3c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm9 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm-6.5-4c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm4 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2z" />
          </svg>
        </div>
        <div class="flex flex-col">
          <span class="text-base font-extrabold text-[#0f382f] leading-tight tracking-tight">
            Huellas Admin
          </span>
          <span class="text-[10px] uppercase font-bold text-stone-400 tracking-wider">
            Panel de Gestión
          </span>
        </div>
      </div>

      <!-- Menú de Navegación del Administrador -->
      <nav class="p-4 space-y-1 text-sm font-medium">
        <!-- 1. Dashboard / Resumen -->
        <a
          href="#"
          @click.prevent="activeTab = 'dashboard'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'dashboard'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0 opacity-80" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
          </svg>
          <span>Dashboard</span>
        </a>

        <!-- 2. Animales / Mascotas (Activo) -->
        <a
          href="#"
          @click.prevent="activeTab = 'pets'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'pets'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0" :class="activeTab === 'pets' ? 'text-[#a8dc8c]' : 'text-stone-500'" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
          </svg>
          <span class="flex-1">Mascotas</span>
          <span class="px-2 py-0.5 rounded-full text-[10px] font-bold" :class="activeTab === 'pets' ? 'bg-[#a8dc8c] text-[#0f382f]' : 'bg-stone-100 text-stone-600'">
            {{ petCount }}
          </span>
        </a>

        <!-- 3. Registro de Ingreso -->
        <a
          href="#"
          @click.prevent="$emit('open-create')"
          class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-stone-600 hover:bg-stone-50 hover:text-[#0f382f] transition-all cursor-pointer"
        >
          <svg class="w-5 h-5 shrink-0 text-stone-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span>Nuevo Registro</span>
        </a>

        <!-- 4. Adopciones -->
        <a
          href="#"
          @click.prevent="activeTab = 'adoptions'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'adoptions'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0 text-stone-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
          </svg>
          <span>Adopciones</span>
        </a>

        <!-- 5. Solicitudes / Adoptantes -->
        <a
          href="#"
          @click.prevent="activeTab = 'applicants'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'applicants'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0 text-stone-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z" />
          </svg>
          <span>Adoptantes</span>
        </a>

        <!-- 6. Calendario & Citas -->
        <a
          href="#"
          @click.prevent="activeTab = 'calendar'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'calendar'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0 text-stone-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
          </svg>
          <span>Calendario</span>
        </a>

        <!-- 7. Tareas & Cuidados -->
        <a
          href="#"
          @click.prevent="activeTab = 'tasks'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'tasks'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0 text-stone-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4" />
          </svg>
          <span>Tareas</span>
        </a>

        <!-- 8. Contratos -->
        <a
          href="#"
          @click.prevent="activeTab = 'contracts'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'contracts'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0 text-stone-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2-2z" />
          </svg>
          <span>Contratos</span>
        </a>

        <!-- 9. Reportes -->
        <a
          href="#"
          @click.prevent="activeTab = 'reports'"
          :class="[
            'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
            activeTab === 'reports'
              ? 'bg-[#0f382f] text-white font-bold shadow-sm'
              : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
          ]"
        >
          <svg class="w-5 h-5 shrink-0 text-stone-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
          </svg>
          <span>Reportes</span>
        </a>
      </nav>
    </div>

    <!-- Zona Inferior de la Barra Lateral -->
    <div class="p-4 border-t border-stone-100 space-y-1.5 text-sm font-medium">
      <a
        href="#"
        @click.prevent="$emit('go-public')"
        class="flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-stone-700 hover:bg-[#a8dc8c]/25 hover:text-[#0f382f] transition-all cursor-pointer"
      >
        <svg class="w-5 h-5 shrink-0 text-[#0f382f]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        <span>Volver a la Web</span>
      </a>

      <button
        @click="$emit('logout')"
        type="button"
        class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-red-600 hover:bg-red-50 transition-all cursor-pointer text-left"
      >
        <svg class="w-5 h-5 shrink-0 text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
        </svg>
        <span>Cerrar Sesión</span>
      </button>
    </div>
  </aside>
</template>

<script setup>
import { ref } from 'vue'

defineProps({
  petCount: {
    type: Number,
    default: 0
  }
})

defineEmits(['go-public', 'open-create', 'logout'])

const activeTab = ref('pets')
</script>

