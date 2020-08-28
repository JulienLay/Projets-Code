module.exports = {
    name: 'github',
    description: "Ceci est une commande permettant d'accéder à mon Github!",
    execute(message, args){
        if(message.member.roles.cache.has('748937678321352704')){
            message.channel.send('https://github.com/JulienLay');
        } else {
            message.channel.send('Tu dois avoir le rôle de "Modérateur" pour pouvoir utiliser cette commande.');
        }
    }
}