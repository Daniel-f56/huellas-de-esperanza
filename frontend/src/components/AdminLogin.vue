
<template>
  <div class="min-h-screen flex items-center justify-center bg-[#f6f3eb] px-4">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-xl p-8">
      <div class="text-center mb-8">
        <div class="text-4xl mb-3">🐾</div>
        <h1 class="text-2xl font-bold text-[#0f382f]">
          Acceso administrativo
        </h1>
        <p class="text-sm text-stone-500 mt-2">
          Inicia sesión para gestionar las mascotas y solicitudes.
        </p>
      </div>

      <form @submit.prevent="iniciarSesion" class="space-y-5">
        <div>
          <label class="block text-sm font-semibold text-[#0f382f] mb-2">
            Usuario
          </label>
          <input
            v-model="username"
            type="text"
            required
            autocomplete="username"
            class="w-full px-4 py-3 border border-stone-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#3b8754]"
            placeholder="Ingresa tu usuario"
          />
        </div>

        <div>
          <label class="block text-sm font-semibold text-[#0f382f] mb-2">
            Contraseña
          </label>
          <input
            v-model="password"
            type="password"
            required
            autocomplete="current-password"
            class="w-full px-4 py-3 border border-stone-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#3b8754]"
            placeholder="Ingresa tu contraseña"
          />
        </div>

        <p v-if="error" class="text-sm text-red-600">
          {{ error }}
        </p>

        <button
          type="submit"
          :disabled="loading"
          class="w-full py-3 rounded-xl bg-[#0f382f] text-white font-bold hover:bg-[#164e41] transition-colors disabled:opacity-60"
        >
          {{ loading ? 'Ingresando...' : 'Iniciar sesión' }}
        </button>
      </form>

      <button
        @click="$emit('back')"
        type="button"
        class="w-full mt-5 text-sm text-stone-500 hover:text-[#0f382f]"
      >
        ← Volver al sitio público
      </button>
    </div>
  </div>
</template>

<script setup>
    import { ref } from 'vue'
    import { apiService } from '../services/api.js'

    const username = ref('')
    const password = ref('')
    const error = ref('')
    const loading = ref(false)

    const emit = defineEmits(['back', 'login-success'])

    const iniciarSesion = async () => {
        error.value = ''
        loading.value = true

        try {
            await apiService.iniciarSesion(username.value, password.value)
            emit('login-success')
        } catch (err) {
            error.value = err.message || 'No fue posible iniciar sesión.'
        } finally {
            loading.value = false
        }
    }
</script>
