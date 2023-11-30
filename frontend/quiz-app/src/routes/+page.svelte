<script>
	export let data;
	import InicioJogo from './quiz/InicioJogo.svelte';
	import Perguntas from './quiz/Perguntas.svelte';

</script>

<section>
	<h1>Quiz - app</h1>
	<div>
		<h2>Preencha os dados para começar:</h2>

		<span> Start Quiz </span>
		{#if !data.qtd}
			<InicioJogo />
		{/if}

		{#if data.qtd > 0}
		{console.log(data.perguntas)}
			<Perguntas questions={data.perguntas} />
		{/if}
	</div>
</section>
