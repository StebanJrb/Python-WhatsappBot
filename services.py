import requests
import sett
import json

def get_whatsapp_message(message):

    if 'type' not in message :
        text = 'mensaje no reconocido'
        return text
    typeMessage = message['type']
    
    if typeMessage == 'text':
        text = message['text']['body']
    elif typeMessage == 'button':
        text = message['button']['text']
    elif typeMessage == 'interactive' and message['interactive']['type'] == 'list_reply':
        text = message['interactive']['list_reply']['title']
    elif typeMessage == 'interactive' and message['interactive']['type'] == 'button_reply':
        text = message['interactive']['button_reply']['title']
    else:
        text = 'mensaje no procesado'
    return text

def send_whatsapp_message(data):
    try:
        whatsapp_token = sett.whatsapp_token
        whatsapp_url = sett.whatsapp_url
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + whatsapp_token}
        response = requests.post(whatsapp_url, 
                                 headers=headers, 
                                 data=data)
        
        if response.status_code == 200:
            return 'mensaje enviado', 200
        else:
            return 'error al enviar mensaje', response.status_code
    except Exception as e:
        return e,403
    
def text_Message(number, text):
    data = json.dumps(
            {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": text
                }
            }
    )
    return data

def buttonReply_Message(number, options, body, footer, sedd, messageId):
    buttons = []
    for i, option in enumerate(options):
        buttons.append(
            {
                "type": "reply",
                "reply": {
                    "id": sedd + "_btn_" + str(i+1),
                    "title": option
                }
            }
        )

    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "button",
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "buttons": buttons
                }
            }
        }
    )
    return data

def listReply_Message(number, options, body, footer, sedd, messageId):
    rows = []
    for i, option in enumerate(options):
        rows.append(
            {
                "id": sedd + "_row_" + str(i+1),
                "title": option,
                "description": ""
            }
        )

    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "interactive",
            "interactive": {
                "type": "list",
                "body": {
                    "text": body
                },
                "footer": {
                    "text": footer
                },
                "action": {
                    "button": "Ver Opciones",
                    "sections": [
                        {
                            "title": "Secciones",
                            "rows": rows
                        }
                    ]
                }
            }
        }
    )
    return data

def document_Message(number, url, caption, filename):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "document",
            "document": {
                "link": url,
                "caption": caption,
                "filename": filename
            }
        }
    )
    return data

def sticker_Message(number, sticker_id):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "sticker",
            "sticker": {
                "id": sticker_id
            }
        }
    )
    return data

def get_media_id(media_name , media_type):
    media_id = ""
    if media_type == "sticker":
        media_id = sett.stickers.get(media_name, None)
    #elif media_type == "image":
    #    media_id = sett.images.get(media_name, None)
    #elif media_type == "video":
    #    media_id = sett.videos.get(media_name, None)
    #elif media_type == "audio":
    #    media_id = sett.audio.get(media_name, None)
    return media_id

def replyReaction_Message(number, messageId, emoji):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "type": "reaction",
            "reaction": {
                "message_id": messageId,
                "emoji": emoji
            }
        }
    )
    return data

def replyText_Message(number, messageId, text):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": number,
            "context": { "message_id": messageId },
            "type": "text",
            "text": {
                "body": text
            }
        }
    )
    return data

def markRead_Message(messageId):
    data = json.dumps(
        {
            "messaging_product": "whatsapp",
            "status": "read",
            "message_id":  messageId
        }
    )
    return data

def commercial_Turn(number):
    turns = []

    

def chat_administrator(text, number, messageId, name):
    text = text.lower() #mensaje que envio el usuario
    list = []
    
    if "hola" in text:
        body = "Hola!! Te has contactado con Vertice Universal.\nTu punto de partida a multiples destinos.🌏\nPara nosotros es un placer atender tu solicitud¿Que te interesa el dia de hoy?"
        footer = "Equipo VerticeUniversal"
        options = ["Visa Estudiante 👨🏻‍🎓", "Visa Turista 😎","Renovacion Visa USA 🇺🇸","Extension Estadia USA 🇺🇸","Reagendar Cita USA 2024 🇺🇸"]
        
        replyListData = listReply_Message(number, options, body, footer, "sed1", messageId)
        replyReaction = replyReaction_Message(number, messageId, "🫡")
        list.append(replyReaction)
        list.append(replyListData)
    
    elif "visa estudiante" in text:
        body = "Escoge tu proximo pais de destino como estudiante y conoce sus requisitos basicos"
        footer = "Equipo VerticeUniversal"
        options = ["Estudiante USA","Estudiante CANADA","Estudiante AUSTRALIA","Estudiante MALTA"]
        
        replyListData = listReply_Message(number, options, body, footer, "sed1", messageId)
        list.append(replyListData)
    
    elif "visa turista" in text:
        body = "Escoge tu próximo país de destino como turista y conoce sus requisitos básicos"
        footer = "Equipo VerticeUniversal"
        options = ["Turista USA","Turista CANADA","Turista AUSTRALIA"]
        
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        list.append(replyButtonData)
    
    elif "renovacion visa usa" in text:
        bodyMessage = '''Si deseas renovar tu VISA a los Estados Unidos. 🇺🇸
🔸Debes contar con un pasaporte que tenga una vigencia superior a 6 meses. 🪪
🔸Si tu VISA ya venció, podrás renovarla siempre que no haya superado un periodo de 48 meses.🗓️
🔸Si la VISA que deseas renovar se te otorgó siendo menor de edad.🚼, tendrás que presentar entrevista consular.
🔸Si eres ciudadano venezolano 🇻🇪, debes presentar entrevista consular obligatoria.
🔸Completar formulario de solicitud formal de RENOVACION VISA USA de nuestra Agencia.

Los costos generales son los siguientes en Moneda USD:
✓ Pago Embajada Americana $185 USD
✓ Trámite y Asesoría $75 USD.
'''

        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)

    elif "extension estadia usa" in text:
        bodyMessage ='''Deseas Extender tu Estadía en 🇺🇸
🔸Para poder extender tu estadía en USA, lo más importante es que no hayas superado el tiempo máximo que se te permitió al ingreso.
🔸Debes contar con un pasaporte que tenga una vigencia superior a 6 meses.
🔸Debes contar con fondos suficientes o un patrocinador que respalde tu solicitud para una estadía de 1 año.

Entre los beneficios que obtendrás están:
🔸Poder vivir legalmente dentro de los USA indefinidamente.👌🏽
🔸Aceptar una oferta laboral 📃 en tu profesión o actividad en el futuro.
🔸Poder iniciar tu propio negocio.
🔸Aplicar a otras VISAS ejemplo VISA EB3👷🏻 o VISA F1 ESTUDIANTE 👨🏼‍🎓.
🔸Y la más importante, la tranquilidad de vivir sin esconderse, entre muchas otras.

Los costos generales son los siguientes en Moneda USD:
✓ Inscripción F1 $200 USD👨🏼‍🎓
✓ SEVIS $350 USD para F1👨🏼‍🎓
✓ BIOMETRICOS $85 USD
✓ i-539 FORM USCIS $370 USD
✓ HONORARIOS TRAMITE Y ASESORIA $700 USD

🔸Todas las solicitudes de Extensión de Estadía y Cambio de Estatus son diferentes y particulares a cada caso en específico.
🔸Los valores son una referencia y pueden variar.
'''
        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)

    elif "reagendar cita usa 2024" in text:
        bodyMessage = '''Deseas REAGENDAR🤩 TU VISA A USA 🇺🇸
🔸Esta solicitud tiene un costo de 300 COP.
🔸Solamente es reagendable solicitudes individuales👤.
🔸Aplica para solicitantes nuevos o que estén en 2025.

☘ Si deseas reagendar y obtener más información contacta a nuestras representantes.
'''

        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)
    elif "estudiante usa" in text:
        bodyMessage = '''VISA DE ESTUDIANTE 👨🏼‍🎓
USA 🇺🇸
Para solicitar tu VISA hacia USA necesitas:
🔸Foto de pasaporte vigente. 🪪
🔸Si cuentas con VISA USA 🇺🇲, añadir foto con sellos
🔸Una foto tuya 📸 en fondo blanco actual.👤
🔸Extractos bancarios para demostrar solvencia económica.💰
🔸Formulario de solicitud formal de VISA de nuestra Agencia.

*_Nosotros nos encargamos de todo._*🤓

Acompañamiento durante la solicitud, agendamiento de citas, diligenciamiento de formularios, solicitud i-20, envío, recepción, seguimiento de documentos y preparación para la entrevista consular de 1Hr.

Los costos generales son los siguientes en Moneda USD:
✓ Inscripción al College en USA $100-$200 USD aprox.
✓ Pago Embajada Americana $185 USD
✓ Pago SEVIS $350 USD
✓ Trámite y Asesoría $90 USD.
*📑Traducción De Documentos y Certificados adicionales. (Solo si se requiere)
*🩺Seguro Medico Internacional para estudiantes (Sugerido)
'''
        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)

    elif "estudiante canada" in text:
        bodyMessage = '''VISA DE ESTUDIANTE 👨🏼‍🎓
CANADA 🇨🇦
Para solicitar tu VISA hacia CANADA necesitas:
🔸Foto de pasaporte vigente. 🪪
🔸Si cuentas con VISA USA 🇺🇲, añadir foto con sellos
🔸Una foto tuya 📸 en fondo blanco actual.👤
🔸Extractos bancarios para demostrar solvencia económica.💰
🔸Formulario de solicitud formal de VISA de nuestra Agencia.

*_Nosotros nos encargamos de todo._*🤓

Acompañamiento durante la solicitud, agendamiento de citas, diligenciamiento de formularios, solicitud LOA, envío, recepción, seguimiento de documentos, carta de intención y su preparación.

Los costos generales son los siguientes en Moneda CAD:
✓ Inscripción al College de CANADA $180 USD CAD. Aprox
✓ Pago Embajada Canada. $180 CAD
✓ Pago Biométricos $85  CAD
✓ Trámite y Asesoría $130  CAD
*📑Traducción De Documentos y Certificados adicionales.
*📚Pago anticipado de tu programa de idiomas x 6 meses
*🩺Seguro Medico Internacional para estudiantes Obligatorio.
'''
        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)

    elif "estudiante australia" in text:
        bodyMessage = '''VISA DE ESTUDIANTE👨🏼‍🎓
AUSTRALIA🇦🇺
Para solicitar tu VISA hacia AUSTRALIA necesitas:
🔸Foto de pasaporte vigente. 🪪
🔸Si cuentas con VISA USA 🇺🇲, añadir foto con sellos
🔸Una foto tuya 📸 en fondo blanco actual.👤
🔸Extractos bancarios para demostrar solvencia económica.💰
🔸Formulario de solicitud formal de VISA de nuestra Agencia.

*_Nosotros nos encargamos de todo._*🤓

Acompañamiento durante la solicitud, agendamiento de citas, diligenciamiento de formularios, solicitud CEO, envío, recepción, seguimiento de documentos, carta de intención y preparación de GTE.

Los costos generales son los siguientes en Moneda AUD:
✓ Pago ante la embajada $650 AUD
✓ Pago de Inscripción College $200 AUD Aprox.
✓ Pago Biométricos $60 AUD
✓ Trámite y Asesoría $200 USD AUD
✓ Exámenes médicos $480.000 COP
*📚 Pago Anticipado de tu Programa de Idiomas x 6.
*🩺 Seguro Médico Internacional para Estudiantes Obligatorio.
'''
        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)

    elif "turista usa" in text:
        bodyMessage = '''VISA DE TURISTA😎
USA 🇺🇸
Para solicitar tu VISA TURISTA A USA necesitas:
🔸Foto de pasaporte vigente. 🪪
🔸Si cuentas con VISA USA 🇺🇲, añadir foto con sellos.
🔸Una foto tuya 📸 en fondo blanco actual.👤
🔸Extractos bancarios para demostrar solvencia económica.💰
🔸Formulario de solicitud formal de VISA de nuestra Agencia.

*_Nosotros nos encargamos de todo._*🤓

Acompañamiento durante la solicitud, agendamiento de citas, diligenciamiento de formularios, solicitud VISA B1/B2, envío, recepción, seguimiento de documentos y preparación para la entrevista consular de 1Hr.

Los costos generales son los siguientes en Moneda USD:
✓ Pago Embajada Americana $185 USD
✓ Trámite y Asesoría $75 USD.
'''
        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)

    elif "turista canada" in text:
        bodyMessage = '''VISA DE TURISTA😎
CANADA 🇨🇦
Para solicitar tu VISA A CANADA necesitas:
🔸Foto de pasaporte vigente. 🪪
🔸Si cuentas con VISA USA 🇺🇲, añadir foto con sellos.
🔸Una foto tuya 📸 en fondo blanco actual.👤
🔸Extractos bancarios para demostrar solvencia económica.💰
🔸Formulario de solicitud formal de VISA de nuestra Agencia.

*_Nosotros nos encargamos de todo._*🤓

Acompañamiento durante la solicitud, agendamiento de citas, diligenciamiento de formularios, solicitud VISA VISITANTE TEMPORAL, envío, recepción, seguimiento de documentos y preparación de cartas de invitación e intención.

Los costos generales son los siguientes en Moneda CAD:
✓ Pago Embajada Canada $100 CAD
✓ Pago Biométricos $85  CAD
✓ Trámite y Asesoría $130 USD
✓ Traducción de Documentos y Certificados.
'''
        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)

    elif "turista australia" in text:
        bodyMessage = '''VISA DE TURISTA😎
AUSTRALIA🇦🇺 🇦
Para solicitar tu VISA A AUSTRALIA necesitas:
🔸Foto de pasaporte vigente. 🪪
🔸Si cuentas con VISA USA 🇺🇲, añadir foto con sellos.
🔸Una foto tuya 📸 en fondo blanco actual.👤
🔸Extractos bancarios para demostrar solvencia económica.💰
🔸Formulario de solicitud formal de VISA de nuestra Agencia.

*_Nosotros nos encargamos de todo._*🤓

Acompañamiento durante la solicitud, agendamiento de citas, diligenciamiento de formularios, solicitud VISA TURISTA, envío, recepción, seguimiento de documentos y preparación de cartas de invitación e intención.

Los costos generales son los siguientes en Moneda AUD:
✓ Pago Consular $190 AUD
✓ Pago Biométricos $60 AUD
✓ Trámite y Asesoría $140 USD
✓ Exámenes médicos $480.000 COP
✓ Traducción de Documentos y Certificados.
'''
        body = "Deseas ser contactad@ por una de nuestras asesoras? 👩🏻‍💻"
        footer = "Equipo VerticeUniversal"
        options = ["Si✅ ","No❌"]
        
        replyTextData = text_Message(number, bodyMessage)
        replyButtonData = buttonReply_Message(number, options, body, footer, "sed1", messageId)
        
        list.append(replyTextData)
        list.append(replyButtonData)
    
    elif "si" in text:
        bodyMessage = '''Para nosotros es un placer atenderte, por favor déjanos la siguiente información para poder ayudarte con tu solicitud de VISA:
Nombre👤:
Correo Electrónico📧:
Destino que te interesa y tipo de visa🌏:

Pronto uno de nuestros asesores se pondrá en contacto contigo para brindarte toda la asesoría y acompañamiento necesario en el proceso.

Gracias por elegir Vertice Universal.🌐 ¡Esperamos poder ayudarte a cumplir tus planes de viaje y estadía en el extranjero!
''' 
        
        replyTextData = text_Message(number, bodyMessage)
        
        list.append(replyTextData)
    
    elif "no" in text:
        bodyMessage = '''Gracias por contactar con Vertice Universal. 🌐
Nos especializamos en brindar servicios de asesoría y acompañamiento para obtener distintos tipos de VISAS a varios destinos internacionales.
Si en el momento no te encuentras interesado en ninguna de las opciones anteriores, no te preocupes, estamos aquí para ayudarte en futuras oportunidades.
Si en el futuro cambias de opinión o tienes cualquier consulta, no dudes en contactarnos.

Recuerda que estamos disponibles para atender tus inquietudes y asistirte en cada paso del proceso.
Deseamos que tengas una excelente experiencia en tus planes de viaje y estadía en el extranjero.

Si en el futuro deseas recibir más información o asesoría personalizada, por favor, no dudes en contactar a nuestras representantes.
'''
        
        replyTextData = text_Message(number, bodyMessage)
        list.append(replyTextData)
    else :
        data = text_Message(number,"Lo siento, no entendí lo que dijiste. escribe hola para volver a empezar")
        list.append(data)

    for item in list:
        send_whatsapp_message(item)    


    


