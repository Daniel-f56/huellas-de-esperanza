/**
 * Servicio Centralizado de API & Base de Datos Local - Huellas de Esperanza
 * 
 * Gestiona el ciclo completo de las mascotas (CRUD), adopciones y contacto.
 * Los datos se sincronizan con localStorage ('huellas_mascotas_db') para persistir
 * entre recargas y reflejarse de inmediato en la sección pública "Encuentra a un amigo".
 */

import { INITIAL_PETS_DB, PARTNERS_DATA, STATS_DATA, ADOPTION_STEPS } from '../data/pets.js'

const DB_KEY = 'huellas_mascotas_db'

function loadLocalDB() {
  try {
    const raw = localStorage.getItem(DB_KEY)
    if (raw) {
      const parsed = JSON.parse(raw)
      if (Array.isArray(parsed) && parsed.length > 0) {
        return parsed
      }
    }
  } catch (e) {
    console.error('Error cargando base de datos local:', e)
  }
  // Si no hay datos en localStorage, inicializamos con los datos por defecto
  saveLocalDB(INITIAL_PETS_DB)
  return [...INITIAL_PETS_DB]
}

function saveLocalDB(data) {
  try {
    localStorage.setItem(DB_KEY, JSON.stringify(data))
  } catch (e) {
    console.error('Error guardando en base de datos local:', e)
  }
}

export const apiService = {
  /**
   * Obtiene todas las mascotas registradas en la base de datos
   */
  async getMascotas() {
    return Promise.resolve(loadLocalDB())
  },

  /**
   * Obtiene únicamente las mascotas en estado "disponible" para la vista pública
   */
  async getMascotasDisponibles() {
    const all = loadLocalDB()
    return Promise.resolve(all.filter(p => p.estado === 'disponible'))
  },

  /**
   * Obtiene una mascota por su ID
   */
  async getMascotaPorId(id) {
    const all = loadLocalDB()
    const pet = all.find(p => p.id === Number(id))
    return Promise.resolve(pet || null)
  },

  /**
   * Crea una nueva mascota en la base de datos
   * @param {Object} petData
   * La fecha de registro se genera automáticamente en formato ISO 8601
   * El estado por defecto es "disponible"
   */
  async crearMascota(petData) {
    const all = loadLocalDB()
    
    // Generar nuevo ID incremental
    const maxId = all.reduce((max, p) => (p.id > max ? p.id : max), 0)
    const newId = maxId + 1

    const newPet = {
      id: newId,
      nombre: petData.nombre ? petData.nombre.trim() : 'Sin nombre',
      especie: petData.especie ? petData.especie.toLowerCase().trim() : 'perro',
      raza: petData.raza ? petData.raza.trim() : 'Criollo',
      edad: Number(petData.edad) || 12,
      sexo: petData.sexo ? petData.sexo.toLowerCase().trim() : 'hembra',
      tamano: petData.tamano ? petData.tamano.toLowerCase().trim() : 'mediano',
      descripcion: petData.descripcion ? petData.descripcion.trim() : '',
      foto_url: petData.foto_url ? petData.foto_url.trim() : null,
      estado: petData.estado ? petData.estado.toLowerCase().trim() : 'disponible',
      fecha_registro: new Date().toISOString()
    }

    all.unshift(newPet) // Agregarlo al inicio
    saveLocalDB(all)
    return Promise.resolve(newPet)
  },

  /**
   * Actualiza una mascota existente
   */
  async actualizarMascota(id, petData) {
    const all = loadLocalDB()
    const index = all.findIndex(p => p.id === Number(id))
    if (index === -1) {
      throw new Error(`Mascota con ID ${id} no encontrada`)
    }

    const current = all[index]
    const updated = {
      ...current,
      nombre: petData.nombre !== undefined ? petData.nombre.trim() : current.nombre,
      especie: petData.especie !== undefined ? petData.especie.toLowerCase().trim() : current.especie,
      raza: petData.raza !== undefined ? petData.raza.trim() : current.raza,
      edad: petData.edad !== undefined ? Number(petData.edad) : current.edad,
      sexo: petData.sexo !== undefined ? petData.sexo.toLowerCase().trim() : current.sexo,
      tamano: petData.tamano !== undefined ? petData.tamano.toLowerCase().trim() : current.tamano,
      descripcion: petData.descripcion !== undefined ? petData.descripcion.trim() : current.descripcion,
      foto_url: petData.foto_url !== undefined ? (petData.foto_url ? petData.foto_url.trim() : null) : current.foto_url,
      estado: petData.estado !== undefined ? petData.estado.toLowerCase().trim() : current.estado
      // fecha_registro se conserva intacta
    }

    all[index] = updated
    saveLocalDB(all)
    return Promise.resolve(updated)
  },

  /**
   * Elimina una mascota por su ID
   */
  async eliminarMascota(id) {
    const all = loadLocalDB()
    const filtered = all.filter(p => p.id !== Number(id))
    saveLocalDB(filtered)
    return Promise.resolve(true)
  },

  /**
   * Envía la solicitud de adopción con los 5 campos requeridos
   */
  async enviarSolicitudAdopcion(data) {
    console.log('[API] Solicitud de adopción recibida:', data)
    return Promise.resolve({
      success: true,
      mensaje: 'Solicitud registrada exitosamente',
      data
    })
  },

  /**
   * Envía el formulario de contacto
   */
  async enviarMensajeContacto(data) {
    console.log('[API] Contacto recibido:', data)
    return Promise.resolve({
      success: true,
      mensaje: 'Mensaje enviado exitosamente',
      data
    })
  },

  async getEstadisticas() {
    return Promise.resolve(STATS_DATA)
  },

  async getAliados() {
    return Promise.resolve(PARTNERS_DATA)
  },

  async getPasosAdopcion() {
    return Promise.resolve(ADOPTION_STEPS)
  }
}
