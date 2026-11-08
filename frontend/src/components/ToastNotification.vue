<template>
  <div
    v-if="visible"
    class="fixed bottom-6 right-6 z-50 max-w-sm w-full bg-[#0f382f] text-white rounded-2xl p-4 shadow-2xl border border-[#a8dc8c]/30 animate-in slide-in-from-bottom-5 duration-300 flex items-start gap-3"
  >
    <div class="w-8 h-8 rounded-xl bg-[#a8dc8c] text-[#0f382f] flex items-center justify-center shrink-0 font-bold text-sm">
      ✓
    </div>
    <div class="flex-1">
      <h5 class="text-sm font-bold text-white">{{ title }}</h5>
      <p class="text-xs text-white/80 mt-0.5 leading-snug">{{ message }}</p>
    </div>
    <button
      @click="$emit('dismiss')"
      type="button"
      class="text-white/60 hover:text-white text-xs p-1"
    >
      ✕
    </button>
  </div>
</template>

<script setup>
defineProps({
  visible: {
    type: Boolean,
    default: false
  },
  title: {
    type: String,
    default: 'Éxito'
  },
  message: {
    type: String,
    default: ''
  }
})

defineEmits(['dismiss'])
</script>

