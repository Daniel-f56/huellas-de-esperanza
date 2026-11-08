<template>
  <div class="min-h-screen bg-[#f6f3eb] flex text-[#0f382f]">
    <!-- Barra Lateral Izquierda (Admin Sidebar) -->
    <AdminSidebar
      :pet-count="pets.length"
      @go-public="$emit('go-public')"
      @open-create="openCreateModal"
      @logout="$emit('logout')"
    />

    <!-- Contenido Principal del Dashboard -->
    <div class="flex-1 flex flex-col min-w-0 overflow-y-auto">
      <!-- Barra Superior (Top Bar) -->
      <header class="h-20 bg-white border-b border-stone-200/80 px-6 sm:px-10 flex items-center justify-between shrink-0">
        <div class="flex items-center gap-3">
          <span class="text-xs font-semibold text-stone-400">Administración</span>
          <span class="text-stone-300">/</span>
          <span class="text-xs font-bold text-[#0f382f]">Listado de Animales</span>
        </div>

        <!-- Perfil del Admin y Botón de Navegación a la Web -->
        <div class="flex items-center gap-4">
          <!-- Botón para ver la web pública y probar los cambios en vivo -->
          <button
            @click="$emit('go-public')"
            type="button"
            class="px-3.5 py-1.5 rounded-full bg-stone-100 hover:bg-[#a8dc8c]/30 text-stone-700 hover:text-[#0f382f] text-xs font-bold border border-stone-200 transition-all flex items-center gap-1.5 cursor-pointer"
          >
            <span>🌐 Ver Sitio Público</span>
          </button>

          <!-- Identificación del Usuario Admin (Como en la imagen de referencia) -->
          <div class="text-right hidden sm:block">
            <p class="text-xs text-stone-500">Conectado como:</p>
            <p class="text-xs font-bold text-[#0f382f]">Admin User (Administrador)</p>
          </div>

          <!-- Avatar del Admin -->
          <div class="w-9 h-9 rounded-full bg-[#0f382f] text-[#a8dc8c] flex items-center justify-center font-bold text-xs ring-2 ring-[#a8dc8c]/50">
            AD
          </div>
        </div>
      </header>

      <!-- Cuerpo del Panel -->
      <main class="p-6 sm:p-10 max-w-7xl w-full mx-auto space-y-6">
        <!-- Tarjetas de Métricas Rápidas del Refugio -->
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
          <!-- Total -->
          <div class="bg-white p-4 rounded-2xl border border-stone-200/80 shadow-xs flex items-center justify-between">
            <div>
              <p class="text-[11px] font-bold uppercase tracking-wider text-stone-400">Total Animales</p>
              <p class="text-2xl font-black text-[#0f382f] mt-0.5">{{ pets.length }}</p>
            </div>
            <div class="w-10 h-10 rounded-xl bg-stone-100 flex items-center justify-center text-[#0f382f]">
              🐾
            </div>
          </div>

          <!-- Disponibles (Se muestran en el catálogo público) -->
          <div class="bg-white p-4 rounded-2xl border border-stone-200/80 shadow-xs flex items-center justify-between">
            <div>
              <p class="text-[11px] font-bold uppercase tracking-wider text-stone-400">En Adopción</p>
              <p class="text-2xl font-black text-[#1e6b4d] mt-0.5">{{ countAvailable }}</p>
            </div>
            <div class="w-10 h-10 rounded-xl bg-[#eef8f2] text-[#1e6b4d] flex items-center justify-center font-bold text-sm">
              ✓
            </div>
          </div>

          <!-- En Tratamiento -->
          <div class="bg-white p-4 rounded-2xl border border-stone-200/80 shadow-xs flex items-center justify-between">
            <div>
              <p class="text-[11px] font-bold uppercase tracking-wider text-stone-400">En Tratamiento</p>
              <p class="text-2xl font-black text-amber-600 mt-0.5">{{ countTreatment }}</p>
            </div>
            <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center font-bold text-sm">
              ⚕
            </div>
          </div>

          <!-- Adoptados -->
          <div class="bg-white p-4 rounded-2xl border border-stone-200/80 shadow-xs flex items-center justify-between">
            <div>
              <p class="text-[11px] font-bold uppercase tracking-wider text-stone-400">Adoptados</p>
              <p class="text-2xl font-black text-blue-600 mt-0.5">{{ countAdopted }}</p>
            </div>
            <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center font-bold text-sm">
              ♥
            </div>
          </div>
        </div>

        <!-- Contenedor Principal Blanco (Diseño idéntico a la imagen) -->
        <div class="bg-white rounded-3xl border border-stone-200/80 shadow-sm p-6 sm:p-8 space-y-6">
          
          <!-- Encabezado de la Tarjeta (Título + Botón Agregar Animal) -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-2xl bg-[#a8dc8c]/30 text-[#0f382f] flex items-center justify-center shrink-0">
                <!-- Icono de Mascota -->
                <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24">
                  <path d="M12 13.5c-1.38 0-2.5 1.12-2.5 2.5 0 .8.4 1.5 1 1.95v.05c.4.3.9.5 1.5.5s1.1-.2 1.5-.5v-.05c.6-.45 1-1.15 1-1.95 0-1.38-1.12-2.5-2.5-2.5zm-4.5-3c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm9 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm-6.5-4c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2zm4 0c-.83 0-1.5.89-1.5 2s.67 2 1.5 2 1.5-.89 1.5-2-.67-2-1.5-2z" />
                </svg>
              </div>
              <div>
                <h2 class="text-xl sm:text-2xl font-extrabold text-[#0f382f] tracking-tight">
                  Listado de Animales
                </h2>
                <p class="text-xs text-stone-500">
                  Los animales marcados como "disponible" se reflejan en el catálogo público
                </p>
              </div>
            </div>

            <!-- Botón Principal: + Agregar Animal -->
            <button
              @click="openCreateModal"
              type="button"
              class="px-5 py-2.5 rounded-full bg-[#0f382f] text-white hover:bg-[#164e41] text-xs sm:text-sm font-bold shadow-sm hover:shadow transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer shrink-0"
            >
              <svg class="w-4 h-4 text-[#a8dc8c]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M12 4v16m8-8H4" />
              </svg>
              <span>Agregar Animal</span>
            </button>
          </div>

          <!-- Barra de Filtros y Búsqueda -->
          <div class="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3 pt-2">
            <!-- Input de Búsqueda -->
            <div class="relative flex-1 max-w-md">
              <input
                v-model="searchQuery"
                type="text"
                placeholder="Buscar por nombre, raza o ID..."
                class="w-full pl-10 pr-4 py-2.5 rounded-xl border border-stone-200 text-xs sm:text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f] focus:border-transparent transition-all"
              />
              <div class="absolute inset-y-0 left-0 pl-3.5 flex items-center pointer-events-none text-stone-400">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
            </div>

            <!-- Filtros Dropdown -->
            <div class="flex items-center gap-2 sm:gap-3 flex-wrap">
              <!-- Filtro Especie -->
              <select
                v-model="filterSpecies"
                class="px-3 py-2 rounded-xl border border-stone-200 text-xs font-semibold text-stone-700 bg-white focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
              >
                <option value="all">Todas las Especies</option>
                <option value="perro">🐶 Perros</option>
                <option value="gato">🐱 Gatos</option>
              </select>

              <!-- Filtro Estado -->
              <select
                v-model="filterStatus"
                class="px-3 py-2 rounded-xl border border-stone-200 text-xs font-semibold text-stone-700 bg-white focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
              >
                <option value="all">Todos los Estados</option>
                <option value="disponible">🟢 Disponibles</option>
                <option value="en_tratamiento">🟡 En Tratamiento</option>
                <option value="adoptado">🔵 Adoptados</option>
              </select>

              <!-- Selector de Vista (Tabla vs Cuadrícula) -->
              <div class="flex items-center rounded-xl border border-stone-200 p-0.5 bg-stone-50">
                <button
                  @click="viewMode = 'table'"
                  type="button"
                  :class="[
                    'p-1.5 rounded-lg transition-all cursor-pointer',
                    viewMode === 'table' ? 'bg-white text-[#0f382f] shadow-xs' : 'text-stone-400 hover:text-stone-600'
                  ]"
                  title="Vista en tabla"
                >
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
                  </svg>
                </button>
                <button
                  @click="viewMode = 'grid'"
                  type="button"
                  :class="[
                    'p-1.5 rounded-lg transition-all cursor-pointer',
                    viewMode === 'grid' ? 'bg-white text-[#0f382f] shadow-xs' : 'text-stone-400 hover:text-stone-600'
                  ]"
                  title="Vista en tarjetas"
                >
                  <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>

          <!-- TABLA DE DATOS (Diseño idéntico a la imagen) -->
          <div v-if="viewMode === 'table'" class="overflow-x-auto -mx-6 sm:mx-0">
            <table class="w-full text-left text-xs sm:text-sm">
              <!-- Encabezados de la tabla con flechitas sutiles de ordenamiento -->
              <thead>
                <tr class="border-b border-stone-200/80 text-[11px] font-bold uppercase tracking-wider text-stone-400">
                  <th class="py-3 px-3">FOTO</th>
                  <th class="py-3 px-3 cursor-pointer hover:text-[#0f382f]" @click="sortBy('id')">
                    ID ⇅
                  </th>
                  <th class="py-3 px-3 cursor-pointer hover:text-[#0f382f]" @click="sortBy('nombre')">
                    NOMBRE ⇅
                  </th>
                  <th class="py-3 px-3 cursor-pointer hover:text-[#0f382f]" @click="sortBy('especie')">
                    ESPECIE ⇅
                  </th>
                  <th class="py-3 px-3">RAZA</th>
                  <th class="py-3 px-3 cursor-pointer hover:text-[#0f382f]" @click="sortBy('edad')">
                    EDAD ⇅
                  </th>
                  <th class="py-3 px-3">ESTADO</th>
                  <th class="py-3 px-3">TAMAÑO</th>
                  <th class="py-3 px-3">REGISTRO</th>
                  <th class="py-3 px-3 text-right">ACCIONES</th>
                </tr>
              </thead>

              <!-- Filas de Mascotas -->
              <tbody class="divide-y divide-stone-100">
                <tr
                  v-for="pet in filteredPets"
                  :key="pet.id"
                  class="hover:bg-stone-50/80 transition-colors group"
                >
                  <!-- Foto Circular (Avatar) -->
                  <td class="py-3 px-3">
                    <img
                      :src="getPhotoUrl(pet)"
                      :alt="pet.nombre"
                      class="w-10 h-10 rounded-full object-cover border border-stone-200 shadow-2xs"
                    />
                  </td>

                  <!-- ID Formateado (ej. A001 o #001) -->
                  <td class="py-3 px-3 font-mono font-bold text-stone-600">
                    A{{ String(pet.id).padStart(3, '0') }}
                  </td>

                  <!-- Nombre -->
                  <td class="py-3 px-3 font-bold text-[#0f382f]">
                    {{ pet.nombre }}
                  </td>

                  <!-- Especie -->
                  <td class="py-3 px-3">
                    <span class="inline-flex items-center gap-1 font-medium capitalize">
                      {{ pet.especie === 'gato' ? '🐱 Gato' : '🐶 Perro' }}
                    </span>
                  </td>

                  <!-- Raza -->
                  <td class="py-3 px-3 text-stone-600">
                    {{ pet.raza }}
                  </td>

                  <!-- Edad -->
                  <td class="py-3 px-3 font-medium text-stone-600">
                    {{ formatAge(pet.edad) }}
                  </td>

                  <!-- Estado (Insignia redondeada verde/amarilla/azul como en la imagen) -->
                  <td class="py-3 px-3">
                    <span
                      :class="[
                        'inline-flex items-center px-2.5 py-0.5 rounded-full text-[11px] font-bold capitalize',
                        statusBadge(pet.estado)
                      ]"
                    >
                      {{ formatStatus(pet.estado) }}
                    </span>
                  </td>

                  <!-- Tamaño -->
                  <td class="py-3 px-3 text-stone-600 capitalize">
                    {{ pet.tamano }}
                  </td>

                  <!-- Fecha de Registro -->
                  <td class="py-3 px-3 text-stone-500 text-xs font-mono">
                    {{ formatDate(pet.fecha_registro) }}
                  </td>

                  <!-- Botones de Acción (Info, Editar, Eliminar) -->
                  <td class="py-3 px-3 text-right">
                    <div class="inline-flex items-center gap-1">
                      <!-- Ver Detalle -->
                      <button
                        @click="openDetailModal(pet)"
                        type="button"
                        class="p-1.5 rounded-lg text-stone-400 hover:text-[#0f382f] hover:bg-stone-100 transition-colors cursor-pointer"
                        title="Ver detalle"
                      >
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                      </button>

                      <!-- Editar -->
                      <button
                        @click="openEditModal(pet)"
                        type="button"
                        class="p-1.5 rounded-lg text-stone-400 hover:text-[#0f382f] hover:bg-stone-100 transition-colors cursor-pointer"
                        title="Editar animal"
                      >
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                        </svg>
                      </button>

                      <!-- Eliminar -->
                      <button
                        @click="confirmDelete(pet)"
                        type="button"
                        class="p-1.5 rounded-lg text-stone-400 hover:text-red-600 hover:bg-red-50 transition-colors cursor-pointer"
                        title="Eliminar registro"
                      >
                        <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- VISTA EN TARJETAS (Si el usuario prefiere grid) -->
          <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div
              v-for="pet in filteredPets"
              :key="pet.id"
              class="bg-stone-50 rounded-2xl p-4 border border-stone-200/80 hover:shadow-md transition-all flex flex-col justify-between"
            >
              <div>
                <div class="flex items-center gap-3">
                  <img
                    :src="getPhotoUrl(pet)"
                    :alt="pet.nombre"
                    class="w-14 h-14 rounded-2xl object-cover shrink-0"
                  />
                  <div>
                    <div class="flex items-center gap-2">
                      <h4 class="font-bold text-base text-[#0f382f]">{{ pet.nombre }}</h4>
                      <span class="text-xs font-mono text-stone-400">#A{{ String(pet.id).padStart(3, '0') }}</span>
                    </div>
                    <p class="text-xs text-stone-500">{{ pet.raza }} • {{ pet.especie }}</p>
                    <span
                      :class="[
                        'inline-flex items-center px-2 py-0.5 rounded-full text-[10px] font-bold mt-1',
                        statusBadge(pet.estado)
                      ]"
                    >
                      {{ formatStatus(pet.estado) }}
                    </span>
                  </div>
                </div>

                <p class="mt-3 text-xs text-stone-600 line-clamp-2 leading-relaxed">
                  {{ pet.descripcion }}
                </p>
              </div>

              <div class="mt-4 pt-3 border-t border-stone-200/60 flex items-center justify-between text-xs">
                <span class="text-stone-400 font-mono">{{ formatDate(pet.fecha_registro) }}</span>
                <div class="flex items-center gap-1">
                  <button
                    @click="openEditModal(pet)"
                    class="px-2.5 py-1 rounded-lg bg-white border border-stone-200 text-stone-700 font-bold hover:bg-stone-100 transition-colors"
                  >
                    Editar
                  </button>
                  <button
                    @click="confirmDelete(pet)"
                    class="p-1 rounded-lg text-red-500 hover:bg-red-50"
                  >
                    🗑
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Pie de la Tabla: Contador y resumen -->
          <div class="pt-4 border-t border-stone-100 flex flex-col sm:flex-row items-center justify-between text-xs text-stone-500 gap-2">
            <span>
              Mostrando {{ filteredPets.length }} de {{ pets.length }} animales registrados
            </span>
            <div class="flex items-center gap-1.5">
              <span class="w-2 h-2 rounded-full bg-[#1e6b4d]"></span>
              <span>Los marcados como "Disponible" son visibles en el catálogo principal</span>
            </div>
          </div>
        </div>
      </main>
    </div>

    <!-- Modales del Administrador -->
    <AdminPetModal
      v-if="showCreateEditModal"
      :pet-to-edit="petEditing"
      @close="closeCreateEditModal"
      @save="handleSavePet"
    />

    <AdminPetDetailModal
      v-if="petDetailing"
      :pet="petDetailing"
      @close="petDetailing = null"
      @edit="openEditFromDetail"
    />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import AdminSidebar from './AdminSidebar.vue'
import AdminPetModal from './AdminPetModal.vue'
import AdminPetDetailModal from './AdminPetDetailModal.vue'

const props = defineProps({
  pets: {
    type: Array,
    required: true
  }
})

const emit = defineEmits(['go-public', 'create-pet', 'update-pet', 'delete-pet', 'logout'])

const searchQuery = ref('')
const filterSpecies = ref('all')
const filterStatus = ref('all')
const viewMode = ref('table')
const sortKey = ref('id')
const sortOrder = ref('asc')

const showCreateEditModal = ref(false)
const petEditing = ref(null)
const petDetailing = ref(null)

// Contadores de métricas
const countAvailable = computed(() => props.pets.filter(p => p.estado === 'disponible').length)
const countTreatment = computed(() => props.pets.filter(p => p.estado === 'en_tratamiento').length)
const countAdopted = computed(() => props.pets.filter(p => p.estado === 'adoptado').length)

// Filtrado y ordenamiento de la tabla
const filteredPets = computed(() => {
  let list = [...props.pets]

  // Búsqueda por texto (nombre, raza o ID)
  if (searchQuery.value.trim() !== '') {
    const q = searchQuery.value.toLowerCase().trim()
    list = list.filter(p => {
      const idStr = String(p.id)
      const name = (p.nombre || '').toLowerCase()
      const breed = (p.raza || '').toLowerCase()
      return idStr.includes(q) || name.includes(q) || breed.includes(q)
    })
  }

  // Filtro de Especie
  if (filterSpecies.value !== 'all') {
    list = list.filter(p => (p.especie || '').toLowerCase() === filterSpecies.value)
  }

  // Filtro de Estado
  if (filterStatus.value !== 'all') {
    list = list.filter(p => (p.estado || '').toLowerCase() === filterStatus.value)
  }

  // Ordenamiento
  list.sort((a, b) => {
    let valA = a[sortKey.value]
    let valB = b[sortKey.value]

    if (typeof valA === 'string') valA = valA.toLowerCase()
    if (typeof valB === 'string') valB = valB.toLowerCase()

    if (valA < valB) return sortOrder.value === 'asc' ? -1 : 1
    if (valA > valB) return sortOrder.value === 'asc' ? 1 : -1
    return 0
  })

  return list
})

const sortBy = (key) => {
  if (sortKey.value === key) {
    sortOrder.value = sortOrder.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortKey.value = key
    sortOrder.value = 'asc'
  }
}

const getPhotoUrl = (pet) => {
  if (pet.foto_url) return pet.foto_url
  if (pet.image) return pet.image
  return 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80'
}

const formatAge = (meses) => {
  if (!meses) return '1 a.'
  if (meses >= 12) {
    const a = Math.floor(meses / 12)
    return `${a} a.`
  }
  return `${meses} m.`
}

const formatDate = (isoString) => {
  if (!isoString) return '-'
  try {
    const d = new Date(isoString)
    const year = d.getFullYear()
    const month = String(d.getMonth() + 1).padStart(2, '0')
    const day = String(d.getDate()).padStart(2, '0')
    return `${year}-${month}-${day}`
  } catch {
    return isoString
  }
}

const formatStatus = (st) => {
  if (st === 'disponible') return 'Disponible'
  if (st === 'en_tratamiento') return 'En Tratamiento'
  if (st === 'adoptado') return 'Adoptado'
  return st || 'Disponible'
}

const statusBadge = (st) => {
  if (st === 'disponible') return 'bg-[#eef8f2] text-[#1e6b4d] border border-[#cce7d7]'
  if (st === 'en_tratamiento') return 'bg-amber-100 text-amber-800 border border-amber-200'
  if (st === 'adoptado') return 'bg-blue-100 text-blue-800 border border-blue-200'
  return 'bg-stone-100 text-stone-700'
}

const openCreateModal = () => {
  petEditing.value = null
  showCreateEditModal.value = true
}

const openEditModal = (pet) => {
  petEditing.value = pet
  showCreateEditModal.value = true
}

const openDetailModal = (pet) => {
  petDetailing.value = pet
}

const openEditFromDetail = (pet) => {
  petDetailing.value = null
  openEditModal(pet)
}

const closeCreateEditModal = () => {
  showCreateEditModal.value = false
  petEditing.value = null
}

const handleSavePet = (petData) => {
  if (petEditing.value && petEditing.value.id) {
    emit('update-pet', { id: petEditing.value.id, data: petData })
  } else {
    emit('create-pet', petData)
  }
  closeCreateEditModal()
}

const confirmDelete = (pet) => {
  if (window.confirm(`¿Estás seguro de que deseas eliminar a "${pet.nombre}" de la base de datos?`)) {
    emit('delete-pet', pet.id)
  }
}
</script>

