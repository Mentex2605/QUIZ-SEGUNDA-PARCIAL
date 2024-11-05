import flet as ft

# Preguntas y respuestas del quiz de cultura general
preguntas = [
    {"pregunta": "¿Cuál es el planeta más cercano al Sol?", "respuesta": "Mercurio", "comentario": "Mercurio es el planeta más cercano al Sol en nuestro sistema solar."},
    {"pregunta": "¿Cuántos continentes tiene la Tierra?", "respuesta": "7", "comentario": "La Tierra tiene 7 continentes."},
    {"pregunta": "¿Cuál es el animal terrestre más rápido?", "respuesta": "Guepardo", "comentario": "El guepardo es el animal terrestre más rápido."},
    {"pregunta": "¿Cuál es el río más largo del mundo?", "respuesta": "Amazonas", "comentario": "El Amazonas es el río más largo del mundo."},
    {"pregunta": "¿Cuál es el país más grande en extensión?", "respuesta": "Rusia", "comentario": "Rusia es el país más grande en extensión territorial."},
    {"pregunta": "¿En qué año llegó el hombre a la Luna?", "respuesta": "1969", "comentario": "El hombre llegó a la Luna en 1969."},
    {"pregunta": "¿Cuál es el océano más grande del mundo?", "respuesta": "Pacífico", "comentario": "El Océano Pacífico es el más grande del mundo."},
    {"pregunta": "¿Cuántos huesos tiene el cuerpo humano adulto?", "respuesta": "206", "comentario": "El cuerpo humano adulto tiene 206 huesos."},
    {"pregunta": "¿Cuál es el elemento químico más abundante en la atmósfera de la Tierra?", "respuesta": "Nitrógeno", "comentario": "El nitrógeno es el elemento más abundante en la atmósfera."},
    {"pregunta": "¿Quién pintó la Mona Lisa?", "respuesta": "Leonardo da Vinci", "comentario": "Leonardo da Vinci pintó la famosa obra de la Mona Lisa."},
]

# Variables globales para el puntaje, la pregunta actual y el historial de puntajes
puntaje = 0
indice_pregunta = 0
puntajes_historicos = []

# Función principal de Flet
def main(page: ft.Page):
    # Configuración de la página
    page.title = "Quiz de Cultura General"
    page.padding = 20
    page.bgcolor = ft.colors.BLACK  # Fondo de la página negro

    # Campo para ingresar el nombre del jugador
    txt_nombre = ft.TextField(
        label="Ingresa tu nombre",
        width=300,
        border_color=ft.colors.DEEP_PURPLE,
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE  # Texto blanco
    )

    # Sección de la pregunta
    lbl_pregunta = ft.Text(
        preguntas[indice_pregunta]["pregunta"],
        size=26,
        color=ft.colors.WHITE,  # Texto blanco
        weight="bold"
    )

    # Campo de entrada para la respuesta
    txt_respuesta = ft.TextField(
        label="Escribe tu respuesta aquí",
        width=300,
        border_color=ft.colors.DEEP_PURPLE,
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE  # Texto blanco
    )

    # Etiquetas para mostrar comentarios y puntaje
    lbl_resultado = ft.Text(size=20, color=ft.colors.WHITE)  # Texto blanco
    lbl_puntaje = ft.Text(f"Puntaje: {puntaje}", size=18, color=ft.colors.WHITE)  # Texto blanco
    lbl_historial = ft.Text(f"Historial de Puntajes: {puntajes_historicos}", size=18, color=ft.colors.WHITE)  # Texto blanco

    # Función para manejar la respuesta del usuario
    def responder(e):
        global puntaje, indice_pregunta
        respuesta_usuario = txt_respuesta.value.strip()

        # Verifica si la respuesta es correcta
        if respuesta_usuario.lower() == preguntas[indice_pregunta]["respuesta"].lower():
            lbl_resultado.value = "¡Correcto! " + preguntas[indice_pregunta]["comentario"]
            lbl_resultado.color = ft.colors.GREEN
            puntaje += 1  # Aumenta el puntaje
            lbl_puntaje.value = f"Puntaje: {puntaje}"
        else:
            lbl_resultado.value = f"Incorrecto. {preguntas[indice_pregunta]['comentario']}"
            lbl_resultado.color = ft.colors.RED

        # Avanza a la siguiente pregunta o finaliza el quiz
        indice_pregunta += 1
        if indice_pregunta < len(preguntas):
            lbl_pregunta.value = preguntas[indice_pregunta]["pregunta"]
            txt_respuesta.value = ""  # Limpia el campo de respuesta
        else:
            lbl_pregunta.value = "¡Quiz finalizado!"
            txt_respuesta.visible = False  # Oculta el campo de respuesta
            btn_responder.visible = False  # Oculta el botón de respuesta
            btn_reiniciar.visible = True  # Muestra el botón de reiniciar

            # Guarda el puntaje final en el historial
            nombre_jugador = txt_nombre.value.strip()
            puntajes_historicos.append(f"{nombre_jugador}: {puntaje}")
            lbl_historial.value = f"Historial de Puntajes: {puntajes_historicos}"

        # Actualiza los elementos en la página
        page.update()

    # Función para reiniciar el quiz
    def reiniciar_quiz(e):
        global puntaje, indice_pregunta
        puntaje = 0
        indice_pregunta = 0
        lbl_pregunta.value = preguntas[indice_pregunta]["pregunta"]
        lbl_puntaje.value = f"Puntaje: {puntaje}"
        lbl_resultado.value = ""
        txt_respuesta.value = ""
        txt_respuesta.visible = True
        btn_responder.visible = True
        btn_reiniciar.visible = False
        page.update()

    # Botón para enviar la respuesta
    btn_responder = ft.ElevatedButton("Responder", on_click=responder, bgcolor=ft.colors.DEEP_PURPLE, color=ft.colors.WHITE)

    # Botón para reiniciar el quiz 
    btn_reiniciar = ft.ElevatedButton("Reiniciar", on_click=reiniciar_quiz, visible=False, bgcolor=ft.colors.TEAL, color=ft.colors.WHITE)

    # Layout de la página usando Column para organizar los elementos
    page.add(
        ft.Column(
            [
                txt_nombre,
                ft.Container(lbl_pregunta, padding=20, alignment=ft.alignment.center),
                txt_respuesta,
                btn_responder,
                ft.Container(lbl_resultado, padding=10),
                ft.Row([lbl_puntaje, lbl_historial], alignment="spaceBetween"),
                btn_reiniciar
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
