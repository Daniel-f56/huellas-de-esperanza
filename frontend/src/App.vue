<template>
  <!-- VISTA 1: DASHBOARD DEL ADMINISTRADOR (Matching imagen de referencia) -->
  <AdminDashboard
    v-if="currentView === 'admin'"
    :pets="pets"
    @go-public="currentView = 'public'"
    @create-pet="handleCreatePet"
    @update-pet="handleUpdatePet"
    @delete-pet="handleDeletePet"
    @logout="currentView = 'public'"
  />

  <!-- VISTA 2: SITIO WEB PÚBLICO -->
  <div v-else class="min-h-screen flex flex-col bg-[#f6f3eb] text-[#0f382f] relative">
    <!-- Top Global Navbar con acceso al panel admin -->
    <Navbar @open-admin="currentView = 'admin'" />

    <!-- Flujo Principal de Contenidos -->
    <main class="flex-1">
      <!-- 1. Sección Hero de Bienvenida -->
      <section class="pt-6 pb-12 sm:pt-12 sm:pb-16 overflow-hidden">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12 items-center">
            <!-- Texto Izquierdo del Hero -->
            <div class="lg:col-span-7 space-y-6">
              <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-[#a8dc8c]/35 border border-[#0f382f]/10 text-[#0f382f] text-xs font-bold uppercase tracking-wider whitespace-nowrap">
                <span class="w-2 h-2 rounded-full bg-[#3b8754] animate-pulse"></span>
                Adopción Consciente & Responsable
              </div>

              <h1 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-extrabold text-[#0f382f] tracking-tight leading-[1.12]">
                Dales una segunda oportunidad, encuentra a tu compañero de vida.
              </h1>

              <p class="text-sm sm:text-base lg:text-lg text-stone-700 leading-relaxed max-w-xl">
                En <strong class="text-[#0f382f]">Huellas de Esperanza</strong> rescatamos, rehabilitamos y encontramos familias amorosas para animales que han sufrido abandono o maltrato.
              </p>

              <!-- Botones de Acción del Hero -->
              <div class="flex flex-wrap items-center gap-3 sm:gap-4 pt-1">
                <a
                  href="#find-a-friend"
                  class="whitespace-nowrap px-6 sm:px-7 py-3 sm:py-3.5 rounded-full bg-[#0f382f] text-white hover:bg-[#164e41] text-xs sm:text-sm font-bold shadow-lg hover:shadow-xl transition-all duration-200 flex items-center gap-2 group cursor-pointer"
                >
                  <span>Explorar Mascotas Disponibles</span>
                  <span class="text-[#a8dc8c] transform group-hover:translate-x-1 transition-transform">→</span>
                </a>
                <a
                  href="#rescue-rehab"
                  class="whitespace-nowrap px-5 sm:px-6 py-3 sm:py-3.5 rounded-full bg-white hover:bg-stone-50 text-[#0f382f] border border-stone-300 text-xs sm:text-sm font-semibold shadow-xs transition-colors"
                >
                  Conocer Nuestra Labor
                </a>
              </div>

              <!-- Píldoras de garantía -->
              <div class="pt-4 flex flex-wrap items-center gap-x-6 gap-y-2 border-t border-stone-200/80 max-w-lg text-xs sm:text-sm text-stone-600">
                <div class="flex items-center gap-1.5 whitespace-nowrap">
                  <span class="text-[#2b8a3e] font-bold">✓</span>
                  <span>100% Vacunados</span>
                </div>
                <div class="flex items-center gap-1.5 whitespace-nowrap">
                  <span class="text-[#2b8a3e] font-bold">✓</span>
                  <span>Esterilizados</span>
                </div>
                <div class="flex items-center gap-1.5 whitespace-nowrap">
                  <span class="text-[#2b8a3e] font-bold">✓</span>
                  <span>Seguimiento Continuo</span>
                </div>
              </div>
            </div>

            <!-- Imagen Derecha del Hero -->
            <div class="lg:col-span-5 relative">
              <div class="relative mx-auto max-w-md lg:max-w-none">
                <!-- Tarjeta Principal de Foto -->
                <div class="aspect-[4/3] rounded-3xl overflow-hidden shadow-2xl border-4 border-white bg-stone-100">
                  <img
                    src="https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=1000&q=80"
                    alt="Voluntaria feliz con cachorro rescatado"
                    class="w-full h-full object-cover"
                  />
                </div>

                <!-- Insignia Flotante 1 (Arriba Derecha) -->
                <div class="absolute -top-3 -right-3 sm:-top-4 sm:-right-4 bg-white/95 backdrop-blur-md px-3.5 py-2 sm:px-4 sm:py-2.5 rounded-2xl shadow-xl border border-stone-200/80 flex items-center gap-2.5 whitespace-nowrap">
                  <div class="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-[#a8dc8c] text-[#0f382f] flex items-center justify-center font-bold text-sm shrink-0">
                    🐾
                  </div>
                  <div class="text-left">
                    <p class="text-xs font-extrabold text-[#0f382f]">Refugio Activo</p>
                    <p class="text-[11px] text-stone-500">Bogotá & alrededores</p>
                  </div>
                </div>

                <!-- Insignia Flotante 2 (Abajo Izquierda) -->
                <div class="absolute -bottom-4 -left-3 sm:-bottom-5 sm:-left-4 bg-[#0f382f] text-white px-4 py-2.5 sm:px-5 sm:py-3 rounded-2xl shadow-xl border border-[#174d40] flex items-center gap-3 whitespace-nowrap">
                  <span class="text-xl sm:text-2xl font-black text-[#a8dc8c]">100%</span>
                  <div class="text-left text-xs">
                    <p class="font-bold">Adopción Responsable</p>
                    <p class="text-white/70">Sin ánimo de lucro</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 2. Estadísticas de Impacto (48 adoptions + 208 treatments) -->
      <StatsCard />

      <!-- 3. Showcase Central: "¡Descubre a tu nuevo mejor amigo!" (Sincronizado con Admin) -->
      <PetShowcase
        :pets="pets"
        :favorites="favorites"
        @select-pet="openPetModal"
        @open-catalog="scrollToCatalog"
        @toggle-favorite="toggleFavorite"
      />

      <!-- 4. Proceso de Adopción Responsable en 4 Pasos -->
      <AdoptionSteps />

      <!-- 5. Historias y Misión -->
      <section id="rescue-rehab" class="py-10 sm:py-14">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <!-- Izquierda: "Una Segunda Oportunidad" -->
            <div id="second-chance">
              <SuccessStoryCard />
            </div>

            <!-- Derecha: "Rescate y Rehabilitación" con ilustración del perro -->
            <div>
              <RescueRehabCard />
            </div>
          </div>
        </div>
      </section>

      <!-- 6. Aliados y Formulario de Contacto -->
      <section id="partners" class="py-8 sm:py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Izquierda: Aliados Patrocinadores (Silpo & Purina) -->
            <div class="lg:col-span-7">
              <PartnersCard />
            </div>

            <!-- Derecha: Contacto y Formulario "¡Escríbenos!" -->
            <div id="contact" class="lg:col-span-5">
              <ContactCard @message-sent="handleMessageSent" />
            </div>
          </div>
        </div>
      </section>
    </main>

    <!-- Botón Flotante para cambiar al Panel Admin fácilmente -->
    <button
      @click="currentView = 'admin'"
      type="button"
      class="fixed bottom-6 left-6 z-40 bg-[#0f382f] text-white hover:bg-[#164e41] px-4 py-2.5 rounded-full shadow-2xl border border-[#a8dc8c]/40 text-xs font-bold flex items-center gap-2 cursor-pointer transition-transform hover:scale-105 select-none"
      title="Acceso directo al Panel de Gestión de Mascotas"
    >
      <span class="w-2.5 h-2.5 rounded-full bg-[#a8dc8c] animate-pulse"></span>
      <span>⚙️ Administrar Mascotas</span>
    </button>

    <!-- Pie de Página Global -->
    <FooterSection />

    <!-- Modales Públicos -->
    <PetDetailModal
      v-if="selectedPet"
      :pet="selectedPet"
      @close="selectedPet = null"
      @adopt="startAdoption"
    />

    <AdoptionModal
      v-if="adoptingPet"
      :pet="adoptingPet"
      @close="adoptingPet = null"
      @submit-success="handleAdoptionSubmitted"
    />

    <!-- Notificación Toast -->
    <ToastNotification
      :visible="toast.show"
      :title="toast.title"
      :message="toast.message"
      @dismiss="toast.show = false"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import Navbar from './components/Navbar.vue'
import StatsCard from './components/StatsCard.vue'
import PetShowcase from './components/PetShowcase.vue'
import AdoptionSteps from './components/AdoptionSteps.vue'
import SuccessStoryCard from './components/SuccessStoryCard.vue'
import RescueRehabCard from './components/RescueRehabCard.vue'
import PartnersCard from './components/PartnersCard.vue'
import ContactCard from './components/ContactCard.vue'
import FooterSection from './components/FooterSection.vue'
import PetDetailModal from './components/PetDetailModal.vue'
import AdoptionModal from './components/AdoptionModal.vue'
import ToastNotification from './components/ToastNotification.vue'
import AdminDashboard from './components/admin/AdminDashboard.vue'
import { apiService } from './services/api.js'

// Control de vista: 'public' (sitio web de adopción) o 'admin' (panel administrativo)
const currentView = ref('public')

const pets = ref([])
const selectedPet = ref(null)
const adoptingPet = ref(null)

// Cargar las mascotas desde el servicio centralizado (con persistencia)
const loadPets = async () => {
  pets.value = await apiService.getMascotas()
}

onMounted(() => {
  loadPets()
})

// Gestión de favoritos con persistencia en localStorage
const favorites = ref([])
try {
  const savedFavs = localStorage.getItem('huellas_favoritos')
  if (savedFavs) {
    favorites.value = JSON.parse(savedFavs)
  }
} catch {
  favorites.value = []
}

const toggleFavorite = (id) => {
  if (favorites.value.includes(id)) {
    favorites.value = favorites.value.filter(item => item !== id)
  } else {
    favorites.value.push(id)
  }
  try {
    localStorage.setItem('huellas_favoritos', JSON.stringify(favorites.value))
  } catch {
    // Si localStorage no está disponible
  }
}

const toast = ref({
  show: false,
  title: '',
  message: ''
})

const showToast = (title, message) => {
  toast.value = {
    show: true,
    title,
    message
  }
  setTimeout(() => {
    toast.value.show = false
  }, 5000)
}

const openPetModal = (pet) => {
  selectedPet.value = pet
}

const startAdoption = (pet) => {
  selectedPet.value = null
  adoptingPet.value = pet
}

// Operaciones de Administrador (CRUD de Mascotas)
const handleCreatePet = async (petData) => {
  const newPet = await apiService.crearMascota(petData)
  await loadPets()
  showToast(
    `¡${newPet.nombre} registrado con éxito!`,
    `El animal ha sido guardado en la base de datos y ya está visible en el catálogo de adopción.`
  )
}

const handleUpdatePet = async ({ id, data }) => {
  await apiService.actualizarMascota(id, data)
  await loadPets()
  showToast(
    '¡Mascota actualizada!',
    `Los cambios de ${data.nombre} han sido guardados y sincronizados.`
  )
}

const handleDeletePet = async (id) => {
  await apiService.eliminarMascota(id)
  await loadPets()
  showToast(
    'Mascota eliminada',
    'El animal ha sido removido del sistema.'
  )
}

const handleAdoptionSubmitted = async ({ pet, applicant }) => {
  adoptingPet.value = null

  await apiService.enviarSolicitudAdopcion({
    mascota_id: pet.id,
    mascota_nombre: pet.nombre || pet.name,
    nombre: applicant.nombre,
    correo: applicant.correo,
    numero: applicant.numero,
    direccion: applicant.direccion,
    motivo: applicant.motivo
  })

  showToast(
    `¡Solicitud registrada para ${pet.nombre || pet.name}!`,
    `Gracias ${applicant.nombre}, nos comunicaremos contigo al número ${applicant.numero} para continuar con el proceso.`
  )
}

const handleMessageSent = async (formData) => {
  await apiService.enviarMensajeContacto(formData)

  showToast(
    '¡Mensaje recibido con éxito!',
    `Gracias por escribirnos, ${formData.name}. Nuestro equipo te responderá a la brevedad.`
  )
}

const scrollToCatalog = () => {
  const el = document.getElementById('find-a-friend')
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' })
  }
}
</script>
