
<script>
	import { onMount } from "svelte";
    import { getAcertos } from "../../lib/functions";


	export let qtdTotal
    export let pontos = {};

    onMount(async () => {
        pontos = await getAcertos();
        console.log(pontos);
    });




    console.log(pontos)
</script>


<div>
<p>Jogador: {pontos.nome}</p>
<p>Pontuação: {pontos.acertos} / {qtdTotal}</p>
</div>