import requests

# URL base de la API
BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. Solicitud GET - Obtener publicaciones
def get_posts():
    print("\n[GET] Obtener publicaciones:")
    response = requests.get(f"{BASE_URL}/posts")
    if response.status_code == 200:
        posts = response.json()
        for post in posts[:5]: 
            print(f"- ID: {post['id']} | Título: {post['title']}")
    else:
        print(f"Error al obtener publicaciones: {response.status_code}")

# 2. Solicitud POST - Crear una nueva publicación
def create_post():
    print("\n[POST] Crear nueva publicación:")
    new_post = {
        "title": "Aprendiendo APIs",
        "body": "Esta publicación fue creada usando JSONPlaceholder.",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    if response.status_code == 201:
        created_post = response.json()
        print(f"Publicación creada con éxito: ID {created_post['id']} | Título: {created_post['title']}")
    else:
        print(f"Error al crear publicación: {response.status_code}")

# 3. Solicitud PUT - Actualizar una publicación completa
def update_post(post_id):
    print(f"\n[PUT] Actualizar publicación con ID {post_id}:")
    updated_post = {
        "title": "Título actualizado",
        "body": "Este es el contenido actualizado de la publicación.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=updated_post)
    if response.status_code == 200:
        updated_data = response.json()
        print(f"Publicación actualizada: ID {updated_data['id']} | Título: {updated_data['title']}")
    else:
        print(f"Error al actualizar publicación: {response.status_code}")

# 4. Solicitud PATCH - Actualizar parcialmente una publicación
def patch_post(post_id):
    print(f"\n[PATCH] Actualizar parcialmente la publicación con ID {post_id}:")
    partial_update = {
        "title": "Título modificado parcialmente"
    }
    response = requests.patch(f"{BASE_URL}/posts/{post_id}", json=partial_update)
    if response.status_code == 200:
        updated_data = response.json()
        print(f"Publicación actualizada parcialmente: ID {updated_data['id']} | Título: {updated_data['title']}")
    else:
        print(f"Error al actualizar parcialmente: {response.status_code}")

# 5. Solicitud DELETE - Eliminar una publicación
def delete_post(post_id):
    print(f"\n[DELETE] Eliminar publicación con ID {post_id}:")
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        print("Publicación eliminada con éxito.")
    else:
        print(f"Error al eliminar publicación: {response.status_code}")

# Llamada a las funciones para probar
if __name__ == "__main__":
    get_posts()  
    create_post()  
    update_post(1)  
    patch_post(1)  
    delete_post(1)  
