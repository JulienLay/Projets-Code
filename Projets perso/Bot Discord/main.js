const Discord = require('discord.js');

const client = new Discord.Client();

const prefix = '!';

const fs = require('fs');
const ping = require('./commands/ping');

client.commands = new Discord.Collection();

const commandFiles = fs.readdirSync('./commands/').filter(file => file.endsWith('.js'));
for(const file of commandFiles){
    const command = require(`./commands/${file}`);

    client.commands.set(command.name, command)
}

client.once('ready', () => {
    console.log('JeyBot est en ligne!');
});

client.on('message', message => {
    if(!message.content.startsWith(prefix) || message.author.bot) return;

    const args = message.content.slice(prefix.length).split(/ +/);
    const command = args.shift().toLowerCase();

    if(command === 'ping'){
        client.commands.get('ping').execute(message, args);
    } else if (command === 'github') {
        client.commands.get('github').execute(message, args);
    }
});

client.login('NzQ4OTIyMDQxMTQ2NTQwMTU5.X0keAA.gbzp8wjdvsCBS4PabwErbPj00w8');