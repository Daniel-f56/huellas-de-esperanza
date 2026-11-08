<template>
  <section id="find-a-friend" class="py-10 sm:py-16">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <!-- Contenedor principal Verde Bosque Profundo -->
      <div class="bg-[#0f382f] text-white rounded-3xl sm:rounded-[36px] p-6 sm:p-10 lg:p-12 shadow-2xl relative overflow-hidden border border-[#164e41]">
        
        <!-- Encabezado de la Sección -->
        <div class="text-center max-w-2xl mx-auto mb-8 sm:mb-10">
          <span class="text-xs sm:text-sm font-bold tracking-[0.2em] uppercase text-[#a8dc8c] block mb-2">
            ENCUENTRA UN AMIGO
          </span>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-white">
            ¡Descubre a tu nuevo mejor amigo!
          </h2>
          <p class="mt-3 text-sm sm:text-base text-white/75">
            Conoce a nuestros rescatados listos para ser adoptados. Cada uno de ellos tiene una historia única y mucho amor para entregarte.
          </p>

          <!-- Barra de Búsqueda Dinámica -->
          <div class="mt-6 max-w-md mx-auto relative">
            <div class="relative">
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Buscar por nombre, raza o personalidad..."
                class="w-full pl-11 pr-10 py-3 rounded-full bg-white/10 text-white placeholder-white/50 text-xs sm:text-sm border border-white/20 focus:outline-none focus:ring-2 focus:ring-[#a8dc8c] focus:bg-white/15 transition-all shadow-inner"
              />
              <!-- Icono de lupa -->
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-white/60">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
              <!-- Botón limpiar búsqueda -->
              <button
                v-if="searchQuery"
                @click="searchQuery = ''"
                type="button"
                class="absolute inset-y-0 right-0 pr-4 flex items-center text-white/60 hover:text-white cursor-pointer"
              >
                ✕
              </button>
            </div>
          </div>

          <!-- Pestañas de Filtrado Interactivas -->
          <div class="mt-5 flex flex-wrap items-center justify-center gap-2 sm:gap-2.5">
            <button
              v-for="tab in filterTabs"
              :key="tab.id"
              @click="activeFilter = tab.id"
              type="button"
              :class="[
                'px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition-all duration-200 cursor-pointer flex items-center gap-1.5',
                activeFilter === tab.id
                  ? 'bg-[#a8dc8c] text-[#0f382f] shadow-md scale-105'
                  : 'bg-white/10 text-white/80 hover:bg-white/20 hover:text-white'
              ]"
            >
              <span>{{ tab.label }}</span>
            </button>

            <!-- Pestaña de Favoritos si existen -->
            <button
              v-if="favorites.length > 0"
              @click="activeFilter = 'favorites'"
              type="button"
              :class="[
                'px-4 py-2 rounded-full text-xs sm:text-sm font-semibold transition-all duration-200 cursor-pointer flex items-center gap-1.5',
                activeFilter === 'favorites'
                  ? 'bg-[#d97736] text-white shadow-md scale-105'
                  : 'bg-white/10 text-white/80 hover:bg-white/20 hover:text-white'
              ]"
            >
              <span>♥ Mis Favoritos ({{ favorites.length }})</span>
            </button>
          </div>
        </div>

        <!-- Grid de las Tarjetas de Mascotas (2 filas x 4 columnas en pantallas grandes) -->
        <div v-if="filteredPets.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-5">
          <PetCard
            v-for="pet in displayedPets"
            :key="pet.id"
            :pet="pet"
            :is-favorite="favorites.includes(pet.id)"
            @select="$emit('select-pet', pet)"
            @toggle-favorite="$emit('toggle-favorite', $event)"
          />
        </div>

        <!-- Estado vacío si el filtro no tiene resultados -->
        <div v-else class="py-16 text-center text-white/70">
          <p class="text-lg">No encontramos mascotas con este criterio de búsqueda.</p>
          <button
            @click="resetFilters"
            class="mt-3 px-5 py-2 rounded-full bg-[#a8dc8c] text-[#0f382f] text-xs font-bold hover:bg-[#bcebb4] transition-colors cursor-pointer"
          >
            Ver todos los amigos disponibles
          </button>
        </div>

        <!-- Enlace Inferior: Ver Más Amigos en Adopción → -->
        <div class="mt-10 sm:mt-12 text-center">
          <button
            @click="toggleShowAll"
            type="button"
            class="inline-flex items-center gap-2 text-sm sm:text-base font-semibold text-[#d97736] hover:text-[#f3985a] transition-all duration-200 group cursor-pointer"
          >
            <!-- Icono de Huella Cálida -->
            <svg class="w-5 h-5 fill-current group-hover:rotate-12 transition-transform duration-200" viewBox="0 0 24 24">
              <path d="M12 13.5c-1.38 0-2.5 1.12-2.5 2.5 0 .8.4 1.5 1 1.95v.05c.4.3.9.5 1.5.5s1.1-.2 1.5-.5v-.05c.6-.45 1-1.15 1-1.95 0-1.38-1.12-2.5-2.5-2.5zm-4.5-3c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm9 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm-6.5-4c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm4 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2z" />
            </svg>
            <span class="tracking-wide underline underline-offset-4 decoration-current/40 group-hover:decoration-current">
              {{ showAllPets ? 'Mostrar Menos Amigos' : 'Ver Más Amigos en Adopción' }}
            </span>
            <span class="transform group-hover:translate-x-1.5 transition-transform duration-200">
              →
            </span>
          </button>
        </div>

        <!-- Efectos decorativos de fondo sutiles -->
        <div class="absolute -top-24 -left-24 w-80 h-80 rounded-full bg-[#a8dc8c]/5 blur-3xl pointer-events-none"></div>
        <div class="absolute -bottom-24 -right-24 w-80 h-80 rounded-full bg-[#a8dc8c]/5 blur-3xl pointer-events-none"></div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue'
import PetCard from './PetCard.vue'

const props = defineProps({
  pets: {
    type: Array,
    required: true
  },
  favorites: {
    type: Array,
    default: () => []
  }
})

defineEmits(['select-pet', 'open-catalog', 'toggle-favorite'])

const activeFilter = ref('all')
const searchQuery = ref('')
const showAllPets = ref(false)

const filterTabs = [
  { id: 'all', label: 'Todos' },
  { id: 'dog', label: '🐶 Perros' },
  { id: 'cat', label: '🐱 Gatos' },
  { id: 'small', label: '🐾 Pequeños (< 5kg)' },
  { id: 'senior', label: '🌿 Adultos & Senior (> 5 años)' }
]

const filteredPets = computed(() => {
  // En la vista pública solo mostramos animales con estado 'disponible'
  let list = props.pets.filter(p => !p.estado || p.estado.toLowerCase() === 'disponible')

  // Filtro por término de búsqueda (nombre, raza o descripción)
  if (searchQuery.value.trim() !== '') {
    const q = searchQuery.value.toLowerCase().trim()
    list = list.filter(p => {
      const name = (p.nombre || p.name || '').toLowerCase()
      const breed = (p.raza || p.breed || '').toLowerCase()
      const desc = (p.descripcion || p.description || '').toLowerCase()
      return name.includes(q) || breed.includes(q) || desc.includes(q)
    })
  }

  // Filtro por pestaña activa
  if (activeFilter.value === 'dog') {
    list = list.filter(p => (p.especie || p.species || '').toLowerCase() === 'perro')
  } else if (activeFilter.value === 'cat') {
    list = list.filter(p => (p.especie || p.species || '').toLowerCase() === 'gato')
  } else if (activeFilter.value === 'small') {
    list = list.filter(p => {
      const isSmallSize = (p.tamano || '').toLowerCase() === 'pequeño' || (p.tamano || '').toLowerCase() === 'pequeno'
      const weightNum = parseFloat(p.weight)
      return isSmallSize || (!isNaN(weightNum) && weightNum < 5)
    })
  } else if (activeFilter.value === 'senior') {
    list = list.filter(p => {
      // 5 años o más (60 meses)
      const isSeniorMonths = typeof p.edad === 'number' && p.edad >= 60
      const ageNum = parseInt(p.age)
      return isSeniorMonths || (!isNaN(ageNum) && ageNum >= 5)
    })
  } else if (activeFilter.value === 'favorites') {
    list = list.filter(p => props.favorites.includes(p.id))
  }

  return list
})

const displayedPets = computed(() => {
  if (showAllPets.value || searchQuery.value.trim() !== '' || activeFilter.value !== 'all') {
    return filteredPets.value
  }
  return filteredPets.value.slice(0, 8)
})

const toggleShowAll = () => {
  showAllPets.value = !showAllPets.value
}

const resetFilters = () => {
  activeFilter.value = 'all'
  searchQuery.value = ''
}
</script>
