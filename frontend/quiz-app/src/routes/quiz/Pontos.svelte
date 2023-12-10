<script>
	import { onMount } from 'svelte';
	import { getAcertos } from '../../lib/functions';
    import { goto } from '$app/navigation';

	export let qtdTotal;
	export let pontos = {};

	onMount(async () => {
		pontos = await getAcertos();
		console.log(pontos);
	});



	function jogarNovamente() {
		goto('/');
	}

	console.log(pontos);
</script>

<div>
	<p>Jogador: {pontos.nome}</p>
	<p>Pontuação: {pontos.acertos} / {qtdTotal}</p>
</div>

<button on:click={(jogarNovamente)}> Jogar novamente? </button>
