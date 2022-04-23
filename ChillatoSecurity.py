from pyrogram import *
from pyrogram.types import *
from pyrogram.raw import *

api_id =
api_hash = ""
securitytoken = ""

Security = Client("securitystorage", api_id, api_hash, bot_token=securitytoken)

@Security.on_message(filters.private & filters.command("start"))
async def start(client, message):
    await message.reply_text(f"""
<b>👋🏻 Ciao {message.from_user.mention}</b>

<i>👉🏻 Aggiungimi in un supergruppo e impostami come Amministratore per farmi entrare subito in azione! 

❓ QUALI SONO I COMANDI?
Premi [QUI](https://telegra.ph/COMANDI-04-06-2) per vedere tutti i comandi e il loro funzionamento</i>  
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("➕ AGGIUNGIMI IN UN GRUPPO ➕", url=f"t.me/ChillatoSecurityBot?startgroup=start")]]), disable_web_page_preview=True)


@Security.on_message(filters.group & filters.command("ban"))
async def ban(client, message):
    staff = await client.get_chat_member(message.chat.id, message.from_user.id)
    if staff.status == "administrator" or staff.status == "creator":
        try:
            utenteban = await client.get_users(message.text.split(" ")[1])
            await client.ban_chat_member(message.chat.id, utenteban.id)
            await message.reply_text(f"🚷 {message.from_user.mention} ha bannato {utenteban.mention}")
        except:
            if message.reply_to_message:
                await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                await message.reply_text(f"🚷 {message.from_user.mention} ha bannato {message.reply_to_message.from_user.mention}")

@Security.on_message(filters.group & filters.command("unban"))
async def unban(client, message):
    staff = await client.get_chat_member(message.chat.id, message.from_user.id)
    if staff.status == "administrator" or staff.status == "creator":
        try:
            utentesbannato = await client.get_users(message.text.split(" ")[1])
            await client.unban_chat_member(message.chat.id, utentesbannato.id)
            await message.reply_text(f"✅ {message.from_user.mention} ha sbannato {utentesbannato.mention}")
        except:
            if message.reply_to_message:
                await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                await message.reply_text(f"✅ {message.from_user.mention} ha sbannato {message.reply_to_message.from_user.mention}")

@Security.on_message(filters.group & filters.command("kick"))
async def kick(client, message):
    staff = await client.get_chat_member(message.chat.id, message.from_user.id)
    if staff.status == "administrator" or staff.status == "creator":
        try:
            utentekickato = await client.get_users(message.text.split(" ")[1])
            await client.ban_chat_member(message.chat.id, utentekickato.id)
            await client.unban_chat_member(message.chat.id, utentekickato.id)
            await message.reply_text(f"⛔️ {message.from_user.mention} ha kickato {utentekickato.mention}")
        except:
            if message.reply_to_message:
                await client.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                await client.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
                await message.reply_text(f"⛔️ {message.from_user.mention} ha kickato {message.reply_to_message.from_user.mention}")

@Security.on_message(filters.group & filters.command("mute"))
async def mute(client, message):
    staff = await client.get_chat_member(message.chat.id, message.from_user.id)
    if staff.status == "administrator" or staff.status == "creator":
        try:
            utentemutato = await client.get_users(message.text.split(" ")[1])
            await client.restrict_chat_member(message.chat.id, utentemutato.id, ChatPermissions(can_send_messages=False, can_send_media_messages=False, can_send_other_messages=False))
            await message.reply_text(f"🔇 {message.from_user.mention} ha mutato {utentemutato.mention}")
        except:
            if message.reply_to_message:
                await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(can_send_messages=False, can_send_media_messages=False, can_send_other_messages=False))
                await message.reply_text(f"🔇 {message.from_user.mention} ha mutato {message.reply_to_message.from_user.mention}")

@Security.on_message(filters.group & filters.command("unmute"))
async def unmute(client, message):
    staff = await client.get_chat_member(message.chat.id, message.from_user.id)
    if staff.status == "administrator" or staff.status == "creator":
        try:
            utentesmutato = await client.get_users(message.text.split(" ")[1])
            await client.rrestrict_chat_member(message.chat.id, utentesmutato.id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
            await message.reply_text(f"🔊 {message.from_user.mention} ha smutato {utentesmutato.mention}")
        except:
            if message.reply_to_message:
                await client.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True))
                await message.reply_text(f"🔊 {message.from_user.mention} ha smutato {message.reply_to_message.from_user.mention}")


@Security.on_message(filters.group & filters.command("templink"))
async def templink(client, message):
    staff = await client.get_chat_member(message.chat.id, message.from_user.id)
    if staff.status == "administrator" or staff.status == "creator" and staff.can_invite_users == True:
        try:
            link = await client.create_chat_invite_link(message.chat.id, member_limit=1)
            await client.send_message(message.from_user.id, "**Ecco a te il link temporaneo VALIDO PER UNA PERSONA invialo a chi vuoi: **"+link["invite_link"], disable_web_page_preview=True)
            await message.reply_text("Ti ho inviato il link in privato !")
        except:
            await message.reply_text("❌ ERRORE ❌\n\nControlla se hai avviato il bot e di avermi messo admin e riprova !")

@Security.on_message(filters.new_chat_members)
async def benvenuto(client, message):
    for user in message.new_chat_members:
        if user.is_self:
            await message.reply_text(f"Grazie per avermi aggiunto {message.from_user.mention}!\n\nPer farmi funzionare fammi admin!")
        else:
            try:
                await client.get_chat_member(message.from_user.id)
            except:
                await message.reply_text(f"Benvenuto {user.mention} =)")
