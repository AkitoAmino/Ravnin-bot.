"""
MIT License

Copyright (c) 2021 Standby 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import re, random

# Funcion que muestra el mensaje de ayuda requerido - Fin
def icon_bot(media,args):
    try:

        args.subclient.send_message(args.chatId,
                               "Icon trocado.")
        args.subclient.edit_profile(icon=str(media))

    except Exception:

        args.subclient.send_message(args.chatId,
                               "O comando tá errado... ou talvez nasci degenerada.")

def fondo_perfil(media,args):
    try:

        args.subclient.send_message(args.chatId,
                               "Fundo do perfil trocado.")
        args.subclient.edit_profile(backgroundImage=str(media))

    except Exception:

        args.subclient.send_message(args.chatId,
                               "Não é assim o comando, e eu também esqueci.")

def portada(media,args):
    try:

        args.subclient.send_message(args.chatId,
                               "Imagem do chat alterada.")
        args.subclient.edit_chat(chatId=args.chatId, icon=str(media))

    except Exception:

        args.subclient.send_message(args.chatId,
                               "Errou o comando inteiro.")


def fondo(media,args):
    try:

        args.subclient.send_message(args.chatId,
                               "Fundo do chat trocado, agora vou trocar seu fundo")
        args.subclient.edit_chat(chatId=args.chatId,
                            backgroundImage=str(media))

    except Exception:

        args.subclient.send_message(args.chatId,
                               "comando todo cagado")

def acepto(media,args):
    try:

        args.subclient.send_message(args.chatId,
                               f"{random.choice(casarse)} ")
        args.subclient.edit_chat(chatId=args.chatId,
                            backgroundImage=str(media))

    except Exception:

        args.subclient.send_message(args.chatId,
                               "Errou o comando")

def delete(args, replyToMessage, admins):

      if args.profileId in admins:
         args.subclient.delete_message(args.chatId,replyToMessage, False, "Prueba")
         args.subclient.send_message(args.chatId,"Mensagem apagada haha! >:3")


def trivia(args,replyMessage,idioma,mensaje):
      
      if re.search("Ciencia", replyMessage["content"]):
           result = "Ciencia"
      elif re.search("Geografía", replyMessage["content"]):
           result = "Geografía"
      elif re.search("Música", replyMessage["content"]):
           result = "Música"
      elif re.search("Arte", replyMessage["content"]):
           result = "Arte"
      elif re.search("General", replyMessage["content"]):
           result = "General"
      elif re.search("Anime", replyMessage["content"]):
           result = "Anime"

      search_question = idioma[f"{result}"]
      pregunta = None
      respuesta = None

      for i in search_question:
          if pregunta == None:
             pregunta = re.search(i["pregunta"],
                                             replyMessage["content"])

          if respuesta == None:
             respuesta = re.search(i["respuesta_correcta"],
                                              replyMessage["content"])

      pregunta = pregunta.group() + "?"
      respuesta = respuesta.group()

      if pregunta != None:
         comp = re.search(respuesta, replyMessage["content"])
         comp = comp.span()
         params2 = replyMessage["content"][comp[0]-4:comp[0]-3]
         if params2 == mensaje:
            args.subclient.send_message(
              args.chatId,
              f"[C]✧ Que gênio!\n\n[C]Respondeu corretamente a pergunta; {pregunta}! \n\n[C]R. {mensaje}"
            )
         else:
            args.subclient.send_message(
              args.chatId,
              f"[C]✧ animal burrao\n\n[C]respondeu incorretamente; {pregunta}! \n\n[C]reposta != {mensaje}")

responder_acciones = {
    '.fondo': fondo,
    '.portada': portada,
    "-icon": icon_bot,
    "-fondo": fondo_perfil,
	"-delete": delete
}

casarse = ["Y los declaro marido y mujer.", "VIVAN LOS NOVIOOOOOOS!!!!", "QUE VIVAN LOS DESGRACIAAAADOS!!!", "QUE VIVA EL AMARRE.. VIVAAAAA"]
