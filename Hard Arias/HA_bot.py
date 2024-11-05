import discord
from discord.ext import commands, tasks
from datetime import datetime
import random
import json
import logging

logging.basicConfig(
    filename='bot_log.txt',  # Archivo donde se guardarán los logs
    level=logging.INFO,  # Nivel de logging
    format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del log
)

TOKEN = 'TOKEN'  #TOKEN VERIFICACIÓN --> CAMBIAR ESTO
#-------------------------------------------------------------------------------------------------+
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

main_channel_id = 1195846133788975146 #ID DEL CANAL GENERAL --> CAMBIAR ESTO
guild_id = 1195846133788975144 #ID DEL SERVIDOR --> CAMBIAR ESTO
usuario_especifico_id = 210385272309809152 #ID DEL USUARIO AL QUE QUIERES MOLESTAR --> CAMBIAR ESTO (Arias 839180198313590895)

intentos_de_entrada = 0

rol_asignado = False

# Cargar datos del archivo JSON
try:
    with open('palabras.json', 'r') as file:
        palabras = json.load(file)
except FileNotFoundError:
    logging.error("El archivo 'palabras.json' no fue encontrado.")
    palabras = {'arias_roles': []}  # Inicializar si no existe el archivo
except json.JSONDecodeError:
    logging.error("Error al decodificar el archivo JSON.")
    palabras = {'arias_roles': []}  # Inicializar si hay un error en el formato

@bot.event
async def on_ready():
    logging.info("El bot está activo 🍒")
    verificar_hora.start()  # Inicia la tarea de verificación de hora
    desconectar_usuario.start()  # Inicia la tarea de desconexión de usuario

@tasks.loop(hours=1)  # Verifica cada hora
async def verificar_hora():
    global rol_asignado
    hora_actual = datetime.now().strftime('%H:%M')

    if "10:00" <= hora_actual < "12:00" and not rol_asignado:
        guild = bot.get_guild(guild_id) 
        canal_principal = bot.get_channel(main_channel_id)

        # Verificar si se obtiene el canal y el servidor
        if not guild or not canal_principal:
            logging.error("No se pudo obtener el servidor o el canal principal.")
            return
        
        arias_roles = palabras.get('arias_roles', [])
        if not arias_roles:  # Verificar si hay roles disponibles
            logging.warning("No hay roles disponibles para asignar.")
            return

        rol_aleatorio = random.choice(arias_roles)
        flag = False
        color_hex = discord.Color(random.randint(0, 0xFFFFFF))
        while not flag:
            try:
                rol = await guild.create_role(name=rol_aleatorio, color=color_hex)
                flag = True
            except discord.Forbidden:
                logging.error("No tengo permisos para crear roles.")
                return
            except discord.HTTPException as e:
                logging.error(f"Error al crear el rol: {e}")
                return

        arias_roles.remove(rol_aleatorio)
        palabras['arias_roles'] = arias_roles  # Actualizar roles
        with open('palabras.json', 'w') as file:
            json.dump(palabras, file, indent=2)

        try:
            member = guild.get_member(usuario_especifico_id)
            await member.add_roles(rol)
            await canal_principal.send(f"Se ha asignado el rol de {rol.name} a {member.display_name}")
        except discord.Forbidden:
            logging.error("No tengo permisos para asignar roles.")
        except discord.HTTPException as e:
            logging.error(f"Error al asignar el rol: {e}")

        rol_asignado = True  # Marcar como rol asignado en esta ventana horaria

    elif hora_actual >= "20:00" or hora_actual < "10:00":
        rol_asignado = False  # Reiniciar para la próxima ventana horaria

@verificar_hora.before_loop
async def before_verificar_hora():
    await bot.wait_until_ready()
    logging.info("Esperando para iniciar la tarea de verificación de hora...")

@tasks.loop(seconds=1)  # Verifica cada segundo para desconectar rápidamente
async def desconectar_usuario():
    global intentos_de_entrada
    canal_principal = bot.get_channel(main_channel_id)
    guild = bot.get_guild(guild_id)

    if guild:
        member = guild.get_member(usuario_especifico_id)
        if member and member.voice and member.voice.channel:
            try:
                await member.move_to(None)  # Desconectar del canal de voz
                intentos_de_entrada += 1
                intentos = [
                    f"intento nº{intentos_de_entrada}",
                    f"prueba nº{intentos_de_entrada}",
                    f"intentona nº{intentos_de_entrada}",
                    f"tiro nº{intentos_de_entrada}",
                    f"oportunidad nº{intentos_de_entrada}",
                    f"asalto nº{intentos_de_entrada}",
                    f"desafío nº{intentos_de_entrada}",
                    f"apuesta nº{intentos_de_entrada}",
                    f"movimiento nº{intentos_de_entrada}"
                ]
                jefes = [
                    "vaya jefe intentando entrar!",
                    "qué valiente intentando entrar!",
                    "qué audaz intentando entrar!",
                    "el intrépido intentando entrar.",
                    "el atrevido intentando entrar.",
                    "el valiente intentando entrar!",
                    "el decidido intentando entrar.",
                    "el aventurero intentando entrar!",
                    "el osado intentando entrar!",
                    "el arriesgado intentando entrar!"
                ]

                mensaje = f"Este es el {random.choice(intentos)} de Arias, {random.choice(jefes)}"
                await canal_principal.send(mensaje)
                logging.info(mensaje)  # Guardar mensaje en el log
            except discord.Forbidden:
                logging.error("No tengo permisos para mover al usuario.")
            except discord.HTTPException as e:
                logging.error(f"Error al mover al usuario: {e}")
    else:
        logging.error("No se pudo obtener el servidor o usuario.")

@desconectar_usuario.before_loop
async def before_desconectar_usuario():
    await bot.wait_until_ready()
    logging.info("Esperando para iniciar la tarea de desconexión de voz...")

bot.run(TOKEN)
