# Role-bot-DC
This Discord bot automatically assigns random roles to a specific user between certain hours and sends messages to the designated channel when it is active. The bot also loads role names from a JSON file to ensure variety in role assignment.
Prerequisites

    Python 3.x: Make sure you have Python installed.
    Discord Developer Portal: You need to create a bot in the Discord Developer Portal. Follow this tutorial (watch up to 9 minutes) to get your bot’s TOKEN.

Libraries Used:

    discord.py: This library allows interaction with the Discord API.
    random: To randomly select roles from the JSON file.
    json: To load and update role names from a local file.
    datetime: To check the current time for role assignment.
    tasks from discord.ext: To run scheduled tasks (e.g., checking the time at regular intervals).

Installation

    Install the required libraries by running:

    bash

    pip install discord.py

    Set up the bot:
        Create a bot through the Discord Developer Portal.
        Add your bot’s TOKEN in the code where it says TOKEN = 'TOKEN'.
        Replace the values for main_channel_id, guild_id, and usuario_especifico_id with the corresponding IDs from your Discord server.

How to Get IDs:

    main_channel_id: The ID of the channel where the bot will send messages (usually a general channel).
    guild_id: The ID of the Discord server.
    usuario_especifico_id: The ID of the user you want to assign random roles to.

You can enable developer mode in Discord’s settings to easily copy these IDs.
How the Bot Works:

    on_ready Event:
        When the bot starts, it will print a message in the console and send a message to the specified channel (main_channel_id) announcing that it is active.
        It also starts a scheduled task that checks the time every 58 minutes.

    Scheduled Task (verificar_hora):
        This task runs every 58 minutes to check if the current time is between 16:00 and 18:00.
        If it is, the bot will:
            Choose a random role from the palabras.json file.
            Assign that role to the specific user (usuario_especifico_id).
            Remove the assigned role from the list in palabras.json to prevent duplicates.

    Error Handling:
        If the bot tries to create a role that already exists, it will catch the error and print a message in the console but will keep running.

JSON File (palabras.json):

This file should contain a list of role names you want to assign. Here’s an example of how it could look:

json

{
  "arias_roles": ["Role1", "Role2", "Role3"]
}

Customization:

    Time Range: You can change the time range for role assignment in this line:

    python

    if "16:00" <= hora_actual < "18:00":

    Role List: Add or remove role names from palabras.json to suit your needs.
>[!NOTE]
>Running the Bot:

>Once everything is set up, you can run the bot with:

>python bot.py

>Make sure the bot’s TOKEN, channel, and user IDs are correctly configured in the code. The bot will run continuously, checking every 58 minutes to see if it’s the right time to assign roles.
>
> [!TIP]
>Important Notes:

    Ensure your bot has the necessary permissions to create roles and assign them.
    Do not share your TOKEN publicly, as it grants full access to your bot.

Troubleshooting:

    Bot not responding: Make sure your bot is online, the token is correct, and the bot is added to your Discord server with proper permissions.
    Roles not being created: Check the bot’s permissions to manage roles. The bot’s role in the server should be higher than the roles it’s trying to assign.
