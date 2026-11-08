<template>
  <div class="bg-[#0f382f] text-white rounded-3xl p-6 sm:p-8 lg:p-10 shadow-xl border border-[#164e41] flex flex-col justify-between">
    <!-- Encabezado en Español -->
    <div class="mb-6">
      <span class="text-xs font-bold tracking-[0.2em] uppercase text-[#a8dc8c] block">
        CONTACTO
      </span>
      <h3 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight mt-1">
        Ponte en Contacto
      </h3>
    </div>

    <!-- Tarjeta Blanca de Formulario en Español -->
    <div class="bg-white text-[#0f382f] rounded-2xl p-6 sm:p-7 shadow-md">
      <h4 class="text-xl sm:text-2xl font-extrabold text-[#0f382f] tracking-tight">
        ¡Escríbenos!
      </h4>
      <p class="mt-2 text-xs sm:text-sm text-stone-600 leading-relaxed">
        ¿Tienes dudas sobre el proceso, deseas unirte como voluntario o iniciar una adopción? Contáctanos y te responderemos muy pronto.
      </p>

      <!-- Formulario -->
      <form @submit.prevent="handleSubmit" class="mt-5 space-y-3.5">
        <div>
          <label class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            Nombre Completo
          </label>
          <input
            v-model="form.name"
            type="text"
            required
            placeholder="Tu nombre y apellido"
            class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f] focus:border-transparent transition-all"
          />
        </div>

        <div>
          <label class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            Teléfono o Correo Electrónico
          </label>
          <input
            v-model="form.contact"
            type="text"
            required
            placeholder="Celular o correo de contacto"
            class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f] focus:border-transparent transition-all"
          />
        </div>

        <div>
          <label class="block text-xs font-bold text-stone-700 uppercase tracking-wider mb-1">
            Mensaje
          </label>
          <textarea
            v-model="form.message"
            rows="3"
            required
            placeholder="¿En qué podemos ayudarte o qué mascota te interesa conocer?"
            class="w-full px-3.5 py-2.5 rounded-xl border border-stone-300 text-sm text-[#0f382f] placeholder-stone-400 focus:outline-none focus:ring-2 focus:ring-[#0f382f] focus:border-transparent transition-all resize-none"
          ></textarea>
        </div>

        <!-- Botón de Envío -->
        <button
          type="submit"
          :disabled="isSubmitting"
          class="w-full py-3 px-4 rounded-full bg-[#0f382f] text-white hover:bg-[#154b3e] text-sm font-bold shadow transition-all duration-200 flex items-center justify-center gap-2 cursor-pointer disabled:opacity-75"
        >
          <span v-if="!isSubmitting">Enviar Mensaje</span>
          <span v-else>Enviando...</span>
          <svg v-if="!isSubmitting" class="w-4 h-4 text-[#a8dc8c]" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M14 5l7 7m0 0l-7 7m7-7H3" />
          </svg>
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const emit = defineEmits(['message-sent'])

const isSubmitting = ref(false)
const form = reactive({
  name: '',
  contact: '',
  message: ''
})

const handleSubmit = () => {
  isSubmitting.value = true
  setTimeout(() => {
    isSubmitting.value = false
    emit('message-sent', { ...form })
    form.name = ''
    form.contact = ''
    form.message = ''
  }, 600)
}
</script>
