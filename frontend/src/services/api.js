
import {
  PARTNERS_DATA,
  STATS_DATA,
  ADOPTION_STEPS
} from '../data/pets.js'

const API_MASCOTAS =
  import.meta.env.VITE_API_MASCOTAS_URL || 'http://127.0.0.1:8001'

const API_ADOPCIONES =
  import.meta.env.VITE_API_ADOPCIONES_URL || 'http://127.0.0.1:8002'

const TOKEN_KEY = 'admin_token'

// Obtener el token guardado.
function obtenerToken() {
  return sessionStorage.getItem(TOKEN_KEY)
}

// Agregar el token a las peticiones administrativas.
function headersAdmin(headers = {}) {
  const token = obtenerToken()

  return {
    ...headers,
    ...(token && { Authorization: `Bearer ${token}` })
  }
}

// Realiza las peticiones HTTP y controla los errores de las APIs.
async function request(url, options = {}) {
  const response = await fetch(url, options)

  const data = await response.json().catch(() => null)

  if (!response.ok) {
    throw new Error(
      data?.detail || `Error en la solicitud (${response.status})`
    )
  }

  return data
}

// Normaliza los datos para mantener compatibilidad con el frontend.
function normalizarMascota(pet) {
  return {
    ...pet,
    tamano: pet.tamano === 'pequeño' ? 'pequeno' : pet.tamano
  }
}

export const apiService = {
  // Iniciar sesión como administrador.
  async iniciarSesion(username, password) {
    const formData = new URLSearchParams()
    formData.append('username', username)
    formData.append('password', password)

    const respuesta = await request(`${API_ADOPCIONES}/auth/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: formData
    })

    sessionStorage.setItem(TOKEN_KEY, respuesta.access_token)

    return respuesta
  },

  // Cerrar sesión.
  cerrarSesion() {
    sessionStorage.removeItem(TOKEN_KEY)
  },

  // Consultar si existe una sesión administrativa.
  estaAutenticado() {
    return Boolean(obtenerToken())
  },

  // Obtener todas las mascotas.
  async getMascotas() {
    const mascotas = await request(`${API_MASCOTAS}/mascotas`)
    return mascotas.map(normalizarMascota)
  },

  // Obtener únicamente las mascotas disponibles.
  async getMascotasDisponibles() {
    const mascotas = await this.getMascotas()
    return mascotas.filter(pet => pet.estado === 'disponible')
  },

  // Obtener una mascota por su ID.
  async getMascotaPorId(id) {
    const mascota = await request(`${API_MASCOTAS}/mascotas/${id}`)
    return normalizarMascota(mascota)
  },

  // Registrar una nueva mascota.
  async crearMascota(petData) {
    const payload = {
      nombre: petData.nombre.trim(),
      especie: petData.especie.toLowerCase().trim(),
      raza: petData.raza?.trim() || null,
      edad: Number(petData.edad),
      sexo: petData.sexo.toLowerCase().trim(),
      tamano: petData.tamano.toLowerCase().trim().replace('pequeño', 'pequeno'),
      descripcion: petData.descripcion?.trim() || null,
      foto_url: petData.foto_url?.trim() || null
    }

    const mascota = await request(`${API_MASCOTAS}/mascotas`, {
      method: 'POST',
      headers: headersAdmin({
        'Content-Type': 'application/json'
      }),
      body: JSON.stringify(payload)
    })

    return normalizarMascota(mascota)
  },

  // La API actual no dispone de un endpoint para editar mascotas.
  async actualizarMascota() {
    throw new Error(
      'La API actual no permite editar los datos de una mascota.'
    )
  },

  // Marcar una mascota como no disponible.
  async eliminarMascota(id) {
    return request(
      `${API_MASCOTAS}/mascotas/${id}/estado?nuevo_estado=no_disponible`,
      {
        method: 'PATCH',
        headers: headersAdmin()
      }
    )
  },

  // Registrar una solicitud de adopción.
  async enviarSolicitudAdopcion(data) {
    const payload = {
      mascota_id: Number(data.mascota_id),
      nombre_solicitante: data.nombre_solicitante || data.nombre,
      correo: data.correo,
      telefono: data.telefono || data.numero,
      direccion: data.direccion,
      motivo: data.motivo
    }

    return request(`${API_ADOPCIONES}/solicitudes`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    })
  },

  // Consultar solicitudes (administrador).
  async getSolicitudes() {
    return request(`${API_ADOPCIONES}/solicitudes`, {
      headers: headersAdmin()
    })
  },

  // Aprobar una solicitud.
  async aprobarSolicitud(id) {
    return request(`${API_ADOPCIONES}/solicitudes/${id}/aprobar`, {
      method: 'PATCH',
      headers: headersAdmin()
    })
  },

  // Rechazar una solicitud.
  async rechazarSolicitud(id) {
    return request(`${API_ADOPCIONES}/solicitudes/${id}/rechazar`, {
      method: 'PATCH',
      headers: headersAdmin()
    })
  },

  // El formulario de contacto continúa siendo una demostración local.
  async enviarMensajeContacto(data) {
    console.log('[Contacto]', data)

    return {
      success: true,
      mensaje: 'Mensaje recibido correctamente',
      data
    }
  },

  // Datos estáticos del sitio.
  async getEstadisticas() {
    return STATS_DATA
  },

  async getAliados() {
    return PARTNERS_DATA
  },

  async getPasosAdopcion() {
    return ADOPTION_STEPS
  }
}
