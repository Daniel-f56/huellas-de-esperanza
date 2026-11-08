<template>
  <div
    class="fixed inset-0 z-50 overflow-y-auto bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 sm:p-6"
    @click.self="$emit('close')"
  >
    <div class="relative bg-white rounded-3xl max-w-2xl w-full overflow-hidden shadow-2xl border border-stone-200 animate-in fade-in zoom-in-95 duration-200">
      <!-- Encabezado del Modal -->
      <div class="p-6 bg-[#0f382f] text-white flex items-center justify-between">
        <div>
          <span class="text-xs font-bold uppercase tracking-widest text-[#a8dc8c]">
            {{ isEditing ? 'Actualización de Mascota' : 'Nuevo Registro de Mascota' }}
          </span>
          <h3 class="text-2xl font-extrabold mt-0.5">
            {{ isEditing ? `Editar a ${form.nombre}` : 'Registrar Nuevo Animal' }}
          </h3>
          <p class="text-xs text-white/75 mt-0.5">
            Los datos ingresados aparecerán de inmediato en el catálogo público si su estado es "disponible".
          </p>
        </div>

        <button
          @click="$emit('close')"
          type="button"
          class="w-9 h-9 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center transition-transform hover:scale-105 cursor-pointer shrink-0"
        >
          ✕
        </button>
      </div>

      <!-- Formulario -->
      <form @submit.prevent="handleSubmit" class="p-6 sm:p-8 space-y-5 max-h-[80vh] overflow-y-auto">
        <!-- Fila 1: Nombre y Especie -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="admin-nombre" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Nombre de la Mascota *
            </label>
            <input
              id="admin-nombre"
              v-model="form.nombre"
              type="text"
              required
              placeholder="Ej. Luna"
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            />
          </div>

          <div>
            <label for="admin-especie" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Especie *
            </label>
            <select
              id="admin-especie"
              v-model="form.especie"
              required
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            >
              <option value="perro">🐶 Perro</option>
              <option value="gato">🐱 Gato</option>
            </select>
          </div>
        </div>

        <!-- Fila 2: Raza y Edad en meses -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="admin-raza" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Raza *
            </label>
            <input
              id="admin-raza"
              v-model="form.raza"
              type="text"
              required
              placeholder="Ej. Criolla, Labrador, etc."
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            />
          </div>

          <div>
            <label for="admin-edad" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Edad (en meses) *
            </label>
            <div class="relative">
              <input
                id="admin-edad"
                v-model.number="form.edad"
                type="number"
                min="1"
                max="240"
                required
                placeholder="Ej. 24"
                class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
              />
              <span class="absolute right-3 top-2.5 text-xs text-stone-400 pointer-events-none">
                {{ formatAgeMonths(form.edad) }}
              </span>
            </div>
          </div>
        </div>

        <!-- Fila 3: Sexo y Tamaño -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="admin-sexo" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Sexo *
            </label>
            <select
              id="admin-sexo"
              v-model="form.sexo"
              required
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            >
              <option value="hembra">♀ Hembra</option>
              <option value="macho">♂ Macho</option>
            </select>
          </div>

          <div>
            <label for="admin-tamano" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Tamaño *
            </label>
            <select
              id="admin-tamano"
              v-model="form.tamano"
              required
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            >
              <option value="pequeño">Pequeño (&lt; 10 kg)</option>
              <option value="mediano">Mediano (10 - 25 kg)</option>
              <option value="grande">Grande (&gt; 25 kg)</option>
            </select>
          </div>
        </div>

        <!-- Fila 4: Estado -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label for="admin-estado" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Estado en la Plataforma *
            </label>
            <select
              id="admin-estado"
              v-model="form.estado"
              required
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            >
              <option value="disponible">🟢 Disponible (visible en catálogo)</option>
              <option value="en_tratamiento">🟡 En Tratamiento / Cuidados</option>
              <option value="adoptado">🔵 Adoptado</option>
            </select>
            <p class="text-[11px] text-stone-500 mt-1">
              Predefinido como "disponible" para nuevas mascotas.
            </p>
          </div>

          <div v-if="isEditing">
            <label class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Fecha de Registro
            </label>
            <input
              type="text"
              disabled
              :value="formatDate(form.fecha_registro)"
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-200 bg-stone-100 text-xs text-stone-500 cursor-not-allowed"
            />
          </div>
        </div>

        <!-- Fila 5: URL de la Foto con Previsualización -->
        <div>
          <label for="admin-foto" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            URL de la Fotografía (Opcional)
          </label>
          <div class="flex gap-2">
            <input
              id="admin-foto"
              v-model="form.foto_url"
              type="url"
              placeholder="https://ejemplo.com/foto-mascota.jpg"
              class="flex-1 px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            />
            <button
              type="button"
              @click="setRandomPhoto"
              class="px-3.5 py-2.5 rounded-xl bg-stone-100 hover:bg-stone-200 text-stone-700 text-xs font-bold shrink-0 transition-colors cursor-pointer"
              title="Cargar foto de muestra según la especie"
            >
              🎲 Foto sugerida
            </button>
          </div>

          <!-- Previsualización de imagen -->
          <div v-if="form.foto_url" class="mt-3 flex items-center gap-3 p-2 bg-stone-50 rounded-2xl border border-stone-200">
            <img
              :src="form.foto_url"
              alt="Previsualización"
              class="w-16 h-16 rounded-xl object-cover shrink-0"
              @error="handleImageError"
            />
            <div class="text-xs text-stone-600">
              <p class="font-bold text-[#0f382f]">Previsualización en vivo</p>
              <p class="text-[11px] text-stone-500 truncate max-w-sm">{{ form.foto_url }}</p>
            </div>
          </div>
        </div>

        <!-- Fila 6: Descripción -->
        <div>
          <label for="admin-descripcion" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            Descripción y Personalidad *
          </label>
          <textarea
            id="admin-descripcion"
            v-model="form.descripcion"
            rows="3"
            required
            placeholder="Perrita cariñosa y juguetona, sociable con niños..."
            class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f] resize-none"
          ></textarea>
        </div>

        <!-- Botones de Acción -->
        <div class="pt-4 border-t border-stone-100 flex items-center justify-end gap-3">
          <button
            @click="$emit('close')"
            type="button"
            class="px-5 py-2.5 rounded-full border border-stone-300 text-stone-600 hover:bg-stone-50 font-semibold text-xs cursor-pointer"
          >
            Cancelar
          </button>
          <button
            type="submit"
            class="px-6 py-2.5 rounded-full bg-[#0f382f] text-white hover:bg-[#164e41] font-bold text-xs shadow-md transition-all flex items-center gap-1.5 cursor-pointer"
          >
            <span>{{ isEditing ? 'Guardar Cambios' : 'Registrar Animal' }}</span>
            <span class="text-[#a8dc8c]">✓</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed, watch } from 'vue'

const props = defineProps({
  petToEdit: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['close', 'save'])

const isEditing = computed(() => !!props.petToEdit)

// Estado del formulario según el esquema exacto de base de datos
const form = reactive({
  id: null,
  nombre: '',
  especie: 'perro',
  raza: '',
  edad: 12,
  sexo: 'hembra',
  tamano: 'mediano',
  descripcion: '',
  foto_url: null,
  estado: 'disponible', // Estado disponible predefinido
  fecha_registro: ''
})

// Si se pasa una mascota para editar, poblamos los campos
watch(
  () => props.petToEdit,
  (newVal) => {
    if (newVal) {
      form.id = newVal.id
      form.nombre = newVal.nombre || newVal.name || ''
      form.especie = newVal.especie || 'perro'
      form.raza = newVal.raza || newVal.breed || ''
      form.edad = newVal.edad !== undefined ? newVal.edad : 12
      form.sexo = newVal.sexo || 'hembra'
      form.tamano = newVal.tamano || 'mediano'
      form.descripcion = newVal.descripcion || newVal.description || ''
      form.foto_url = newVal.foto_url || newVal.image || null
      form.estado = newVal.estado || 'disponible'
      form.fecha_registro = newVal.fecha_registro || ''
    } else {
      // Valores limpios por defecto
      form.id = null
      form.nombre = ''
      form.especie = 'perro'
      form.raza = 'Criollo'
      form.edad = 12
      form.sexo = 'hembra'
      form.tamano = 'mediano'
      form.descripcion = ''
      form.foto_url = null
      form.estado = 'disponible'
      form.fecha_registro = ''
    }
  },
  { immediate: true }
)

const formatAgeMonths = (meses) => {
  if (!meses) return ''
  if (meses >= 12) {
    const anios = Math.floor(meses / 12)
    const m = meses % 12
    if (m === 0) return `(${anios} ${anios === 1 ? 'año' : 'años'})`
    return `(${anios} a. ${m} m.)`
  }
  return `(${meses} meses)`
}

const formatDate = (isoString) => {
  if (!isoString) return 'Automática'
  try {
    const date = new Date(isoString)
    return date.toLocaleDateString('es-CO', {
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

const samplePhotos = {
  perro: [
    'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1587300003388-59208cc962cb?auto=format&fit=crop&w=800&q=80'
  ],
  gato: [
    'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1574158622682-e40e69881006?auto=format&fit=crop&w=800&q=80',
    'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=800&q=80'
  ]
}

const setRandomPhoto = () => {
  const list = samplePhotos[form.especie] || samplePhotos.perro
  const random = list[Math.floor(Math.random() * list.length)]
  form.foto_url = random
}

const handleImageError = () => {
  // Manejador si la URL de la imagen falla
}

const handleSubmit = () => {
  emit('save', {
    ...form,
    // Aseguramos que la edad sea un número
    edad: Number(form.edad) || 12
  })
}
</script>

