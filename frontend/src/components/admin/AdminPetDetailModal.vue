<template>
  <div
    v-if="pet"
    class="fixed inset-0 z-50 overflow-y-auto bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 sm:p-6"
    @click.self="$emit('close')"
  >
    <div class="relative bg-white rounded-3xl max-w-lg w-full overflow-hidden shadow-2xl border border-stone-200 animate-in fade-in zoom-in-95 duration-200">
      <!-- Botón de Cerrar -->
      <button
        @click="$emit('close')"
        type="button"
        class="absolute top-4 right-4 z-10 w-8 h-8 rounded-full bg-white/80 hover:bg-white text-[#0f382f] flex items-center justify-center shadow-md backdrop-blur-sm transition-transform hover:scale-105 cursor-pointer"
      >
        ✕
      </button>

      <!-- Cabecera con Foto -->
      <div class="relative h-48 w-full bg-stone-200">
        <img
          :src="petImage"
          :alt="pet.nombre"
          class="w-full h-full object-cover"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent"></div>

        <div class="absolute bottom-4 left-5 right-5 text-white flex items-end justify-between">
          <div>
            <span class="text-xs font-mono font-bold bg-white/20 px-2 py-0.5 rounded-md backdrop-blur-xs text-[#a8dc8c]">
              ID: #{{ formatId(pet.id) }}
            </span>
            <h3 class="text-2xl font-black mt-1">
              {{ pet.nombre }}
            </h3>
            <p class="text-xs text-white/80">{{ pet.raza }}</p>
          </div>

          <!-- Badge de Estado -->
          <span
            :class="[
              'px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider',
              statusClasses(pet.estado)
            ]"
          >
            {{ formatStatus(pet.estado) }}
          </span>
        </div>
      </div>

      <!-- Ficha de Datos Técnicos en Base de Datos -->
      <div class="p-6 space-y-4">
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
          <div class="p-2.5 rounded-xl bg-stone-50 border border-stone-200/80 text-center">
            <span class="text-[10px] font-bold uppercase text-stone-400 block">Especie</span>
            <span class="text-xs font-bold text-[#0f382f] capitalize">{{ pet.especie }}</span>
          </div>

          <div class="p-2.5 rounded-xl bg-stone-50 border border-stone-200/80 text-center">
            <span class="text-[10px] font-bold uppercase text-stone-400 block">Sexo</span>
            <span class="text-xs font-bold text-[#0f382f] capitalize">{{ pet.sexo }}</span>
          </div>

          <div class="p-2.5 rounded-xl bg-stone-50 border border-stone-200/80 text-center">
            <span class="text-[10px] font-bold uppercase text-stone-400 block">Edad</span>
            <span class="text-xs font-bold text-[#0f382f]">{{ formatAge(pet.edad) }}</span>
          </div>

          <div class="p-2.5 rounded-xl bg-stone-50 border border-stone-200/80 text-center">
            <span class="text-[10px] font-bold uppercase text-stone-400 block">Tamaño</span>
            <span class="text-xs font-bold text-[#0f382f] capitalize">{{ pet.tamano }}</span>
          </div>
        </div>

        <!-- Descripción -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-wider text-stone-500 mb-1">
            Descripción
          </h4>
          <p class="text-xs sm:text-sm text-stone-700 bg-stone-50 p-3 rounded-xl border border-stone-200/60 leading-relaxed">
            {{ pet.descripcion || 'Sin descripción registrada.' }}
          </p>
        </div>

        <!-- Metadatos de Base de Datos -->
        <div class="p-3 rounded-xl bg-stone-50 border border-stone-200/60 text-xs text-stone-600 space-y-1">
          <div class="flex justify-between">
            <span class="text-stone-400">Fecha de Registro:</span>
            <span class="font-mono font-medium text-[#0f382f]">{{ formatDate(pet.fecha_registro) }}</span>
          </div>
          <div class="flex justify-between">
            <span class="text-stone-400">Estado de Visibilidad:</span>
            <span class="font-medium text-[#0f382f]">
              {{ pet.estado === 'disponible' ? 'Visible en "Encuentra a un amigo"' : 'Oculto del catálogo público' }}
            </span>
          </div>
        </div>

        <!-- Botones de Acción -->
        <div class="pt-3 border-t border-stone-100 flex items-center justify-end gap-2">
          <button
            @click="$emit('edit', pet)"
            type="button"
            class="px-4 py-2 rounded-xl bg-[#0f382f] text-white text-xs font-bold hover:bg-[#164e41] transition-colors flex items-center gap-1.5 cursor-pointer"
          >
            <svg class="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
            </svg>
            <span>Editar Mascota</span>
          </button>
          <button
            @click="$emit('close')"
            type="button"
            class="px-4 py-2 rounded-xl border border-stone-300 text-stone-600 text-xs font-semibold hover:bg-stone-50 transition-colors cursor-pointer"
          >
            Cerrar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  pet: {
    type: Object,
    default: null
  }
})

defineEmits(['close', 'edit'])

const petImage = computed(() => {
  if (props.pet?.foto_url) return props.pet.foto_url
  if (props.pet?.image) return props.pet.image
  return 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80'
})

const formatId = (id) => {
  if (!id) return '001'
  return String(id).padStart(3, '0')
}

const formatAge = (meses) => {
  if (!meses) return 'No especificada'
  if (meses >= 12) {
    const anios = Math.floor(meses / 12)
    return `${anios} ${anios === 1 ? 'año' : 'años'} (${meses} m.)`
  }
  return `${meses} meses`
}

const formatDate = (isoString) => {
  if (!isoString) return 'No registrada'
  try {
    const d = new Date(isoString)
    return d.toLocaleString('es-CO', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  } catch {
    return isoString
  }
}

const formatStatus = (st) => {
  if (st === 'disponible') return 'Disponible'
  if (st === 'adoptado') return 'Adoptado'
  if (st === 'en_tratamiento') return 'En Tratamiento'
  return st || 'Disponible'
}

const statusClasses = (st) => {
  if (st === 'disponible') return 'bg-[#a8dc8c] text-[#0f382f]'
  if (st === 'adoptado') return 'bg-blue-500 text-white'
  if (st === 'en_tratamiento') return 'bg-amber-400 text-[#0f382f]'
  return 'bg-stone-200 text-stone-800'
}
</script>

