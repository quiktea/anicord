import discord
from datetime import datetime
class EmbedParsers():
    @staticmethod
    async def parseforsearch(data : dict, colour : discord.Colour):
        data = data.get("data")
        embeds = []
        for x in data:
            attrs = x.get("attributes")
            description = attrs.get("description")
            en_title = attrs.get("titles").get("en")
            jp_title = attrs.get("titles").get("ja_jp")
            image = attrs.get("posterImage").get("original")
            age_rating = attrs.get("ageRating")
            nsfw = str(attrs.get("nsfw"))
            embed = discord.Embed(
                title = f"{en_title}\n*{jp_title}*",
                colour = colour,
                description = description,
                timestamp = datetime.utcnow()
            )
            embed.set_image(url = image)
            embeds.append(embed)

        return embeds

        
            




        