import { getPerguntas, definirJogador } from "../lib/functions.js";

export async function load({ url }) {
    const qtd = url.searchParams.get("qtd");
    const nome = url.searchParams.get("nome") || "";
    const tema = url.searchParams.get("tema");

    let questoes = [];

    definirJogador(nome)

    if (qtd > 0) {
        async function questoesTema(tema, qtd) {
            const res = await getPerguntas(tema, qtd);
            questoes = res;
            return questoes;
        }

        const perguntas_selecionadas = await questoesTema(tema, qtd);



        return {
            props: {
                perguntas: perguntas_selecionadas,
                tema,
                nome,
                qtd
            }
        };

    } else {
        // Lógica para tratar o caso em que qtd não é maior que 0
        return {
            props: {
                perguntas: [],
                tema,
                nome,
                qtd
            }
            
        };
        
    }
    
}
