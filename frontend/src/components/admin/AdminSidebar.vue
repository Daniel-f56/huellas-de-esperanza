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
  <!-- Mascotas -->
  <a
    href="#"
    @click.prevent="$emit('change-tab', 'pets')"
    :class="[
      'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
      activeTab === 'pets'
        ? 'bg-[#0f382f] text-white font-bold shadow-sm'
        : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
    ]"
  >
    <span>🐾</span>
    <span class="flex-1">Mascotas</span>
    <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-stone-100 text-stone-600">
      {{ petCount }}
    </span>
  </a>

  <!-- Solicitudes -->
  <a
    href="#"
    @click.prevent="$emit('change-tab', 'applications')"
    :class="[
      'flex items-center gap-3 px-3.5 py-2.5 rounded-xl transition-all cursor-pointer',
      activeTab === 'applications'
        ? 'bg-[#0f382f] text-white font-bold shadow-sm'
        : 'text-stone-600 hover:bg-stone-50 hover:text-[#0f382f]'
    ]"
  >
    <span>📋</span>
    <span>Solicitudes de adopción</span>
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
  defineProps({
  petCount: {
    type: Number,
    default: 0
  },
  activeTab: {
    type: String,
    default: 'pets'
  }
})

defineEmits([
  'go-public',
  'open-create',
  'logout',
  'change-tab'
])
</script>

