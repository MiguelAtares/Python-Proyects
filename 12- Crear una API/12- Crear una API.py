from flask import Flask, jsonify, request  

app = Flask(__name__)  
# Creamos una ruta básica
@app.route('/') 
def home(): 
    return "Bienvenido a la API de Star Wars"  

characters = [ 
    {"id": 1, "name": "Luke Skywalker", "species": "Human"},
    {"id": 2, "name": "Darth Vader", "species": "Human"},
    {"id": 3, "name": "Yoda", "species": "Unknown"}
]

@app.route('/characters', methods=['GET', 'POST']) 
def manage_characters(): 
    if request.method == 'GET': 
        species = request.args.get('species')  
        if species:
            filtered_characters = [character for character in characters if character["species"] == species]  
            if not filtered_characters:
                return jsonify({"error":f"No se encontraron personajes con la especie {species}"})  
            return jsonify(filtered_characters)  # Devolvemos la lista de personajes filtrada en formato JSON.
        return jsonify(characters) 
    
    elif request.method == 'POST':
        try:
            new_character = request.get_json()  
            required_fields = ["id", "name", "species"]  # Campos obligatorios
            for field in required_fields:
                if field not in new_character:
                    raise KeyError(f"Falta el campo obligatorio: {field}")
            
            if any(c["id"] == new_character["id"] for c in characters): 	
                raise ValueError(f"Ya existe un personaje con el id {new_character['id']}")
            
            # Agregamos el nuevo personaje
            characters.append(new_character)
            return jsonify({"message": "Personaje añadido exitosamente", "character": new_character}), 201
        
        except KeyError as ke:
            return jsonify({"error": str(ke)}), 400  # Error de campo faltante. 
        except ValueError as ve:
            return jsonify({"error": str(ve)}), 409  # Error de conflicto de ID. 
        except Exception as e:
            return jsonify({"error": "Ocurrió un error inesperado"}), 500 #Captura cualquier error.

@app.route('/characters/<int:id>') 
def get_characters_by_id(id):
    try:
        character = next((c for c in characters if c["id"] == id), None) 
        if character is None:
            # Lanzar un error si el personaje no existe
            raise ValueError(f"No se encontro un personaje con el id {id}")
        return jsonify(character)  # Devolver el personaje encontrado
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404  # Devolver un error 404
    except Exception as e:
        # Manejo genérico de errores
        return jsonify({"error": "Ocurrio un error inesperado"}), 500


@app.route('/characters/update/<int:id>', methods=['PUT', 'PATCH']) 
def update_character_by_id(id): 
    try:
        character = next((c for c in characters if c["id"] == id), None)
        if not character:
            raise ValueError(f"No se encontró un personaje con el id {id}")
        
        updates = request.get_json()  # Obtener los datos enviados en el cuerpo de la solicitud
        if request.method == 'PUT':
            # Validar que se envíen todos los campos en un PUT
            required_fields = ["id", "name", "species"]
            for field in required_fields:
                if field not in updates:
                    raise KeyError(f"Falta el campo obligatorio: {field}")
            character.update(updates)
        elif request.method == 'PATCH':
            # Solo actualizamos los campos enviados en un PATCH
            character.update(updates)
        
        return jsonify({"message": "Personaje actualizado exitosamente", "character": character}), 200
    except KeyError as ke:
        return jsonify({"error": str(ke)}), 400
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado"}), 500

# Endpoint para eliminar un personaje por ID
@app.route('/characters/delete/<int:id>', methods=['DELETE'])
def delete_character_by_id(id):
    try:
        character = next((c for c in characters if c["id"] == id), None)
        if not character:
            raise ValueError(f"No se encontró un personaje con el id {id}")
        characters.remove(character)  
        return jsonify({"message": f"Personaje con id {id} eliminado exitosamente"}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado"}), 500

if __name__ == "__main__": 
    app.run(debug=True)  
