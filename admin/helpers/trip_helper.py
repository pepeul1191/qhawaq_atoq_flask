from PIL import Image
from io import BytesIO

def get_image_metadata(image):  
  # Leer la imagen en formato PIL
  image_pil = Image.open(image)
  # Extraer los metadatos EXIF
  exif_data = image_pil._getexif()
  # Convertir los datos EXIF a un formato más legible
  tags = {Image.TAG[key]: value for key, value in exif_data.items() if key in Image.TAG}
  # Obtener la latitud, longitud y altitud si están disponibles
  latitude = tags.get('GPSInfo').get(2)
  longitude = tags.get('GPSInfo').get(4)
  altitude = tags.get('GPSInfo').get(6)

  return latitude, longitude, altitude