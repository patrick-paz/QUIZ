

let perguntas = []


export async function getPerguntas(tema, qtd_perg) {

    const res = await fetch(`http://127.0.0.1:8000/questoes?tema=${tema}&qtd_perg=${qtd_perg}`, {
        method: 'POST'
    });
    const json = await res.json();
    perguntas = json;
    return perguntas;
}


//#########################################################


export async function definirJogador(data) {

    let resposta;

    const jogador = {
        nome: data
    }
    const res = await fetch(`http://127.0.0.1:8000/definir_jogador`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jogador)
    });
    if (res.ok) {
        // Mensagem de confirmação de criação de usuário
        resposta = 'Jogador: ' + (jogador.nome);
        console.log(resposta)

    } else {
        const erro = await res.json();
        resposta = erro.detail;
    }
    return resposta
}

//#########################################################

export async function corrigirResposta(resJogador, resCorreta) {

    let resposta;

    const respostas = {
        jogador_resposta: resJogador,
        resposta_correta: resCorreta
    }
    const res = await fetch(`http://127.0.0.1:8000/atualizar_acerto`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(respostas)
    });
    if (res.ok) {

        const resok = await res.json();
        resposta = resok.detail;

    } else {
        const erro = await res.json();
        resposta = erro.detail;
    }
    return resposta
}


//#########################################################

export async function getAcertos() {

    const res = await fetch(`http://127.0.0.1:8000/get_jogador`, {
        method: 'GET'
    });
    const json = await res.json();
    perguntas = json;
    return perguntas;
}
