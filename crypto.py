'''
================== Crypto Cog ==================
| Author  : Adam Valdez
| Source  : https://www.github.com/adamvaldez
| Website : https:www.planetcryptoid.tech
| Date    : 3/11/2018     
=================================================
'''

import discord
from discord.ext import commands
import urllib.request
import json


class Crypto:
    """Planet Cryptoid's Crypto Price Cog (powered by coinmarketcap.com)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def btc(self):
        """What is Bitcoin's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=5"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 5:
            if data[i]['name'] == "Bitcoin":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " (" +
                                   data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def eth(self):
        """What is Ethereum's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 5:
            if data[i]['name'] == "Ethereum":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " (" +
                                   data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def xrp(self):
        """What is Ripple's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 5:
            if data[i]['name'] == "Ripple":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " (" +
                                   data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def bch(self):
        """What is Bitcoin Cash's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 10:
            if data[i]['name'] == "Bitcoin Cash":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " (" +
                                   data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def ltc(self):
        """What is Litecoins's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 10:
            if data[i]['name'] == "Litecoin":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " (" +
                                   data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def neo(self):
        """What is NEO's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=15"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 10:
            if data[i]['name'] == "NEO":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " (" +
                                   data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def xrm(self):
        """What is Monero's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=15"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 10:
            if data[i]['name'] == "Monero":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " (" +
                                   data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def xlm(self):
        """What is Stellar's live price"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=15"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        while i < 10:
            if data[i]['name'] == "Stellar":
                await self.bot.say(data[i]['name'] + " is priced $" + data[i]['price_usd'] + " ("
                                   + data[i]['percent_change_1h'] + "%)")
                break
            else:
                i += 1

    @commands.command()
    async def top5(self):
        """Get top 5 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=5"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 5:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " (" +
                               data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1

    @commands.command()
    async def top10(self):
        """Get top 10 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=10"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 10:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " ("
                               + data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1


    @commands.command()
    async def top20(self):
        """Get top 20 prices from coinmarketcap"""
        url = "https://api.coinmarketcap.com/v1/ticker/?limit=20"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        i = 0
        rank = 1
        await self.bot.say("=== Coin Marketcap Rankings ===")
        while i < 20:
            await self.bot.say(str(rank) + ".) " + data[i]['name'] + " | $" + data[i]['price_usd'] + " ("
                               + data[i]['percent_change_1h'] + "%)")
            i += 1
            rank += 1

    @commands.command()
    async def credits(self):
        """Post link for f3 Web Design Competition"""
        await self.bot.say("This Cog was created by Adam Valdez")
        await self.bot.say("Visit Planet Cryptoid for more Free Crypto Projects")
        await self.bot.say("https://www.planetcryptoid.tech")

    @commands.command()
    async def source(self):
        """Post link to github source"""
        await self.bot.say("This Cog was created by Adam Valdez")
        await self.bot.say("https://www.github.com/adamvaldez")

    @commands.command()
    async def vote(self):
        """Post link for f3 Web Design Competition"""
        await self.bot.say("f3 Global Web Design Competition!")
        await self.bot.say("Please vote for Planet Cryptoid")
        await self.bot.say("https://f3.space/website/planet-cryptoid")


def setup(bot):
    bot.add_cog(Crypto(bot))
