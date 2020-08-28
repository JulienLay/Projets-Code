module.exports = {
    name: 'ping',
    description: "Ceci est une commande de ping!",
    execute(message, args){
        message.channel.send('pong');
    }
}