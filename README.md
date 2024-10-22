# Discord Role Assignment Bot

This Discord bot automatically assigns random roles to a specific user within a set time frame and sends notifications in the designated channel when it's active. The bot is built with the `discord.py` library and utilizes scheduled tasks to handle time-based actions.
<br>
![imagen](https://github.com/user-attachments/assets/0184a770-ff17-4bad-a56a-12c11cd6c721)
## Prerequisites

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Discord Developer Portal**: Create a bot on the [Discord Developer Portal](https://discord.com/developers/applications). Follow this [tutorial](https://www.youtube.com/watch?v=2k9x0s3awss) (watch up to 9 minutes) to obtain your bot’s `TOKEN`.

### Libraries Required

- **discord.py**: For interacting with the Discord API.
- **random**: For randomly selecting roles.
- **json**: For loading and updating roles from a local file.
- **datetime**: To check the current time.
- **tasks** from `discord.ext`: To run scheduled tasks.
<br>

### Installation

1. Install the required libraries:

    ```bash
    pip install discord.py
    ```

2. **Configure the Bot**:
    - Set your bot’s `TOKEN` in the code: `TOKEN = 'YOUR_BOT_TOKEN'`.
    - Replace the placeholders for `main_channel_id`, `guild_id`, and `usuario_especifico_id` with the actual IDs from your Discord server.

### How to Obtain IDs

- **`main_channel_id`**: ID of the channel where the bot will send messages (usually the general channel).
- **`guild_id`**: ID of the Discord server.
- **`usuario_especifico_id`**: ID of the user who will receive the random roles.

Enable Developer Mode in Discord’s settings to easily copy these IDs.

## Bot Functionality
<br>
### Key Features

- **Event Handling**:
    - **on_ready**: When the bot starts, it announces its activation in the designated channel.
    - **Scheduled Task (verificar_hora)**: Checks every 58 minutes to see if it’s time to assign roles.
<br>

### Role Assignment Process

1. **Time Check**: Runs between 16:00 and 18:00.
2. **Role Selection**: Randomly selects a role from the JSON file.
3. **Role Assignment**: Assigns the selected role to the specified user.
4. **Role Management**: Removes the assigned role from the JSON file to avoid duplication.
<br>

### JSON File Structure (`palabras.json`)

Create a JSON file to store role names in the following format:

```json
{
  "arias_roles": ["Role1", "Role2", "Role3"]
}
```
## Customization Options

- **Change Time Range**: You can change the time range for role assignment by modifying the following line in your code:

    ```python
    if "16:00" <= hora_actual < "18:00":
    ```

- **Update Role List**: Add or remove role names from `palabras.json` to suit your needs.
<br><br>
>[!NOTE]
> **Running the Bot**: Once everything is set up, you can run the bot with:
>
> ```bash
> python bot.py
> ```

>[!TIP]
>Important Notes:
>
>Make sure the bot’s TOKEN, channel, and user IDs are correctly configured in the code. The bot will run continuously, checking every 58 minutes to see if it’s the right time to assign roles.
>Ensure your bot has the necessary permissions to create roles and assign them.
>Do not share your TOKEN publicly, as it grants full access to your bot.

> [!WARNING]
>Troubleshooting:
>
>Bot not responding: Make sure your bot is online, the token is correct, and the bot is added to your Discord server with proper permissions.
>Roles not being created: Check the bot’s permissions to manage roles. The bot’s role in the server should be higher than the roles it’s trying to assign.
