import Helpers


# ----------------------------------------------------------------------------------------------------------------------

# As descrições contidas aqui, servem para todos os metodos.
# Caso algum metodo utilise-as de forma diferente, tera uma descrição na parte superior do metodo.
# apiKey => Sua chave de acesso a api do Zapus.
# chatWid => Informe o número do contato no formato id do WhatsApp. EX 5522999999999@c.us.
# message => Você pode enviar emoticons no corpo da mensagem.
# sendByAccount => Api token do usuário registrado dentro do Zapus.me, todas as mensagens enviada serão vinculadas ao
# usuário em questão.

# ----------------------------------------------------------------------------------------------------------------------
# phone => Se não for enviado o código do país ex. Brasil 55, junto ao DDD e o número do seu contato, por padrão iremos
# assumir o código do país vinculado ao seu cadastro.
def haveWhatsapp(apiKey, phone):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'phone': phone,
    }

    post = Helpers.post('/tools/have-whatsapp', header, body)
    Helpers.logs('tools', 'have-whatsapp', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# status => Informe o novo status que deseja aplicar.
def status(apiKey, status):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'status': status,
    }

    post = Helpers.post('/tools/profile/status', header, body)
    Helpers.logs('tools', 'status', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# name => Informe o nome de perfil que deseja aplicar.
def name(apiKey, name):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'name': name,
    }

    post = Helpers.post('/tools/profile/name', header, body)
    Helpers.logs('tools', 'name', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# photo => Informe a foto no formato base64 data uri.
def picture(apiKey, photo):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'photo': photo,
    }

    post = Helpers.post('/tools/profile/picture', header, body)
    Helpers.logs('tools', 'picture', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# phone => Se não for enviado o código do país ex. Brasil 55, junto ao DDD e o número do seu contato, por padrão iremos
# assumir o código do país vinculado ao seu cadastro.
def getPicture(apiKey, phone):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'phone': phone,
    }

    post = Helpers.post('/tools/profile/get-picture', header, body)
    Helpers.logs('tools', 'get-picture', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def device(apiKey):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/tools/profile/device', header, body)
    Helpers.logs('tools', 'device', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
def restartService(apiKey):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {}

    post = Helpers.post('/tools/restart-service', header, body)
    Helpers.logs('tools', 'restart-service', post)
    return post


# ----------------------------------------------------------------------------------------------------------------------
# chatWid => Se informado iremos sincronizar apenas o chat em questão, para sincronizar todos os chats basta deixar esse
# parâmetro vazio. Informe o contato no formato id do WhatsApp.
# onlyFiles => Envie true para sincronizar apenas mensagens com arquivos (gif, vídeos, imagens, documentos, stickers e
# etc..), envie false para sincronizar apenas mensagens que não contenha arquivos.
def syncWhatsApp(apiKey, chatWid, onlyFiles):
    header = {
        'Connection': 'keep-alive',
        'content-type': 'application/json',
        'apiKey': apiKey
    }

    body = {
        'chat_wid': chatWid,
        'onlyFiles': onlyFiles,
    }

    post = Helpers.post('/tools/sync-whatsApp', header, body)
    Helpers.logs('tools', 'sync-whatsApp', post)
    return post
# ----------------------------------------------------------------------------------------------------------------------
