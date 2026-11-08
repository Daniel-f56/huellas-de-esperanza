/**
 * Base de datos inicial de Mascotas - Huellas de Esperanza
 * 
 * Cada registro cumple con el esquema exacto requerido por el sistema:
 * {
 *   "id": number,
 *   "nombre": string,
 *   "especie": "perro" | "gato",
 *   "raza": string,
 *   "edad": number (meses),
 *   "sexo": "hembra" | "macho",
 *   "tamano": "pequeño" | "mediano" | "grande",
 *   "descripcion": string,
 *   "foto_url": string | null,
 *   "estado": "disponible" | "adoptado" | "en_tratamiento",
 *   "fecha_registro": string (ISO 8601)
 * }
 */

export const INITIAL_PETS_DB = [
  {
    id: 1,
    nombre: "June",
    especie: "gato",
    raza: "Tabby Doméstico",
    edad: 12,
    sexo: "hembra",
    tamano: "pequeño",
    descripcion: "June es una gatita curiosa, tranquila y extremadamente cariñosa. Le encanta dormir bajo los rayos de sol y recibir caricias.",
    foto_url: "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-01T10:15:00.000000Z"
  },
  {
    id: 2,
    nombre: "Quackers",
    especie: "perro",
    raza: "Mestizo Shiba / Spitz",
    edad: 24,
    sexo: "macho",
    tamano: "mediano",
    descripcion: "Quackers es un torbellino de alegría y ternura. Aprende trucos con rapidez y adora jugar con pelotas en el parque.",
    foto_url: "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-02T14:20:00.000000Z"
  },
  {
    id: 3,
    nombre: "Pebble",
    especie: "perro",
    raza: "Chihuahua Mini",
    edad: 12,
    sexo: "hembra",
    tamano: "pequeño",
    descripcion: "Pebble es diminuta pero con un corazón gigantesco. Es un poco tímida los primeros 5 minutos, luego no querrá separarse de ti.",
    foto_url: "https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-03T09:30:00.000000Z"
  },
  {
    id: 4,
    nombre: "Freckle",
    especie: "perro",
    raza: "Labrador Mestizo",
    edad: 36,
    sexo: "macho",
    tamano: "grande",
    descripcion: "Freckle es el compañero perfecto para caminatas y aventuras al aire libre. Carácter noble, equilibrado y obediente.",
    foto_url: "https://images.unsplash.com/photo-1552053831-71594a27632d?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-04T16:45:00.000000Z"
  },
  {
    id: 5,
    nombre: "Brownie",
    especie: "perro",
    raza: "Pastor Mestizo Negro",
    edad: 60,
    sexo: "macho",
    tamano: "mediano",
    descripcion: "Brownie es un perro sereno, de mirada dulce y pasos tranquilos. Sabe caminar con correa de manera impecable y adora la compañía humana.",
    foto_url: "https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-05T11:10:00.000000Z"
  },
  {
    id: 6,
    nombre: "Marley",
    especie: "perro",
    raza: "Golden Mestizo",
    edad: 60,
    sexo: "hembra",
    tamano: "grande",
    descripcion: "Marley siempre tiene una sonrisa dibujada en el rostro. Es muy sociable con otros perros y adora correr en campos abiertos.",
    foto_url: "https://images.unsplash.com/photo-1587300003388-59208cc962cb?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-05T18:00:00.000000Z"
  },
  {
    id: 7,
    nombre: "Archi",
    especie: "gato",
    raza: "Naranja Doméstico",
    edad: 48,
    sexo: "macho",
    tamano: "pequeño",
    descripcion: "Archi es un gato majestuoso de pelaje naranja suave como la seda. Es tranquilo, educado y disfruta de largas siestas.",
    foto_url: "https://images.unsplash.com/photo-1574158622682-e40e69881006?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-06T08:20:00.000000Z"
  },
  {
    id: 8,
    nombre: "Coolie",
    especie: "perro",
    raza: "Sabueso Mestizo Senior",
    edad: 96,
    sexo: "macho",
    tamano: "grande",
    descripcion: "Coolie es un perro senior con alma de cachorro sabio. No requiere mucho ejercicio, solo paseos cortos, buena comida y mucho amor.",
    foto_url: "https://images.unsplash.com/photo-1561037404-61cd46aa615b?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-06T15:40:00.000000Z"
  },
  {
    id: 9,
    nombre: "Luna",
    especie: "perro",
    raza: "Criolla",
    edad: 24,
    sexo: "hembra",
    tamano: "mediano",
    descripcion: "Perrita cariñosa y juguetona.",
    foto_url: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=800&q=80",
    estado: "disponible",
    fecha_registro: "2026-11-07T22:15:16.312282Z"
  }
];

export const ADOPTION_STEPS = [
  {
    number: '01',
    title: 'Encuentra a tu compañero',
    subtitle: 'Explora perfiles y compatibilidad',
    description: 'Revisa las fichas de nuestros rescatados, sus niveles de energía, edades y compatibilidad con niños u otras mascotas.',
    icon: 'search'
  },
  {
    number: '02',
    title: 'Postúlate en línea',
    subtitle: 'Formulario sin costo ni compromiso',
    description: 'Completa el formulario de adopción con tus datos de contacto y cuéntanos por qué deseas abrirle las puertas de tu hogar.',
    icon: 'form'
  },
  {
    number: '03',
    title: 'Visita guiada al refugio',
    subtitle: 'Conoce en persona a tu match',
    description: 'Te invitamos a compartir un momento de juego y paseo con el animal para ver cómo interactúan juntos.',
    icon: 'heart'
  },
  {
    number: '04',
    title: 'Bienvenida a casa',
    subtitle: 'Firma de acuerdo y seguimiento',
    description: 'Entregamos a la mascota con carnet veterinario al día, microchip y asesoramiento permanente para su bienestar.',
    icon: 'home'
  }
];

export const PARTNERS_DATA = [
  {
    name: 'Cadena Silpo',
    badge: 'Aliado de Alimentos',
    description: 'Reconocida cadena de supermercados comprometida con el bienestar animal, donando toneladas de alimento de calidad y suministros para nuestros refugios de emergencia.',
    details: 'Ha donado más de 12 toneladas de alimento nutritivo para nuestros rescatados.',
    logoText: 'Silpo'
  },
  {
    name: 'Compañía Purina',
    badge: 'Nutrición & Cuidado',
    description: 'Su inquebrantable compromiso con el bienestar animal y la nutrición ha transformado de forma profunda y positiva la vida de nuestros amigos peludos.',
    details: 'Nutrición científica garantizada para cada etapa de recuperación de nuestros perros y gatos.',
    logoText: 'PURINA'
  },
  {
    name: 'Red Veterinaria Integral',
    badge: 'Aliado Clínico',
    description: 'Equipo de veterinarios voluntarios que realizan esterilizaciones, cirugías reconstructivas y chequeos preventivos.',
    details: 'Cobertura médica 24/7 para emergencias de rescate animal.',
    logoText: 'Clínica Veterinaria'
  }
];

export const STATS_DATA = {
  adoptions: {
    number: '48',
    title: 'Adopciones Exitosas',
    description: 'animales adoptados exitosamente en hogares amorosos y responsables.'
  },
  treatments: {
    number: '208',
    title: 'Tratamientos Médicos Brindados',
    description: 'animales que reciben atención médica, vacunas completas y cuidado preventivo.'
  }
};
