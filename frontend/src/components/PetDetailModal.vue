<template>
  <div
    v-if="pet"
    class="fixed inset-0 z-50 overflow-y-auto bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 sm:p-6"
    @click.self="$emit('close')"
  >
    <div class="relative bg-white rounded-3xl max-w-2xl w-full overflow-hidden shadow-2xl border border-stone-200 animate-in fade-in zoom-in-95 duration-200">
      <!-- Botón de Cerrar -->
      <button
        @click="$emit('close')"
        type="button"
        class="absolute top-4 right-4 z-10 w-9 h-9 rounded-full bg-white/90 hover:bg-white text-[#0f382f] flex items-center justify-center shadow-md backdrop-blur-sm transition-transform hover:scale-105 cursor-pointer"
        aria-label="Cerrar modal"
      >
        ✕
      </button>

      <!-- Foto de Cabecera -->
      <div class="relative h-64 sm:h-72 w-full bg-stone-200">
        <img
          :src="petImage"
          :alt="petName"
          class="w-full h-full object-cover"
        />
        <div class="absolute inset-0 bg-gradient-to-t from-black/75 via-black/25 to-transparent"></div>

        <!-- Nombre e Insignia en la Foto -->
        <div class="absolute bottom-4 left-6 right-6 text-white">
          <div class="flex items-center gap-3">
            <h2 class="text-3xl sm:text-4xl font-extrabold tracking-tight">
              {{ petName }}
            </h2>
            <span class="px-3 py-1 rounded-full text-xs font-bold uppercase tracking-wider bg-[#a8dc8c] text-[#0f382f]">
              {{ petSpecies }}
            </span>
          </div>
          <p class="text-sm text-white/90 mt-1 font-medium">
            {{ pet.raza || pet.breed || 'Mestizo' }}
          </p>
        </div>
      </div>

      <!-- Cuerpo del Modal -->
      <div class="p-6 sm:p-8 space-y-6">
        <!-- 3 Insignias Principales (Género, Edad, Tamaño) -->
        <div class="grid grid-cols-3 gap-3">
          <div
            :class="[
              'p-3 rounded-2xl flex flex-col items-center justify-center text-center border',
              petGender === 'Hembra'
                ? 'bg-[#fff2eb] text-[#c05621] border-[#fcd7c6]'
                : 'bg-[#eef8f2] text-[#1e6b4d] border-[#cce7d7]'
            ]"
          >
            <span class="text-xs uppercase tracking-wider font-semibold opacity-75">Género</span>
            <span class="text-sm sm:text-base font-extrabold mt-0.5">{{ petGenderSymbol }} {{ petGender }}</span>
          </div>

          <div class="p-3 rounded-2xl bg-stone-50 border border-stone-200 flex flex-col items-center justify-center text-center">
            <span class="text-xs uppercase tracking-wider font-semibold text-stone-500">Edad</span>
            <span class="text-sm sm:text-base font-extrabold text-[#0f382f] mt-0.5">{{ petAgeFormatted }}</span>
          </div>

          <div class="p-3 rounded-2xl bg-stone-50 border border-stone-200 flex flex-col items-center justify-center text-center">
            <span class="text-xs uppercase tracking-wider font-semibold text-stone-500">Tamaño</span>
            <span class="text-sm sm:text-base font-extrabold text-[#0f382f] mt-0.5">{{ petSizeFormatted }}</span>
          </div>
        </div>

        <!-- Biografía e Historia -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-[#0f382f]/70 mb-2">
            Sobre {{ petName }}
          </h4>
          <p class="text-sm sm:text-base text-stone-700 leading-relaxed">
            {{ pet.descripcion || pet.description || 'Mascota rescatada llena de ternura esperando un hogar responsable.' }}
          </p>
        </div>

        <!-- Estado de Salud y Cuidados -->
        <div>
          <h4 class="text-xs font-bold uppercase tracking-widest text-[#0f382f]/70 mb-2.5">
            Estado de Salud & Cuidados
          </h4>
          <div class="flex flex-wrap gap-2">
            <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold bg-[#eef8f2] text-[#1e6b4d] border border-[#cce7d7]">
              ✓ Vacunación al día
            </span>
            <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold bg-[#eef8f2] text-[#1e6b4d] border border-[#cce7d7]">
              ✓ Esterilizado/a
            </span>
            <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold bg-[#eef8f2] text-[#1e6b4d] border border-[#cce7d7]">
              ✓ Desparasitación al día
            </span>
            <span class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full text-xs font-semibold bg-[#eef8f2] text-[#1e6b4d] border border-[#cce7d7]">
              ✓ Microchip de identificación
            </span>
          </div>
        </div>

        <!-- Botones de Acción -->
        <div class="pt-4 border-t border-stone-200 flex flex-col sm:flex-row items-center gap-3">
          <button
            @click="$emit('adopt', pet)"
            type="button"
            class="w-full sm:flex-1 py-3.5 px-6 rounded-full bg-[#0f382f] text-white hover:bg-[#164e41] font-bold text-sm shadow-md hover:shadow-lg transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer"
          >
            <span>Iniciar Solicitud de Adopción</span>
            <span class="text-[#a8dc8c]">→</span>
          </button>
          <button
            @click="$emit('close')"
            type="button"
            class="w-full sm:w-auto py-3.5 px-5 rounded-full border border-stone-300 text-stone-600 hover:bg-stone-50 font-semibold text-sm transition-colors cursor-pointer"
          >
            Seguir explorando
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

defineEmits(['close', 'adopt'])

const petName = computed(() => props.pet?.nombre || props.pet?.name || 'Amigo')

const petImage = computed(() => {
  if (props.pet?.foto_url) return props.pet.foto_url
  if (props.pet?.image) return props.pet.image
  return 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80'
})

const petSpecies = computed(() => {
  const esp = (props.pet?.especie || props.pet?.species || 'perro').toLowerCase()
  return esp === 'gato' ? 'Gato' : 'Perro'
})

const petGender = computed(() => {
  const sx = (props.pet?.sexo || props.pet?.gender || 'hembra').toLowerCase()
  return sx === 'macho' ? 'Macho' : 'Hembra'
})

const petGenderSymbol = computed(() => {
  return petGender.value === 'Macho' ? '♂' : '♀'
})

const petAgeFormatted = computed(() => {
  if (props.pet?.edad !== undefined && typeof props.pet.edad === 'number') {
    const meses = props.pet.edad
    if (meses >= 12) {
      const anios = Math.floor(meses / 12)
      return `${anios} ${anios === 1 ? 'año' : 'años'}`
    }
    return `${meses} meses`
  }
  return props.pet?.age || '1 año'
})

const petSizeFormatted = computed(() => {
  if (props.pet?.tamano) {
    const t = props.pet.tamano.toLowerCase()
    if (t === 'pequeño' || t === 'pequeno') return 'Pequeño'
    if (t === 'mediano') return 'Mediano'
    if (t === 'grande') return 'Grande'
    return props.pet.tamano
  }
  return props.pet?.weight || 'Mediano'
})
</script>
