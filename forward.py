from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

...

@client.on(events.NewMessage(pattern=r"^/forward (text|forward) (.+?) (\d+) (\d+) (\d+)-(\d+) (\d+)$", outgoing=True))
async def forward_command(event):
    mode, konten, jumlah_grup, durasi, jeda_min, jeda_max, total_perhari = event.pattern_match.groups()
    jumlah_grup = int(jumlah_grup)
    durasi = int(durasi)
    jeda_min = int(jeda_min)
    jeda_max = int(jeda_max)
    total_perhari = int(total_perhari)

    user_id = event.sender_id
    job_id = str(uuid.uuid4())[:8]

    grup_target = await ambil_grup_aktif(client, jumlah_grup)
    if not grup_target:
        await event.reply("Tidak ditemukan grup aktif.")
        return

    # Resolve channel jika mode forward
    if mode == "forward":
        try:
            username_channel, message_id = konten.split()
            if not username_channel.startswith("@"):
                username_channel = f"@{username_channel}"

            entity = await client.get_entity(username_channel)
            channel_id = entity.id
            konten = f"{channel_id} {message_id}"
        except Exception as e:
            await event.reply(f"Gagal membaca channel atau pesan: {e}")
            return

    ...
