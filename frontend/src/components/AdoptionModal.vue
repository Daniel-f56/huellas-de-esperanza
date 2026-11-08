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
        class="absolute top-4 right-4 z-10 w-8 h-8 rounded-full bg-white/20 hover:bg-white/40 text-white flex items-center justify-center transition-transform hover:scale-105 cursor-pointer"
        aria-label="Cerrar modal"
      >
        ✕
      </button>

      <!-- Encabezado del Modal -->
      <div class="p-6 bg-[#0f382f] text-white">
        <span class="text-xs font-bold uppercase tracking-widest text-[#a8dc8c]">
          Formulario de Adopción Responsable
        </span>
        <h3 class="text-2xl font-extrabold mt-1">
          Solicitud para adoptar a {{ pet.name }}
        </h3>
        <p class="text-xs sm:text-sm text-white/80 mt-1">
          Completa tus datos para registrar tu postulación en nuestra base de datos.
        </p>

        <!-- Mini resumen de la mascota -->
        <div class="mt-4 flex items-center gap-3 bg-white/10 p-2.5 rounded-2xl backdrop-blur-sm border border-white/10">
          <img
            :src="pet.image"
            :alt="pet.name"
            class="w-12 h-12 rounded-xl object-cover"
          />
          <div class="text-xs">
            <p class="font-bold text-white text-sm">{{ pet.name }} ({{ pet.species }})</p>
            <p class="text-white/75">{{ pet.age }} • {{ pet.weight }} • {{ pet.gender }}</p>
          </div>
        </div>
      </div>

      <!-- Formulario con ÚNICAMENTE los 5 campos requeridos para la base de datos -->
      <form @submit.prevent="handleSubmit" class="p-6 space-y-4">
        <!-- 1. Nombre -->
        <div>
          <label for="nombre" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            Nombre Completo
          </label>
          <input
            id="nombre"
            v-model="form.nombre"
            type="text"
            required
            placeholder="Ingresa tu nombre completo"
            class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
          />
        </div>

        <!-- Fila de Correo y Número -->
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
          <!-- 2. Correo -->
          <div>
            <label for="correo" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Correo Electrónico
            </label>
            <input
              id="correo"
              v-model="form.correo"
              type="email"
              required
              placeholder="ejemplo@correo.com"
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            />
          </div>

          <!-- 3. Número -->
          <div>
            <label for="numero" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
              Número de Teléfono / Celular
            </label>
            <input
              id="numero"
              v-model="form.numero"
              type="tel"
              required
              placeholder="3001234567"
              class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
            />
          </div>
        </div>

        <!-- 4. Dirección -->
        <div>
          <label for="direccion" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            Dirección
          </label>
          <input
            id="direccion"
            v-model="form.direccion"
            type="text"
            required
            placeholder="Calle, carrera o barrio de residencia"
            class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f]"
          />
        </div>

        <!-- 5. Motivo -->
        <div>
          <label for="motivo" class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            Motivo por el cual quieres adoptar
          </label>
          <textarea
            id="motivo"
            v-model="form.motivo"
            rows="3"
            required
            placeholder="Cuéntanos las razones por las cuales deseas darle un hogar a esta mascota..."
            class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f] resize-none"
          ></textarea>
        </div>

        <!-- Botones de Acción -->
        <div class="pt-3 flex items-center justify-end gap-3">
          <button
            @click="$emit('close')"
            type="button"
            class="px-5 py-2.5 rounded-full border border-stone-300 text-stone-600 hover:bg-stone-50 font-semibold text-xs cursor-pointer"
          >
            Cancelar
          </button>
          <button
            type="submit"
            :disabled="isSubmitting"
            class="px-6 py-2.5 rounded-full bg-[#0f382f] text-white hover:bg-[#164e41] font-bold text-xs shadow-md transition-all flex items-center gap-1.5 cursor-pointer disabled:opacity-75"
          >
            <span v-if="!isSubmitting">Enviar Solicitud de Adopción</span>
            <span v-else>Guardando...</span>
            <span class="text-[#a8dc8c]">♥</span>
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const props = defineProps({
  pet: {
    type: Object,
    default: null
  }
})

const emit = defineEmits(['close', 'submit-success'])

const isSubmitting = ref(false)

// Exactamente los 5 campos requeridos para la base de datos
const form = reactive({
  nombre: '',
  correo: '',
  numero: '',
  direccion: '',
  motivo: ''
})

const handleSubmit = () => {
  isSubmitting.value = true

  emit('submit-success', {
    pet: props.pet,
    applicant: {
      nombre: form.nombre,
      correo: form.correo,
      numero: form.numero,
      direccion: form.direccion,
      motivo: form.motivo
    },

    // Se ejecuta cuando la API registra correctamente la solicitud.
    onSuccess: () => {
      form.nombre = ''
      form.correo = ''
      form.numero = ''
      form.direccion = ''
      form.motivo = ''
      isSubmitting.value = false
    },

    // Se ejecuta si la API devuelve un error.
    onError: () => {
      isSubmitting.value = false
    }
  })
}
</script>
