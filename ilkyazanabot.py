from telethon.sync import TelegramClient, events
from datetime import datetime, timedelta
import random
import telethon

# Botu kullanabilirsiniz tek ricamız @BotAltyapiKanali katılmanız 

bot_calisiyor = False

sudo_users = ["6958129929"]

owner_id = input("Telegram id gir: ")
botaltyapi = input("API ID girin: ")
botlar_diyari = input("API hash girin: ")
telethon_telefon_numarasi = input("Telefon numaranızı girin (örneğin: +1234567890): ")

print("\033[91mBot aktif @BotAltyapiKanali")

telethon_client = TelegramClient('yarrakyazanabot.session', botaltyapi, botlar_diyari)

botaltyapi = {
    "yazana": "bdb",
    "𝕪𝕒𝕫𝕒𝕟𝕒": "k",
    "𝚢𝚊𝚣𝚊𝚗𝚊": "ah",
    "Yᗩᘔᗩᑎᗩ": "ah",
    "𝔂𝓪𝔃𝓪𝓷𝓪": "ajh",
    "𝐲𝐚𝐳𝐚𝐧𝐚": "u",
    "𝒚𝒂𝒛𝒂𝒏𝒂": "y",
    "𝑦𝑎𝑧𝑎𝑛𝑎": "f",
    "𝘆𝗮𝘇𝗮𝗻𝗮": "mm",
    "𝙮𝙖𝙯𝙖𝙣𝙖": "s",
    "𝘺𝘢𝘻𝘢𝘯𝘢": "o",
    "ʏᴀᴢᴀɴᴀ": "u",
    "𝔶𝔞𝔷𝔞𝔫𝔞": "t",
    "🅨︎🅐︎🅩︎🅐︎🅝︎🅐︎": "r",
    "Ⓨ︎Ⓐ︎Ⓩ︎Ⓐ︎Ⓝ︎Ⓐ︎": "e",
    "ʸᵃᶻᵃⁿᵃ": "w",
    "🆈︎🅰︎🆉︎🅰︎🅽︎🅰︎": "A",
    "🅈🄰🅉🄰🄽🄰": "d",
    "ʎɐzɐuɐ": "h",
    "y̾a̾z̾a̾n̾a̾̾": "m",
    "y͜͡a͜͡z͜͡a͜͡n͜͡a͜͡": "n",
    "y͟a͟z͟a͟n͟a͟": "x",
    "y a  z a  n a": "z",
    "чαzαnα": "v",
    "y̶a̶z̶a̶n̶a̶": "x",
    "y̶a̶z̶a̶n̶a̶": "a",
    "y͎a͎z͎a͎n͎a͎": "w",
    "⚟y⚞⚟a⚞⚟z⚞⚟a⚞⚟n⚞⚟a⚞": "e",
    "y꙲a꙲z꙲a꙲n꙲a꙲": "t",
    "⟅y⟆⟅a⟆⟅z⟆⟅a⟆⟅n⟆⟅a⟆": "u",
    "࿙y࿚࿙a࿚࿙z࿚࿙a࿚࿙n࿚࿙a࿚": "p",
    "y⃠a⃠z⃠a⃠n⃠a⃠": "l",
    "y̸a̸z̸a̸n̸a̸": "f",
    "y҈a҈z҈a҈n҈a҈": "s",
    "y҉a҉z҉a҉n҉a҉": "a",
    "ㄚ卂乙卂几卂": "d",
    "y͆a͆z͆a͆n͆a͆": "q",
    "y̺a̺z̺a̺n̺a̺": "w",
    "y>a>z>a>n>a>": "r",
    "y}a}z|a|n[a": "y",
    "£i#l$k½y}a}z|a|n[a": "o",
    "½i]l\k£y[a}z]a}n}a": "k",
    "y[a}z]a}n}a": "j",
    "yzna": "ks",
    "yazan": "shgs",
    "yazab": "hd",
    "YAZAN": "j",
    "𝐘𝐀𝐙𝐀𝐍𝐀": "y",
    "🇾 🇦 🇿 🇦 🇳 🇦 ": "o",
    "🆈︎🅰︎🆉︎🅰︎🅽︎🅰︎": "x",
    "𝚈𝙰𝚉𝙰𝙽𝙰": "x",
    "𝕐𝔸ℤ𝔸ℕ𝔸": "o",
    "𝐘𝐀𝐙𝐀𝐍𝐀": "y",
    "𝒀𝑨𝒁𝑨𝑵𝑨": "o",
    "𝑌𝐴𝑍𝐴𝑁𝐴": "z",
    "YAZANA": "j",
    "𝒴𝒜𝒵𝒜𝒩𝒜": "o",
    "𝓨𝓐𝓩𝓐𝓝𝓐": "o",
    "ʸᵃᶻᵃⁿᵃ": "w",
    "Yᗩᘔᗩᑎᗩ": "ah",
    "𝗬𝗔𝗭𝗔𝗡𝗔": "y",
    "𝙮𝙖𝙯𝙖𝙣𝙖": "s",
    "𝘠𝘈𝘡𝘈𝘕𝘈": "z",
    "𝖸𝖠𝖹𝖠𝖭𝖠": "y",
    "Ⓨ︎Ⓐ︎Ⓩ︎Ⓐ︎Ⓝ︎Ⓐ︎": "e",
    "🅨︎🅐︎🅩︎🅐︎🅝︎🅐︎": "r",
    "𝔲𝔞𝔷𝔞𝔫𝔞": "u",
    "𝖀𝕬𝖅𝕬𝕹𝕬": "u",
    "ɐuɐzɐʎ": "h",
    "Y͜͡A͜͡Z͜͡A͜͡N͜͡A͜͡": "n",
    "Y̆̈Ă̈Z̆̈Ă̈N̆̈Ă̈": "q",
    "Y̑̈Ȃ̈Z̑̈Ȃ̈N̑̈Ȃ̈": "m",
    "🇾 🇦 🇿 🇦 🇳 🇦 ": "o",
    "🅈🄰🅉🄰🄽🄰": "d",
    "🆈︎🅰︎🆉︎🅰︎🅽︎🅰︎": "x",
    "ꪗꪖɀꪖꪀꪖ": "w",
    "ㄚ卂乙卂几卂": "d",
    "Y̾A̾Z̾A̾N̾A̾": "m",
    "Y̥ͦḀͦZ̥ͦḀͦN̥ͦḀͦ": "l",
    "Y͟A͟Z͟A͟N͟A͟": "x",
    "ꌩꍏꁴꍏꈤꍏ": "f",
    "Y҉A҉Z҉A҉N҉A҉": "s",
    "Y҈A҈Z҈A҈N҈A҈": "s",
    "Y̸A̸Z̸A̸N̸A̸": "f",
    "Y⃠A⃠Z⃠A⃠N⃠A⃠": "l",
    "Y̺͆A̺͆Z̺͆A̺͆N̺͆A̺͆": "q",
    "Y͎A͎Z͎A͎N͎A͎": "w",
    "ሃልጊልክል": "x",
    "Y̶A̶Z̶A̶N̶A̶": "x",
    "Yazan": "shgs"
    
}

ramowlf = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

def get_yarrak(text):
    ramazan = text.split()
    if len(ramazan) < 3:
        return None
    else:
        return ' '.join(ramazan[1:-1])

async def telethon_main():
    await telethon_client.connect()

    if not await telethon_client.is_user_authorized():
        await telethon_client.send_code_request(telethon_telefon_numarasi)
        code = input("Doğrulama kodunu girin: ")

        try:
            await telethon_client.sign_in(telethon_telefon_numarasi, code)
        except telethon.errors.SessionPasswordNeededError:
            two_step_code = input("İki adımlı doğrulama kodunu girin: ")
            try:
                await telethon_client.sign_in(password=two_step_code)
            except Exception as e:
                print(f"İki adımlı doğrulama sırasında hata oluştu: {e}")
                return
        except Exception as e:
            print(f"Giriş sırasında hata oluştu: {e}")
            return

    print("Bot hesaba başarılı şekilde giriş yaptı")

    @telethon_client.on(events.NewMessage)
    async def yunusbaligi(event):
        global bot_calisiyor

        user_id = event.sender_id
        text = event.raw_text.lower()

        if text == "a" and not bot_calisiyor:
            if str(user_id) in owner_id.split(','):
                bot_calisiyor = True
                await event.respond("")
                return
            else:
                await event.respond("")
                return
        elif text == "b" and bot_calisiyor:
            if str(user_id) in owner_id.split(','):
                bot_calisiyor = False
                await event.respond("")
                return
            else:
                await event.respond("")
                return

        if bot_calisiyor:
            message_text = event.raw_text.strip()
            if message_text.startswith('') and message_text.endswith('yazana'):
                response_text = get_yarrak(message_text)
                if response_text:
                    await event.respond(response_text, reply_to=event.id)

            for kelime, cevap in botaltyapi.items():
                if f" {kelime} " in f" {text} ":
                    try:
                        bot_altyapi = random.choice(ramowlf)
                        yanit = f"{bot_altyapi}"
                        await event.respond(yanit, reply_to=event.id)
                    except IndexError:
                        await event.respond(cevap, reply_to=event.id)

    @telethon_client.on(events.NewMessage(pattern=r'\.alive'))
    async def a_dedin_yarrami_yedin(event):
        try:
            message = event.message

            if str(message.sender_id) not in sudo_users:
                await telethon_client.send_message(message.chat_id, "")
                return

            dalyarak = """```python
print("Merhaba ben @BotAltyapiKanali Ailesi Tarafından Tasarlandım")
```"""

            await telethon_client.send_message(message.chat_id, dalyarak)

        except Exception as e:
            error_message = f"Hata oluştu: {e}"
            await telethon_client.send_message(message.chat_id, error_message)

    @telethon_client.on(events.NewMessage(pattern="^\.menu(?: |$)"))
    async def menu_handler(event):
        menu_text = "Komutlar Menüsü açıldı\n\n"
        menu_text += "A - komutu ilk yazana botunu aktif eder\n\n"
        menu_text += "b - komutu ilk yazana botunu devre dışı bırakır\n\n"
        menu_text += "Bizi Önermeyi Unutmayın @BotAltyapiKanali"
        await event.respond(menu_text)

if __name__ == '__main__':
    with telethon_client:
        telethon_client.loop.run_until_complete(telethon_main())
        telethon_client.run_until_disconnected()
        