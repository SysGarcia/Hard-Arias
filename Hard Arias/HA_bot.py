import discord
from discord.ext import commands, tasks
from datetime import datetime
import random
import json

#ESTO LO CONSIGUES DE LA PÁGINA WEB DE DESARROLLADORES DE DISCORD UNA VEZ HAYAS SEGUIDO LIGERAMENTE
#ESTE TUTORIAL VER HASTA LOS 9MIN APROX --> https://www.youtube.com/watch?v=2k9x0s3awss

TOKEN = 'TOKEN'  #TOKEN VERIFICACIÓN --> CAMBIAR ESTO
#-------------------------------------------------------------------------------------------------+
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

main_channel_id = 1195846133788975146 #ID DEL CANAL GENERAL --> CAMBIAR ESTO
guild_id = 1195846133788975144 #ID DEL SERVIDOR --> CAMBIAR ESTO
usuario_especifico_id = 839180198313590895 #ID DEL USUARIO AL QUE QUIERES MOLESTAR --> CAMBIAR ESTO

#APERTURA ARCHIVO JSON CON LOS NOMBRES DE LOS ROLES A CREAR/ASIGNAR
with open('palabras.json', 'r') as file:
    palabras = json.load(file)

#EVENTO INICIAL
@bot.event
async def on_ready():
    print("El bot está activo 🍒")
    channel = bot.get_channel(main_channel_id)
    await channel.send("El bot está activo 🍒")
    
    # INICIAR BUCLE VERIFICACIÓN DE LA HORA
    verificar_hora.start()

@tasks.loop(minutes=58)
async def verificar_hora():
    hora_actual = datetime.now().strftime('%H:%M')

    if "16:00" <= hora_actual < "18:00": #CAMBIAR SI SE QUIERE QUE SE HAGA EN LOS RANGOS DE TIEMPO QUE SE GUSTEN
        channel = bot.get_channel(main_channel_id)
        if channel:
            await channel.send("Es hora de asignar roles automáticamente entre las 4 y 6 PM")
            guild = bot.get_guild(guild_id) 

            arias_roles = palabras.get('arias_roles', [])
            rol_aleatorio = random.choice(arias_roles)
            flag = False
            while flag == False:
                try:
                    rol = await guild.create_role(name=rol_aleatorio)
                    flag=True
                except: 
                    print("Se ha intentado crear un rol que ya existe JOJOJOJO")
            arias_roles.remove(rol_aleatorio)

            with open('palabras.json', 'w') as file:
                json.dump(arias_roles, file, indent=2)

            member = guild.get_member(usuario_especifico_id)
            await member.add_roles(rol)
            await channel.send(f"Se ha asignado el rol de {rol.name} al pringao de {member.display_name}")

        else:
            print("No se pudo obtener el canal")
        
@verificar_hora.before_loop
async def before_verificar_hora():
    print('Esperando para iniciar el bucle de verificación de hora...')
    await bot.wait_until_ready()

bot.run(TOKEN)