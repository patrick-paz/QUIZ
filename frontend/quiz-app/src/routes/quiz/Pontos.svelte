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

<div class='container'>
	<h2>Fim de jogo!!</h2>
	<p>Jogador: {pontos.nome}</p>
	<p>Pontuação: {pontos.acertos} / {qtdTotal}</p>

<button class ='button' on:click={(jogarNovamente)}> Jogar novamente? </button>

</div>

<style>

.container{
	border: 1;
	border-style: solid;
	border-color: black;
	padding: 70px 70px 70px;
	background-color: #2E2EFE;
	align-items: center;
}
h2{
	margin-bottom: 30px;

}
p{
	font-weight: bolder;
	text-align: center;
	border: solid 2px;
	border-radius: 10px;
	padding: 5px;
	background-color: darkgreen;
}

.button{
	display: flex;
	flex-direction: column;
	align-items: center;
	margin: auto;
	margin-top: 30px;
	background-color: #FF0000; 
	color: white;
	font-weight: bolder;
	border: 3px;
	border-style: solid;
	border-color: black;
	border-radius: 10px;
	padding: 10px;
}


</style>
