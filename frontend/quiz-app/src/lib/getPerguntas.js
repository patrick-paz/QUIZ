

let perguntas = []


export async function getPerguntas(tema, qtd_perg) {

    const res = await fetch(`http://127.0.0.1:8000/questoes?tema=${tema}&qtd_perg=${qtd_perg}`, {
        method: 'POST'
    });
    const json = await res.json();
    perguntas = json;
    return perguntas;
}