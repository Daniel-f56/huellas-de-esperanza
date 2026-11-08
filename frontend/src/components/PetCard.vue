<template>
  <div
    @click="$emit('select', pet)"
    class="group cursor-pointer bg-[#faf8f5] rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col border border-stone-200/60 hover:-translate-y-1"
  >
    <!-- Contenedor de Imagen de la Mascota -->
    <div class="relative w-full aspect-[4/3] overflow-hidden bg-stone-200">
      <img
        :src="petImage"
        :alt="petName"
        class="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500"
        loading="lazy"
      />
      <!-- Badge de ver perfil al hacer hover -->
      <div class="absolute inset-0 bg-black/20 opacity-0 group-hover:opacity-100 transition-opacity duration-200 flex items-center justify-center">
        <span class="px-3.5 py-1.5 rounded-full bg-white/95 text-[#0f382f] text-xs font-bold shadow backdrop-blur-sm transform translate-y-2 group-hover:translate-y-0 transition-transform duration-200">
          Ver Perfil Completo 🐾
        </span>
      </div>

      <!-- Tag de Estado / Disponibilidad -->
      <div class="absolute top-2.5 left-2.5">
        <span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-white/95 text-[#0f382f] shadow-sm backdrop-blur-sm">
          <span class="w-1.5 h-1.5 rounded-full bg-[#2b8a3e]"></span>
          {{ pet.estado === 'disponible' ? 'En Adopción' : (pet.estado || 'Disponible') }}
        </span>
      </div>

      <!-- Botón de Favorito (Corazón) -->
      <button
        @click.stop="$emit('toggle-favorite', pet.id)"
        type="button"
        class="absolute top-2.5 right-2.5 w-8 h-8 rounded-full bg-white/90 hover:bg-white flex items-center justify-center shadow-sm backdrop-blur-sm transition-transform hover:scale-110 z-10 cursor-pointer"
        :aria-label="isFavorite ? 'Quitar de favoritos' : 'Agregar a favoritos'"
      >
        <svg
          class="w-4 h-4 transition-colors duration-200"
          :class="isFavorite ? 'text-[#d97736] fill-current' : 'text-stone-500 fill-none stroke-current'"
          viewBox="0 0 24 24"
          stroke-width="2"
        >
          <path stroke-linecap="round" stroke-linejoin="round" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
        </svg>
      </button>
    </div>

    <!-- Pie de Tarjeta con Datos de la Mascota -->
    <div class="p-3.5 flex flex-col justify-between flex-1 bg-white">
      <!-- Fila Superior: Nombre y Tag de Especie -->
      <div class="flex items-center justify-between mb-2.5">
        <h3 class="text-base sm:text-lg font-bold text-[#0f382f] tracking-tight group-hover:text-[#1c6b54] transition-colors truncate">
          {{ petName }}
        </h3>

        <!-- Insignia de Especie (Perro o Gato) -->
        <div class="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg border border-stone-200 text-stone-600 bg-stone-50 text-xs font-medium shrink-0">
          <!-- Icono de Perro -->
          <svg v-if="petSpecies === 'Perro'" class="w-3.5 h-3.5 text-[#0f382f]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z" />
          </svg>
          <!-- Icono de Gato -->
          <svg v-else class="w-3.5 h-3.5 text-[#0f382f]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m0 0l-4-4m4 4l4-4M3 9l9-6 9 6" />
          </svg>
          <span>{{ petSpecies }}</span>
        </div>
      </div>

      <!-- Fila Inferior: 3 Píldoras (Género, Edad, Tamaño) -->
      <div class="grid grid-cols-3 gap-1.5 pt-1">
        <!-- Píldora de Género -->
        <span
          :class="[
            'inline-flex items-center justify-center gap-0.5 py-1 px-1.5 rounded-full text-[11px] font-semibold border truncate',
            petGender === 'Hembra'
              ? 'bg-[#fff2eb] text-[#c05621] border-[#fcd7c6]'
              : 'bg-[#eef8f2] text-[#1e6b4d] border-[#cce7d7]'
          ]"
        >
          <span class="text-xs leading-none font-bold">{{ petGenderSymbol }}</span>
          <span class="truncate">{{ petGender }}</span>
        </span>

        <!-- Píldora de Edad -->
        <span class="inline-flex items-center justify-center py-1 px-1.5 rounded-full text-[11px] font-medium text-stone-600 bg-stone-50 border border-stone-200 truncate">
          {{ petAgeFormatted }}
        </span>

        <!-- Píldora de Tamaño / Peso -->
        <span class="inline-flex items-center justify-center py-1 px-1.5 rounded-full text-[11px] font-medium text-stone-600 bg-stone-50 border border-stone-200 truncate">
          {{ petSizeFormatted }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  pet: {
    type: Object,
    required: true
  },
  isFavorite: {
    type: Boolean,
    default: false
  }
})

defineEmits(['select', 'toggle-favorite'])

const petName = computed(() => props.pet.nombre || props.pet.name || 'Amigo')

const petImage = computed(() => {
  if (props.pet.foto_url) return props.pet.foto_url
  if (props.pet.image) return props.pet.image
  return 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80'
})

const petSpecies = computed(() => {
  const esp = (props.pet.especie || props.pet.species || 'perro').toLowerCase()
  return esp === 'gato' ? 'Gato' : 'Perro'
})

const petGender = computed(() => {
  const sx = (props.pet.sexo || props.pet.gender || 'hembra').toLowerCase()
  return sx === 'macho' ? 'Macho' : 'Hembra'
})

const petGenderSymbol = computed(() => {
  return petGender.value === 'Macho' ? '♂' : '♀'
})

const petAgeFormatted = computed(() => {
  if (props.pet.edad !== undefined && typeof props.pet.edad === 'number') {
    const meses = props.pet.edad
    if (meses >= 12) {
      const anios = Math.floor(meses / 12)
      return `${anios} ${anios === 1 ? 'año' : 'años'}`
    }
    return `${meses} meses`
  }
  return props.pet.age || '1 año'
})

const petSizeFormatted = computed(() => {
  if (props.pet.tamano) {
    const t = props.pet.tamano.toLowerCase()
    if (t === 'pequeño' || t === 'pequeno') return 'Pequeño'
    if (t === 'mediano') return 'Mediano'
    if (t === 'grande') return 'Grande'
    return props.pet.tamano
  }
  return props.pet.weight || 'Mediano'
})
</script>
